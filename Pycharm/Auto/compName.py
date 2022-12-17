import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.get('https://500.co/companies')
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.filters')))
name = driver.find_elements_by_css_selector(".company-name")
sector = driver.find_elements_by_xpath("//div[@class='table-rows']/div[@class='grid table-row']/div[2]")
tech = driver.find_elements_by_xpath("//div[@class='table-rows']/div[@class='grid table-row']/div[3]")
country = driver.find_elements_by_xpath("//div[@class='span-3 m-span-12']/div[@class='table-value']")
# for (i, j, k, l) in zip(name, sector, tech, country):
#     print(i.text, j.text, k.text, l.text)

with open('mycsv2.csv', 'w', newline='') as file2:
    write2 = csv.writer(file2)
    write2.writerow(['Name', 'Sector', 'Tech', 'Country'])
    for (i, j, k, l) in zip(name, sector, tech, country):
        write2.writerow([i.text, j.text, k.text, l.text])


driver.close()