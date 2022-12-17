import pytest

# @pytest.fixture()
# def setup():
#     print('SETUP')
#
# def test_t1(setup):
#     print('T1')
#
# @pytest.mark.usefixtures('setup')
# def test_t2():
#     print('T2')

# @pytest.fixture(autouse=True)
# def setup():
#     print('SETUP')
#
# def test_t1():
#     print('T1')
# def test_t2():
#     print('T2')
"""
test_fixtur.py::test_t1 SETUP
T1
PASSED
test_fixtur.py::test_t2 SETUP
T2
PASSED
"""

# @pytest.fixture()
# def setup():
#     print('SETUP')
#     yield
#     print('TearDown')
#
# def test_t1(setup):
#     print('T1')
#
# @pytest.mark.usefixtures('setup')
# def test_t2():
#     print('T2')

"""
test_fixtur.py::test_t1 SETUP
T1
PASSEDTearDown

test_fixtur.py::test_t2 SETUP
T2
PASSEDTearDown

"""
# @pytest.fixture()
# def setup1():
#     print('SETUP1')
#
# @pytest.fixture()
# def setup2(request):
#     print('SETUP2')
#
#     def teardown_a():
#         print('Teardown A')
#
#     def teardown_b():
#         print('Teardown B')
#     request.addfinalizer(teardown_a)
#     request.addfinalizer(teardown_b)
#
# def test_t1(setup1):
#     print('T1')
#
# @pytest.mark.usefixtures('setup2')
# def test_t2():
#     print('T2')

"""
test_fixtur.py::test_t1 SETUP1
T1
PASSED
test_fixtur.py::test_t2 SETUP2
T2
PASSEDTeardown B
Teardown A

"""

from pytest import raises

def valraise():
    raise ValueError

def test_error():
    with raises(ValueError):
        valraise()