class node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)
class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
class queue:
    def __init__(self):
        self.linkedlist = linkedlist()
    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return ' '.join(values)
    
    def enqueue(self,value):
        newnode = node(value)
        if self.linkedlist.head == None:
            self.linkedlist.head = newnode
            self.linkedlist.tail = newnode
        else:
            self.linkedlist.tail.next = newnode
            self.linkedlist.tail = newnode
    def isempty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False
    def dequeue(self):
        if self.isempty():
            return "queue is empty"
        else:
            tempnode = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return tempnode.value
    def peek(self):
        if self.isempty():
            return "no node in queue"
        else:
            return self.linkedlist.head.value
    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None


q = queue()
q.enqueue(10)   
q.enqueue(20)  
q.enqueue(30)  

print(q.dequeue())  
print(q.dequeue())  
print(q.dequeue())
print(q.dequeue()) 
