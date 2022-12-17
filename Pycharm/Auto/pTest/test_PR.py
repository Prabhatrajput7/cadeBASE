import pytest


@pytest.mark.skip
def test_1():
    pass


@pytest.mark.xfail
def test_2():
    pass


#@pytest.mark.smoke
@pytest.mark.xfail
def test_3(newfx):
    print(newfx[0])


#@pytest.mark.smoke
@pytest.mark.xfail
def test_4(Multivalue):
    print(Multivalue[1])#firefoc and E

@pytest.mark.smoke
def test_5(Browsers):
    print(Browsers['chrome'])



