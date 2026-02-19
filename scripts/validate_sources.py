#!/usr/bin/env python3
"""
Source Validation Script

Validates the democratic-sources.json file for:
- Valid JSON syntax
- Required fields present
- URL format validation
- Optional URL reachability testing

Usage:
    python scripts/validate_sources.py [--check-urls] [--timeout TIMEOUT]
    
Options:
    --check-urls     Test URL reachability (slower)
    --timeout TIMEOUT  Timeout for URL checks in seconds (default: 10)
"""

import json
import sys
import os
import re
import argparse
from typing import Dict, List, Any, Tuple
from urllib.parse import urlparse


# Required fields for each source
REQUIRED_FIELDS = [
    'id',
    'name',
    'category',
    'url',
    'tier',
    'has_rss',
    'last_verified'
]

# Optional fields
OPTIONAL_FIELDS = [
    'rss_url',
    'description',
    'social_media',
    'notes'
]

# Valid category values
VALID_CATEGORIES = [
    'party',
    'caucus',
    'progressive',
    'labor',
    'civil-rights',
    'environmental',
    'voting',
    'think-tank',
    'data',
    'news'
]

# Valid tier values
VALID_TIERS = [1, 2, 3]


def load_json_file(filepath: str) -> Tuple[bool, Any, str]:
    """
    Load and parse a JSON file.
    
    Returns:
        (success, data, error_message)
    """
    if not os.path.exists(filepath):
        return False, None, f"File not found: {filepath}"
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return True, data, ""
    except json.JSONDecodeError as e:
        return False, None, f"JSON parse error: {e}"
    except Exception as e:
        return False, None, f"Error reading file: {e}"


def validate_url(url: str) -> Tuple[bool, str]:
    """
    Validate URL format.
    
    Returns:
        (is_valid, error_message)
    """
    if not url:
        return False, "URL is empty"
    
    try:
        result = urlparse(url)
        if not result.scheme:
            return False, "URL missing scheme (http/https)"
        if result.scheme not in ['http', 'https']:
            return False, f"Invalid scheme: {result.scheme}"
        if not result.netloc:
            return False, "URL missing domain"
        return True, ""
    except Exception as e:
        return False, f"URL parse error: {e}"


def check_url_reachable(url: str, timeout: int = 10) -> Tuple[bool, str]:
    """
    Check if a URL is reachable.
    
    Note: This is a basic check and may not work for all URLs due to
    firewalls, bot protection, etc.
    
    Returns:
        (is_reachable, message)
    """
    try:
        import urllib.request
        import urllib.error
        
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Guard1-SourceValidator/1.0'}
        )
        
        response = urllib.request.urlopen(req, timeout=timeout)
        status_code = response.getcode()
        
        if status_code == 200:
            return True, f"Reachable (status: {status_code})"
        else:
            return False, f"Status code: {status_code}"
            
    except urllib.error.HTTPError as e:
        return False, f"HTTP Error: {e.code} {e.reason}"
    except urllib.error.URLError as e:
        return False, f"URL Error: {e.reason}"
    except Exception as e:
        return False, f"Error: {str(e)}"


def validate_source(source: Dict[str, Any], index: int) -> List[str]:
    """
    Validate a single source entry.
    
    Returns:
        List of error messages (empty if valid)
    """
    errors = []
    source_id = source.get('id', f'index_{index}')
    
    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in source:
            errors.append(f"Source '{source_id}': Missing required field '{field}'")
    
    # Validate ID format (kebab-case)
    if 'id' in source:
        if not re.match(r'^[a-z0-9-]+$', source['id']):
            errors.append(f"Source '{source_id}': ID should be kebab-case (a-z, 0-9, hyphens)")
    
    # Validate category
    if 'category' in source:
        if source['category'] not in VALID_CATEGORIES:
            errors.append(
                f"Source '{source_id}': Invalid category '{source['category']}'. "
                f"Valid: {VALID_CATEGORIES}"
            )
    
    # Validate tier
    if 'tier' in source:
        if source['tier'] not in VALID_TIERS:
            errors.append(
                f"Source '{source_id}': Invalid tier '{source['tier']}'. "
                f"Valid: {VALID_TIERS}"
            )
    
    # Validate main URL
    if 'url' in source:
        is_valid, msg = validate_url(source['url'])
        if not is_valid:
            errors.append(f"Source '{source_id}': Invalid URL - {msg}")
    
    # Validate RSS URL if has_rss is True
    if source.get('has_rss') and source.get('rss_url'):
        is_valid, msg = validate_url(source['rss_url'])
        if not is_valid:
            errors.append(f"Source '{source_id}': Invalid RSS URL - {msg}")
    
    # If has_rss is True but no rss_url, that's an error
    if source.get('has_rss') and not source.get('rss_url'):
        errors.append(f"Source '{source_id}': has_rss is True but rss_url is missing")
    
    # If rss_url is provided but has_rss is False, that's inconsistent
    if not source.get('has_rss') and source.get('rss_url'):
        errors.append(f"Source '{source_id}': has_rss is False but rss_url is provided")
    
    return errors


def validate_sources_file(
    filepath: str, 
    check_urls: bool = False,
    url_timeout: int = 10
) -> Tuple[bool, List[str]]:
    """
    Validate the sources JSON file.
    
    Returns:
        (is_valid, list_of_errors)
    """
    errors = []
    
    # Load JSON
    success, data, msg = load_json_file(filepath)
    if not success:
        return False, [msg]
    
    # Check top-level structure
    if 'sources' not in data:
        return False, ["Missing 'sources' array in JSON"]
    
    sources = data['sources']
    if not isinstance(sources, list):
        return False, ["'sources' should be an array"]
    
    if len(sources) == 0:
        errors.append("Warning: No sources defined")
    
    # Validate each source
    for i, source in enumerate(sources):
        source_errors = validate_source(source, i)
        errors.extend(source_errors)
    
    # Check for duplicate IDs
    ids = [s.get('id') for s in sources if 'id' in s]
    if len(ids) != len(set(ids)):
        duplicates = [x for x in ids if ids.count(x) > 1]
        errors.append(f"Duplicate source IDs: {set(duplicates)}")
    
    # Optional: Check URLs if requested
    if check_urls:
        print(f"\n=== Checking URL reachability (timeout: {url_timeout}s) ===")
        url_errors = []
        
        for source in sources:
            source_id = source.get('id', 'unknown')
            
            # Check main URL
            if 'url' in source:
                print(f"Checking {source_id} main URL...", end=" ")
                is_reachable, msg = check_url_reachable(source['url'], url_timeout)
                if not is_reachable:
                    url_errors.append(f"Source '{source_id}' URL: {msg}")
                    print(f"FAIL ({msg})")
                else:
                    print(f"OK")
            
            # Check RSS URL if present
            if source.get('has_rss') and source.get('rss_url'):
                print(f"Checking {source_id} RSS URL...", end=" ")
                is_reachable, msg = check_url_reachable(source['rss_url'], url_timeout)
                if not is_reachable:
                    url_errors.append(f"Source '{source_id}' RSS: {msg}")
                    print(f"FAIL ({msg})")
                else:
                    print(f"OK")
        
        if url_errors:
            errors.extend(["\n=== URL Reachability Issues ==="])
            errors.extend(url_errors)
    
    return len(errors) == 0, errors


def main():
    parser = argparse.ArgumentParser(
        description='Validate democratic-sources.json'
    )
    parser.add_argument(
        '--check-urls',
        action='store_true',
        help='Test URL reachability (slower)'
    )
    parser.add_argument(
        '--timeout',
        type=int,
        default=10,
        help='Timeout for URL checks in seconds'
    )
    parser.add_argument(
        '--file',
        default='data/democratic-sources.json',
        help='Path to sources JSON file'
    )
    
    args = parser.parse_args()
    
    # Determine file path
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(base_path, args.file)
    
    print(f"=== Validating {filepath} ===")
    
    is_valid, errors = validate_sources_file(
        filepath,
        check_urls=args.check_urls,
        url_timeout=args.timeout
    )
    
    if is_valid:
        print("\n[PASS] Validation PASSED")
        return 0
    else:
        print("\n[FAIL] Validation FAILED")
        for error in errors:
            print(f"  - {error}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
