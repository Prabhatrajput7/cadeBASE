# removing element from frondend o(n) top =  o(1)
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class Stack:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.top = new_node
#         self.height = 1
#
#     def print_stack(self):
#         temp = self.top
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
#
#     def push(self, value):
#         new_node = Node(value)
#         if self.height == 0:
#             self.top = new_node
#         else:
#             new_node.next = self.top
#             self.top = new_node
#         self.height += 1
#         return True
#
#     def pop(self):
#         if self.height == 0:
#             return None
#         temp = self.top
#         self.top = self.top.next
#         temp.next = None
#         self.height -= 1
#         return temp
#
#
# my_stack = Stack(7)
# my_stack.push(23)
# my_stack.push(3)
# my_stack.push(11)
#
# print(my_stack.pop(), '\n')
#
# my_stack.print_stack()





# top is at 4 its a temp var we are using to add node
#none<-1<-2<-3<-4



class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Stackk:
    def __init__(self):
        self.top = None
        self.h = 0

    def display(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self,value):
        newn = Node(value)
        newn.next = self.top
        self.top = newn
        self.h+=1

    def by(self):
        if self.top is None:
            return False
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.h -= 1
            return temp.value

    def topp(self):
        if self.top is None:
            return False
        else:
            return self.top.value

s = Stackk()
s.push(7)
s.push(8)
s.push(9)
print('*',s.by())
#9->8->-7>None
s.display()
s.push(99)
print(s.topp())
s.display()





# class Stack:
#     def __init__(self):
#         self.s = list()
#     def push(self,item):
#         self.s.append(item)
#     def pop(self):
#         if len(self.s) < 1:
#             return False
#         else:
#             return self.s.pop()
#     def display(self):
#         if len(self.s) < 1:
#             return False
#         else:
#             return self.s
#     def topper(self):
#         if len(self.s) < 1:
#             return False
#         else:
#             return self.s[len(self.s)-1]
#
# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# print(s.pop())
# print(s.display())
# print(s.topper())
















