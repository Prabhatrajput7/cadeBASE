"""
x = dict(name = "John", age = 36, country = "Norway") || {'anme:'john'..}
new_dict = dict([['name','Andrei'],['age',32],['magic_power',False]])
x = frozenset(mylist) || frozenset({'cherry', 'banana', 'apple'})
x = car.keys() || dict_keys(['brand', 'model', 'year']) || list(x) ['brand', 'model', 'year']

lis = [[11, 22, 33, 44], [55, 66, 77], [88, 99]]
flatList = sum(lis, [])
[] started with this and added [11, 22, 33, 44], [55, 66, 77] & [88, 99]
print('New list', flatList)

import numpy as np
lst = [[11, 33], [22, 55], [11], [77, 88]]
new = list(np.concatenate(lst))
print(new)
        1                     2
(j in f for sub in test_list for j in sub)
            2                          1
matrix = [[j for j in range(5)] for i in range(5)]

"""
# one-liner logic to take input for rows and columns
mat = [[int(input()) for x in range (C)] for y in range(R)]


l = [
    {'name':'C','age':5},
    {'name':'B','age':3},
    {'name':'A','age':2},
]

l.sort(key= lambda x:x['name'])
print(l)

def fx(ele):
    return ele['name']

l.sort(key= fx)
print(l)

import operator
l.sort(key=operator.itemgetter('name'))
print(l)

import sys
l = list('hello')
l2 = list(range(0,100))
l3 = range(0,100)
print(l3) #range(0, 100)
print(sys.getsizeof(l3))

d1 = {'name':'one'}
d2 = {'age': 'two'}
d3 = d1 | d2
print(d3)

t= 100_000_000
print(f'{t:,}')

#  truncatre a file means resize a file f.truncate(number here in byte)
#  tell tells the current postiion of pointer in a file starts with 0

from collections import Counter
lst = [0,12,3,0,1,2,0,1,0,12]
print(dict(Counter(lst)))

import random

lr = [1,2,3,4,5,6,1,2,3,4,5,6]
print(random.choices(lr,k=5))
sf = random.shuffle(lr) # suffle the original list
print(lr)
sam = random.sample(lr, k=5)
print(sam)
# Note choices takes any element from a list ex list(range(1,10)) chocies can print dup but in this case sameple will not print dup

from itertools import permutations, combinations
lc = [1,2,3]
print(list(combinations(lc,2))) # wont give err if enter number is bigger than len of list retuns a blank list (1,2)&(2,1) consider same
print(list(permutations(lc,2))) # (1,2)&(2,1) consider different

# jo file run hote hai vohi main file hote hai

# randl just takes there left and right
# find gives -1 index if error if not found
# randl split split from rightandleft

txt = "50"
x = txt.zfill(10)
print(x) #0000000050

amount = 49
print(f'{amount:.2f}') #49.00

# lower vs casefold casefold include more character like Beta in germany
# digit vs numeric both 0-9 no decimal and -ve number numeric include 0-9 digit of other languages as well
# int('111',2) -> 7
# The isdigit() method accepts only decimals, subscripts, and superscripts. Python isdecimal()

"""
String Type	                Example	Python      .isdecimal()#unicode	Python .isdigit()	Python .isnumeric()
Base 10 Numbers         	'0123'	            True	                       True	        True
Fractions and Superscripts	   '⅔', '2²'	    False	                    True        	True
Roman Numerals	                'ↁ'	        False	                     False	        True
"""
# x = divmod(5, 2) (2, 1) Q||R
"""
flush() moves data from ram to disk when we write a data. data is present in ram when we close it it moves the data to dish
tell() tell the location of pointer
seek() sets the pointer like seek(0) to fisrt
write("\n.....\n")
truncate(20) make file 20 byte size
1 byte = 8 bit
isatty() method returns True if the file stream is interactive, example: connected to a terminal device.
"""