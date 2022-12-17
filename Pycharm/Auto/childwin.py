import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/windows')
driver.find_element_by_link_text("Click Here").click()
child = driver.window_handles[1]
driver.switch_to.window(child)
print(driver.find_element_by_tag_name('h3').text)
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_tag_name('h3').text)
driver.quit()