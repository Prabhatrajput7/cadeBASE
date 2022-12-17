import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.find_element_by_link_text('Shop').click()
names = driver.find_elements_by_xpath("//h4[@class='card-title']/a")
price = driver.find_elements_by_xpath("//div[@class='card-body']/h5")
lst = []
for i,j in zip(names,price):
    txt = str(j.text[1:])#a = float(txt[1:])
    lst.append(txt)
    if i.text == 'Blackberry':
        i.find_element_by_xpath('parent::h4 // parent::div // parent::div / div[2] / button').click()
print(f'Total coast of all device>> '+str(sum(float(i) for i in lst)))
driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()
driver.find_element_by_css_selector("button[class='btn btn-success']").click()
driver.find_element_by_css_selector("#country").send_keys('ind')
wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.LINK_TEXT,'India')))
driver.find_element_by_link_text('India').click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("input[class*='btn-success']").click()
tx = driver.find_element_by_css_selector("div[class*='alert-dismissible']").text
assert 'Success! Thank you!' in tx


