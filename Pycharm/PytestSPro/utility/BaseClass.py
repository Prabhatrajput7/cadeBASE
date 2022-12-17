import logging
import inspect
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures('setup')
class BaseClass:
    def test_getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('logfiles.log')

        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verifylinkpresent(self,text):
        wait = WebDriverWait(self.driver, 8)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def gender(self,locator,text):
        dd = Select(locator)
        dd.select_by_visible_text(text)



