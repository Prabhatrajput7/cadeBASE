import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/iframe')
driver.switch_to.frame('mce_0_ifr')
driver.find_element_by_xpath("//body[@id = 'tinymce']").clear()
driver.find_element_by_xpath("//body[@id = 'tinymce']").send_keys('yo yo')
driver.switch_to.default_content()
print(driver.find_element_by_xpath("//div[@class = 'example']/h3").text)
#print(driver.find_element_by_tag_name('h3').text)