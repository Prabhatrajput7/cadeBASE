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
#driver.find_element_by_name('name').send_keys('Viggy')
driver.find_element_by_css_selector("input[name='name']").send_keys('em')
driver.find_element_by_name('email').send_keys('Viggy@gmail.com')
driver.find_element_by_id('exampleInputPassword1').send_keys('123456789')
driver.find_element_by_id('exampleCheck1').click()
dd = Select(driver.find_element_by_id('exampleFormControlSelect1'))
dd.select_by_visible_text('Female')
dd.select_by_index(0)#male

#driver.find_element_by_id('exampleFormControlSelect1').send_keys('Female')
driver.find_element_by_id('inlineRadio1').click()
driver.find_element_by_name('bday').send_keys('01-01-2000')
driver.find_element_by_xpath("//input[@type='submit']").click()
#print(driver.find_element_by_css_selector("div[class*='alert-success']").text)
print(driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text)

time.sleep(5)
driver.close()
