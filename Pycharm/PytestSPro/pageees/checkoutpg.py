from selenium.webdriver.common.by import By

from pageees.confirmpg import Confirmpg


class Checkoutpg:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*Checkoutpg.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*Checkoutpg.cardFooter)

    def checkOutItems(self):
        self.driver.find_element(*Checkoutpg.checkOut).click()
        conf = Confirmpg(self.driver)
        return conf


