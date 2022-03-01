class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value) -> None:
        node = Node(value)
        self.first = node
        self.last = node
        self.length = 1

    def all(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def enqueue(self, value):
        node = Node(value)
        if self.first and self.last is None:
            self.first = node
            self.last  = node
            self.length+=1
        self.last.next = node
        self.last = node
        self.length+=1
    
    def dequeue(self):
        if self.first and self.last is None:
            return None
        if self.length == 1:
            self.first = None
            self.last = None
            self.length-=1
        temp = self.first
        self.first = temp.next
        temp = None
        self.length-=1
        return temp


queue = Queue(2)
queue.enqueue(3)
queue.dequeue()
queue.all()