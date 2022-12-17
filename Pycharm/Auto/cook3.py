import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pprint
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.google.co.in/')
mycook = driver.get_cookies()
pprint.pprint(len(mycook))
pprint.pprint(mycook)
print('#####################################################')
addcook = {'name':'Tom','value':'infinite'}
driver.add_cookie(addcook)
mycook2 = driver.get_cookies()
pprint.pprint(len(mycook2))
pprint.pprint(mycook2)
print('#####################################################')
driver.delete_cookie('Tom')
mycook3 = driver.get_cookies()
pprint.pprint(len(mycook3))
pprint.pprint(mycook3)