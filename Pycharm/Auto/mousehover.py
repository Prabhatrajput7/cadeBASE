from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
action = ActionChains(driver)
# move = driver.find_element_by_css_selector("#mousehover")
# action.move_to_element(move).perform()
# top = driver.find_element_by_link_text("Top")
# action.move_to_element(top).click().perform()
# action.click(on_element = top).perform()
action.key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL).perform()
