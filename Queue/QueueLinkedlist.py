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
    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next
class queue:
    def __init__(self):
        self.linkedlist = linkedlist()
    def enqueue(self, value):
        newnode = node(value)
        if self.linkedlist.head == None:
            self.linkedlist.head = newnode
            self.linkedlist.tail = newnode
        else:
            self.linkedlist.tail.next = newnode
            self.linkedlist.tail = newnode
    def isempty(self):
        return self.linkedlist.head == None
    def dequeue(self):
        if self.isempty():
            return "queue is empty"
        else:
            temp = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return temp
    def peek(self):
        if self.isempty():
            return "queue is empty"
        else:
            return self.linkedlist.head
    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None

q = queue()

print("Is queue empty?", q.isempty())  

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front element (peek):", q.peek())  

print("Dequeued:", q.dequeue())  
print("Dequeued:", q.dequeue())  

q.enqueue(40)
q.enqueue(50)

print("Front element (peek):", q.peek())  

print("Dequeued:", q.dequeue())  
print("Dequeued:", q.dequeue())  
print("Dequeued:", q.dequeue())  

print("Is queue empty?", q.isempty())  

q.enqueue(100)
q.enqueue(200)
print("Front element before delete:", q.peek())  

q.delete()
print("Is queue empty after delete?", q.isempty())  
