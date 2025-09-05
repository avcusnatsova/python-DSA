class stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.list = []

    def __str__(self):
        values = [ str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    def isempty(self):
        return self.list == []
    
    def isfull(self):
        return len(self.list) == self.maxsize
    
    def push(self,value):
        if self.isfull():
            return "the stack is full"
        else:
            self.list.append(value)
            return f"{value} has been inserted"

    def pop(self):
        if self.isempty():
            return "there is no element to pop"
        else:
            return self.list.pop() 
        
    def peek(self):
        if self.isempty():
            return "there is no element in stack"
        else:
            return self.list[-1]
    def delete(self):
        self.list = []
        return "stack has been deleted"
    
customStack = stack(3)   
print("Is empty?", customStack.isempty())   
print("Is full?", customStack.isfull())     

print(customStack.push(10))   
print(customStack.push(20))   
print(customStack.push(30))   
print(customStack.push(40))  

print("\nStack content (top to bottom):")
print(customStack)             

print("\nPeek top element:", customStack.peek())  
print("Popped element:", customStack.pop())        

print("\nStack after pop:")
print(customStack)             

print("\nDelete stack:", customStack.delete())     
print("Is empty now?", customStack.isempty())      