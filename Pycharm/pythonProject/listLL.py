# initaling LL

#appending tail O(1) removing from tail O(n)
#appending and removing head O(1)
#removing and adding in b/w O(n)
#getting value in a LL O(n)

#GFGs
# traversing O(n) space O(1)
# class Node:
#     def __init__(self,item):
#         self.item = item
#         self.next = None
#
# class L:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#     def display(self,l):
#         temp = l
#         while temp:
#             print(temp.value)
#             temp = temp.next
#     def find(self,l,no): #searching element
#         temp = l
#         pos = 1
#         while temp:
#             if temp.value == no:
#                 return pos
#             temp = temp.next
#             pos+=1
#         return -1
#     def insertfirst(self,l,item):
#         newnode = Node(item)
#         newnode.next = l
#         return newnode
#
#
#
#
# head = L(5)
# head.next = L(10)
# head.next.next = L(20)
# head.display(head)
# print(head.find(head,10))
# print(head.find(head,2))
# head.insertfirst(head,2)
# head.display(head)





class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Link:
    def __init__(self):
        self.head = None
        self.tail = None
        self.h=0

    def insertend(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.h +=1

    def insertfront(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.h += 1

    def deletend(self):
        if self.head is None:
            return False
        else:
            temp = self.head
            pre = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.h -= 1

    def deletefront(self):
        if self.head is None:
            return False
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.h -=1

    def indexx(self,num):
        pos = 0
        temp = self.head
        while temp:
            if temp.value == num:
                return pos #add pos to get position of the number
            temp = temp.next
            pos+=1
        return -1

    def indexx2(self,idx):
        if idx < 0 or idx >= self.h:
            return False
        else:
            temp = self.head
            for i in range(idx):
                temp =temp.next
            return temp #add.value to get the value of node

    def insertbet(self,num,ind):
        if ind < 0 or ind > self.h:
            return False
        elif ind ==0:
            return self.insertfront(num)
        elif ind == self.h:
            return self.insertend(num)
        node = Node(num)
        temp = self.indexx2(ind - 1)
        node.next = temp.next
        temp.next = node
        self.h +=1


    def deletebetin(self,id):
        if id < 0 or id > self.h:
            return False
        elif id ==0:
            return self.deletefront()
        elif id == self.h:
            return self.deletend()
        temp = self.indexx2(id - 1)
        temp2 = self.indexx2(id)
        temp.next = temp2.next
        temp2.next = None
        self.h -=1


    def deletebetnum(self,num):
        check = self.indexx(num)
        self.deletebetin(check)

    def reverse(self):
        temp = self.head
        self.head,self.tail = self.tail,self.head
        after = temp.next
        before = None
        for i in range(self.h):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def display(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


l = Link()
l.insertend(5)
l.insertend(10)
l.insertend(15)
l.insertend(20)
l.insertend(25)
l.insertend(30)
l.insertfront(0)
l.insertfront(2)
l.deletefront()
l.deletend()
# l.display()
print('index = ',l.indexx(0)) #tell index on putting number
print(l.indexx2(2)) #tell number on putting index
# l.insertbet(30,1)
# print('Insert b/w')
# l.display()
# l.deletebetin(1)
# print('delete via index')
# l.display()
# print('delete ***')
#l.deletebetnum(5)
l.display()
# print('************')
# l.reverse()
# l.display()










