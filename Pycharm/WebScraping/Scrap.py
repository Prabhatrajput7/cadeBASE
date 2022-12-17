import requests
import pprint
from send_data import giving_data

url1,url2 = 'https://news.ycombinator.com/','https://news.ycombinator.com/news?p=2'
args = (requests.get(url1),requests.get(url2))
mlink ,msub = giving_data(*args)

def custom_points(links, subtext):
    lst = []
    for i, j in enumerate(links):
        title = links[i].getText()
        href = links[i].get('href',None)
        vote = subtext[i].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 100:
                lst.append({'Points':points,title: href })
    return sorted(lst,key=lambda x:x['Points'],reverse=True)

pprint.pprint(custom_points(mlink , msub))