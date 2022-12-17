import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Basepage:
    def __init__(self,driver):
        self.driver= driver

    def clicking(self,locator):
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located(locator)).click()

    def texting(self,locator):
        txt = WebDriverWait(self.driver,5).until(EC.presence_of_element_located(locator)).text()
        return txt

    def sendval(self,locator,val):
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located(locator)).send_keys(val)

    def visible(self,locator):
        vis = WebDriverWait(self.driver,5).until(EC.presence_of_element_located(locator))
        return bool(vis)

    def title(self,title):
        return WebDriverWait(self.driver,5).until(EC.title_is(title))