import requests
from bs4 import BeautifulSoup

url = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(url.text, 'html.parser')
# comt = "<p>this is a comment</p>"
# soup2 = BeautifulSoup(comt)
# print(soup2.p.string)
# exit()

#print(soup.body)
#print(soup.find_all('a',class_='titlelink'))
links = soup.select('.titlelink')
points = soup.select('')


#.children is generator
#.content list
#.string to get test
#stripped_string remove unwanted spaces and enter work same as string
#.parent and #.parents [gen] itm.name for i in parents
#siblings next sibling previsous sibling

# print(links)
# for i in links:
#     print(i.get('href'))

# for f in links:
#     print(i.get_text())

