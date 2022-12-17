class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None

class DD:
    def __init__(self):
        self.head = None
        self.tail = None
        self.h =0

    def insertend(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
        self.h +=1

    def insertfront(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
        self.h += 1

    def deleteend(self):
        if self.head is None:
            return False
        elif self.h ==1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
            temp.previous = None
            self.h -=1

    def deletefront(self):
        if self.head is None:
            return False
        elif self.h ==1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.previous = None
            temp.next = None
            self.h -=1

    def indexnum(self,num):
        temp = self.head
        pr = 0
        while temp:
            if temp.value == num:
                return pr
            temp = temp.next
            pr+=1
        return -1

    def numindex(self,idx):
        if idx<0 or idx>self.h:
            return False
        else:
            temp = self.head
            for i in range(idx):
                temp=temp.next
            return temp #add.value to get the value

    def insertbw(self,num,idx):
        if idx<0 or idx>self.h:
            return False
        elif idx == 0:
            return self.insertfront(num)
        elif idx == self.h:
            return self.insertend(num)
        node = Node(num)
        temp = self.numindex(idx-1)
        temp2 = self.numindex(idx+1)
        node.next = temp.next
        temp.next = node
        node.previous = temp
        temp2.previous = node
        self.h +=1

    def reverse(self):
        temp = self.tail
        while temp:
            print(temp.value)
            temp = temp.previous

    def realreverse(self):
        temp = self.head
        self.head, self.tail = self.tail, self.head
        after = temp.next
        before = None
        for i in range(self.h):
            after = temp.next
            temp.next = before
            temp.prev = after
            before = temp
            temp = after


    def sortingll(self):
        temp = self.head
        lst = []
        while temp:
            lst.append(temp.value)
            temp = temp.next
        return sorted(lst)

    def display(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def deleteinbw(self,ind):
        if self.head is None:
            return False
        elif self.h == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.numindex(ind-1)
            temp2 = self.numindex(ind)
            temp3 = self.numindex(ind+1)
            temp.next = temp2.next
            temp3.previous = temp2.previous
            temp2.previous = None
            temp2.next = None
        self.h -=1

    def deletevno(self,num):
        check = self.indexnum(num)
        self.deleteinbw(check)

d = DD()
d.insertend(11)
d.insertend(13)
d.insertend(15)
d.insertend(17)
d.insertfront(9)
d.display()
# print('********')
# d.deleteend()
# d.deletefront()
# d.display()
# print('Index of num is', d.indexnum(13))
# print('Number on index',d.numindex(1))
# d.insertbw(50,1)
d.insertbw(60,1)
print('********')
d.display()
print('********')
d.deletevno(60)
# d.deleteinbw(1)
d.display()
# d.realreverse()
# d.reverse()
# print('********')
# d.display()
#print(d.sortingll())