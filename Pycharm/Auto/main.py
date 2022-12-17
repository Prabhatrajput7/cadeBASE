import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.seleniumeasy.com/test/')
item = driver.find_element_by_link_text('Input Forms').click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Simple Form Demo"))
    )
    element.click()
    search = driver.find_element_by_class_name('form-control')
    search.send_keys('test')
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-default"))
    )
    element.click()
    time.sleep(5)
finally:
    driver.quit()


