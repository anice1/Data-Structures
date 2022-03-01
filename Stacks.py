class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        node = Node(value)
        self.top = node
        self.height = 1

    def all(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        node = Node(value)
        if self.top is None:
            self.top = node
            self.height+=1

        node.next = self.top
        self.top = node
        self.height+=1
    
    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        temp = None
        self.height-=1

stack = Stack(2)
stack.push(4)
stack.pop()
stack.all()