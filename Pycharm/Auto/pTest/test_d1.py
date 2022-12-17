#-v view pass fail: more info metadate output
#-s see print statement: logs in output pass or fail
#-k to run all a particulare one like -k name: method name execution
#py.test to execute all tc
#-m to run make one
#skip tc @pytest.mark.skip
#@pytest.mark.xfail test would run but in output you won't see it
#conftest to hold fixture to be shared to all files
#py.test -v -s
#to run a particular file py.test name.py
#-k tcname

import pytest


# @pytest.mark.smoke
# def test_f1(setup):
#     print('pass')
#
#
# @pytest.mark.xfail
# def test_f22():
#     print('fail')

def test_crossB(Browser):
    print('**',Browser)

def test_crossB2(Multivalue):
    print(Multivalue[0])

def test_valueM(Multivalue):
    print(Multivalue)




