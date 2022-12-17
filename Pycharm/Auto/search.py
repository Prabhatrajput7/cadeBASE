import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
driver.find_element_by_id('autosuggest').send_keys('ind')
# driver.find_element_by_id('autosuggest').clear()
#driver.find_element_by_css_selector("input[id='autosuggest']").send_keys('ind')
time.sleep(2)
c = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
for i in c:
    if i.text == 'India':
        i.click()
        break
assert driver.find_element_by_id('autosuggest').get_attribute('value') == "India"