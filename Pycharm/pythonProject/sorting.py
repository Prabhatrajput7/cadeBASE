# sorting

# bubble
# wring compare 2-2-2 and hold the last elemt thats why n-i-1

# def bubble(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
# arr = [45,20,15,85,11]
# print(bubble(arr))



# import copy
# l = [1,2,3,4,5]
# # l2 = l
# # l2[0] = 7
# # print(l,l2)
#
# import copy
#
# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.copy(old_list)
#
# new_list[1][1] = 'AA'
#
# print("Old list:", old_list)
# print("New list:", new_list)

# s = 'yomynameisheymynameis'
# d = {}.fromkeys(s,0)
# for i in s:
# 	if i in d:
# 		d[i]+=1
# print(max(d.values()))







# def b(lst):
#     for i in range(len(lst)-1,0,-1):
#         for j in range(i):
#             if lst[j]>lst[j+1]:
#                 lst[j],lst[j+1] = lst[j+1],lst[j]
#     return lst
# lst = [9,8,2,1,5,4]
# print(b(lst))





# seletion


# def s(a):
#     for i in range(len(a)):
#         min = i
#         for j in range(i+1,len(a)):
#             if a[min]>a[j]:
#                 min = j
#         a[i], a[min] = a[min], a[i]
#     return a
#
#
# lst = [9,8,2,1,5,4]
# lst2 = [4,2,6,5,1,3]
# print(s(lst2))

######################################################3


#insertion sort

# def I(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j>-1 and key<arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr
# lst2 = [4,2,6,5,1,3]
# print(I(lst2))























###################################################
#P

# def bb(a):
#     for i in range(len(a)-1,0,-1):
#         for j in range(i):
#             if a[j]>a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
#     return a
# lst = [9,8,74,52,1,4]
# print(bb(lst))



# def ss(a):
#     for i in range(len(a)):
#         min = i
#         for j in range(i+1,len(a)):
#             if a[min]>a[j]:
#                 min = j
#         a[i],a[min] = a[min],a[i]
#     return a
# lst = [9,8,74,52,1,4]
# print(ss(lst))


#i

# def ii(a):
#     for i in range(1,len(a)):
#         k = a[i]
#         j = i-1
#         while j>-1 and a[j]>k:
#             a[j+1],j = a[j],j-1
#         a[j+1] = k
#     return a
# lst = [9,8,74,52,1,4]
# print(ii(lst))


#merge

# def merge(list1, list2):
#     combined = []
#     i = 0
#     j = 0
#     print('1 ',list1)
#     print('2 ',list2)
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             print('first while')
#             combined.append(list1[i])
#             print('list',combined)
#             i += 1
#         else:
#             combined.append(list2[j])
#             print('2 while')
#             print('list',combined)
#             j += 1
#     while i < len(list1):
#         combined.append(list1[i])
#         print('3 while')
#         print('list',combined)
#         i += 1
#     while j < len(list2):
#         combined.append(list2[j])
#         print('4 while')
#         print('list',combined)
#         j += 1
#     print('return')
#     return combined
# #print(merge([1, 2, 7, 8], [3, 4, 5, 6]))
#
# def merge_sort(my_list):
#     if len(my_list) == 1:
#         return my_list
#     mid = int(len(my_list) / 2)
#     left = my_list[:mid]
#     right = my_list[mid:]
#     return merge(merge_sort(left), merge_sort(right))
#
#
# print(merge_sort([3, 1, 4, 2]))




#quick

# def swap(my_list, index1, index2):
#     my_list[index1],my_list[index2] = my_list[index2],my_list[index1]
#
#
# def pivot(my_list, pivot_index, end_index):
#     swap_index = pivot_index
#
#     for i in range(pivot_index+1, end_index+1):
#         if my_list[i] < my_list[pivot_index]:
#             swap_index += 1
#             swap(my_list, swap_index, i)
#             print(my_list," ",swap_index)
#     swap(my_list, pivot_index, swap_index)
#     print(swap_index)
#     return swap_index
#
# my_list = [4,6,1,7,3,2,5]
#
# print(pivot(my_list, 0, 6))
#
# print(my_list)


# def swap(my_list, index1, index2):
#     my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
#
# def pivot(my_list, pivot_index, end_index):
#     swap_index = pivot_index
#     for i in range(pivot_index+1, end_index):
#         if my_list[i] < my_list[pivot_index]:
#             swap_index += 1
#             swap(my_list, swap_index, i)
#     swap(my_list, pivot_index, swap_index)
#     print('upper',my_list)
#     return swap_index
#
#
# def quick_sort_helper(my_list, left, right):
#     if left < right:
#         print(my_list, " ", left, " ", right )
#         pivot_index = pivot(my_list, left, right)
#         print('P',pivot_index)
#         print('one',quick_sort_helper(my_list, left, pivot_index-1))
#         print('b/w')
#         print('two',quick_sort_helper(my_list, pivot_index+1, right))
#         print('******')
#         print('end',my_list)
#     return my_list
#
# def quick_sort(my_list):
#     return quick_sort_helper(my_list, 0, len(my_list))
#
# print(quick_sort([4,6,1,7,3,2,5]))







# def quicker(lst):
#     l1,l2 = [],[]
#     if len(lst)<=1:
#         return  lst
#     else:
#         pivot = lst.pop()
#     for i in lst:
#         if i < pivot:
#             l1.append(i)
#         else:
#             l2.append(i)
#     return quicker(l1)+[pivot]+quicker(l2)
# print(quicker([9,8,4,8,5,2,1,0]))
# [3,2,1,5,4]
# 321 [4] 5
# [1 2 3]








#heap

"""
# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
	largest = i  # Initialize largest as root
	l = 2 * i + 1  # left = 2*i + 1
	r = 2 * i + 2  # right = 2*i + 2
	# See if left child of root exists and is
	# greater than root
	if l < n and arr[i] < arr[l]:
		largest = l
	# See if right child of root exists and is
	# greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r
	# Change root, if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]  # swap
		# Heapify the root.
		heapify(arr, n, largest)


# The main function to sort an array of given size


def heapSort(arr):
	n = len(arr)
	# Since last parent will be at ((n//2)-1) we can start at that location.
	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i)

	# One by one extract elements
	for i in range(n - 1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]  # swap
		heapify(arr, i, 0)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
	print("%d" % arr[i])


"""
