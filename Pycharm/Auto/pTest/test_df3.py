import pytest

@pytest.fixture(scope='class')
def setup():
    print('i m first')
    yield
    print('lasttt')

@pytest.mark.usefixtures("setup")
class Testex:

    def test_fixdemo(self):
        print('fixdemo')

    def test_fixdemo2(self):
        print('fixdemo2')

    def test_fixdemo3(self):
        print('fixdemo3')

    def test_fixdemo4(self):
        print('fixdemo4')

