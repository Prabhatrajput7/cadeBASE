from selenium.webdriver.common.by import By


class Confirmpg:
    def __init__(self, driver):
        self.driver = driver

    search = (By.CSS_SELECTOR,"input[class*='filter-input']")

    def seaching(self):
        return self.driver.find_element(*Confirmpg.search)

