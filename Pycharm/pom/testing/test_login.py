import pytest
from page.signin import Signin
from conf.confd import Details

@pytest.mark.usefixtures('setup')
class Testlogin:
    def test_link(self):
        self.check = Signin(self.driver)
        self.check.clicckingurl()

    def test_login(self, data):
        print(data)
        self.lg = Signin(self.driver)
        self.lg.sendkey(Details.username,Details.password)
