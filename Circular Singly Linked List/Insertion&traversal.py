class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class CSLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        if not self.head:
            return "List is empty."

        result = ''
        temp = self.head
        while True:
            result += str(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            result += ' -> '
        return result + ' -> (back to head)'

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise Exception("Index out of range")

        new_node = Node(value)

        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
    def traversal(self):
            if not self.head:
                return 
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next
                if current == self.head:
                    break
    def search(self,target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index 
            current = current.next
            index += 1
        return -1
    def get(self,index):
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    def setvalue(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None 
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
             temp = self.head
             while temp.next != self.tail:
                 temp = temp.next
             temp.next = self.head
             self.tail = temp
        popped_node.next = None
        self.length -= 1
        return popped_node
    def remove(self, index):
        if index < -1 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == -1 or index == self.length-1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node    
    def delete_all(self):
        if self.length == 0:
            return 
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0
    
linked_list = CSLL()
print(linked_list)  # List is empty.

linked_list.append(10)
linked_list.insert(0, 20)
linked_list.insert(1, 30)
linked_list.insert(2, 40)
linked_list.prepend(50)

print(linked_list)

#linked_list.traversal()
#print(linked_list.search(10))
#print(linked_list.setvalue(1,99))
#print(linked_list.pop_first())
#print(linked_list.pop())
#print(linked_list.remove(3))
print(linked_list.delete_all())
print(linked_list)
