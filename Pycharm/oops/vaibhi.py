# lst = [(4,1),(2,5),(3,2)]
# print(sorted(lst))  [(2, 5), (3, 2), (4, 1)]
# print(sorted(lst, key=lambda x:x[1])) [(4, 1), (3, 2), (2, 5)]

# i = 5
# def check(x=i):
#     return x
# i = 6
# print(check(i))
# output = 6 as we pass i in print(check(i))

# i = 5
# def check(x=i):
#     return x
# i = 6
# print(check())
# output = 5 as we are not passing i in print(check(i))

# lst = [1,1,2,4,5,5,5,5] remove dups in a list
# print(list({}.fromkeys(lst)))

# dic = {
#     'name':'zack',
#     'age':25
# }
# print(sorted(dic))
# output ['age', 'name']

# dic = [
#     {
#         'name':'zack'
#     },
#     {
#         'name':'champ'
#     }
# ]
# print(sorted(dic,key=lambda x:x['name']))
# [{'name': 'champ'}, {'name': 'zack'}]

# sort vs sorted
# sorted returns a new list and sort modifies the original one