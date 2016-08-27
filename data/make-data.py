'''
Generate some fake data in json form for our D3.js visualization
'''

import random
import json
import math

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
    'Google': ['Engineering', 'Legal', 'Product',],
    'Apple': ['Engineering', 'Product', 'Research',],
    'IBM': ['Watson', 'zSeries', 'pSeries'],
    'blekko': ['Executives', 'Engineering', 'Sales'],
}

actual_friends = { 'Facebook': { 'Engineering':
                                 [
                                     {
                                         'name': 'Bryan O\'Sullivan',
                                         'title': 'Director',
                                         'fb': 'bryan.osullivan',
                                         'photo': 'https://www.facebook.com/photo.php?fbid=10153210826061094&set=a.440993296093.224463.645786093&type=3&theater',
                                     },
                                 ],
                                 'Product':
                                 [
                                     {
                                         'name': 'Daniel Swarz',
                                         'title': 'Director of Product', 
                                         'fb': 'egone',
                                         'photo': 'https://www.facebook.com/photo.php?fbid=10154588604180809&set=a.494442720808.261304.525565808&type=3&theater',
                                     },
                                 ],
                                 'Ad Sales':
                                 [
                                     {
                                         'name': 'David Chang',
                                         'title': 'Director of Sales', 
                                         'fb': '688221624',
                                         'photo': 'https://www.facebook.com/photo.php?fbid=10151654028851625&set=a.458849106624.235499.688221624&type=3&theater'
                                     },
                                 ],
                               },
                   'Google': { 'Engineering':
                               [
                                   {
                                       'name': 'Keith Peters',
                                       'title': 'Senior MTS', 
                                       'fb': 'keith.peters',
                                       'photo': 'https://www.facebook.com/photo.php?fbid=478856718239&set=a.425296008239.206578.588163239&type=3&theater',
                                   },
                               ],
                               'Legal':
                               [
                                   {
                                       'name': 'Tamara Bedic',
                                       'title': 'Senior Counsel',
                                       'fb': 'tamara.bedic.7',
                                       'photo': 'https://www.facebook.com/photo.php?fbid=100529223306560&set=a.154092251283590.34421.100000484480494&type=3&theater',
                                   },
                               ],
                               'Product':
                               [
                                   {
                                       'name': 'Nan Boden',
                                       'title': 'Head of Global Technology Partners',
                                       'fb': 'nan.boden.3',
                                       'photo': 'https://scontent.xx.fbcdn.net/v/t1.0-1/c0.34.160.160/p160x160/1622684_10200931693849516_1042634274_n.jpg?oh=6936c9c06e66e884c96da0adc36926af&oe=58477F79',
                                   },
                               ],
                             },
                   'IBM': { 'Watson':
                            [
                                {
                                    'name': 'Rich Skrenta',
                                    'title': 'Director',
                                    'fb': 'skrenta',
                                    'photo': 'https://www.facebook.com/photo.php?fbid=10152782613176934&set=a.459302176933.248914.500211933&type=3&theater',
                                },
                            ],
                          },
                   'blekko': { 'Executives':
                               [
                                   {
                                       'name': 'Greg Lindahl',
                                       'title': 'CTO',
                                       'fb': 'greg.lindahl',
                                       'photo': 'https://www.facebook.com/photo.php?fbid=10153370710981925&set=a.426806721924.210554.589041924&type=3&theater'
                                   },
                               ],
                             },
                   'Apple': { 'Engineering':
                              [
                                  {
                                      'name': 'Robert Walsh',
                                      'title': 'Senior Evangelist',
                                      'fb': 'rjwalsh3',
                                      'photo': 'https://www.facebook.com/photo.php?fbid=10208220799612291&set=a.1514341413100.72410.1071372811&type=3&theater',
                                  },
                              ],
                              'Product':
                              [
                                  {
                                      'name': 'Adrianna Gould',
                                      'title': 'Product Manager',
                                      'fb': 'gould.adrianna',
                                      'photo': 'https://www.facebook.com/photo.php?fbid=10207925809076356&set=a.1482888465440.2071825.1030692829&type=3&theater',
                                  },
                              ],
                            }
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
        num_friends = d_size * c_size * random.uniform(0.75, 1.25) # 121 += 25%
        num_friends = num_friends / 121.0 / 1.25 # now 0-1
        num_friends = int(math.sqrt(num_friends) * 4.5) + 2
        for p in range(1,num_friends):
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

