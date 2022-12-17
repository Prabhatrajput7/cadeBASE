# conda create -n oldi python=3.7
from functools import reduce

def mulby2(num):
    return num * 2
print(list(map(mulby2, [2,4,6])))


def divisible2(num):
    return num % 2 == 0
print(list(filter(divisible2, [2,4,5,7,5])))

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
print(list(zip(l1,l2)))

l11 = [1,2,3]

def redd(acc,item):
    return acc + item
print(reduce(redd,l11,0))


print(list(map(lambda x: x*2, [2,5,8])))

print(reduce(lambda acc,x: acc+x*2, [2,5,8]))

l3 = [(1,2),(2,1),(3,4),(4,3)]
l3.sort(key= lambda x:x[1],reverse=True)
print(l3)

myd = {
    'a':1,
    'b':2
}

print(sorted(myd.items(), key=lambda x:x[1],reverse=True))
d = {k:v+2 for k,v in myd.items()}
print(d)

trry = {n:n*2 for n in [1,2,3]}
print(trry)

from functools import reduce

some_list = [[14], [215, 383, 87], [298], [374], [2,3,4,5,6,7]]
single_list = reduce(lambda x,y: x+y, some_list)
print(single_list)

lis = [[11, 22, 33, 44], [55, 66, 77], [88, 99]]
flatList = sum(lis, [])
print('New list', flatList, sum(flatList))
# lower asci
# casefold unicode

# isdigit no
# numarin no + unicode

