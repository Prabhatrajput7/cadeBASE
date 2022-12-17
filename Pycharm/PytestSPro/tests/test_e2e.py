import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

#@pytest.mark.usefixtures('setup')
from pageees.checkoutpg import Checkoutpg
from pageees.homepg import Homepg
from utility.BaseClass import BaseClass

class Test_1(BaseClass):

    def test_test1(self):
        log = self.test_getlogger()
        homepg = Homepg(self.driver)
        check = homepg.shopitme()
        cards = check.getCardTitles()
        log.info('Getting Names')
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                check.getCardFooter()[i].click()
        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()

        congpg = check.checkOutItems()
        log.info('Enter country as ind')
        congpg.seaching().send_keys('ind')
        #self.driver.find_element_by_css_selector("input[class*='filter-input']").send_keys('ind')
        self.verifylinkpresent('India')
        self.driver.find_element_by_link_text('India').click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("input[class*='btn-success']").click()
        tx = self.driver.find_element_by_css_selector("div[class*='alert-dismissible']").text
        log.info('Data '+tx)
        assert 'Success! Thank you!' in tx

