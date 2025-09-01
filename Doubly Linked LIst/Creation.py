class node:
    def __init__(self, value =None):
        self.value = value
        self.next = None
        self.prev = None
class dll:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def createdll(self, nodeValue):
        newnode = node(nodeValue)
        newnode.prev =None
        newnode.next = None
        self.head = newnode
        self.tail = newnode
        return "dll is created"
    def insertnode(self, nodeValue, location):
        if self.head is None:
            print("The node cannot be inserted")
        else:
            newnode = node(nodeValue)
            if location == 0:
                newnode.prev = None
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode
            elif location == 1:
                newnode.next = None
                newnode.prev = self.tail
                self.tail.next = newnode
                self.tail = newnode
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                newnode.next = temp.next
                newnode.prev = temp
                newnode.next.prev = newnode
                temp.next = newnode
DLL = dll()
DLL.createdll(5)
#print([n.value for n in DLL])
DLL.insertnode(0,0)
DLL.insertnode(2,1)
DLL.insertnode(1,1)
print([node.value for node in DLL])