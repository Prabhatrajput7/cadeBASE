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
driver.find_element_by_name('name').send_keys('hello')
#assert driver.find_element_by_name('name').get_attribute('value') == 'hello'
#js involves
print(driver.execute_script('return document.getElementsByName("name")[0].value'))
cl = driver.find_element_by_link_text('Shop')
#driver.execute_script(arguments[0#acccess cl],cl,xyz)
driver.execute_script('arguments[0].click();',cl)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
