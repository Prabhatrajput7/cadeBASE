import pytest

from pTest.BassClass import Baseclass

class Testex2(Baseclass):
    def test_userpro(self, dataload):
        log = self.test_getlogger()
        log.info(dataload)

    @pytest.fixture(params=['abc', 'xyz', 'abcxyz.com'])
    def dataload(self,request):
        print('fetching pre data')
        return request.param

