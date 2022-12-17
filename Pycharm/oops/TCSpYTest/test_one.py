# def test_first():
#     assert True


# class Test_ek:
#     def test_t1(self):
#         assert 3 == 3
#     def test_t2(self):
#         assert 'a'=='a'

# def setup_function(function):
#     if function == test1:
#         print('Setting up Test1')
#     elif function == test2:
#         print('Setting up Test2')
#     else:
#         print('Nothing to set')
#
# def teardown_function(function):
#     if function == test1:
#         print('TearDown Test')
#     elif function == test2:
#         print('TearDown Test2')
#     else:
#         print('Nothing to Tear down')
#
# def test1():
#     print('INSIDE Test1')
#
# def test2():
#     print('INSIDE Test2')

"""
test_one.py::test1 Setting up Test1
INSIDE Test1
PASSEDTearDown Test

test_one.py::test2 Setting up Test2
INSIDE Test2
PASSEDTearDown Test2

"""


# def setup_module(fx):
#     print('SETUP')
#
# def teardown_module(fx):
#     print('TearDOWN')
#
#
# def setup_function(function):
#     if function == test1:
#         print('Setting up Test1')
#     elif function == test2:
#         print('Setting up Test2')
#     else:
#         print('Nothing to set')
#
# def teardown_function(function):
#     if function == test1:
#         print('TearDown Test')
#     elif function == test2:
#         print('TearDown Test2')
#     else:
#         print('Nothing to Tear down')
#
# def test1():
#     print('INSIDE Test1')
#
# def test2():
#     print('INSIDE Test2')

"""
test_one.py::test1 SETUP
Setting up Test1
INSIDE Test1
PASSEDTearDown Test

test_one.py::test2 Setting up Test2
INSIDE Test2
PASSEDTearDown Test2
TearDOWN

"""

# class TestClass:
#     @classmethod
#     def setup_class(cls):
#         print('SETUP')
#     @classmethod
#     def teardown_class(cls):
#         print('TearDOWN')
#
#     def setup_method(self,method):
#         if method == self.test1:
#             print('Setting up Test1')
#         elif method == self.test2:
#             print('Setting up Test2')
#         else:
#             print('Nothing to set')
#
#     def teardown_method(self,method):
#         if method == self.test1:
#             print('TearDown Test')
#         elif method == self.test2:
#             print('TearDown Test2')
#         else:
#             print('Nothing to Tear down')
#
#     def test1(self):
#         print('INSIDE Test1')
#
#     def test2(self):
#         print('INSIDE Test2')

"""
test_one.py::TestClass::test1 SETUP
Setting up Test1
INSIDE Test1
PASSEDTearDown Test

test_one.py::TestClass::test2 Setting up Test2
INSIDE Test2
PASSEDTearDown Test2
TearDOWN
"""