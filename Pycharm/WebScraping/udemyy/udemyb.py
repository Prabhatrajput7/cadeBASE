import requests
import pprint
from bs4 import BeautifulSoup
# import time
# import csv

# def books():
#     l =[]
#     for i in range(1,2):
#         url = f'http://books.toscrape.com/catalogue/page-{i}.html'
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         names = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
#         for name in names:
#             href = name.article.h3.a.get('href')
#             title = name.article.h3.a.get('title')
#             title = name.article.h3.a.get_text()
#             price = name.find('div', class_='product_price').p.text.replace('Â','')
#             stock = name.find('p', class_='instock availability').text.strip()
#             l.append({'Link': href, 'Title': title, 'Price': price, 'Stock': stock})
#     return l
#
# c = books()
# print(c)
import csv
import psycopg2
try:
    conn = psycopg2.connect(host='localhost' ,dbname='booksrap', user='postgres', port='5432', password = 'pikachu')
    cur = conn.cursor()
    sql = 'select * from bobs'
    cur.execute(sql)
    print(cur)
    # with open('mycsv2.csv', 'w', newline='', encoding="utf-8") as file2:
    #     write2 = csv.writer(file2)
    #     write2.writerow(i[0] for i in cur.description)
    #     write2.writerows(cur)
    # cur.execute("CREATE TABLE Bobs (link VARCHAR(255), title VARCHAR(255), price VARCHAR(255),stock VARCHAR(255))")
    # sql = 'INSERT INTO Bobs (link, title, price, stock) VALUES (%s, %s, %s, %s)'
    # for i in c:
    #     val = (i['Link'], i['Title'], i['Price'], i['Stock'])
    #     cur.execute(sql, val)
    # conn.commit()
    # print('Done')
except Exception as error:
    print(error)












# with open('books.csv', 'w',encoding="utf-8",newline='') as file:
#     cs = csv.writer(file)
#     cs.writerow(['link','title','price','stock'])
#     for i in c:
#         cs.writerow([i['Link'],i['Title'],i['Price'],i['Stock']])




