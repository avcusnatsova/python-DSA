class node:
    def __init__(self,value):
        self.value = value
        self.next = None
    def __str__ (self):
        return str(self.value)
class csll:
    def __init__ (self,value):
        newnode = node(value)
        newnode.next = newnode
        self.head = newnode
        self.tail = newnode
        self.length = 1
    def __init__(self, value =None):
        self.head = None
        self.tail = None
        self.length = 0

        if value is not None:
            newnode = node(value)
            newnode.next = newnode
            self.head = newnode
            self.tail = newnode
            self.length = 1
circular_list = csll(10)
print("Head:", circular_list.head)
print("Tail:", circular_list.tail)
print("Tail.next:", circular_list.tail.next)
