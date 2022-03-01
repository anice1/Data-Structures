class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def all(self):
        if self.head and self.tail is None:
            return None
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        node = Node(value)
        if self.head and self.tail is None:
            # create a node
            self.head = node
            self.tail = node
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        # increment length
        self.length+=1
    
    def prepend(self, value):
        node = Node(value)
        temp = self.head
        self.head.prev = node
        self.head = node
        node.next = temp
        # increment length
        self.length+=1
        return node

    def get(self, index):
        # check if index is in arange
        if self.head and self.tail is None:
            return None
        if index<0 or index>self.length:
            raise IndexError('Index out of range')
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def pop(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length-=1
            return self.head

        if index == self.length:
            self.tail = self.tail.prev
            self.tail = None
            self.length-=1
            return self.tail

        temp = self.get(index)
        if temp is not None:
            pre = self.get(index-1)
            pre.next = temp.next
            temp = None
            self.length -=1
            return temp
        raise IndexError('Index out of range')

    def insert(self, index, value):
        if index == 0:
            return self.append(value)

        if index == self.length:
            return self.prepend(value)

        node = Node(value)
        temp = self.get(index)
        pre = self.get(index-1)

        if temp is not None:
            pre.next = node
            node.prev = pre
            node.next = temp
            temp.prev = node
            self.length+=1
            return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            before.prev = after



# instantiate our class
doubly = DoublyLinkedList(1)
# Append a value to doubly
doubly.append(5)
# doubly.prepend(9)
# doubly.pop(2)
doubly.insert(0, 20)
doubly.insert(2, 290)
doubly.insert(3, 2300)
doubly.all()
print('=====Reverse=====')
doubly.reverse()
print(doubly.all())