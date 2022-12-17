class Node:

    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None


class CC:

    def __init__(self):
        self.head = None
        self.tail = None
        self.h = 0

    def pushlast(self,data):
        n = Node(data)

        if self.head is None:
            self.head = n
            self.tail = n
            self.tail.next = self.head
            self.head.previous = self.tail
        else:
            self.tail.next = n
            n.previous = self.tail
            self.tail = n
            self.tail.next = self.head
            self.head.previous = self.tail
        self.h += 1

    def pushfront(self,data):
        n = Node(data)

        if self.head is None:
            self.head = n
            self.tail = n
            self.tail.next = self.head
            self.head.previous = self.tail
        else:
            n.next = self.head
            self.head.previous = n
            self.head = n
            self.tail.next = self.head
            self.head.previous = self.tail
        self.h += 1

    def dllast(self):

        if self.head is None:
            return -1
        else:
            temp = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
            temp.previous = None
            self.tail.next = self.head
            self.head.previous = self.tail

        self.h -=1

    def dlfront(self):
        if self.head is None:
            return -1
        else:
            temp = self.head
            self.head = self.head.next
            self.head.previous = None
            temp.next = None
            self.tail.next = self.head
            self.head.previous = self.tail
        self.h -=1

    def idx(self,data):

        if data<0 or data >self.h:
            return -1
        else:
            temp = self.head
            for _ in range(data):
                temp = temp.next
        return temp.value


    def reverse(self):

        if self.head is None:
            return -1

        else:
            temp = self.head
            self.head, self.tail = self.tail,self.head
            after = temp.next
            before = None
            for i in range(self.h):
                after = temp.next
                temp.next = before
                temp.previous = after
                before = temp
                temp = after

        temp.next = self.head
        self.head.previous = temp


    def display(self):

        if self.head is None:
            return -1
        else:
            curr = self.head
            while True:
                print(curr.value, end=" ")
                curr = curr.next
                if (curr == self.head):
                    break

cir = CC()
cir.pushlast(4)
cir.pushlast(5)
cir.pushlast(6)
cir.pushfront(3)
cir.pushfront(2)
cir.dllast()
cir.dlfront()
# print(cir.idx(2))
cir.display()
cir.reverse()
cir.pushlast(6)
print('\n')
cir.display()
