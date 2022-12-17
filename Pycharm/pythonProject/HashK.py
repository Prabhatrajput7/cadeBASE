#key value pairs gives us an address
#its a one way
#example {'nails': 1000} this will give as 2 when we ask for 2 it wont give us  {'nails': 1000}  this is Determistic
# [collision in hash] two list have same address 2 ['nails',1000]['n', 1000] -> [['nails', 1000],['n', 1000]]
# separate chaining says if u encounter collision the search below till u get free ADDRESS space and insert the value over there

#another way of doing hashing by LL instead of List

#total length is equal to a prime number can reduce collisions

# searching item in a dict is O(1)
# hach O(1) for every case
#if all item are at one address and we neeed to find last then O(n)

#searching common element in 2 list this is not a good apporach

# def lst(l1,l2):
#     for i in l1:
#         for j in l2:
#             if i == j:
#                 return True
#     return False
# print(lst([1,2,3],[4,5,1]))

# using dict

# def lst(l1,l2):
#     d ={}
#     for i in l1:
#         d[i] = True
#     for j in l2:
#         if j in d:
#             return True
#     return False
# print(lst([1,2,3],[4,5,1]))

# lst = [['bihar',30],['delhi',15]]
# print(lst[0][1])

# class HashTable:
#     def __init__(self, size=7):
#         self.data_map = [None] * size
#
#     def __hash(self, key):
#         my_hash = 0
#         for letter in key:
#             my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
#         return my_hash
#
#     def print_table(self):
#         for i, val in enumerate(self.data_map):
#             print(i, ": ", val)
#
#     def set_item(self, key, value):
#         index = self.__hash(key)
#         if self.data_map[index] is None:
#             self.data_map[index] = []
#         self.data_map[index].append([key, value])
#
#     def get_item(self, key):
#         index = self.__hash(key)
#         if self.data_map[index] is not None:
#             for i in range(len(self.data_map[index])):
#                 if self.data_map[index][i][0] == key:
#                     return self.data_map[index][i][1]
#         return None
#
#     def keys(self):
#         all_keys = []
#         for i in range(len(self.data_map)):
#             if self.data_map[i] is not None:
#                 for j in range(len(self.data_map[i])):
#                     all_keys.append(self.data_map[i][j][0])
#         return all_keys
#
#
# my_hash_table = HashTable()
#
# my_hash_table.set_item('bolts', 1400)
# my_hash_table.set_item('washers', 50)
# my_hash_table.set_item('lumber', 70)
# print(my_hash_table.print_table())
# print(my_hash_table.keys())





class Hash:
    def __init__(self,size=7):
        self.lst = [None]*size
    def __hash(self,key):
        ihash = 0
        for i in key:
            ihash = (ihash + ord(i) * 23) % len(self.lst)
        return ihash
    def set_value(self,key,value):
        index = self.__hash(key)
        if self.lst[index] == None:
            self.lst[index] =[]
        self.lst[index].append([key,value])
    def get_value(self,key):
        index = self.__hash(key)
        if self.lst[index] is not None:
            for i in range(len(self.lst[index])):
                if self.lst[index][i][0] == key:
                    return self.lst[index][i][1]
    def keys(self):
        keys =[]
        for i in range(len(self.lst)):
            if self.lst[i] is not None:
                for j in range(len(self.lst[i])):
                    keys.append(self.lst[i][j][0])
        return keys
    def printing(self):
        for i, j in enumerate(self.lst):
            print(f'{i} = {j}')
        return self.lst
h = Hash()
h.set_value('kira',7)
h.set_value('ria',69)
h.set_value('kia',4)
# print(h.get_value('ria'))
print(h.keys())
print(h.printing())





