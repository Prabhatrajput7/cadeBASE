import itertools

# counter = itertools.count(start = 5,step=-5)
# print(next(counter))
# next(counter)
# print(next(counter))

# lst = [10,11,12,13]
# print(list(zip(counter,lst)))
# print(list(itertools.zip_longest(range(10),lst)))
#
# cycle = itertools.cycle([1,2,3])
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))

# rep = itertools.repeat(2,times=5) #error if next is more than five
# print(next(rep))
# print(next(rep))
# print(next(rep))
# print(next(rep))
# print(next(rep))
# print(next(rep))

# print(list(map(pow, range(10), itertools.repeat(2))))
# print(list(itertools.starmap(pow, [(0,2),(1,2),(2,2),(3,2),(4,2)])))

# a = 'abc'
# print(list(itertools.combinations(a,2)))#oder not matter
# print(list(itertools.permutations(a,2)))#order matter
# print(list(itertools.product(a,repeat=2)))
# print(list(itertools.combinations_with_replacement(a,2))


# l1,l2,l3 =[0,1,2],['a','b','c'],[None,None,None]
# chain = itertools.chain(l1,l2,l3)
# print(list(chain))

# def yo(n,m):
#     return n*n,m*m
# print(yo(5,2))

# from faker import Faker
#
# fake = Faker()
#
# demo = fake.simple_profile(sex=None)
# print(demo)



