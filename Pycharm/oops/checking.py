"""
def list_oper(list1, list2):
    sq = [i * i for i in list1]
    cube = [i ** 3 for i in list1]
    if all(item for item in sq if item in list2) and all(item in list2 for item in cube):
        return f'Squares and Cubes are present'
    elif all(item in list2 for item in sq):
        print(sq, list2)
        return f'Squares are present'
    elif all(item in list2 for item in cube):
        print(cube)
        return f'Cubes are only present'
    else:
        return f'No such pattern is present'

l = [1,2,3,4]
l2 =[1,4,9,16,8,64]
print(list_oper(l,l2))
"""

lst = [
    {
        'one':1
    },
    {
        'two':2
    }
]

dct = {
    'check':lst
}

for i in dct.values():
    print(i[0])