from bs4 import BeautifulSoup
# with open('index.html', 'r') as file:
#     soup = BeautifulSoup(file, 'html.parser')
# print(soup.prettify()) #prettify() indentation
# t1 = soup.title
# t1.string = 'Pycharm'
# print(soup.title)
#
# p = soup.find_all('p')
# plen = len(soup.find_all('p'))
# print(p.find_all('b'))
# for i in range(plen):
#     print(p[i].find_all('b'))
import re
import requests
import pprint
# res = requests.get(
#     'https://www.flipkart.com/asus-zephyrus-s17-2021-core-i9-11th-gen-32-gb-3-tb-ssd-windows-10-home-16-gb-graphics-nvidia-geforce-rtx-3080-gx703hs-kf058ts-gaming-laptop/p/itmffc55c5cb7288?pid=COMG5C28GNFDHZUP&lid=LSTCOMG5C28GNFDHZUPPF1WD5&marketplace=FLIPKART&q=nvidia+geforce+rtx+3080&store=search.flipkart.com&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_5_4_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_5_4_na_na_na&fm=SEARCH&iid=b62ada63-5c4d-4ab1-a52f-6f3c29a8db4f.COMG5C28GNFDHZUP.SEARCH&ppt=clp&ppn=the-non-fiction-store&ssid=ol84nn9f4w0000001637388960676&qH=8eb35487d38f83e1')
# soup2 = BeautifulSoup(res.text, 'html.parser')
# price = soup2.find_all(text="₹")
# print(price[0].parent)#[0] as it use list


########################################################################################################################

# with open('index2.html', 'r') as file:
#     soup3 = BeautifulSoup(file, 'html.parser')

# tag = soup3.find('option')
# print(tag.attrs)
# print(tag)
# tag['value'] = 'new new'
# tag['selected'] = 'yeah'
# tag.string = 'typo'
# print(tag)

# tags = soup3.find_all(['p','div'])
# optiontag = soup3.find_all(['option'], text='Undergraduate',value="undergraduate")
# print(tags,optiontag)

# ctag = soup3.find(class_='btn-item')
# print(ctag.attrs['href'])

# dollar = soup3.find_all(text=re.compile('\$.*'), limit=1)
# for i in dollar:
#     print(i.strip())

# change = soup3.find_all('input', type="text")
# for i in change:
#     i['placeholder'] = 'I changed you'
#
# with open('change.html', 'w') as file2:
#     file2.write(str(soup3))
#####################################################################################################################

# res2 = requests.get('https://coinmarketcap.com/')
# soup4 = BeautifulSoup(res2.text,'html.parser')

#tbody = soup4.tbody
#print(tbody)
# tbodyinside = tbody.contents #gives a list of tags inside tbody
# print(tbodyinside[0].next_sibling) #siblings all next rap it in list with using s
# print(tbodyinside[1].previous_sibling)
# print(list(tbodyinside[0].descendants))
#down children contents descendants
# prices = soup4.find_all('div', class_= "sc-131di3y-0 cLgOOr")
# for i in prices:
#     print(i.string[1:])
# tbody = soup4.tbody
# crypto = {}
# for i in tbody.contents[:10]:
#     name, price = i.contents[2:4]
#     cname = name.p.string
#     cprice = price.a.string
#     crypto[cname] = cprice
# print(crypto)
######################################################################################################################

