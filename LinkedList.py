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
        self.length += 1
        # return True

    def prepend(self, value):
        node = Node(value)
        if self.head and self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        # return True

    def pop(self, index=None):
        # check if there are no items in the linkedlist
        if self.head and self.tail is None:
            self.head = None
            self.tail = None
            return None
        # pop the last item in the linkedlist
        if not index:
            temp = self.head
            pre = self.head
            while not temp.next == None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            return temp

        # Pop a particular value in the linked list
        temp = self.get(index)
        if temp is not None:
            pre = self.get(index - 1)
            pre.next = temp.next
            temp.next = None
            self.length -=1
        
    def pop_first(self):
        if self.head and self.tail is None:
            return None
        temp = self.head
        self.head = self.head.next
        temp = None
        self.length-=1

    def get(self, index):
        if index<0 or index >self.length:
            raise IndexError('Index out of range')
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        # check if index is in range
        temp = self.get(index)
        if temp is not None:
            node = Node(value)
            # check if index is first, yes? prepend
            if index == 0:
                return self.prepend(value)
            # check if index is last, yes? append
            if index == self.length:
                return self.append(value)

            temp = self.get(index - 1)
            # set temp.next to node
            node.next = temp.next
            temp.next = node
            self.length+=1
            # return True
    
    def remove(self, index):
        temp = self.get(index)
        if temp is None:
            return None
        if index ==0:
            return self.pop_first()
        elif index == self.length:
            return self.pop()
        pre = self.get(index-1)
        # drop temp to None
        pre.next = temp.next
        temp.next = None
        self.length -=1
        return temp

    def reverse(self):
        # switch head to tail and tail to head
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def all(self):
        elements = self.head
        while elements is not None:
            print(elements.value)
            elements = elements.next


# Initiate our linkedlist
linked_list = LinkedList(1)

# Append values to the linked list
linked_list.append(20)
linked_list.append(10)
linked_list.append(10)
linked_list.append(50)

linked_list.reverse()
print(linked_list.all())
