class node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __iter__(self):
        node = self.head
        count = 0
        while node and count < self.length:
            yield node
            node = node.next
            count += 1
    #create DLL
    def create(self, nodeValue):
        newnode = node(nodeValue)
        newnode.next = newnode
        newnode.prev = newnode
        self.head = newnode
        self.tail = newnode
        self.length = 1
        return "CDLL is created"
    def append(self, value):
        if self.head is None:
            return self.create(value)
        newnode = node(value)
        newnode.prev = self.tail
        newnode.head = self.head
        self.tail.next = newnode
        self.head.prev = newnode
        self.tail = newnode
        self.length += 1
    def prepend(self, value):
        if self.head is None:
            return self.create(value)
        newnode = node(value)
        newnode.next = self.head
        newnode.prev = self.tail
        self.tail.next = newnode
        self.head.prev = newnode
        self.head = newnode
        self.length +=1
    def insert(self, value, location):
        if self.head is None:
            return self.create(value)
        elif location <= 0:
            self.prepend(value)
        elif location >= self.length:
            self.append(value)
        else:
            temp = self.head
            for _ in range(location - 1):
                temp = temp.next
            newnode = node(value)
            newnode.next = temp.next
            newnode.prev = temp
            temp.next.prev = newnode
            temp.next = newnode
            self.length += 1
    def traverse(self):
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            count = 0
            while count < self.length:
                print(temp.value, end=" ")
                temp = temp.next
                count += 1
            print()
    def reverse(self):
        if self.head is None:
            print("list is empty")
        else:
            temp = self.tail
            count = 0
            while count < self.length:
                print(temp.value, end = " ")
                temp = temp.next
                count += 1
            print()
    def search(self,value):
        temp = self.head
        count = 0
        while count < self.length:
            if temp.value == value:
                return f"found at index{count}"
            temp = temp.next
            count += 1
        return "not founc"
    def delete(self,location):
        if self.length == 0:
            print("list is empty")
            return
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return
        if location == 0:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        elif location >= self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.tail.prev = self.tail
        else:
            temp = self.head
            for _ in range(location - 1):
                temp = temp.next
            temp.next = temp.next.next
            temp.next.prev = temp
        self.length -= 1
    def __str__(self):
        return "<->".join([str(node.value) for node in self]) + "(circular)"
    
cdll = CDLL()
cdll.create(10)
cdll.append(20)
cdll.append(30)
cdll.prepend(5)
cdll.insert(15,2)
print([n.value for n in cdll])

cdll.traverse()
cdll.reverse()

print(cdll.search(15))
print(cdll.search(99))

cdll.delete(0)
print([n.value for n in cdll])

cdll.delete(2)
print([n.value for n in cdll])



