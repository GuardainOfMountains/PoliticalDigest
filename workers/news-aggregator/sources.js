/**
 * Source Manager for Cloudflare Worker
 * 
 * Provides similar functionality to Python src/sources.py
 * but optimized for Cloudflare Workers environment.
 * 
 * Reads from:
 * - /feeds.json (politician RSS feeds)
 * - /data/democratic-sources.json (reference sources)
 */

const CACHE_TTL = 5 * 60; // 5 minutes

/**
 * SourceManager class for Cloudflare Workers
 */
export class SourceManager {
  constructor(env = null) {
    this.env = env;
    this._feedsCache = null;
    this._sourcesCache = null;
  }

  /**
   * Fetch JSON from URL with caching
   */
  async _fetchJSON(url, cacheKey, ctx) {
    // Check cache first
    const cache = caches.default;
    const cachedResponse = await cache.match(cacheKey);
    
    if (cachedResponse) {
      try {
        return await cachedResponse.json();
      } catch (e) {
        // Cache miss on parse error
      }
    }
    
    // Fetch fresh
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Failed to fetch ${url}: ${response.status}`);
    }
    
    const data = await response.json();
    
    // Cache the response
    ctx.waitUntil(
      cache.put(
        cacheKey,
        new Response(JSON.stringify(data), {
          headers: { 'Content-Type': 'application/json' }
        })
      )
    );
    
    return data;
  }

  /**
   * Load feeds.json data
   */
  async loadFeeds(baseUrl, ctx) {
    if (this._feedsCache) {
      return this._feedsCache;
    }
    
    try {
      const url = `${baseUrl}/feeds.json`;
      this._feedsCache = await this._fetchJSON(url, 'feeds:json', ctx);
      return this._feedsCache;
    } catch (e) {
      console.error('Error loading feeds.json:', e);
      return {};
    }
  }

  /**
   * Load democratic-sources.json data
   */
  async loadSources(baseUrl, ctx) {
    if (this._sourcesCache) {
      return this._sourcesCache;
    }
    
    try {
      const url = `${baseUrl}/data/democratic-sources.json`;
      this._sourcesCache = await this._fetchJSON(url, 'sources:json', ctx);
      return this._sourcesCache;
    } catch (e) {
      console.error('Error loading democratic-sources.json:', e);
      return { sources: [] };
    }
  }

  /**
   * Get all RSS feeds combining feeds.json and democratic-sources.json
   * Returns array of { name, url, ... }
   */
  async getAllFeeds(baseUrl, ctx) {
    const feeds = {};
    
    // Load both data sources
    const feedsData = await this.loadFeeds(baseUrl, ctx);
    const sourcesData = await this.loadSources(baseUrl, ctx);
    
    // Add feeds from feeds.json (politician feeds)
    for (const [key, value] of Object.entries(feedsData)) {
      if (value.feeds && Array.isArray(value.feeds)) {
        for (const feedUrl of value.feeds) {
          // Skip placeholder URLs
          if (feedUrl && !feedUrl.includes('example.com') && feedUrl.trim()) {
            feeds[feedUrl] = {
              name: value.name || key,
              url: feedUrl,
              party: value.party,
              role: value.role,
              source: 'feeds.json'
            };
          }
        }
      }
    }
    
    // Add feeds from democratic-sources.json
    for (const source of (sourcesData.sources || [])) {
      if (source.has_rss && source.rss_url) {
        const rssUrl = source.rss_url;
        // Avoid duplicates
        if (!feeds[rssUrl]) {
          feeds[rssUrl] = {
            name: source.name,
            url: rssUrl,
            category: source.category,
            tier: source.tier,
            source: 'democratic-sources.json'
          };
        }
      }
    }
    
    return Object.values(feeds);
  }

  /**
   * Get reference sources with optional filters
   */
  async getReferenceSources(baseUrl, ctx, options = {}) {
    const sourcesData = await this.loadSources(baseUrl, ctx);
    let sources = sourcesData.sources || [];
    
    // Apply filters
    if (options.category) {
      sources = sources.filter(s => s.category === options.category);
    }
    
    if (options.tier !== undefined) {
      sources = sources.filter(s => s.tier === options.tier);
    }
    
    if (options.hasRss !== undefined) {
      sources = sources.filter(s => s.has_rss === options.hasRss);
    }
    
    return sources;
  }

  /**
   * Get source by name
   */
  async getSourceByName(baseUrl, ctx, name) {
    const sourcesData = await this.loadSources(baseUrl, ctx);
    return (sourcesData.sources || []).find(s => s.name === name);
  }

  /**
   * Get source by ID
   */
  async getSourceById(baseUrl, ctx, id) {
    const sourcesData = await this.loadSources(baseUrl, ctx);
    return (sourcesData.sources || []).find(s => s.id === id);
  }

  /**
   * Get statistics about sources
   */
  async getStats(baseUrl, ctx) {
    const feeds = await this.getAllFeeds(baseUrl, ctx);
    const sourcesData = await this.loadSources(baseUrl, ctx);
    const sources = sourcesData.sources || [];
    
    // Count by category
    const categories = {};
    for (const s of sources) {
      const cat = s.category || 'unknown';
      categories[cat] = (categories[cat] || 0) + 1;
    }
    
    // Count by tier
    const tiers = {};
    for (const s of sources) {
      const tier = s.tier || 0;
      tiers[tier] = (tiers[tier] || 0) + 1;
    }
    
    // Count with RSS
    const rssCount = sources.filter(s => s.has_rss).length;
    
    return {
      total_feeds: feeds.length,
      total_sources: sources.length,
      sources_with_rss: rssCount,
      by_category: categories,
      by_tier: tiers
    };
  }

  /**
   * Clear cache (for testing)
   */
  clearCache() {
    this._feedsCache = null;
    this._sourcesCache = null;
  }
}

// Export singleton instance
export const sourceManager = new SourceManager();

export default {
  SourceManager,
  sourceManager
};
