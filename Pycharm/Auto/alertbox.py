import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
t = 'buddy'
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.find_element_by_css_selector('#name').send_keys(t)
driver.find_element_by_id('alertbtn').click()
at = driver.switch_to.alert
time.sleep(2)
#al_txt = at.text
assert t in at.text
at.accept()
#at.dismiss()  to click on cancel button in a pop up
