'''
Generate some fake data in json form for our D3.js visualization
'''

import random
import json

distribution = [x**1.5 for x in range(1,6)]
distribution.reverse()

firsts = []
with open('first', 'r') as f:
    for line in f:
        firsts.append(line.strip())

lasts = []
with open('last', 'r') as f:
    for line in f:
        lasts.append(line.strip())

company_list = [ 'Facebook', 'Google', 'Apple', 'IBM', 'blekko' ]

company_departments = {
    'Facebook': ['Engineering', 'Product', 'Ad Sales', 'HR',],
    'Google': ['Engineering', 'Product', 'Legal',],
    'Apple': ['Engineering', 'Product', 'Research',],
    'IBM': ['Watson', 'zSeries', 'pSeries'],
    'blekko': ['Executives', 'Engineering', 'Sales'],
}

actual_friends = { 'Facebook': { 'Engineering':
                                 [ {
                                     'name': 'Bryan O\'Sullivan',
                                     'title': 'Director',
                                     'fb': 'bryan.osullivan',
                                   },
                                 ],
                               },
                   'Google': { 'Legal':
                               [ {
                                   'name': 'Tamara Bedic',
                                   'title': 'Senior Counsel',
                                   'fb': 'tamara.bedic.7',
                                 },
                               ],
                               'Product':
                               [ {
                                   'name': 'Nan Boden',
                                   'title': 'Head of Global Technology Partners',
                                   'fb': 'nan.boden.3',
                                 },
                               ],
                             },
                   'IBM': { 'Watson':
                            [ {
                                'name': 'Rich Skrenta',
                                'title': 'Director',
                                'fb': 'skrenta',
                              },
                            ],
                          },
                   'blekko': { 'Executives':
                               [ {
                                   'name': 'Greg Lindahl',
                                   'title': 'CTO',
                                   'fb': 'greg.lindahl',
                                 },
                               ],
                             },
                   'Apple': { 'Product':
                              [ {
                                  'name': 'Robert Walsh',
                                  'title': 'Senior Evangelist',
                                  'fb': 'rjwalsh3',
                                },
                              ],
                            },
                   }

def get_person(c, d):
    possible = actual_friends.get(c, {}).get(d)
    if possible is not None:
        person = possible[0]
        possible.pop(0)
        if len(possible) == 0:
            del actual_friends[c][d]
        return person

    f = firsts[random.randrange(0, len(firsts))]
    l = lasts[random.randrange(0, len(lasts))]
    return {'name': f+' '+l}

company_d = distribution[:]
j1 = []
for c in company_list:
    c_size = company_d.pop(0)
    department_d = distribution[:]
    j2 = []
    for d in company_departments[c]:
        d_size = department_d.pop(0)
        people_d = distribution[:]
        j3 = []
        for p in range(1,5):
            p_size = people_d.pop(0)
            person = get_person(c, d)
            size = p_size * d_size * c_size * random.uniform(0.75, 1.25)
#            print('name {} title {} fb-id {} department {} company {} size {}'
#                  .format(person['name'], person.get('title'), person.get('fb'), d, c, size))
            person['size'] = size
            j3.append(person)
        j2.append({'name': d, 'children': j3})
    j1.append({'name': c, 'children': j2})

print(json.dumps({'name':'Friends', 'children': j1}))

