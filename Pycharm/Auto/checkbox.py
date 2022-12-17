import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
c = driver.find_elements_by_xpath("//input[@type='checkbox']")
for i in c:
    if i.get_attribute('value') == 'option2':
        i.click()
        assert i.is_selected()



