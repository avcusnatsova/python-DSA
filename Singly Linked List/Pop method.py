'''class node:
    def __init__ (self, value):
        self.value = value
        self.next = None
class sll:
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None
    def append(self,value):
        newnode = node(value)
        if self.head == None:
            self.head = newnode
        else:
            current = self.head
    while current.next:
        current = current.next
    current.next = newnode
         self.tail.next = newnode
        self.tail = newnode
        self.length += 1
    def pop_first(self):
        if self.length == 0:
            return None
        poppednode = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            poppednode.next = None
        self.length -= 1
        return poppednode
    def pop(self):
        if self.length == 0:
            return None
        poppednode = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        self.length -= 1
        return poppednode 
ll = sll()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

#ll.pop_first()
ll.pop()
current = ll.head
while current is not None:
    print(current.value)
    current = current.next'''

#remove

class node:
    def __init__(self, value):
        self.value = value
        self.next = None

class sll:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        newnode = node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        poppednode = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            poppednode.next = None
        self.length -= 1
        return poppednode

    def pop(self):
        if self.length == 0:
            return None
        poppednode = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        self.length -= 1
        return poppednode

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
ll = sll()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

ll.pop()  # remove last

current = ll.head
while current is not None:
    print(current.value)
    current = current.next
