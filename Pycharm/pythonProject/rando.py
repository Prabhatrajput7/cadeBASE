import random

# rand = random.random() #diff value between 0-1 not 0 and 1 [EXCLUSIVE]
# print(rand)

# rand = random.uniform(1,10) #random value /w 1-10 not 1 and 10 [EXCLUSIVE]
# print(rand)

# rand = random.randint(1,10) # random b/w 1-10 1 and 10 included  [INCLUSIVE]
# print(rand)

# greet = ['hi','hello','yo']
# print(random.choice(greet))

# greet = ['hi','hello','yo']
# print(random.choices(greet,k=5)) ['yo', 'hi', 'hi', 'yo', 'yo']

# greet = ['hi','hello','yo']
# print(random.choices(greet,weights=[2,2,1],k=5)) weight 2+2+1 = 5 hi has 2/5 chance for selecting

# a = list(range(1,10))
# random.shuffle(a)
# print(a) #modify original list [8, 9, 7, 6, 3, 4, 5, 1, 2]

# pas = '4BCDefgh!JKLmn0pQR5Tuvw*YZ'
# gen = random.sample(pas,8)
# print(''.join(gen))
#
# lst = list(map(chr,range(33,127)))
# password = random.sample(lst,10)
# print(lst)

low = list(map(chr,range(97,123)))
low.extend(list(map(chr,range(65,91))))
low.extend(list(map(chr,range(48,58))))
low.extend(list(map(chr,range(33,48))))
low.extend(list(map(chr,range(33,48))))
random.shuffle(low)
print(low)

# import string
# print(list(string.punctuation))