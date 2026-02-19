#!/usr/bin/env python3
"""
Generate state elected officials pages from JSON data.

Usage:
    python scripts/generate_state_pages.py
"""

import json
import os
import re
from datetime import datetime

# Base path
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_PATH, 'data', 'state-elected-officials.json')
OUTPUT_DIR = os.path.join(BASE_PATH, 'public', 'articles')

# Pennsylvania template sections for reference
# This generates pages in similar style

def generate_state_page(state_data):
    """Generate HTML page for a state."""
    name = state_data['name']
    abbrev = state_data['abbreviation'].lower()
    
    # Count Democrats
    dem_senators = [s for s in state_data['senators'] if s['party'] == 'Democrat']
    dem_reps = [r for r in state_data['representatives'] if r['party'] == 'Democrat']
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} Democratic Elected Officials — My Political Digest</title>
  <meta name="description" content="A comprehensive guide to {name}'s Democratic elected officials at the state and federal levels.">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,600;0,700;1,400&family=Work+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="../css/styles.css">
</head>
<body>
  <!-- Progress Bar -->
  <div class="progress-bar" id="progressBar"></div>

  <header class="site-header">
    <div class="container">
      <div class="brand"><a href="../index.html">My Political Digest</a></div>
      <button class="menu-toggle" aria-expanded="false" aria-label="Toggle menu">☰</button>
      <nav class="nav">
        <ul class="nav-list">
          <li><a href="../index.html">Home</a></li>
          <li><a href="../article.html">Articles</a></li>
          <li><a href="../state.html">State</a></li>
          <li><a href="../federal.html">Federal</a></li>
          <li><a href="../about.html">About</a></li>
          <li><button id="themeToggle" class="theme-toggle" aria-label="Toggle theme">🌙 Dark</button></li>
        </ul>
      </nav>
    </div>
  </header>

  <main class="article">
    <!-- Article Header -->
    <header class="article-header">
      <div class="container">
        <span class="article-category">State Politics</span>
        <h1>{name}'s Democratic Elected Officials</h1>
        <p class="article-subtitle">A guide to the Democrats representing {name} at the state and federal levels.</p>
        <div class="article-meta">
          <time datetime="{datetime.now().strftime('%Y-%m-%d')}">{datetime.now().strftime('%B %d, %Y')}</time>
          <span class="separator">•</span>
          <span class="read-time">5 min read</span>
        </div>
      </div>
    </header>

    <!-- THE FACTS - Grey -->
    <section class="section section-facts">
      <div class="container">
        <div class="section-label facts-label">The Facts</div>
        <div class="article-content">
          <p>{name}'s Democratic Party represents a significant portion of the state's electorate. Below is a list of current Democratic elected officials from {name}.</p>
          
          <div class="quote-block" style="border-left-color: var(--purple-500); background: var(--purple-50); padding: var(--space-4); border-radius: var(--radius-md); margin: var(--space-4) 0;">
            <strong>📝 For Complete Lists:</strong> For the full {name} Democratic Party directory, visit the official <a href="{state_data['statePartyUrl']}" target="_blank">{name} Democratic Party website</a>.
          </div>

'''
    
    # Governor & Lieutenant Governor
    if state_data['governor']['party'] == 'Democrat':
        html += f'''          <h3>Governor & Lieutenant Governor</h3>
          <p>The executive branch leadership.</p>
          
          <table class="data-table" style="margin: var(--space-4) 0;">
            <thead>
              <tr>
                <th>Name</th>
                <th>Position</th>
                <th>Official Website</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>{state_data['governor']['name']}</strong></td>
                <td>Governor</td>
                <td><a href="{state_data['governor']['website']}" target="_blank">Website</a></td>
              </tr>
'''
        if state_data['lieutenantGovernor'].get('name') and state_data['lieutenantGovernor'].get('name') != 'Position does not exist':
            html += f'''              <tr>
                <td><strong>{state_data['lieutenantGovernor']['name']}</strong></td>
                <td>Lieutenant Governor</td>
                <td><a href="{state_data['lieutenantGovernor'].get('website', '#')}" target="_blank">Website</a></td>
              </tr>
'''
        html += '''            </tbody>
          </table>

'''
    
    # U.S. Senate
    html += f'''          <h3>U.S. Senate</h3>
          <p>{name}'s U.S. Senators.</p>
          
          <table class="data-table" style="margin: var(--space-4) 0;">
            <thead>
              <tr>
                <th>Name</th>
                <th>Party</th>
                <th>Official Website</th>
              </tr>
            </thead>
            <tbody>
'''
    for senator in state_data['senators']:
        html += f'''              <tr>
                <td><strong>{senator['name']}</strong></td>
                <td>{senator['party']}</td>
                <td><a href="{senator['website']}" target="_blank">Website</a></td>
              </tr>
'''
    html += '''            </tbody>
          </table>

'''
    
    # U.S. House Representatives
    dem_reps = [r for r in state_data['representatives'] if r['party'] == 'Democrat']
    if dem_reps:
        html += f'''          <h3>U.S. House Representatives</h3>
          <p>Democratic members of the U.S. House of Representatives from {name}.</p>
          
          <table class="data-table" style="margin: var(--space-4) 0;">
            <thead>
              <tr>
                <th>Name</th>
                <th>District</th>
                <th>Official Website</th>
              </tr>
            </thead>
            <tbody>
'''
        for rep in dem_reps:
            html += f'''              <tr>
                <td><strong>{rep['name']}</strong></td>
                <td>{rep['district']}</td>
                <td><a href="{rep['website']}" target="_blank">Website</a></td>
              </tr>
'''
        html += '''            </tbody>
          </table>

'''
    
    # State Senate
    if state_data['stateSenateLeader']['party'] == 'Democrat':
        html += f'''          <h3>{name} State Senate</h3>
          <p>Democratic leadership in the {name} State Senate.</p>
          
          <table class="data-table" style="margin: var(--space-4) 0;">
            <thead>
              <tr>
                <th>Name</th>
                <th>Position</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>{state_data['stateSenateLeader']['name']}</strong></td>
                <td>{state_data['stateSenateLeader']['position']}</td>
              </tr>
            </tbody>
          </table>

'''
    
    # State House
    if state_data['stateHouseLeader']['party'] == 'Democrat':
        html += f'''          <h3>{name} House of Representatives</h3>
          <p>Democratic leadership in the {name} House.</p>
          
          <table class="data-table" style="margin: var(--space-4) 0;">
            <thead>
              <tr>
                <th>Name</th>
                <th>Position</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>{state_data['stateHouseLeader']['name']}</strong></td>
                <td>{state_data['stateHouseLeader']['position']}</td>
              </tr>
            </tbody>
          </table>

'''
    
    # Statistics
    total_dems = len(dem_senators) + len(dem_reps)
    html += f'''          <div class="stat-highlight" style="margin: var(--space-4) 0;">
            <span class="stat-number">{len(dem_reps)}</span>
            <span class="stat-label">Democratic U.S. House Members</span>
          </div>
          <div class="stat-highlight" style="margin: var(--space-4) 0;">
            <span class="stat-number">{len(dem_senators)}</span>
            <span class="stat-label">Democratic U.S. Senators</span>
          </div>
        </div>
      </div>
    </section>

    <!-- PERSPECTIVE 1 -->
    <section class="section section-perspective-1">
      <div class="container">
        <div class="section-label perspective-label-1">Democratic Priorities</div>
        <div class="perspective-context">
          <h3>Key Democratic Issues in {name}</h3>
          <p>Democrats in {name} focus on issues that resonate with their constituents.</p>
        </div>
        <div class="article-content">
          <p>The Democratic Party in {name} works on a range of issues important to their constituents, including economic opportunity, healthcare access, education, and environmental protection.</p>
          
          <h3>Key Priorities</h3>
          <ul>
            <li><strong>Healthcare:</strong> Expanding access and lowering costs</li>
            <li><strong>Education:</strong> Supporting public schools and workforce development</li>
            <li><strong>Economy:</strong> Creating jobs and supporting small businesses</li>
            <li><strong>Environment:</strong> Protecting natural resources</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- THE NUANCE -->
    <section class="section section-analysis">
      <div class="container">
        <div class="section-label analysis-label">The Nuance</div>
        <div class="article-content">
          <h3>Political Landscape in {name}</h3>
          <p>{name}'s political dynamics create both opportunities and challenges for Democrats.</p>

          <div class="info-grid" style="margin: var(--space-6) 0;">
            <div class="info-item">
              <div class="info-label">Urban Areas</div>
              <div class="info-value">Strong Democratic Support</div>
              <p style="margin-top: var(--space-2); font-size: var(--text-sm);">Major cities tend to vote Democratic in {name}</p>
            </div>
            <div class="info-item">
              <div class="info-label">Suburban Districts</div>
              <div class="info-value">Competitive</div>
              <p style="margin-top: var(--space-2); font-size: var(--text-sm);">Suburban voters increasingly important</p>
            </div>
          </div>

          <h3>Regional Differences</h3>
          <ul>
            <li><strong>Urban vs. Rural:</strong> Different priorities between metropolitan and rural areas</li>
            <li><strong>Economic Concerns:</strong> Balancing growth with preservation</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- REFLECTION -->
    <section class="section section-reflection">
      <div class="container">
        <div class="section-label reflection-label">Reflection</div>
        <div class="article-content">
          <h3>Questions for Readers</h3>
          <ul>
            <li>Who represents you at the federal or state level?</li>
            <li>Do you feel your representative accurately reflects your views?</li>
            <li>What issues would you like to see {name} Democrats prioritize?</li>
          </ul>
          
          <div class="reflection-box">
            <p><em>Consider: How do you evaluate whether your representatives are effectively advocating for your interests?</em></p>
          </div>

          <h3 style="margin-top: var(--space-6);">Explore More</h3>
          <p>Learn about Democrats across the country:</p>
          <ul>
            <li><a href="democratic-party-members.html">Democratic Party Members in Congress</a></li>
            <li><a href="pa-elected-officials.html">Pennsylvania Democrats</a></li>
            <li><a href="minimum-wage.html">The Minimum Wage Debate</a></li>
          </ul>
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>© 2026 My Political Digest — Multiple Perspectives</p>
      <nav class="footer-nav">
        <a href="#">About</a>
        <a href="#">Privacy</a>
        <a href="#">Contact</a>
      </nav>
    </div>
  </footer>

  <script src="../js/script.js"></script>
</body>
</html>
'''
    
    return html


def main():
    """Main function to generate state pages."""
    # Load data
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    states = data.get('states', {})
    print(f"Found {len(states)} states in data file")
    
    # Generate pages
    for state_key, state_data in states.items():
        name = state_data['name']
        abbrev = state_data['abbreviation'].lower()
        
        # Generate filename: al-elected-officials.html
        filename = f"{abbrev}-elected-officials.html"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        html = generate_state_page(state_data)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"Generated: {filename}")
    
    print(f"\nDone! Generated {len(states)} state pages.")


if __name__ == '__main__':
    main()
