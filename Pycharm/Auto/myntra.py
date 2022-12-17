from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.myntra.com/myntra-fashion-store?f=Gender%3Amen%2Cmen%20women')
time.sleep(3)
product = driver.find_elements_by_xpath("//span[@class='product-discountedPrice']")
lst,d =[],{}
for i in product:
    lst.append(i.text)
d = sum([int(i.split('. ')[1]) for i in lst][:3])
print(d)