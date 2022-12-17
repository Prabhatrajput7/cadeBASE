#insert from end[rear] delete from start[front]

#rear removing O(n) and adding O(1)
#front both O(1)
#so insert from end[rear] delete from start[front]

#both withh be O(1)


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class Queue:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.first = new_node
#         self.last = new_node
#         self.length = 1
#
#     def print_queue(self):
#         temp = self.first
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
#
#     def enqueue(self, value):#insert
#         new_node = Node(value)
#         if self.first is None:
#             self.first = new_node
#             self.last = new_node
#         else:
#             self.last.next = new_node
#             self.last = new_node
#         self.length += 1
#         return True
#
#     def dequeue(self):#remove
#         if self.length == 0:
#             return None
#         temp = self.first
#         if self.length == 1:
#             self.first = None
#             self.last = None
#         else:
#             self.first = self.first.next
#             temp.next = None
#         self.length -= 1
#         return temp
#
#
# my_queue = Queue(1)
# my_queue.enqueue(2)
#
# # (2) Items - Returns 2 Node
# print(my_queue.dequeue())
# # (1) Item -  Returns 1 Node
# print(my_queue.dequeue())
# # (0) Items - Returns None
# print(my_queue.dequeue())






# class Queue:
#     def __init__(self):
#         self.q = list()
#     def push(self,item):
#         self.q.append(item)
#     def display(self):
#         if len(self.q) < 1:
#             return False
#         else:
#             return self.q
#     def topper(self):
#         if len(self.q) < 1:
#             return False
#         else:
#             return self.q[len(self.q)-1]
#     def pop(self):
#         if len(self.q) < 1:
#             return False
#         else:
#             return self.q.pop(0)
#
# q = Queue()
# q.push(11)
# q.push(1)
# q.push(2)
# q.push(3)
# q.push(4)
# print(q.display())
# q.pop()
# print(q.display())





class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.f = None
        self.r = None
        self.h =0

    def push(self,value):
        node = Node(value)
        if self.r is None:
            self.f = node
            self.r = node
        else:
            self.r.next = node
            self.r = node
        self.h +=1

    def display(self):
        t = self.f
        while t is not None:
            print(t.value)
            t = t.next

    def pop(self):
        if self.f is None:
            return False
        else:
            temp = self.f
            self.f = self.f.next
            temp.next = None

    def top(self):
        if self.f is None:
            return False
        else:
            return self.r.value

q = Queue()
q.push(7)
q.push(8)
q.push(9)
q.pop()
q.display()
q.push(9)
q.display()
print(q.top())













