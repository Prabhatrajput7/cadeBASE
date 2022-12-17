import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.get('https://test.salesforce.com/')
driver.find_element_by_css_selector('#username').send_keys('hello')
driver.find_element_by_css_selector('.password').send_keys('*****')
driver.find_element_by_link_text('Forgot Your Password?').click()
driver.find_element_by_xpath("//input[@type='button']").click()
# print(driver.find_element_by_xpath("//div[@id='usernamegroup']/label").text)
# print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
# print(driver.find_element_by_css_selector("div[id='usernamegroup'] label").text)
# print(driver.find_element_by_xpath("//form[@name='login']/label").text)
time.sleep(2)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)
driver.close()



