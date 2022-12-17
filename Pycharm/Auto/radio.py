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

rb = driver.find_elements_by_name('radioButton')
rb[2].click()
assert rb[2].is_selected()

assert driver.find_element_by_id('displayed-text').is_displayed()
driver.find_element_by_id('hide-textbox').click()
assert not driver.find_element_by_id('displayed-text').is_displayed()
