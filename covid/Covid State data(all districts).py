#https://api.covid19india.org/state_district_wise.json
import requests
import json
state_name=[]
url='https://api.covid19india.org/state_district_wise.json'
data=requests.get(url).text
dict_state=json.loads(data)
state=input('Enter State Name (Case sensitive):')
for sname in dict_state:
   state_name.append(sname)
if state in state_name:
      dict_dist = dict_state[state]
      for district in dict_dist:
          dists=dict_dist[district]
          # print(dists)
          for data in dists:
              dist = dists[data]
              print(data)
              print('Active Cases:', dist['active'])
              print('Confirmed Cases:', dist['confirmed'])
              print('Deceased Cases:', dist['deceased'])
              print('Recovered Cases:', dist['recovered'])
              print()
