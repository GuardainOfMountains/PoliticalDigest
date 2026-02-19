/**
 * News Aggregator Worker
 * Fetches RSS feeds for selected politicians and returns combined headlines
 * 
 * Usage: GET /?ids=politician-id-1,politician-id-2,...
 * 
 * Caching: 5 minutes
 */

const CACHE_TTL = 5 * 60; // 5 minutes in seconds

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const ids = url.searchParams.get('ids');
    
    if (!ids) {
      return new Response(JSON.stringify({ error: 'Missing ids parameter' }), {
        headers: { 'Content-Type': 'application/json' }
      });
    }
    
    // Check cache first
    const cacheKey = `news:${ids}`;
    const cache = caches.default;
    const cachedResponse = await cache.match(cacheKey);
    
    if (cachedResponse) {
      return cachedResponse;
    }
    
    const politicianIds = ids.split(',').map(id => id.trim()).filter(id => id);
    
    try {
      // Fetch feeds.json from the origin
      const feedsUrl = url.origin + '/feeds.json';
      const feedsResponse = await fetch(feedsUrl);
      
      if (!feedsResponse.ok) {
        throw new Error('Failed to fetch feeds configuration');
      }
      
      const feedsData = await feedsResponse.json();
      
      // Fetch all feeds in parallel
      const feedPromises = politicianIds.map(async (id) => {
        const politician = feedsData[id];
        if (!politician) {
          return {
            id,
            name: id,
            articles: [],
            error: 'Politician not found'
          };
        }
        
        const articles = [];
        
        for (const feedUrl of politician.feeds) {
          try {
            const feedResponse = await fetch(feedUrl, {
              headers: {
                'User-Agent': 'Mozilla/5.0 (compatible; MyPoliticalDigest/1.0)'
              }
            });
            
            if (!feedResponse.ok) {
              continue;
            }
            
            const feedText = await feedResponse.text();
            const parsed = parseRSS(feedText, feedUrl);
            
            articles.push(...parsed);
          } catch (e) {
            // Silently handle feed errors
            console.error(`Error fetching feed ${feedUrl}:`, e);
          }
        }
        
        return {
          id,
          name: politician.name,
          party: politician.party,
          role: politician.role,
          articles: articles.slice(0, 10) // Limit to 10 per politician
        };
      });
      
      const results = await Promise.all(feedPromises);
      
      // Flatten articles for combined list
      const allArticles = [];
      results.forEach(politician => {
        politician.articles.forEach(article => {
          allArticles.push({
            ...article,
            politicianId: politician.id,
            politicianName: politician.name,
            politicianParty: politician.party,
            politicianRole: politician.role
          });
        });
      });
      
      // Sort by date (newest first)
      allArticles.sort((a, b) => {
        const dateA = new Date(a.pubDate);
        const dateB = new Date(b.pubDate);
        return dateB - dateA;
      });
      
      const response = new Response(JSON.stringify({
        articles: allArticles.slice(0, 50), // Limit to 50 total
        politicians: results.filter(p => p.articles.length > 0),
        timestamp: new Date().toISOString()
      }), {
        headers: {
          'Content-Type': 'application/json',
          'Cache-Control': `public, max-age=${CACHE_TTL}`
        }
      });
      
      // Store in cache
      ctx.waitUntil(cache.put(cacheKey, response.clone()));
      
      return response;
      
    } catch (error) {
      return new Response(JSON.stringify({
        error: 'Failed to fetch news',
        message: error.message
      }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' }
      });
    }
  }
};

/**
 * Simple RSS Parser
 * Parses RSS/Atom feeds without external dependencies
 */
function parseRSS(xmlText, feedUrl) {
  const articles = [];
  
  try {
    // Extract channel title for source name
    let sourceName = 'Unknown Source';
    const channelMatch = xmlText.match(/<channel>[\s\S]*?<title>([^<]+)<\/title>/i);
    if (channelMatch) {
      sourceName = channelMatch[1].trim();
    }
    
    // Try Atom format first
    const atomEntries = xmlText.match(/<entry>[\s\S]*?<\/entry>/gi) || [];
    
    for (const entry of atomEntries) {
      const title = extractTag(entry, 'title');
      const link = extractTag(entry, 'link') || extractAttribute(entry, 'link', 'href');
      const pubDate = extractTag(entry, 'published') || extractTag(entry, 'updated');
      
      if (title && link) {
        articles.push({
          title: cleanText(title),
          link: cleanText(link),
          pubDate: pubDate ? new Date(pubDate).toISOString() : new Date().toISOString(),
          sourceName
        });
      }
    }
    
    // If no Atom entries, try RSS format
    if (articles.length === 0) {
      const rssItems = xmlText.match(/<item>[\s\S]*?<\/item>/gi) || [];
      
      for (const item of rssItems) {
        const title = extractTag(item, 'title');
        const link = extractTag(item, 'link');
        const pubDate = extractTag(item, 'pubDate');
        
        if (title) {
          articles.push({
            title: cleanText(title),
            link: cleanText(link) || '',
            pubDate: pubDate ? new Date(pubDate).toISOString() : new Date().toISOString(),
            sourceName
          });
        }
      }
    }
    
  } catch (e) {
    console.error('RSS Parse Error:', e);
  }
  
  return articles;
}

/**
 * Extract content from XML tag
 */
function extractTag(xml, tagName) {
  const regex = new RegExp(`<${tagName}[^>]*>([\\s\\S]*?)<\\/${tagName}>`, 'i');
  const match = xml.match(regex);
  return match ? match[1].trim() : null;
}

/**
 * Extract attribute from XML tag
 */
function extractAttribute(xml, tagName, attrName) {
  const regex = new RegExp(`<${tagName}[^>]*${attrName}=["']([^"']+)["']`, 'i');
  const match = xml.match(regex);
  return match ? match[1] : null;
}

/**
 * Clean text content
 */
function cleanText(text) {
  if (!text) return '';
  return text
    .replace(/<[^>]+>/g, '')
    .replace(/&/g, '&')
    .replace(/</g, '<')
    .replace(/>/g, '>')
    .replace(/"/g, '"')
    .replace(/'/g, "'")
    .trim();
}
