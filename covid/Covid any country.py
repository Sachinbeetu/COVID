from bs4 import BeautifulSoup
import requests
url = 'https://www.worldometers.info/coronavirus/'
r = requests.get(url)
html = r.content
# print(html)
soup=BeautifulSoup(html,'html.parser')
title=str(soup.title)
nt=title.split()
print('Enter Country Name(First letter should be capital)')
print('It shows error when site data is not fully updated')
country = input('Country Name: ')
print('World')
print('Live cases : ',nt[3])
print('Total Deaths : ',nt[6])
p = soup.find_all('tr')
for line in p:
    line=line.text.split()
    if country in line:
        break
        #print(line)
print("\n",country)
if int(line[0]) > 18:
    line[0]=int(line[0])+1
    print('Place:',line[0])
else :
    print('Place:',line[0])
print('Total cases today:',line[2])
print('New Cases',line[3])
print('Deaths: ',line[4])
print('Recovered :',line[6])
print('Total tests Done:',line[12])
print('Total Active cases:',line[8])
print('Data taken from: https://www.worldometers.info/coronavirus/')