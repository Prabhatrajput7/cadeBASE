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
driver.find_element_by_css_selector("a[href*='shop']").click()
mobile = driver.find_elements_by_xpath("//div[@class='card h-100']")
for i in mobile:
    pn = i.find_element_by_xpath("div/h4/a").text
    if pn == 'Blackberry':
        i.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_css_selector("button[class*='btn-success']").click()
driver.find_element_by_css_selector("input[class*='filter-input']").send_keys('ind')
wait = WebDriverWait(driver,8)
wait.until(EC.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element_by_link_text('India').click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("input[class*='btn-success']").click()
tx = driver.find_element_by_css_selector("div[class*='alert-dismissible']").text
assert 'Success! Thank you!' in tx

driver.get_screenshot_as_file('s.png')
