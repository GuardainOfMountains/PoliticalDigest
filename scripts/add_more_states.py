#!/usr/bin/env python3
"""Add more states to the JSON data file."""

import json
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_PATH, 'data', 'state-elected-officials.json')

# More states to add
more_states = {
    'maryland': {
        'name': 'Maryland',
        'abbreviation': 'MD',
        'statePartyUrl': 'https://www.mddems.org/',
        'governor': {
            'name': 'Wes Moore',
            'party': 'Democrat',
            'website': 'https://governor.maryland.gov/'
        },
        'lieutenantGovernor': {
            'name': 'Aruna Miller',
            'party': 'Democrat',
            'website': 'https://governor.maryland.gov/'
        },
        'senators': [
            {'name': 'Ben Cardin', 'party': 'Democrat', 'website': 'https://www.cardin.senate.gov/'},
            {'name': 'Chris Van Hollen', 'party': 'Democrat', 'website': 'https://www.vanhollen.senate.gov/'}
        ],
        'representatives': [
            {'name': 'Andy Harris', 'district': 'MD-01', 'party': 'Republican', 'website': 'https://harris.house.gov/'},
            {'name': 'Dutch Ruppersberger', 'district': 'MD-02', 'party': 'Democrat', 'website': 'https://ruppersberger.house.gov/'},
            {'name': 'John Sarbanes', 'district': 'MD-03', 'party': 'Democrat', 'website': 'https://sarbanes.house.gov/'},
            {'name': 'Anthony Brown', 'district': 'MD-04', 'party': 'Democrat', 'website': 'https://anthonybrown.house.gov/'},
            {'name': 'Steny Hoyer', 'district': 'MD-05', 'party': 'Democrat', 'website': 'https://hoyer.house.gov/'},
            {'name': 'David Trone 'MD-06', 'district':', 'party': 'Democrat', 'website': 'https://trone.house.gov/'},
            {'name': 'Jamie Raskin', 'district': 'MD-08', 'party': 'Democrat', 'website': 'https://raskin.house.gov/'}
        ],
        'stateSenateLeader': {'name': 'Mel Griffith', 'position': 'President', 'party': 'Democrat'},
        'stateHouseLeader': {'name': 'Adrienne Jones', 'position': 'Speaker', 'party': 'Democrat'}
    },
    'massachusetts': {
        'name': 'Massachusetts',
        'abbreviation': 'MA',
        'statePartyUrl': 'https://massdems.org/',
        'governor': {
            'name': 'Maura Healey',
            'party': 'Democrat',
            'website': 'https://www.mass.gov/governor'
        },
        'lieutenantGovernor': {
            'name': 'Kim Driscoll',
            'party': 'Democrat',
            'website': 'https://www.mass.gov/ltgovernor'
        },
        'senators': [
            {'name': 'Elizabeth Warren', 'party': 'Democrat', 'website': 'https://www.warren.senate.gov/'},
            {'name': 'Ed Markey', 'party': 'Democrat', 'website': 'https://www.markey.senate.gov/'}
        ],
        'representatives': [
            {'name': 'Richard Neal', 'district': 'MA-01', 'party': 'Democrat', 'website': 'https://neal.house.gov/'},
            {'name': 'Jim McGovern', 'district': 'MA-02', 'party': 'Democrat', 'website': 'https://mcgovern.house.gov/'},
            {'name': 'Lori Trahan', 'district': 'MA-03', 'party': 'Democrat', 'website': 'https://trahan.house.gov/'},
            {'name': 'Katherine Clark', 'district': 'MA-05', 'party': 'Democrat', 'website': 'https://clark.house.gov/'},
            {'name': 'Seth Moulton', 'district': 'MA-06', 'party': 'Democrat', 'website': 'https://moulton.house.gov/'},
            {'name': 'Ayanna Pressley', 'district': 'MA-07', 'party': 'Democrat', 'website': 'https://pressley.house.gov/'},
            {'name': 'Stephen Lynch', 'district': 'MA-08', 'party': 'Democrat', 'website': 'https://lynch.house.gov/'},
            {'name': 'Bill Keating', 'district': 'MA-09', 'party': 'Democrat', 'website': 'https://keating.house.gov/'}
        ],
        'stateSenateLeader': {'name': 'Karen Spilka', 'position': 'President', 'party': 'Democrat'},
        'stateHouseLeader': {'name': 'Ron Mariano', 'position': 'Speaker', 'party': 'Democrat'}
    },
    'michigan': {
        'name': 'Michigan',
        'abbreviation': 'MI',
        'statePartyUrl': 'https://michigandems.com/',
        'governor': {
            'name': 'Gretchen Whitmer',
            'party': 'Democrat',
            'website': 'https://www.michigan.gov/whitmer'
        },
        'lieutenantGovernor': {
            'name': 'Garlin Gilchrist',
            'party': 'Democrat',
            'website': 'https://www.michigan.gov/whitmer/ltgovernor'
        },
        'senators': [
            {'name': 'Debbie Stabenow', 'party': 'Democrat', 'website': 'https://www.stabenow.senate.gov/'},
            {'name': 'Gary Peters', 'party': 'Democrat', 'website': 'https://www.peters.senate.gov/'}
        ],
        'representatives': [
            {'name': 'Jack Bergman', 'district': 'MI-01', 'party': 'Republican', 'website': 'https://bergman.house.gov/'},
            {'name': 'John Moolenaar', 'district': 'MI-02', 'party': 'Republican', 'website': 'https://moolenaar.house.gov/'},
            {'name': 'Bill Huizenga', 'district': 'MI-04', 'party': 'Republican', 'website': 'https://huizenga.house.gov/'},
            {'name': 'Randy Friend', 'district': 'MI-03', 'party': 'Republican', 'website': 'https://friend.house.gov/'},
            {'name': 'Tim Walberg', 'district': 'MI-07', 'party': 'Republican', 'website': 'https://walberg.house.gov/'},
            {'name': 'Dan Kildee', 'district': 'MI-05', 'party': 'Democrat', 'website': 'https://kildee.house.gov/'},
            {'name': 'Debbie Dingell', 'district': 'MI-12', 'party': 'Democrat', 'website': 'https://dingell.house.gov/'},
            {'name': 'Rashida Tlaib', 'district': 'MI-13', 'party': 'Democrat', 'website': 'https://tlaib.house.gov/'},
            {'name': 'Elissa Slotkin', 'district': 'MI-07', 'party': 'Democrat', 'website': 'https://slotkin.house.gov/'}
        ],
        'stateSenateLeader': {'name': 'Sam Singh', 'position': 'Senate Democratic Leader', 'party': 'Democrat'},
        'stateHouseLeader': {'name': 'Joe Tate', 'position': 'Speaker', 'party': 'Democrat'}
    },
    'minnesota': {
        'name': 'Minnesota',
        'abbreviation': 'MN',
        'statePartyUrl': 'https://www.dfl.org/',
        'governor': {
            'name': 'Tim Walz',
            'party': 'Democrat',
            'website': 'https://mn.gov/governor/'
        },
        'lieutenantGovernor': {
            'name': 'Peggy Flanagan',
            'party': 'Democrat',
            'website': 'https://mn.gov/ltgovernor/'
        },
        'senators': [
            {'name': 'Amy Klobuchar', 'party': 'Democrat', 'website': 'https://www.klobuchar.senate.gov/'},
            {'name': 'Tina Smith', 'party': 'Democrat', 'website': 'https://www.smith.senate.gov/'}
        ],
        'representatives': [
            {'name': 'Brad Finstad', 'district': 'MN-01', 'party': 'Republican', 'website': 'https://finstad.house.gov/'},
            {'name': 'Angie Craig', 'district': 'MN-02', 'party': 'Democrat', 'website': 'https://craig.house.gov/'},
            {'name': 'Dean Phillips', 'district': 'MN-03', 'party': 'Democrat', 'website': 'https://phillips.house.gov/'},
            {'name': 'Betty McCollum', 'district': 'MN-04', 'party': 'Democrat', 'website': 'https://mccollum.house.gov/'},
            {'name': 'Ilhan Omar', 'district': 'MN-05', 'party': 'Democrat', 'website': 'https://omar.house.gov/'},
            {'name': 'Tom Emmer', 'district': 'MN-06', 'party': 'Republican', 'website': 'https://emmer.house.gov/'},
            {'name': 'Pete Stauber', 'district': 'MN-08', 'party': 'Republican', 'website': 'https://stauber.house.gov/'}
        ],
        'stateSenateLeader': {'name': 'Karla Bigham', 'position': 'Senate Democratic Leader', 'party': 'Democrat'},
        'stateHouseLeader': {'name': 'Lisa Demuth', 'position': 'Speaker', 'party': 'Republican'}
    },
    'mississippi': {
        'name': 'Mississippi',
        'abbreviation': 'MS',
        'statePartyUrl': 'https://msdemocrats.net/',
        'governor': {
            'name': 'Tate Reeves',
            'party': 'Republican',
            'website': 'https://www.govreeves.com/'
        },
        'lieutenantGovernor': {
            'name': 'Delbert Hosemann',
            'party': 'Republican',
            'website': 'https://www.ltgovernorhosemann.com/'
        },
        'senators': [
            {'name': 'Roger Wicker', 'party': 'Republican', 'website': 'https://www.wicker.senate.gov/'},
            {'name': 'Cindy Hyde-Smith', 'party': 'Republican', 'website': 'https://www.hydesmith.senate.gov/'}
        ],
        'representatives': [
            {'name': 'Trent Kelly', 'district': 'MS-01', 'party': 'Republican', 'website': 'https://trentkelly.house.gov/'},
            {'name': 'Bennie Thompson', 'district': 'MS-02', 'party': 'Democrat', 'website': 'https://benniethompson.house.gov/'},
            {'name': 'Michael Guest', 'district': 'MS-03', 'party': 'Republican', 'website': 'https://guest.house.gov/'},
            {'name': 'Mike Ezell', 'district': 'MS-04', 'party': 'Republican', 'website': 'https://ezell.house.gov/'}
        ],
        'stateSenateLeader': {'name': 'Dean Kirby', 'position': 'President', 'party': 'Republican'},
        'stateHouseLeader': {'name': 'Jason White', 'position': 'Speaker', 'party': 'Republican'}
    },
    'missouri': {
        'name': 'Missouri',
        'abbreviation': 'MO',
        'statePartyUrl': 'https://missouridemocrats.org/',
        'governor': {
            'name': 'Mike Parson',
            'party': 'Republican',
            'website': 'https://www.mo.gov/governor/'
        },
        'lieutenantGovernor': {
            'name': 'Mike Kehoe',
            'party': 'Republican',
            'website': 'https://www.mo.gov/ltgovernor/'
        },
        'senators': [
            {'name': 'Josh Hawley', 'party': 'Republican', 'website': 'https://www.hawley.senate.gov/'},
            {'name': 'Eric Schmitt', 'party': 'Republican', 'website': 'https://www.schmitt.senate.gov/'}
        ],
        'representatives': [
            {'name': 'Sam Graves', 'district': 'MO-06', 'party': 'Republican', 'website': 'https://graves.house.gov/'},
            {'name': 'Ann Wagner', 'district': 'MO-02', 'party': 'Republican', 'website': 'https://wagner.house.gov/'},
            {'name': 'Blaine Luetkemeyer', 'district': 'MO-03', 'party': 'Republican', 'website': 'https://luetkemeyer.house.gov/'},
            {'name': 'Vicky Hartzler', 'district': 'MO-04', 'party': 'Republican', 'website': 'https://hartzler.house.gov/'},
            {'name': 'Emanuel Cleaver', 'district': 'MO-05', 'party': 'Democrat', 'website': 'https://cleaver.house.gov/'},
            {'name': 'Jason Smith', 'district': 'MO-08', 'party': 'Republican', 'website': 'https://jasonsmith.house.gov/'}
        ],
        'stateSenateLeader': {'name': 'Caleb Rowden', 'position': 'President Pro Tempore', 'party': 'Republican'},
        'stateHouseLeader': {'name': 'Dean Plocher', 'position': 'Speaker', 'party': 'Republican'}
    },
    'nevada': {
        'name': 'Nevada',
        'abbreviation': 'NV',
        'statePartyUrl': 'https://nvdems.com/',
        'governor': {
            'name': 'Joe Lombardo',
            'party': 'Republican',
            'website': 'https://gov.nv.gov/'
        },
        'lieutenantGovernor': {
            'name': 'Stavros Anthony',
            'party': 'Republican',
            'website': 'https://ltgov.nv.gov/'
        },
        'senators': [
            {'name': 'Catherine Cortez Masto', 'party': 'Democrat', 'website': 'https://www.cortezmasto.senate.gov/'},
            {'name': 'Jacky Rosen', 'party': 'Democrat', 'website': 'https://www.rosen.senate.gov/'}
        ],
        'representatives': [
            {'name': 'Mark Amodei', 'district': 'NV-02', 'party': 'Republican', 'website': 'https://amodei.house.gov/'},
            {'name': 'Susie Lee', 'district': 'NV-03', 'party': 'Democrat', 'website': 'https://susielee.house.gov/'},
            {'name': 'Steven Horsford', 'district': 'NV-04', 'party': 'Democrat', 'website': 'https://horsford.house.gov/'},
            {'name': 'Dina Titus', 'district': 'NV-01', 'party': 'Democrat', 'website': 'https://titus.house.gov/'}
        ],
        'stateSenateLeader': {'name': 'Pat Spearman', 'position': 'Senate Democratic Leader', 'party': 'Democrat'},
        'stateHouseLeader': {'name': 'Yvonne Nichols', 'position': 'Speaker', 'party': 'Democrat'}
    },
    'new_hampshire': {
        'name': 'New Hampshire',
        'abbreviation': 'NH',
        'statePartyUrl': 'https://nhdp.org/',
        'governor': {
            'name': 'Chris Sununu',
            'party': 'Republican',
            'website': 'https://www.nh.gov/governor/'
        },
        'lieutenantGovernor': {
            'name': 'Dave Wylie',
            'party': 'Republican',
            'website': 'https://www.nh.gov/ltgovernor/'
        },
        'senators': [
            {'name': 'Jeanne Shaheen', 'party': 'Democrat', 'website': 'https://www.shaheen.senate.gov/'},
            {'name': 'Maggie Hassan', 'party': 'Democrat', 'website': 'https://www.hassan.senate.gov/'}
        ],
        'representatives': [
            {'name': 'Chris Pappas', 'district': 'NH-01', 'party': 'Democrat', 'website': 'https://pappas.house.gov/'},
            {'name': 'Annie Kuster', 'district': 'NH-02', 'party': 'Democrat', 'website': 'https://kuster.house.gov/'}
        ],
        'stateSenateLeader': {'name': 'Jade McPhee', 'position': 'Senate President', 'party': 'Republican'},
        'stateHouseLeader': {'name': 'Sherman Packard', 'position': 'Speaker', 'party': 'Republican'}
    },
    'new_jersey': {
        'name': 'New Jersey',
        'abbreviation': 'NJ',
        'statePartyUrl': 'https://www.njdems.org/',
        'governor': {
            'name': 'Phil Murphy',
            'party': 'Democrat',
            'website': 'https://nj.gov/governor/'
        },
        'lieutenantGovernor': {
            'name': 'Tahesha Way',
            'party': 'Democrat',
            'website': 'https://nj.gov/ltgovernor/'
        },
        'senators': [
            {'name': 'Cory Booker', 'party': 'Democrat', 'website': 'https://www.booker.senate.gov/'},
            {'name': 'Bob Menendez', 'party': 'Democrat', 'website': 'https://www.menendez.senate.gov/'}
        ],
        'representatives': [
            {'name': 'Jeff Van Drew', 'district': 'NJ-02', 'party': 'Democrat', 'website': 'https://vandrew.house.gov/'},
            {'name': 'Andy Kim', 'district': 'NJ-03', 'party': 'Democrat', 'website': 'https://kim.house.gov/'},
            {'name': 'Chris Smith', 'district': 'NJ-04', 'party': 'Republican', 'website': 'https://chrissmith.house.gov/'},
            {'name': 'Josh Gottheimer', 'district': 'NJ-05', 'party': 'Democrat', 'website': 'https://gottheimer.house.gov/'},
            {'name': 'Frank Pallone', 'district': 'NJ-06', 'party': 'Democrat', 'website': 'https://pallone.house.gov/'},
            {'name': 'Tom Malinowski', 'district': 'NJ-07', 'party': 'Democrat', 'website': 'https://malinowski.house.gov/'},
            {'name': 'Rob Menendez', 'district': 'NJ-08', 'party': 'Democrat', 'website': 'https://menendez.house.gov/'},
            {'name': 'Donald Payne Jr.', 'district': 'NJ-10', 'party': 'Democrat', 'website': 'https://payne.house.gov/'},
            {'name': 'Mikie Sherrill', 'district': 'NJ-11', 'party': 'Democrat', 'website': 'https://sherrill.house.gov/'},
            {'name': 'Bonnie Watson Coleman', 'district': 'NJ-12', 'party': 'Democrat', 'website': 'https://watsoncoleman.house.gov/'}
        ],
        'stateSenateLeader': {'name': 'Nick Scutari', 'position': 'President', 'party': 'Democrat'},
        'stateHouseLeader': {'name': 'Joe Cryan', 'position': 'Speaker', 'party': 'Democrat'}
    },
    'new_mexico': {
        'name': 'New Mexico',
        'abbreviation': 'NM',
        'statePartyUrl': 'https://nmdemocrats.org/',
        'governor': {
            'name': 'Michelle Lujan Grisham',
            'party': 'Democrat',
            'website': 'https://www.governor.state.nm.us/'
        },
        'lieutenantGovernor': {
            'name': 'Howie Morales',
            'party': 'Democrat',
            'website': 'https://www.governor.state.nm.us/'
        },
        'senators': [
            {'name': 'Martin Heinrich', 'party': 'Democrat', 'website': 'https://www.heinrich.senate.gov/'},
            {'name': 'Ben Ray Lujan', 'party': 'Democrat', 'website': 'https://www.lujan.senate.gov/'}
        ],
        'representatives': [
            {'name': 'Yvette Herrell', 'district': 'NM-02', 'party': 'Republican', 'website': 'https://herrell.house.gov/'},
            {'name': 'Teresa Leger Fernandez', 'district': 'NM-03', 'party': 'Democrat', 'website': 'https://legerfernandez.house.gov/'},
            {'name': 'Melanie Stansbury', 'district': 'NM-01', 'party': 'Democrat', 'website': 'https://stansbury.house.gov/'}
        ],
        'stateSenateLeader': {'name': 'Micheal Sanchez', 'position': 'President Pro Tempore', 'party': 'Democrat'},
        'stateHouseLeader': {'name': 'Javier Martinez', 'position': 'Speaker', 'party': 'Democrat'}
    }
}


def main():
    # Load existing data
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Add more states
    data['states'].update(more_states)
    
    # Save
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    
    print(f'Added {len(more_states)} more states')
    print(f'Total states now: {len(data["states"])}')


if __name__ == '__main__':
    main()
