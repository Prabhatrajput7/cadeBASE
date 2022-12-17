import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
from pageees.homepg import Homepg
from testdataa.homerelateddata import HomeRelated, apple
from utility.BaseClass import BaseClass


class TestHP(BaseClass):
    def test_formsub(self,getdata):
        print(getdata)
        homepg = Homepg(self.driver)
        homepg.givename().send_keys(getdata["fname"])
        homepg.giveemail().send_keys(getdata["ename"])
        self.driver.find_element_by_id('exampleInputPassword1').send_keys('123456789')
        self.driver.find_element_by_id('exampleCheck1').click()
        self.gender(homepg.givedrop(), getdata["gender"])
        self.driver.find_element_by_id('inlineRadio1').click()
        self.driver.find_element_by_name('bday').send_keys('01-01-2000')
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        print(self.driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text)
        time.sleep(2)
        self.driver.refresh()

    # @pytest.fixture(params=HomeRelated.text_to_pass)
    # def getdata(self, request):
    #     return request.param

    # @pytest.fixture(params=HomeRelated.get_testdataEX('Testcase1'))
    # def getdata(self, request):
    #     return request.param

    @pytest.fixture(params=apple.get_testdataEXC('Testcase1'))
    def getdata(self, request):
        return request.param

