#https://api.covid19india.org/state_district_wise.json
import requests
import json
url='https://api.covid19india.org/state_district_wise.json'
data=requests.get(url).text

dict=json.loads(data)
s=input('Enter State name for data access(Case sensitive):')
i=input('Enter District name (Case Sensitive):')
state = dict[s]

dists=state['districtData']
dist=dists[i]
print('Active Cases:',dist['active'])
print('Confirmed Cases:',dist['confirmed'])
print('Deceased Cases:',dist['deceased'])
print('Recovered Cases:',dist['recovered'])
