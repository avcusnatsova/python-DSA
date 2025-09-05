class stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = self.list[:]
        values.reverse()
        values = [str(x) for x in values]
        return '\n'.join(values)
    #isempty
    def isempty (self):
        if self.list == []:
            return True
        else:
            return False
    
    #push
    def push(self, value):
        self.list.append(value)
        return "element has been pushed"
    
    #pop
    def pop(self):
        if self.isempty():
            return "there no element"
        else:
            return self.list.pop()
        
    #peek
    def seek(self):
        if self.isempty():
            return "there no element"
        else:
            return self.list[len(self.list) - 1]
    
    #delete stack
    def delete(self):
        self.list = []


customstack = stack()
#print(customstack.isempty())
customstack.push(1)
customstack.push(2)
customstack.push(3)
print(customstack)
print("element that is popped")
print(customstack.pop())
print("list after popping")
print(customstack)
print("top element after pop")
print(customstack.seek())
print(customstack.delete())
print(customstack.isempty())