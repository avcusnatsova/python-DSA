class queue:
    def __init__(self, maxsize):
        self.items = maxsize*[None]
        self.maxsize = maxsize
        self.start = -1
        self.top = -1
    
    def isfull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxsize:
            return True
        else:
            return False
    def isempty(self):
        if self.top == -1:
            return True
        else:
            return False
    def enqueue(self,value):
        if self.isfull():
            return "queue is full"
        else:
            if self.top + 1== self.maxsize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "the element is inserted"
    def dequeue(self):
        if self.isempty():
            return "queue is empty"
        else:
            firstelement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start +1 == self.maxsize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstelement
    def peek(self):
        if self.isempty():
            return "nothing to see"
        else:
            return self.items[self.start]
    def delete(self):
        self.items = self.maxsize * [None]
        self.top = -1 
        self.start = -1

customQueue = queue(3)

print(customQueue.isempty())   
print(customQueue.isfull())     

print(customQueue.enqueue(10))   
print(customQueue.enqueue(20))   
print(customQueue.enqueue(30))   
print(customQueue.isfull())     

print(customQueue.peek())  

print(customQueue.dequeue())   
print(customQueue.dequeue())   

print(customQueue.enqueue(40))   
print(customQueue.enqueue(50))   

print(customQueue.peek())  

print(customQueue.dequeue())   
print(customQueue.dequeue())   
print(customQueue.dequeue())   

print(customQueue.isempty())   

customQueue.delete()
print(customQueue.items)

