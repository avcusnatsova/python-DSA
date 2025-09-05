class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

# Stack class
class Stack:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.linkedlist]
        return '\n'.join(values)
    
    def isEmpty(self):
        return self.linkedlist.head is None
    
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.linkedlist.head
        self.linkedlist.head = newNode

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            nodeValue = self.linkedlist.head.value
            self.linkedlist.head = self.linkedlist.head.next
            return nodeValue

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.linkedlist.head.value

    def delete(self):
        self.linkedlist.head = None

customStack = Stack()
customStack.push(1)   
customStack.push(2)  
customStack.push(3)  

print("Stack elements (top to bottom):")
print(customStack)

print("\nTop element (peek):", customStack.peek())   
print("Popped element:", customStack.pop())       
print("Stack after pop:")
print(customStack)

customStack.delete()
print("\nAfter deleting stack, is empty?", customStack.isEmpty())
