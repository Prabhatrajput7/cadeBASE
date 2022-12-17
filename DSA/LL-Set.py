class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    

my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

my_linked_list.set_value(1,4)

my_linked_list.print_list()

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
#l.popp()
#l.prepend(4)
#l.pop_f()
#print(l.gett(1))
l.set_value(1,4)
l.printt()  # print the ll new ll 0,10
