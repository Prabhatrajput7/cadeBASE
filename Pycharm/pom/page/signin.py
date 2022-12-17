from page.basepage import Basepage
from selenium.webdriver.common.by import By

class Signin(Basepage):
    email = (By.ID,'email')
    passw = (By.ID, 'passwd')
    button = (By.ID, 'SubmitLogin')
    url = (By.XPATH,'//a[@class="login"]')

    def __init__(self,driver):
        super().__init__(driver)

    def sendkey(self,username,password):
        self.sendval(self.email,username)
        self.sendval(self.passw, password)
        self.clicking(self.button)

    def clicckingurl(self):
        self.clicking(self.url)



