import pytest
import pickle

'''
Write the fixture function unpick which reads the pickle file "file.pickle" and return the list of words
Mark the function as fixture
Open the file "file.pickle" with "rb" and load the data using pickle.load function
'''

from faker import  Faker
ff = Faker()
def storeData():
    lst = [ff.name() for i in range(6720)]
    with open('file.pickle', 'ab') as p:
        pickle.dump(lst, p)
storeData()

# def unpick():
#     with open('file.pickle', 'rb') as p:
#         db = pickle.load(p)
#         return db
# print(unpick())

'''
Write the test method test1 to check whether the count of words is equal to 6720
'''

'''
Write the test method test_len_endswith to check whether the count of words ending with 'ing' is greater than 350
'''

'''
Write the test method test_len_lessthan to check whether the count of words having characters less than 3 is equalto 80
'''

'''
Write the test method test_keyword to check whether the count of keywords present in the list are not equal to zero 
Hint Use keyword keyword function of library keyword.
'''

'''
Write the test method test_word to check whether the word "jupyter" is present in the list
'''

'''
Write the test method test_len_startswith to check whether the count of words that starts with character 'c' is equal to 700
'''

'''
Write the test method test_words_ag to check the count of words that starts with 'a' and endwith 'g' is a two digit number and the second digit is zero
'''

'''
Write the test method char_words to check the whether count of words having alphabets only is greater than 6400
'''

'''
Write the parameterized test method test_words_starts_with to run against a set of multiple inputs
Mark the function as parameterize
Write the function to check the count of words starting with the input character is equal to the output
[('a',570),('e',327),('h',1296),('t',321)] is the set of inputs and outputs
'''
