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


class PlateStack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
    
    def __str__(self):
        return self.stacks
    
    def push(self, item):
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])
    
    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()
    
    def pop_at(self, stackNumber):
        if len(self.stacks[stackNumber]) > 0:
            return self.stacks[stackNumber].pop()
        else:
            return None


customStack= PlateStack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.pop_at(1))