class queue:
    def __init__(self):
        self.items =[]

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isempty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def enqueue(self, value):
        self.items.append(value)
        return "element is inserted at the end of queue"
    
    def dequeue(self):
        if self.isempty():
            return "there is nothing to dequeue"
        else:
            return self.items.pop(0)
        
    def peek(self):
        if self.isempty():
            return "there is nothing to peek"
        else:
            return self.items[0]
    
    def delete(self):
        self.items = []
q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue:", q)          
print("Peek:", q.peek())  
print("Dequeue:", q.dequeue())  
print("Queue after dequeue:", q)  

q.delete()
print("After delete:", q) 

