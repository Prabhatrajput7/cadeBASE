# Binary tree 2 node left and right
# Full tree - complete note

        # 1          #parent
    # 2      #3      #child
    # 4      #5          #leaf

# perfect any level of tree node is completely filled

            # 1
    # 2             #3
# 4      #5     #6          #7


# complete tree

                # 1
        # 2             #3
# 4      #5     #6          #7

# or

                # 1
        # 2             #3
    # 4      #5     #6          #7
# 8      #9

# note the above one is complete and full tree filling the tree form left to right


# binary search tree

# In a BST if a no. is greater than paren node then go to right side otherwise left


# 47    #2n - 1 (n is power here)
# 21                 #53
# 51         #59


# divide and concoren O(logn) best case

# worst case there all items are on left or right that will create a LL O(n)

# insert  LL> BST
# lookup [searing a value] LL< BST
# delete LL< BST

#dfs pre order all the way left then right then node
#DFS post order left right write value


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return True
        temp = self.root
        while True:
            if node.value == temp.value:  # checking same element in a tree
                return False
            elif node.value < temp.value:
                if temp.left is None:
                    temp.left = node
                    return True
                temp = temp.left
            elif node.value > temp.value:
                if temp.right is None:
                    temp.right = node
                    return True
                temp = temp.right

    def getvalue(self,num):
        if self.root == None:
            return False
        temp = self.root
        while temp is not None:
            if num == temp.value:
                return num
            elif num < temp.value:
                temp = temp.left
            elif num > temp.value:
                temp = temp.right
        return -1

    def min(self):
        if self.root == None:
            return False
        temp = self.root
        while temp.left is not None:
            temp = temp.left
        return temp.value

    def max(self):
        if self.root == None:
            return False
        temp = self.root
        while temp.right is not None:
            temp = temp.right
        return temp.value

    def BSTT(self):
        current_node = self.root
        queue,results = [],[]
        queue.append(current_node) #curr is a complete node here
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            # print(current_node.value)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def DFS(self):
        result =[]
        def traverse(curr):
            # pre
            result.append(curr.value)
            if curr.left is not None:
                traverse(curr.left)
            # in
            if curr.right is not None:
                traverse(curr.right)
            # post
        traverse(self.root)
        return result

bst = BST()
bst.insert(47)
bst.insert(21)
bst.insert(18)
bst.insert(27)
bst.insert(76)
bst.insert(52)
bst.insert(82)
# print(bst.root.value)
# print(bst.root.left.value)
# print(bst.root.right.value)
# print(bst.root.right.right.value)
# print('value')
# print(bst.getvalue(15))
# print(bst.min())
# print(bst.max())
# print(bst.BSTT())
print(bst.DFS())