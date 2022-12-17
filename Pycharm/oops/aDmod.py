from collections import Counter, defaultdict, namedtuple
import random
import numpy as np
import string
import os,shutil
import datetime
from datetime import timedelta
import zipfile
"""
lst = list(range(0,15))
print(Counter(lst))

d = {}
d['one'] = 'ONE'
d['two'] = 'TWO'
d = defaultdict(lambda:0)
print(d['three'])

tup = namedtuple('dog',['name','age'])
d = tup(name='vig',age=1)
print(d.age)

print(random.choices(lst,k=10))#repeat
print(random.sample(lst,k=10))#no repeat

print(os.getcwd())
print(os.listdir())#you can pass directory path in list dir as well

with open('move.text','w') as f:
    f.write('Moving')
shutil.move('D:\Python\Pycharm\oops\move.text',"C:\\Users\\Prabh\\Desktop")

os.unlink("D:\Python\Pycharm\oops\move.text")
for i,j,k in os.walk(os.getcwd()):#i is path  j is folder k is files
    print('i', i)
    print('j', j)
    print('k', k)

with open('fileone.txt', 'w') as f:
    f.write('Zipone')

with open('filetwo.txt', 'w') as f2:
    f2.write('Zipwto')  
    
comp = zipfile.ZipFile('compress.zip','w')
comp.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED)
comp.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
comp.close()

op = zipfile.ZipFile('compress.zip','r')
op.extractall('zipopen')

zipf = "D:\\Python\\Pycharm\\oops\\zipopen"
out = "folderzip"
shutil.make_archive(out,'zip',zipf)#destination, format, src

shutil.unpack_archive('folderzip.zip','unzip','zip')#src, destination,format    
"""
