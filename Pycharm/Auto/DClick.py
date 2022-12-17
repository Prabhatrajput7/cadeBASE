from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.get('https://chercher.tech/practice/practice-pop-ups-selenium-webdriver')
action = ActionChains(driver)
action.double_click(driver.find_element_by_id('double-click')).perform()
a = driver.switch_to.alert
time.sleep(1)
a.accept()
