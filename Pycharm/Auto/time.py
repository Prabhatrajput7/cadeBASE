import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

driver.implicitly_wait(5)

#driver.find_element_by_xpath("//input[@type='search']").send_keys('ber')
driver.find_element_by_css_selector('.search-keyword').send_keys('ber')
time.sleep(2)
#c = driver.find_elements_by_css_selector("div[class = 'products'] div")
c = len(driver.find_elements_by_xpath("//div[@class = 'products']/div"))
assert c == 3
b = driver.find_elements_by_xpath("//div[@class = 'product-action']/button")
#xpath for child to grandfather ("//div[@class = 'product-action']/button/parent::div/parent::div/h4")
list = []
for i in b:
    list.append(i.find_element_by_xpath("parent::div/parent::div/h4").text)
    i.click()
print(list)
driver.find_element_by_css_selector("img[alt='Cart']").click()
#driver.find_element_by_xpath("//div[@class='action-block']/button").click()


driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver,5)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".promoCode")))
#time.sleep(2)
list1 =[]
after = driver.find_elements_by_css_selector("p.product-name")
for i in after:
    list1.append(i.text)
print(list1)
assert list == list1

s = 0
total = driver.find_elements_by_xpath("//tr/td[5]/p")
for i in total:
    s += int(i.text)
ta = driver.find_element_by_xpath("//span[@class='totAmt']").text
assert  int(ta) == s
og = driver.find_element_by_xpath("//span[@class='discountAmt']").text
driver.find_element_by_css_selector(".promoCode").send_keys('rahulshettyacademy')
driver.find_element_by_css_selector(".promoBtn").click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element_by_css_selector(".promoInfo").text)
da = driver.find_element_by_xpath("//span[@class='discountAmt']").text
assert int(og) > float(da)


