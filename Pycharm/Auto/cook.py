import pickle
import pprint
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def save_cookies(driver, location):
    pickle.dump(driver.get_cookies(), open(location, "wb"))


def load_cookies(driver, location, url=None):

    cookies = pickle.load(open(location, "rb"))
    #driver.delete_all_cookies()
    # have to be on a page before you can add any cookies, any page - does not matter which
    driver.get("https://google.com" if url is None else url)
    for cookie in cookies:
    #     if isinstance(cookie.get('expiry'), float):#Checks if the instance expiry a float
    #         cookie['expiry'] = int(cookie['expiry'])# it converts expiry cookie to a int
        driver.add_cookie(cookie)


# def delete_cookies(driver, domains=None):
#
#     if domains is not None:
#         cookies = driver.get_cookies()
#         original_len = len(cookies)
#         for cookie in cookies:
#             if str(cookie["domain"]) in domains:
#                 cookies.remove(cookie)
#         if len(cookies) < original_len:  # if cookies changed, we will update them
#             # deleting everything and adding the modified cookie object
#             driver.delete_all_cookies()
#             for cookie in cookies:
#                 driver.add_cookie(cookie)
#     else:
#         driver.delete_all_cookies()


# Path where you want to save/load cookies to/from aka C:\my\fav\directory\cookies.txt
cookies_location = "C:\\Users\\Prabh\\PycharmProjects\\Auto\\cookies.pkl"

# Initial load of the domain that we want to save cookies for
# chrome = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
# chrome.get("https://www.hackerrank.com/auth/login")
# chrome.find_element_by_css_selector("span[class='ui-text']").click()
# WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.ID,'input-1'))).send_keys('Voldemort@gmail.com')
# WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.ID,'input-2'))).send_keys("voldemortX2")
# WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[type='submit']"))).click()
# save_cookies(chrome, cookies_location)
# chrome.quit()


# Load of the page you cant access without cookies, this one will fail
# chrome = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
# chrome.get("https://www.hackerrank.com/settings/account")
#https://www.hackerrank.com/dashboard



#Load of the page you cant access without cookies, this one will go through
chrome = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
load_cookies(chrome, cookies_location)
chrome.get("https://www.hackerrank.com/settings/profile")

# chrome = webdriver.Chrome()
# chrome.get("https://google.com")
# time.sleep(2)
# pprint.pprint(chrome.get_cookies())
# print "=========================\n"
#
# delete_cookies(chrome, domains=["www.google.com"])
# pprint.pprint(chrome.get_cookies())
# print "=========================\n"
#
# delete_cookies(chrome)
# pprint.pprint(chrome.get_cookies())