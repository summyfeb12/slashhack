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
                                         'photo': 'images/12140690_10153210826061094_4587702233746558384_n.jpg?oh=8bec31684643d1575827b94b78c77a39&oe=58443117',
                                     },
                                 ],
                                 'Product':
                                 [
                                     {
                                         'name': 'Daniel Swarz',
                                         'title': 'Director of Product', 
                                         'fb': 'egone',
                                         'photo': 'images/14100301_10154588604180809_2613854826243197204_n.jpg?oh=967fbf15b62cf0c2137cc1736a42051b&oe=5838F00F',
                                     },
                                 ],
                                 'Ad Sales':
                                 [
                                     {
                                         'name': 'David Chang',
                                         'title': 'Director of Sales', 
                                         'fb': '688221624',
                                         'photo': 'images/1384057_10151654028851625_1082069571_n.jpg?oh=deb7f26210f906ea592c9130f45f5ce3&oe=583B122B',
                                     },
                                 ],
                               },
                   'Google': { 'Engineering':
                               [
                                   {
                                       'name': 'Keith Peters',
                                       'title': 'Senior MTS', 
                                       'fb': 'keith.peters',
                                       'photo': 'images/166850_478856718239_26766_n.jpg?oh=35f4f581b9cd9975d6cdfcca0ecf1ae2&oe=585A8C15',
                                   },
                               ],
                               'Legal':
                               [
                                   {
                                       'name': 'Tamara Bedic',
                                       'title': 'Senior Counsel',
                                       'fb': 'tamara.bedic.7',
                                       'photo': 'images/1916459_100529223306560_1995663_n.jpg?oh=e9d3cbca8f91abda66ab2ce2addc9e3e&oe=58492397',
                                   },
                               ],
                               'Product':
                               [
                                   {
                                       'name': 'Nan Boden',
                                       'title': 'Head of Global Technology Partners',
                                       'fb': 'nan.boden.3',
                                       'photo': 'images/1622684_10200931693849516_1042634274_n.jpg?oh=6936c9c06e66e884c96da0adc36926af&oe=58477F79',
                                   },
                               ],
                             },
                   'IBM': { 'Watson':
                            [
                                {
                                    'name': 'Rich Skrenta',
                                    'title': 'Director',
                                    'fb': 'skrenta',
                                    'photo': 'images/10669235_10152782613176934_4156726262375851453_o.jpg',
                                },
                            ],
                          },
                   'blekko': { 'Executives':
                               [
                                   {
                                       'name': 'Greg Lindahl',
                                       'title': 'CTO',
                                       'fb': 'greg.lindahl',
                                       'photo': 'images/12239386_10153370710981925_4214944586379720169_o.jpg',
                                   },
                               ],
                             },
                   'Apple': { 'Engineering':
                              [
                                  {
                                      'name': 'Robert Walsh',
                                      'title': 'Senior Evangelist',
                                      'fb': 'rjwalsh3',
                                      'photo': 'images/13873074_10208220799612291_2535004613615237585_n.jpg?oh=49c7a78d93bddaff787948129d4bcd69&oe=58595F56',
                                  },
                              ],
                              'Product':
                              [
                                  {
                                      'name': 'Adrianna Gould',
                                      'title': 'Product Manager',
                                      'fb': 'gould.adrianna',
                                      'photo': 'images/13912419_10207925809076356_953239921339769129_n.jpg?oh=79c9dadb0990c1d6c58eb233848c7ae5&oe=58411105',
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

