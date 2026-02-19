"""
Source Manager for Guard1/PoliticalDigest

Provides a unified interface to both RSS feeds (feeds.json) and 
reference sources (democratic-sources.json).

Usage:
    from sources import SourceManager
    
    manager = SourceManager()
    
    # Get all RSS feeds
    feeds = manager.get_all_feeds()
    
    # Get reference sources by category
    sources = manager.get_reference_sources(category='party')
    
    # Get sources by tier
    tier1_sources = manager.get_reference_sources(tier=1)
    
    # Lookup by name
    source = manager.get_source_by_name('Democratic National Committee')
"""

import json
import os
from typing import List, Dict, Optional, Any


class SourceManager:
    """
    Manages both RSS feeds and reference sources for the PoliticalDigest project.
    
    Provides methods to:
    - get_all_feeds(): Get all RSS feed sources
    - get_reference_sources(): Get filtered reference sources
    - get_source_by_name(): Look up a source by name
    """
    
    def __init__(self, base_path: Optional[str] = None):
        """
        Initialize SourceManager with paths to JSON files.
        
        Args:
            base_path: Base directory path. Defaults to project root.
        """
        if base_path is None:
            # Determine base path relative to this file
            base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        self.base_path = base_path
        self.feeds_path = os.path.join(base_path, 'public', 'feeds.json')
        self.sources_path = os.path.join(base_path, 'data', 'democratic-sources.json')
        
        # Load data files
        self._feeds_data = None
        self._sources_data = None
    
    def _load_feeds(self) -> Dict[str, Any]:
        """Load feeds.json data."""
        if self._feeds_data is None:
            try:
                with open(self.feeds_path, 'r', encoding='utf-8') as f:
                    self._feeds_data = json.load(f)
            except FileNotFoundError:
                self._feeds_data = {}
            except json.JSONDecodeError:
                self._feeds_data = {}
        return self._feeds_data
    
    def _load_sources(self) -> Dict[str, Any]:
        """Load democratic-sources.json data."""
        if self._sources_data is None:
            try:
                with open(self.sources_path, 'r', encoding='utf-8') as f:
                    self._sources_data = json.load(f)
            except FileNotFoundError:
                self._sources_data = {"sources": []}
            except json.JSONDecodeError:
                self._sources_data = {"sources": []}
        return self._sources_data
    
    def get_all_feeds(self) -> List[Dict[str, Any]]:
        """
        Get all RSS feeds combining feeds.json and democratic-sources.json.
        
        Returns feeds in format:
        [
            {'name': ..., 'url': ..., 'party': ..., 'role': ...},
            ...
        ]
        
        Duplicate feeds are removed by URL.
        """
        feeds = {}
        
        # Add feeds from feeds.json (politician feeds)
        feeds_data = self._load_feeds()
        for key, value in feeds_data.items():
            if isinstance(value, dict) and 'feeds' in value:
                for feed_url in value.get('feeds', []):
                    if feed_url and feed_url not in ['https://example.com/feed.xml', '']:
                        feeds[feed_url] = {
                            'name': value.get('name', key),
                            'url': feed_url,
                            'party': value.get('party'),
                            'role': value.get('role'),
                            'source': 'feeds.json'
                        }
        
        # Add feeds from democratic-sources.json
        sources_data = self._load_sources()
        for source in sources_data.get('sources', []):
            if source.get('has_rss') and source.get('rss_url'):
                rss_url = source['rss_url']
                if rss_url and rss_url not in feeds:  # Avoid duplicates
                    feeds[rss_url] = {
                        'name': source.get('name'),
                        'url': rss_url,
                        'category': source.get('category'),
                        'tier': source.get('tier'),
                        'source': 'democratic-sources.json'
                    }
        
        return list(feeds.values())
    
    def get_reference_sources(
        self, 
        category: Optional[str] = None, 
        tier: Optional[int] = None,
        has_rss: Optional[bool] = None
    ) -> List[Dict[str, Any]]:
        """
        Get filtered reference sources from democratic-sources.json.
        
        Args:
            category: Filter by category (party, data, caucus, etc.)
            tier: Filter by tier (1, 2, or 3)
            has_rss: Filter by whether source has RSS feed
            
        Returns:
            List of source dictionaries
        """
        sources_data = self._load_sources()
        sources = sources_data.get('sources', [])
        
        filtered = []
        for source in sources:
            if category is not None and source.get('category') != category:
                continue
            if tier is not None and source.get('tier') != tier:
                continue
            if has_rss is not None and source.get('has_rss') != has_rss:
                continue
            filtered.append(source)
        
        return filtered
    
    def get_source_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Look up a source by exact name match.
        
        Args:
            name: Source name to search for
            
        Returns:
            Source dictionary if found, None otherwise
        """
        sources_data = self._load_sources()
        for source in sources_data.get('sources', []):
            if source.get('name') == name:
                return source
        return None
    
    def get_source_by_id(self, source_id: str) -> Optional[Dict[str, Any]]:
        """
        Look up a source by ID.
        
        Args:
            source_id: Source ID to search for
            
        Returns:
            Source dictionary if found, None otherwise
        """
        sources_data = self._load_sources()
        for source in sources_data.get('sources', []):
            if source.get('id') == source_id:
                return source
        return None
    
    def get_sources_by_category(self, category: str) -> List[Dict[str, Any]]:
        """
        Get all sources in a specific category.
        
        Args:
            category: Category to filter by
            
        Returns:
            List of sources in that category
        """
        return self.get_reference_sources(category=category)
    
    def get_tier_sources(self, tier: int) -> List[Dict[str, Any]]:
        """
        Get all sources at a specific tier.
        
        Args:
            tier: Tier level (1, 2, or 3)
            
        Returns:
            List of sources at that tier
        """
        return self.get_reference_sources(tier=tier)
    
    def get_rss_sources(self) -> List[Dict[str, Any]]:
        """
        Get all sources that have RSS feeds.
        
        Returns:
            List of sources with RSS feeds
        """
        return self.get_reference_sources(has_rss=True)
    
    def reload(self) -> None:
        """Force reload of all data files."""
        self._feeds_data = None
        self._sources_data = None
    
    def get_stats(self) -> Dict[str, int]:
        """
        Get statistics about loaded sources.
        
        Returns:
            Dictionary with counts of feeds and sources
        """
        feeds = self.get_all_feeds()
        sources_data = self._load_sources()
        sources = sources_data.get('sources', [])
        
        # Count by category
        categories = {}
        for s in sources:
            cat = s.get('category', 'unknown')
            categories[cat] = categories.get(cat, 0) + 1
        
        # Count by tier
        tiers = {}
        for s in sources:
            tier = s.get('tier', 0)
            tiers[tier] = tiers.get(tier, 0) + 1
        
        # Count by RSS availability
        rss_count = sum(1 for s in sources if s.get('has_rss'))
        
        return {
            'total_feeds': len(feeds),
            'total_sources': len(sources),
            'sources_with_rss': rss_count,
            'by_category': categories,
            'by_tier': tiers
        }


# Convenience function for quick access
def get_feeds() -> List[Dict[str, Any]]:
    """Get all feeds using default SourceManager."""
    return SourceManager().get_all_feeds()


def get_sources(category: Optional[str] = None, tier: Optional[int] = None) -> List[Dict[str, Any]]:
    """Get reference sources using default SourceManager."""
    return SourceManager().get_reference_sources(category=category, tier=tier)


if __name__ == '__main__':
    # Test the SourceManager
    manager = SourceManager()
    
    print("=== Source Manager Stats ===")
    stats = manager.get_stats()
    print(f"Total feeds: {stats['total_feeds']}")
    print(f"Total sources: {stats['total_sources']}")
    print(f"Sources with RSS: {stats['sources_with_rss']}")
    print(f"By category: {stats['by_category']}")
    print(f"By tier: {stats['by_tier']}")
    
    print("\n=== All Feeds ===")
    for feed in manager.get_all_feeds()[:5]:
        print(f"  - {feed['name']}: {feed['url']}")
    
    print("\n=== Tier 1 Sources ===")
    for source in manager.get_tier_sources(1):
        print(f"  - {source['name']} ({source['category']})")
