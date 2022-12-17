# import the libs
from selenium import webdriver
from time import sleep

# create the initial window
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')

# go to the home page
driver.get('https://www.geeksforgeeks.org/')

# storing the current window handle to get back to dashboard
main_page = driver.current_window_handle

# wait for page to load completely
sleep(1)

# click on the sign in tab
driver.find_element_by_xpath("//a[@class='header-main__signup login-modal-btn']").click()

sleep(5)

# click to log in using facebook
driver.find_element_by_xpath("//input[@id='luser']").send_keys('checking')
sleep(3)
driver.find_element_by_xpath("//span[@class='close']").click()
# changing the handles to access login page
for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle

# change the control to signin page
driver.switch_to.window(login_page)

# user input for email and password
print('Enter email id : ', end='')
email = input().strip()
print('Enter password : ', end='')
password = input().strip()

# enter the email
driver.find_element_by_xpath('//*[@id ="email"]').send_keys(email)

# enter the password
driver.find_element_by_xpath('//*[@id ="pass"]').send_keys(password)

# click the login button
driver.find_element_by_xpath('//*[@id ="u_0_0"]').click()

# change control to main page
driver.switch_to.window(main_page)

sleep(10)
# print user name
name = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/header/div[2]/div/div/div/div/span').text
print('Your user name is : {}'.format(name))

# closing the window
driver.quit()
