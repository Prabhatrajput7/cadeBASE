from selenium.webdriver.common.by import By

from pageees.checkoutpg import Checkoutpg


class Homepg:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.CSS_SELECTOR,"input[name='name']")
    email = (By.NAME,'email')
    dropd = (By.ID,'exampleFormControlSelect1')

    def shopitme(self):
        self.driver.find_element(*Homepg.shop).click()
        coutpg = Checkoutpg(self.driver)
        return coutpg

    def givename(self):
        return self.driver.find_element(*Homepg.name)

    def giveemail(self):
        return self.driver.find_element(*Homepg.email)

    def givedrop(self):
        return self.driver.find_element(*Homepg.dropd)




