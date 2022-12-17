from bs4 import BeautifulSoup

def giving_data(res,res2):
    soup = BeautifulSoup(res.text, 'html.parser')
    soup2 = BeautifulSoup(res2.text, 'html.parser')
    links = soup.select('.titlelink')
    links2 = soup2.select('.titlelink')
    subtext = soup.select('.subtext')
    subtext2 = soup2.select('.subtext')
    megalink = links + links2
    megasub = subtext + subtext2
    return megalink,megasub

