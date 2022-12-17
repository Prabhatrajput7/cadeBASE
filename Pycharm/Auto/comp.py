import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import csv

driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.randomlists.com/email-addresses')
ps = driver.page_source
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
reg = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$")
emails = []
for i in re.finditer(regex,ps):
    print(i)
    print('*')
    print(i.group())
    emails.append(i.group())
print('############')

# for j in re.findall(regex,ps):
#     print(emails.append(j))

for j,k in enumerate(emails):
    print(f'{j+1} = {k}')

# with open('mycsv.csv', 'w' , newline='') as file:
#     write=csv.writer(file)
#     write.writerow(['Emails'])
#     for i in emails:
#         write.writerow([i])

driver.close()


