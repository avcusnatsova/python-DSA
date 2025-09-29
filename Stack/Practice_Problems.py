'''#1.  Use a single list to implement three stacks.

class multistack:
    def __init__(self, stacksize):
        self.numberstacks = 3
        self.cuslist = [0] * (stacksize * self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stacksize = stacksize
    def isfull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False
        
    def isempty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False
        
    def indexoftop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1
    def push(self, item, stacknum):
        if self.isfull(stacknum):
            return "stack is full"
        else:
            self.sizes[stacknum] += 1
            self.cuslist[self.indexoftop(stacknum)] = item

    def pop(self, stacknum):
        if self.isempty(stacknum):
            return "stack is empty"
        else:
            value = self.cuslist[self.indexoftop(stacknum)]
            self.cuslist[self.indexoftop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value
    def peek(self, stacknum):
        if self.isempty(stacknum):
            return "stack is empty"
        else:
            value = self.cuslist[self.indexoftop(stacknum)]
            return value
        
ms = multistack(3)

ms.push(10, 0)
ms.push(20, 0)
ms.push(30, 1)
ms.push(40, 2)

print("Peek stack 0:", ms.peek(0))
print("Peek stack 1:", ms.peek(1))
print("Peek stack 2:", ms.peek(2))

print("Pop from stack 0:", ms.pop(0))
print("Peek stack 0 after pop:", ms.peek(0))

print("All internal list:", ms.cuslist)'''

#2.   Create Stack with min method

class node():
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = None
    
    def __str__(self):
        string = str(self.value)
        if self.next:
            string += ' , ' + str(self.next)
        return string
class stack():
    def __init__(self):
        self.top = None
        self.minnode = None
    def min(self):
        if not self.minnode:
            return None
        return self.minnode.value
    def push(self, item):
        if self.minnode and (self.minnode.value < item):
            self.minnode = node(value = self.minnode.value, next=self.minnode)
        else:
            self.minnode = node(value = item, next = self.minnode)
        self.top = node(value = item, next =self.top)
    def pop(self):
        if not self.top:
            return None
        self.minnode = self.minnode.next
        item = self.top.value
        self.top = self.top.next
        return item
s = stack()
s.push(5)
print(s.min())
s.push(6)
print(s.min())
s.push(3)
print(s.min())
s.pop()
print(s.min())

def is_balanced(expression):
    stack = []
    # Dictionary to match closing to opening brackets
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        # If it's an opening bracket → push to stack
        if char in "({[":
            stack.append(char)
        # If it's a closing bracket → check stack
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    # If stack is empty, all brackets matched
    return len(stack) == 0

print(is_balanced("()"))        
print(is_balanced("([]){}"))    
print(is_balanced("([)]"))      
print(is_balanced("{[()]}"))    
print(is_balanced("{[(])}"))    
print(is_balanced("((()))"))    
print(is_balanced("(()"))