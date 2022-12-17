import numpy as np
# zeros = np.zeros((5, 3, 3))
# print(zeros.ndim)
# a1 = np.array([1,2,3,4])
# print(np.log(a1))

# import time
#
# t1 = time.time()
# lst = [i for i in range(100000000)]
# t2 = time.time()
# print(t2-t1)
# t3 = time.time()
# np.sum(lst)
# t4 = time.time()
# print(t4-t3)





# a = np.array([[[1,2,3],
#              [4,5,6],
#              [7,8,9]],
#              [[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]],
#               [[1, 2, 3],
#                [4, 5, 6],
#                [7, 8, 9]]]
#              )
# np.save('myarr.npy',a)
# z = np.load('myarr.npy')
# print(z)

# aa = np.array([[[1,2,3],
#              [4,5,6],
#              [7,8,9]],
#              [[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]],
#               [[1, 2, 3],
#                [4, 5, 6],
#                [7, 8, 9]]]
#              )
#
# ab = np.array([[[1,2,3],
#              [4,5,6],
#              [7,8,9]],
#              [[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]],
#               [[1, 2, 3],
#                [4, 5, 6],
#                [7, 8, 9]]]
#              )
# np.savez('myarrs.npz',aa,ab)
# zz = np.load('myarrs.npz')
# az = zz.files
# l = zz['arr_0']
# print(zz['arr_0'])

# print(a.shape)

# simple_array = np.array((1, 2, 3))
# simple_array2 = np.array([1, 2, 3])
# print(simple_array, '*', simple_array2)

# print(np.ones([2,2]))

# zeros = np.zeros([5, 3, 3])
# print(zeros)
# print(np.random.random([5, 3]))
# print(np.linspace(0,2,9))
# print(np.full([2,2],7))
# print(np.eye(2))
# print(np.empty([3,2]))
# print(np.arange(0,10,2))
#
# print(np.random.randn(10))
#
# a4 = np.random.randint(10, size=(2, 3, 3, 3))
# print(a4.ndim,a4.shape)
# print(a4)
# print('*')
# print(a4[:1, :2, :, :2])

# a = np.zeros((2,2))
#
# a[0] = '1'
# print(a)
#
# print(eval(input('enter num')))

"""
Every NumPy array has the attribute base that returns None if the array owns the data.
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base) None
print(y.base) arr

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
[[[[[1 2 3 4]]]]]
shape of array : (1, 1, 1, 1, 4) 

"""