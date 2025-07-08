class slist:
    def __init__ (self):
        self.head = None
        self.tail = None
class node:
    def __init__ (self, value=None):
        self.value = value
        self.next = None

sll = slist()
node1 = node(1)
node2 = node(2)

sll.head = node1
sll.head.next = node2
sll.tail = node2

print(sll)