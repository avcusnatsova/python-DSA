class stack:
    def __init__(self):
        self.items = []

    def push(self,element):
        self.items.append(element)
    
    def pop(self):
        if self.isempty():
            return "stack is empty"
        else:
            return self.items.pop()
    def peek(self):
        if self.isempty():
            return "stack is empty"
        else:
            return self.items[-1]
        
    def isempty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items = []

    def __str__(self):
        if self.isempty():
            return "stack is empty"
        return '\n'.join(map(str, reversed(self.items)))
    
s = stack()

print("Is stack empty?", s.isempty())

s.push(10)
s.push(20)
s.push(30)
s.push(40)

print("\nStack content (top to bottom):")
print(s)

print("\nTop element (peek):", s.peek())

print("Popped element:", s.pop())
print("Popped element:", s.pop())

print("\nStack after popping two elements:")
print(s)

print("\nCurrent size:", s.size())

s.clear()
print("\nAfter clearing, is empty?", s.isempty())
print(s)
