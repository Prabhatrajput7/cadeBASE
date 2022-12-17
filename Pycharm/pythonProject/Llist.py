# removing element from tail, insert and delete in b/w o(n) else o(1)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LL:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.h = 1

    def printt(self):
        while self.head is not None:
            print(self.head.value)
            self.head = self.head.next

    def appendd(self, value):
        node = Node(value)
        if self.h == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.h += 1
        return True

    def popp(self):
        if self.h == 0:
            return False
        elif self.h == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            pre = self.head
            while (temp.next):  # or while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.h -= 1

    def prepend(self, value):
        node = Node(value)
        if self.h == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.h += 1
        return True

    def pop_f(self):
        if self.h == 0:
            return False
        elif self.h == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.h -= 1

    def gett(self, index):
        if index < 0 and index >= self.h:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def set_value(self, index, value):
        temp = self.gett(index)
        if temp:
            temp.value = value
            return True
        return False


l = LL(11)
l.appendd(3)
l.appendd(23)
l.appendd(7)
l.popp()
l.prepend(4)
l.pop_f()
print(l.gett(1)) # here 1 is index
#l.set_value(3,4)
l.printt()  # print the ll new ll 0,10


# class LinkL:
#     def __init__(self,value):
#         self.value = value
#         self.next  =None
#
#     def display(self,head):
#         temp = head
#         while head:
#             print(temp.value)
#             temp = temp.next
#
# l = LinkL(10)
# l.next = LinkL(20)
# l.next.next = LinkL(30)
# l.next.next.next = LinkL(40)
# l.display(l)