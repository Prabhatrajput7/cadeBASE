import pytest

from pTest.BassClass import Baseclass


# @pytest.mark.usefixtures("browser")
# class Testex2(Baseclass):
#     def test_userpro(self, browser):
#         log = self.test_getlogger()
#         log.info(browser)
#         print('-*********')
#         # print(dataload2)

@pytest.mark.usefixtures("newfx")
class Testex2(Baseclass):
    def test_userpro(self):
        # log = self.test_getlogger()
        # log.info(browser)
        print(self.ll)
        # print(dataload2)
