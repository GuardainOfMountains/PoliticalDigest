# Democratic Party Information Sources - Integration Plan

## Executive Summary

This document outlines a comprehensive plan to integrate 100+ Democratic Party information sources into the Guard1/PoliticalDigest project. The plan addresses the current architecture gaps and provides a structured approach for organizing sources by type, priority, and content purpose.

---

## Source Categorization (100+ Sources)

### Category 1: National Party Organizations (5 sources)
| Source | URL | RSS | Tier | Purpose |
|--------|-----|-----|------|---------|
| DNC | democrats.org | ✓ | 1 | Official party platform, news |
| DCCC | dccc.org | ✓ | 1 | House campaign news |
| DSCC | dscc.org | ✓ | 1 | Senate campaign news |
| DGA | democraticgovernors.org | ✓ | 1 | Governor campaign news |
| DLCC | dlcc.org | ✓ | 1 | State legislature news |

### Category 2: State Democratic Parties (56 sources)
- All 50 states + DC + 5 territories (Puerto Rico, US Virgin Islands, Guam, American Samoa, Northern Mariana Islands)
- Most do NOT have RSS feeds
- Primary use: Reference links for state-level content
- Tier: 2 for battleground states, 3 for others

### Category 3: Congressional Caucuses (7 sources)
| Source | URL | RSS | Tier | Purpose |
|--------|-----|-----|------|---------|
| Congressional Progressive Caucus | progressives.house.gov | ✗ | 2 | Progressive policy positions |
| Congressional Black Caucus | cbc.house.gov | ✗ | 2 | Black community issues |
| Congressional Hispanic Caucus | chc.house.gov | ✗ | 2 | Hispanic/Latino issues |
| CAPAC | capac.house.gov | ✗ | 2 | Asian American issues |
| New Democrat Coalition | newdemocratcoalition.house.gov | ✗ | 2 | Moderate positions |
| Blue Dog Coalition | bluedogcaucus-costa.house.gov | ✗ | 2 | Centrist positions |
| Problem Solvers Caucus | problemsolverscaucus.house.gov | ✗ | 2 | Bipartisan solutions |

### Category 4: Progressive Organizations (7 sources)
| Source | URL | RSS | Tier | Purpose |
|--------|-----|-----|------|---------|
| Our Revolution | ourrevolution.com | ✓ | 3 | Progressive activism |
| Justice Democrats | justicedemocrats.com | ✓ | 3 | Primary challenges |
| Sunrise Movement | sunrisemovement.org | ✓ | 3 | Climate action |
| Indivisible | indivisible.org | ✓ | 3 | Grassroots organizing |
| MoveOn | moveon.org | ✓ | 3 | Progressive advocacy |
| Democracy for America | democracyforamerica.com | ✓ | 3 | Progressive candidates |
| Working Families Party | workingfamilies.org | ✓ | 3 | Economic populism |

### Category 5: Labor Organizations (4 sources)
| Source | URL | RSS | Tier | Purpose |
|--------|-----|-----|------|---------|
| AFL-CIO | aflcio.org | ✓ | 2 | Labor union positions |
| SEIU | seiu.org | ✓ | 2 | Service workers |
| AFT | aft.org | ✓ | 2 | Teachers/education |
| NEA | nea.org | ✓ | 2 | Education professionals |

### Category 6: Civil Rights & Social Justice (5 sources)
| Source | URL | RSS | Tier | Purpose |
|--------|-----|-----|------|---------|
| NAACP | naacp.org | ✓ | 2 | Civil rights |
| ACLU | aclu.org | ✓ | 2 | Civil liberties |
| Human Rights Campaign | hrc.org | ✓ | 2 | LGBTQ+ rights |
| Planned Parenthood | plannedparenthood.org | ✓ | 2 | Reproductive rights |
| EMILY's List | emilyslist.org | ✓ | 2 | Pro-choice women candidates |

### Category 7: Environmental Organizations (3 sources)
| Source | URL | RSS | Tier | Purpose |
|--------|-----|-----|------|---------|
| Sierra Club | sierraclub.org | ✓ | 2 | Environmental protection |
| League of Conservation Voters | lcv.org | ✓ | 2 | Environmental scorecard |
| NRDC | nrdc.org | ✓ | 2 | Environmental law |

### Category 8: Voting Rights Organizations (3 sources)
| Source | URL | RSS | Tier | Purpose |
|--------|-----|-----|------|---------|
| Brennan Center | brennancenter.org | ✓ | 2 | Voting rights research |
| Fair Fight | fairfight.com | ✓ | 3 | Election protection |
| Common Cause | commoncause.org | ✓ | 2 | Democracy reform |

### Category 9: Think Tanks & Policy (7 sources)
| Source | URL | RSS | Tier | Purpose |
|--------|-----|-----|------|---------|
| CAP | americanprogress.org | ✓ | 2 | Progressive policy |
| Brookings | brookings.edu | ✓ | 2 | Centrist research |
| Urban Institute | urban.org | ✓ | 2 | Social policy |
| EPI | epi.org | ✓ | 2 | Labor economics |
| CBPP | cbpp.org | ✓ | 2 | Budget policy |
| Roosevelt Institute | rooseveltinstitute.org | ✓ | 3 | Progressive economics |
| Third Way | thirdway.org | ✓ | 3 | Moderate Dem policy |

### Category 10: Data & Research - Election (4 sources)
| Source | URL | RSS | Tier | Purpose |
|--------|-----|-----|------|---------|
| FiveThirtyEight | fivethirtyeight.com | ✓ | 1 | Polling/forecasting |
| Cook Political Report | cookpolitical.com | ✗ | 2 | Election ratings |
| RealClearPolitics | realclearpolitics.com | ✓ | 1 | Polling averages |
| Ballotpedia | ballotpedia.org | ✓ | 1 | Election info |

### Category 11: Data & Research - Voting/Campaign (4 sources)
| Source | URL | RSS | Tier | Purpose |
|--------|-----|-----|------|---------|
| GovTrack | govtrack.us | ✗ | 1 | Voting records |
| OpenSecrets | opensecrets.org | ✗ | 1 | Campaign finance |
| Follow the Money | followthemoney.org | ✗ | 2 | State finance data |
| ProPublica | propublica.org | ✓ | 1 | Investigative journalism |

### Category 12: News Sources - Mainstream (5 sources)
| Source | URL | RSS | Tier | Purpose |
|--------|-----|-----|------|---------|
| MSNBC | msnbc.com | ✓ | 3 | Liberal news |
| CNN Politics | cnn.com/politics | ✓ | 3 | Political news |
| Politico | politico.com | ✓ | 2 | Political news |
| The Hill | thehill.com | ✓ | 3 | Congressional news |
| Roll Call | rollcall.com | ✓ | 3 | Congressional news |

### Category 13: News Sources - Progressive (5 sources)
| Source | URL | RSS | Tier | Purpose |
|--------|-----|-----|------|---------|
| The Nation | thenation.com | ✓ | 3 | Progressive commentary |
| Mother Jones | motherjones.com | ✓ | 3 | Progressive investigation |
| American Prospect | prospect.org | ✓ | 3 | Liberal policy |
| Talking Points Memo | talkingpointsmemo.com | ✓ | 3 | Political news |
| Daily Kos | dailykos.com | ✓ | 3 | Progressive activism |

---

## JSON Schema Design

### New File: `reference/democratic-sources.json`

```json
{
  "version": "1.0",
  "lastUpdated": "2026-02-19",
  "description": "Democratic Party information sources for Guard1/PoliticalDigest",
  "sources": {
    // Each source entry follows this schema:
    "dnc": {
      "id": "dnc",
      "name": "Democratic National Committee",
      "url": "https://democrats.org/",
      "category": "party",
      "tier": 1,
      "hasRss": true,
      "rssUrl": "https://democrats.org/feed/",
      "contentTypes": ["party-platform", "policy-positions", "news"],
      "updateFrequency": "daily",
      "isActive": true,
      "description": "Official national Democratic Party organization"
    }
  }
}
```

### Schema Field Definitions

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique identifier (kebab-case) |
| name | string | yes | Display name |
| url | string | yes | Main website URL |
| category | enum | yes | Source category |
| tier | number | yes | Priority tier (1-3) |
| hasRss | boolean | yes | Whether RSS feed exists |
| rssUrl | string | no | RSS feed URL if hasRss=true |
| contentTypes | array | yes | Types of content available |
| updateFrequency | enum | yes | How often content updates |
| isActive | boolean | yes | Whether source is accessible |
| description | string | no | Brief description |

### Category Enum Values
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

### Update Frequency Enum Values
- `realtime` - Multiple times per day
- `daily` - Once per day
- `weekly` - Once per week
- `monthly` - Once per month
- `quarterly` - Four times per year
- `annually` - Once per year

---

## Priority Tiers

### Tier 1: High Priority (Primary Sources)
- All official party organizations (DNC, DCCC, DSCC, DGA, DLCC)
- Primary data sources (FiveThirtyEight, RealClearPolitics, GovTrack, OpenSecrets, Ballotpedia, ProPublica)
- Congressional official sites (Senate.gov, House.gov)

**Use Case**: Breaking news, official announcements, verified data

### Tier 2: Medium Priority (Reference Sources)
- Congressional caucuses
- Major issue organizations (labor, civil rights, environmental, voting)
- Think tanks (CAP, Brookings, EPI, etc.)
- Mainstream news (Politico)
- State parties in battleground states

**Use Case**: Policy research, background information, perspective gathering

### Tier 3: Lower Priority (Supplementary)
- Progressive news outlets
- Progressive activist organizations
- Most state parties (non-battleground)
- Secondary news sources

**Use Case**: Understanding progressive movement, tracking activist positions

---

## Content Type Mapping

| Content Type | Primary Sources | Update Frequency |
|--------------|-----------------|------------------|
| Policy Positions | DNC Platform, CAP, think tanks | Monthly/Annually |
| Voting Records | GovTrack, Congress.gov | Daily |
| Campaign Finance | OpenSecrets, Follow the Money | Quarterly |
| Polling Data | FiveThirtyEight, RCP | Daily/Weekly |
| State-Level Info | State party websites | Weekly |
| Biographical | Ballotpedia, Congress.gov | Monthly |
| News/Press Releases | DNC, DCCC, state parties | Daily |
| Progressive Perspectives | Progressive orgs, progressive news | Daily |

---

## Cross-Reference Strategy

### Source Verification Rules
1. **Biographical facts** → Cross-reference Ballotpedia + Congress.gov + official sites
2. **Policy positions** → Cross-reference official party platform + think tank analysis
3. **Voting records** → Cross-reference GovTrack + Congress.gov + OpenSecrets
4. **Campaign finance** → Cross-reference OpenSecrets + Follow the Money + FEC
5. **Polling** → Cross-reference FiveThirtyEight + RCP + individual polls
6. **Election ratings** → Cross-reference Cook + FiveThirtyEight + Ballotpedia

### Source Attribution Guidelines
- Always cite official sources for factual claims
- Distinguish between party platform and individual member views
- Note when sources represent specific factions within party
- Include source URLs in article references

---

## Integration with Existing Architecture

### Option A: Extend feeds.json (Not Recommended)
Current structure only handles politicians. Adding 100+ orgs would:
- Mix organization feeds with politician feeds
- Complicate the worker logic
- Make feeds.json harder to maintain

### Option B: Separate Source Database (Recommended)
Create new `reference/democratic-sources.json`:
- Separates organization sources from politician feeds
- Allows rich metadata (categories, tiers, content types)
- Can be extended for Republican sources later
- Works with existing article template

### Implementation Phases

**Phase 1: Core Structure** (Priority: High)
1. Create `reference/democratic-sources.json` schema
2. Add Tier 1 sources (party orgs + data sources)
3. Update article templates to reference sources

**Phase 2: Expanded Coverage** (Priority: Medium)
1. Add Tier 2 sources (caucuses, issue orgs, think tanks)
2. Add RSS feeds for active sources to feeds.json (as new section)
3. Create source citation component

**Phase 3: Full Integration** (Priority: Lower)
1. Add Tier 3 sources
2. Create source lookup utility
3. Add source attribution to all articles

---

## Usage Guidelines for Guard1 Articles

### Do:
- ✓ Use Tier 1 sources for factual claims
- ✓ Cross-reference with official voting records
- ✓ Cite specific sources for policy positions
- ✓ Distinguish between party platform and individual views
- ✓ Show diversity within Democratic coalition

### Don't:
- ✗ Conflate progressive wing with entire party
- ✗ Ignore moderate/centrist Democrats
- ✗ Cherry-pick quotes without context
- ✗ Use single source for controversial claims
- ✗ Assume all Democrats hold same views

### Source Attribution Format
```html
<cite>
  <a href="https://democrats.org/where-we-stand/party-platform/" target="_blank">
    Democratic Party Platform
  </a>
</cite>
```

---

## Summary

This plan provides a comprehensive framework for integrating 100+ Democratic Party information sources into the Guard1/PoliticalDigest project. Key recommendations:

1. **Create new database**: `reference/democratic-sources.json` with structured metadata
2. **Prioritize sources**: Tier system based on reliability and content value
3. **Separate RSS from references**: Only ~25% of sources have useful RSS feeds
4. **Cross-reference strategy**: Always verify with official sources
5. **Phased implementation**: Start with Tier 1, expand over time

The architecture supports future expansion for Republican sources and additional political data.
