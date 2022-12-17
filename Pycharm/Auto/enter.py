from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.google.co.in/')
c = driver.find_elements_by_css_selector('.gLFyf')
for i in c:
    i.send_keys('pokemon')
    i.send_keys(Keys.ENTER)
time.sleep(2)
driver.back()
#c = driver.find_elements_by_css_selector("div[class = 'wM6W7d']")
#driver.find_element_by_css_selector('.gNO89b').click()