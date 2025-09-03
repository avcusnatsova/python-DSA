import random

class node:
    def __init__(self,value):
        self.value = value
        self.next = None
class ll:
    def __init__(self):
        self.head = None
    def __str__(self):
        values =[]
        temp = self.head
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        return "->".join(values)
    def insert(self, value):
        newnode = node(value)
        if self.head is None:
            self.head= newnode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode
    def generate(self,n,min_value,max_value):
        self.head = None
        for _ in range(n):
            self.insert(random.randint(min_value, max_value))
        return self
    def removedups(ll):
        if ll.head is None:
            return ll
        currnode = ll.head
        visited = set([currnode.value])
        while currnode.next:
            if currnode.next.value in visited:
                currnode.next = currnode.next.next
            else:
                visited.add(currnode.next.value)
                currnode = currnode.next
        return ll
customLL = ll()
customLL.generate(10, 0, 9)  # generates 10 nodes with values between 0 and 9
print("Original List:")
print(customLL)

customLL.removedups()
print("\nAfter Removing Duplicates (No Extra Space):")
print(customLL)
