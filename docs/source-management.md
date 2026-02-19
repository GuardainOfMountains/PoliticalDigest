# Source Management Documentation

## Overview

This document explains how to manage information sources in the Guard1/PoliticalDigest project.

## File Structure

```
project-root/
├── public/
│   └── feeds.json           # Active RSS feed subscriptions (politicians)
├── data/
│   └── democratic-sources.json  # Structured reference database (all sources)
├── src/
│   └── sources.py           # SourceManager Python class
├── scripts/
│   └── validate_sources.py  # Validation script
└── workers/
    └── news-aggregator/
        └── worker.js        # Cloudflare Worker for fetching feeds
```

## Purpose of Each File

### feeds.json (`public/feeds.json`)

Contains **active RSS feed subscriptions** for politicians. This is what the news aggregator actually fetches.

- Only contains entries with valid RSS feeds
- Organized by politician ID
- Should NOT contain organizational sources

Example entry:
```json
{
  "josh-shapiro": {
    "name": "Josh Shapiro",
    "party": "Democrat",
    "state": "Pennsylvania",
    "role": "Governor",
    "feeds": ["https://www.governor.pa.gov/news/feed/"]
  }
}
```

### democratic-sources.json (`data/democratic-sources.json`)

Contains **structured reference database** of all information sources.

- Includes ALL sources (RSS and non-RSS)
- Rich metadata: category, tier, description, social media
- Organized by source ID
- Supports filtering by category, tier, RSS availability

Example entry:
```json
{
  "id": "dnc",
  "name": "Democratic National Committee",
  "category": "party",
  "url": "https://democrats.org/",
  "tier": 1,
  "has_rss": true,
  "rss_url": "https://democrats.org/feed/",
  "description": "Official national Democratic Party organization",
  "social_media": {
    "twitter": "@TheDemocrats"
  },
  "notes": "Primary source for party platform",
  "last_verified": "2026-02-19"
}
```

## Source Schema

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier (kebab-case) |
| `name` | string | Display name |
| `category` | string | Category (see below) |
| `url` | string | Main website URL |
| `tier` | integer | Priority tier (1, 2, or 3) |
| `has_rss` | boolean | Whether RSS feed exists |
| `last_verified` | string | Date last verified (YYYY-MM-DD) |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `rss_url` | string | RSS feed URL (if has_rss is true) |
| `description` | string | Brief description |
| `social_media` | object | Social media handles |
| `notes` | string | Internal notes |

### Category Values

- `party` - National/state party organizations
- `caucus` - Congressional caucuses
- `progressive` - Progressive activist organizations
- `labor` - Labor unions
- `civil-rights` - Civil rights organizations
- `environmental` - Environmental groups
- `voting` - Voting rights organizations
- `think-tank` - Policy research organizations
- `data` - Election data and research
- `news` - News sources

### Tier Values

- **Tier 1**: Official party sites, data sources (GovTrack, OpenSecrets, FiveThirtyEight)
- **Tier 2**: Caucuses, major issue orgs, think tanks, battleground state parties
- **Tier 3**: Progressive news, activist organizations, non-battleground states

## Using SourceManager

### Python Usage

```python
from src.sources import SourceManager

# Initialize (loads both feeds.json and democratic-sources.json)
manager = SourceManager()

# Get all RSS feeds (combines both files)
feeds = manager.get_all_feeds()

# Get reference sources by category
party_sources = manager.get_reference_sources(category='party')

# Get sources by tier
tier1 = manager.get_reference_sources(tier=1)

# Get sources with RSS
rss_sources = manager.get_reference_sources(has_rss=True)

# Lookup by name
dnc = manager.get_source_by_name('Democratic National Committee')

# Get statistics
stats = manager.get_stats()
```

### Feed Format

The `get_all_feeds()` method returns feeds in this format:

```python
[
    {
        'name': 'Josh Shapiro',
        'url': 'https://www.governor.pa.gov/news/feed/',
        'party': 'Democrat',
        'role': 'Governor',
        'source': 'feeds.json'
    },
    {
        'name': 'Democratic National Committee',
        'url': 'https://democrats.org/feed/',
        'category': 'party',
        'tier': 1,
        'source': 'democratic-sources.json'
    }
]
```

## Adding New Sources

### Step 1: Add to democratic-sources.json

Add the new source to `data/democratic-sources.json`:

```json
{
  "id": "new-source-id",
  "name": "New Source Name",
  "category": "data",
  "url": "https://example.com/",
  "tier": 2,
  "has_rss": true,
  "rss_url": "https://example.com/feed/",
  "description": "Description of the source",
  "last_verified": "2026-02-19"
}
```

### Step 2: Validate

Run the validation script:

```bash
python scripts/validate_sources.py
```

### Step 3: Add to feeds.json (if has RSS)

If the source has an RSS feed and should be actively fetched:

Add to `public/feeds.json`:

```json
{
  "new-source-id": {
    "name": "New Source Name",
    "party": "Democrat",
    "state": null,
    "role": "Organization",
    "feeds": ["https://example.com/feed/"]
  }
}
```

## Validation Script

### Basic Validation

```bash
python scripts/validate_sources.py
```

### With URL Check

```bash
python scripts/validate_sources.py --check-urls
```

### With Custom Timeout

```bash
python scripts/validate_sources.py --check-urls --timeout 5
```

## Maintenance Tips

1. **Regular verification**: Run `--check-urls` monthly to detect broken links
2. **Update last_verified**: When you verify a source, update this date
3. **Tier reviews**: Periodically review tier assignments as source importance changes
4. **New sources**: Follow the "Adding New Sources" process above

## Troubleshooting

### SourceManager can't find files

Ensure you're running from the project root directory, or pass the correct base_path:

```python
manager = SourceManager('/path/to/project/root')
```

### feeds.json not loading

The SourceManager gracefully falls back to empty data if feeds.json is missing. Check the file path.

### Duplicate feeds

The SourceManager automatically deduplicates feeds by URL. If you see duplicates, check both files.

## Future Enhancements

- Add Republican sources (data/republican-sources.json)
- Add automated URL monitoring
- Add source ranking/quality metrics
- Add API endpoint for source queries
