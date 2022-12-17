import pytest
import pickle
import keyword

'''
Write the fixture function unpick which reads the pickle file "file.pickle" and return the list of words
Mark the function as fixture
Open the file "file.pickle" with "rb" and load the data using pickle.load function
'''
@pytest.fixture()
def unpick():
    with open('file.pickle', 'rb') as p:
        db = pickle.load(p)
        return db




'''
Write the test method test1 to check whether the count of words is equal to 6720
'''

def test1(unpick):
    count = len(unpick)
    assert count == 6720



'''
Write the test method test_len_endswith to check whether the count of words ending with 'ing' is greater than 350
'''
def test_len_endswith(unpick):
    list2 = []
    for item in unpick:
        if item.endswith('ing'):
            list2.append(item)
    assert len(list2) > 350


'''
Write the test method test_len_lessthan to check whether the count of words having characters less than 3 is equalto 80
'''
def test_len_lessthan(unpick):
    list3 = []
    for item in unpick:
        if len(item)<3:
            list3.append(item)
    assert len(list3) == 80

'''
Write the test method test_keyword to check whether the count of keywords present in the list are not equal to zero 
Hint Use keyword keyword function of library keyword.
'''
def test_keyword(unpick):
    list4 = []
    for item in unpick:
        if keyword.iskeyword(item):
            list4.append(item)
    assert len(list4) != 0

'''
Write the test method test_word to check whether the word "jupyter" is present in the list
'''
def test_word(unpick):
    flag = False
    for item in unpick:
        if item == 'jupyter':
            flag= True
            break
    assert flag == True


'''
Write the test method test_len_startswith to check whether the count of words that starts with character 'c' is equal to 700
'''
def test_len_startswith(unpick):
    list5 = []
    for item in unpick:
        if item.startswith('c'):
            list5.append(item)
    assert len(list5) == 700




'''
Write the test method test_words_ag to check the count of words that starts with 'a' and endwith 'g' is a two digit number and the second digit is zero
'''
def test_words_ag(unpick):
    list6 = []
    for item in unpick:
        if item.startswith('a') and item.endswith('g'):
            list6.append(item)
    Flag=False
    if len(list6) in [10,20,30,40,50,60,70,80,90]:
        Flag= True
    assert Flag == True



'''
Write the test method char_words to check the whether count of words having alphabets only is greater than 6400
'''

def char_words(unpick):
    list7 = []
    for item in unpick:
        if item.isalpha():
            list7.append(item)
    assert len(list7) > 6400





'''
Write the parameterized test method test_words_starts_with to run against a set of multiple inputs
Mark the function as parameterize
Write the function to check the count of words starting with the input character is equal to the output
[('a',570),('e',327),('h',1296),('t',321)] is the set of inputs and outputs
'''
@pytest.mark.parametrize("test_input,expected", [('a', 570), ('e', 327), ('h', 1296), ('t', 321)])
def test_words_starts_with(unpick,test_input, expected):
    lst8 = []
    for item in unpick:
        if item.startswith(test_input):
            lst8.append(item)
    assert len(lst8) == expected