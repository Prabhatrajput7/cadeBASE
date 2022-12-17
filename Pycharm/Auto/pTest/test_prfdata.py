import pytest
from pTest.BC import Baseclass
@pytest.mark.usefixtures("newfx")
class Testex2(Baseclass):
    def test_userpro(self, newfx):
        log = self.getlogger()
        log.info(newfx[0])
        #print(dataload)

