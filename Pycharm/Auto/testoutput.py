# class Foo:
#     def __init__(self,x):
#         self.x = x
#         print('A')
#     def __lt__(self, other):
#         print('B')
#         if self.x < other.x:
#             return True
#         else:
#             return False
#
# a = Foo(2)
# b = Foo(3)
# print(a < b)

# v= 'aeiou'
# s = 'aie'
# count = {}.fromkeys(v, 0)
# for i in s:
#     if i in count:
#         count[i]+=1
# print(count)


# class Config:
#     def __init__(self, env):
#         self.base_url = {
#             'dev': 'https://mydev-env.com',
#             'qa': 'https://myqa-env.com',
#             'staging': 'staging'
#         }[env]
#
#         self.app_port = {
#             'dev': 8080,
#             'qa': 80,
#             'staging': 8088
#         }[env]
#
# c = Config('qa')
# print(c.base_url)

# class One:
#     def __init__(self,env):
#         self.base_url = {
#             'dev': 'https://mydev-env.com',
#             'qa': 'https://myqa-env.com',
#             'staging': 'staging'
#             }[env]
#
# def two(b1):
#     a = One(b1)
#     return three(a)
#
# def three(c):
#     print(c.base_url)
#
# qa = 'qa'
# two(qa)



