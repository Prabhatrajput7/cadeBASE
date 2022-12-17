import pytest


@pytest.fixture(scope='class')
def setup():
    print('i m first')
    yield
    print('lasttt')

@pytest.fixture()
def dataload():
    print('fetching pre data')
    return ['abc','xyz','abcxyz.com']

@pytest.fixture(params = [{'name':7}])
def dataload2(request):
    return request.param

@pytest.fixture(params = ['chrome','Firefox','edge'])
def browser(request):
    return request.param

@pytest.fixture(params = [('chrome','Firefox'),'IE11'])
# fixture will share type in [ this will be share not the list ]
def Multivalue(request):
    return request.param


@pytest.fixture(params=['Jackel','main','R6'])
def newfx(request):
    l = request.param[0]
    request.cls.ll = l
    yield
    print('done')


@pytest.fixture(params = [{'chrome':'CH','Firefox':'FF'}])
def Browsers(request):
    return request.param


from pytest import fixture
from selenium import webdriver
@fixture(scope="function")
def driver():
    br = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
    return br
    #yield br
    #print('teardown')