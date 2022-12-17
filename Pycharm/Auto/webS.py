from bs4 import BeautifulSoup as bs
import re
import requests

url = requests.get('https://docs.python.org/3/library/random.html')
soup = bs(url.text,'html.parser')

names = soup.body.findAll('dt')
disc = soup.body.findAll('dd')
fxname =re.findall('id="random.\w+',str(names))
fxname = [i[4:] for i in fxname]
lst = []
for i in disc:
    i = i.text
    i =i.replace('\n',' ')
    lst.append(i)

for j,k in enumerate(lst):
    print(f'{fxname[j]} = {k}')