import pytest
import pickle
import keyword

@pytest.fixture()
def unpick():
    with open('file.pickle', 'rb') as p:
        db = pickle.load(p)
        return db

def test1(unpick):
    count = len(unpick)
    assert count == 6720

def test_len_endswith(unpick):
    list2 = []
    for item in unpick:
        if item.endswith('ing'):
            list2.append(item)
    assert len(list2) < 350

def test_len_lessthan(unpick):
    list3 = []
    for item in unpick:
        if len(item)<3:
            list3.append(item)
    assert len(list3) != 80

def test_keyword(unpick):
    list4 = []
    for item in unpick:
        if keyword.iskeyword(item):
            list4.append(item)
    assert len(list4) == 0

def test_word(unpick):
    flag = False
    for item in unpick:
        if item == 'jupyter':
            flag= True
            break
    assert flag != True

def test_len_startswith(unpick):
    list5 = []
    for item in unpick:
        if item.startswith('c'):
            list5.append(item)
    assert len(list5) < 700

def test_words_ag(unpick):
    list6 = []
    for item in unpick:
        if item.startswith('a') and item.endswith('g'):
            list6.append(item)
    Flag=False
    if len(list6) in [10,20,30,40,50,60,70,80,90]:
        Flag= True
    assert Flag == True

def char_words(unpick):
    list7 = []
    for item in unpick:
        if item.isalpha():
            list7.append(item)
    assert len(list7) > 6400


@pytest.mark.parametrize("test_input,expected", [('a', 570), ('e', 327), ('h', 1296), ('t', 321)])
def test_words_starts_with(unpick,test_input, expected):
    lst8 = []
    for item in unpick:
        if item.startswith(test_input):
            lst8.append(item)
    assert len(lst8) == expected