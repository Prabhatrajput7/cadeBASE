import pickle
import pprint
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chrome = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
# chrome.get("https://www.hackerrank.com/auth/login")
# chrome.find_element_by_css_selector("span[class='ui-text']").click()
# WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.ID,'input-1'))).send_keys('Voldemort@gmail.com')
# WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.ID,'input-2'))).send_keys("voldemortX2")
# WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[type='submit']"))).click()
# # save_cookies(chrome, cookies_location)
# #chrome.quit()
def delete_cookies(driver, domains=None):

    if domains is not None:
        cookies = driver.get_cookies()
        original_len = len(cookies)
        for cookie in cookies:
            if str(cookie["domain"]) in domains:
                cookies.remove(cookie)
        if len(cookies) < original_len:  # if cookies changed, we will update them
            # deleting everything and adding the modified cookie object
            driver.delete_all_cookies()
            for cookie in cookies:
                driver.add_cookie(cookie)
    else:
        driver.delete_all_cookies()

chrome = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
chrome.get("https://google.com")
time.sleep(2)
pprint.pprint(chrome.get_cookies())
print("=========================")


delete_cookies(chrome, domains=["www.google.com"])
pprint.pprint(chrome.get_cookies())
print("=========================\n")