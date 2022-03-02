class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return True
        
        temp = self.root
        while (True):
            if node.value > temp.value:
                if temp.right is None:
                    temp.right = node
                    return False
                temp = temp.right
            elif node.value < temp.value:
                if temp.left is None:
                    temp.left = node
                    return False
                temp = temp.left
            elif node.value == temp.value:
                return False
    
    def contains(self, value):
        if self.root is None:
            return None
        temp = self.root
        while temp is not None:
            if value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
            else:
                return True
        return False

    def minimum(self, node):
        if self.root is None:
            return None
        while node.left is not None:
            node = node.left
        return node
            

binary = BinarySearchTree()
binary.insert(2)
binary.insert(10)
binary.insert(1)
binary.insert(7)
binary.insert(0)
# print(binary.root.value)
# print(binary.root.left.value)
# print(binary.contains(7))
print(binary.minimum(binary.root.right).value)