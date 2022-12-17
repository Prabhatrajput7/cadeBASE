from bs4 import BeautifulSoup
import requests
import pprint
import csv

res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.titlelink')
links2 = soup2.select('.titlelink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

megalink = links + links2
megasub = subtext + subtext2





def custom_points(links, subtext):
    lst = []
    for i, j in enumerate(links):
        title = links[i].getText()
        href = links[i].get('href', None)
        vote = subtext[i].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 100:
                lst.append({'Points':points,'link': href,'Title': title })
    pprint.pprint(lst)
    # saving(lst)
    #return sorted(lst,key=lambda x:x['Points'],reverse=True)

#pprint.pprint(custom_points(megalink , megasub))

def saving(lst):
    with open('data.csv', 'w', newline='') as file2:
        write2 = csv.writer(file2)
        write2.writerow(['Points','Title','Link'])
        for i in lst:
            write2.writerow([i.get('Points'),i.get('Title'),i.get('link')])

custom_points(megalink , megasub)