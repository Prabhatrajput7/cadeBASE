import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pickle
import random

driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.tickertape.in/screener')
data = driver.find_elements_by_xpath("//div[@class = 'jsx-473071598 num-col fixed-col data-col text-center d-flex-col']")

for i in data:
    print(i.text)