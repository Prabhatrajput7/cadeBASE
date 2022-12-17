# import webdriver
# from selenium import webdriver
#
# # import Action chains
# from selenium.webdriver.common.action_chains import ActionChains
#
# # create webdriver object
# driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
# # get geeksforgeeks.org
# driver.get("https://www.geeksforgeeks.org/")
# # get element
# element = driver.find_element_by_link_text("Courses")
#
# # create action chain object
# action = ActionChains(driver)
#
# # click the item
# action.click(element).perform()

# click and hold  the item
# action.click_and_hold(element)

# import webdriver
# from selenium import webdriver
#
# # import Action chains
# from selenium.webdriver.common.action_chains import ActionChains
#
# # create webdriver object
# driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
#
# # get geeksforgeeks.org
# driver.get("https://www.geeksforgeeks.org/")
#
# # get source element
# source_element = driver.find_element_by_link_text("Courses")
#
# # get target element
# target_element = driver.find_element_by_link_text("Hard")
#
# # create action chain object
# action = ActionChains(driver)


# import webdriver
from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

# import KEYS
# from selenium.webdriver.common.keys import Keys
#
# # create webdriver object
# driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
#
# # get geeksforgeeks.org
# driver.get("https://www.geeksforgeeks.org/")
#
# # create action chain object
# action = ActionChains(driver)
#
# # perform the operation
# action.key_down(Keys.CONTROL).send_keys('F').key_up(Keys.CONTROL).perform()
#
#
# # drag and drop the item
# action.drag_and_drop(source_element, target_element)
#
# # perform the operation
# action.perform()

# import webdriver
# from selenium import webdriver
#
# # import Action chains
# from selenium.webdriver.common.action_chains import ActionChains
#
# # create webdriver object
# driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
#
# # get geeksforgeeks.org
# driver.get("https://www.geeksforgeeks.org/")
#
# # create action chain object
# action = ActionChains(driver)
#
# # move the cursor
# action.move_by_offset(500, 200)
#
# # perform the operation
# action.perform()


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.get('https://www.youtube.com/')
cp = driver.find_element_by_xpath('//input[@id="search"]').send_keys('hello')
action = ActionChains(driver)
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).key_down(Keys.CONTROL).send_keys('x').key_up(Keys.CONTROL).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).send_keys(Keys.ENTER).perform()