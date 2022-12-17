import getpass
from termcolor import colored
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
options = Options()
options.headless = True
driver = webdriver.Firefox(executable_path="./geckodriver", options=options)

gmail_address = input("Enter your Gmail address:\t")
gmail_password = getpass.getpass("Enter your password:\t")

url = "https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3Ab46be548ba0c2b22%2C10%3A1627060492%2C16%3A09030757e8ecf391%2C7b9bdf228b74ed6ef5f76cb4ea89e15294d2a8c81bfc924447a8fe74c314f112%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%2253b1724e2c8c46bb8fa328ba99f37fee%22%7D&response_type=code&hl=en&flowName=GeneralOAuthFlow"

driver.get(url)
emailinput = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "identifier")))
emailinput.send_keys(gmail_address)
time.sleep(random.randint(1,10))
nextbutton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "identifierNext")))
ActionChains(driver).move_to_element(nextbutton).click().perform()
time.sleep(random.randint(1,10))

passwordinput = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "password")))
passwordinput.send_keys(gmail_password)
time.sleep(random.randint(1,10))
nextbutton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordNext")))
ActionChains(driver).move_to_element(nextbutton).click().perform()
time.sleep(random.randint(1,10))

print(colored("[P] ","red")+colored(f"You logged in using {gmail_address} ... ", "blue"))
time.sleep(random.randint(1,10))
driver.get("https://youtube.com")
#Save cookies
pickle.dump(driver.get_cookies(), open(cookie_file_name, "wb"))

cookie_file_name = f"{gmail_address.replace('@','').replace('.','')}.pkl"

driver.get("https://youtube.com")
time.sleep(random.randint(1,10))
cookies = pickle.load(open(cookie_file_name, "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
    time.sleep(random.randint(1,10))
    driver.get("https://youtube.com")
    print(colored("[C] ","red")+colored(f"You logged in using {gmail_address} ... ", "blue"))

cookie_file_name = f"{gmail_address.replace('@','').replace('.','')}.pkl"
try:
	driver.get("https://youtube.com")
	time.sleep(random.randint(1,10))
	cookies = pickle.load(open(cookie_file_name, "rb"))
	for cookie in cookies:
		driver.add_cookie(cookie)
		time.sleep(random.randint(1,10))
		driver.get("https://youtube.com")
		print(colored("[C] ","red")+colored(f"You logged in using {gmail_address} ... ", "blue"))


except FileNotFoundError:
	driver.get(url)
	emailinput = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "identifier")))
	emailinput.send_keys(gmail_address)
	time.sleep(random.randint(1,10))
	nextbutton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "identifierNext")))
	ActionChains(driver).move_to_element(nextbutton).click().perform()
	time.sleep(random.randint(1,10))

	passwordinput = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "password")))
	passwordinput.send_keys(gmail_password)
	time.sleep(random.randint(1,10))
	nextbutton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordNext")))
	ActionChains(driver).move_to_element(nextbutton).click().perform()
	time.sleep(random.randint(1,10))

	print(colored("[P] ","red")+colored(f"You logged in using {gmail_address} ... ", "blue"))
	time.sleep(random.randint(1,10))
	driver.get("https://youtube.com")
	#Save cookies
	pickle.dump(driver.get_cookies(), open(cookie_file_name, "wb"))

time.sleep(random.randint(10,20))
driver.close()