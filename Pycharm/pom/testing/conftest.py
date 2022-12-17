import pytest
from selenium import webdriver
from conf.confd import Details

@pytest.fixture(params=['chrome','firefox'], scope='class') #to not to use this line in every file we created a baseclass
def setup(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(executable_path=Details.pathc)
    driver.get(Details.url)
    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture()
def data(request):
    return {
        'name':'Viggi',
        'age':1
    }


