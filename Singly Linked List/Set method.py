class node:
    def __init__ (self,value):
        self.value = value
        self.next = None
class sll:
    def __init__(self):
        self.head = None
    def append(self, value):
        newnode = node(value)
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newnode
    def set(self, index, value):
        if index < 0:
            return False
        current = self.head
        count = 0
        while current:
            if count == index:
                current.value = value
                return True
            current = current.next
            count += 1
        return False
mylist = sll()
mylist.append(10)
mylist.append(20)
mylist.append(30)

mylist.set(1, 50)  # set value at index 1 to 50

# Print updated list
current = mylist.head
while current:
    print(current.value)
    current = current.next