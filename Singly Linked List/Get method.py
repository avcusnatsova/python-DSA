class node:
    def __init__(self, value):
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
    def get(self,index):
        if index < 0:
            return None
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.value
            current = current.next
            count += 1
        return None
ll = sll()
ll.append(10)
ll.append(20)
ll.append(30)

print(ll.get(0))  
print(ll.get(1))  
print(ll.get(2))  
print(ll.get(3))