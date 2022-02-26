class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value=None):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1
    
    def append(self, value):
        node = Node(value)
        # check if head is empty
        if self.head.value and self.tail.value is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length+=1
    
    def pop(self, value=None):
        # check if there are no items in the linkedlist
        if self.head and self.tail is None:
            self.head = None
            self.tail = None
            return None
        # pop the last item in the linkedlist
        elif not value:
            temp = self.head
            pre = self.head
            while not temp.next == None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length-=1
            return temp

        # Pop a particular value in the linked list
        elif value:
            temp = self.head
            while not temp.value  == value:
                temp = temp.next
            self.tail.value = None
            return temp

    def all(self):
        elements = self.head
        while elements is not None:
            print(elements.value)
            elements = elements.next

linked_list = LinkedList(5)
# Append values to the linked list
linked_list.append(20)
linked_list.append(10)

# print('Head:', linked_list.head.value)
# print('Tail:', linked_list.tail.value)
# print(linked_list.all())

# print(linked_list.length)
# print(linked_list.all())
print(linked_list.pop(5))
print(linked_list.all())
