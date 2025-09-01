class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Create DLL
    def createdll(self, nodeValue):
        newnode = Node(nodeValue)
        self.head = newnode
        self.tail = newnode
        self.length = 1
        return "DLL is created"

    # Insert node
    def insertnode(self, nodeValue, location):
        if self.head is None:
            print("The node cannot be inserted")
            return
        newnode = Node(nodeValue)
        if location == 0:  # insert at head
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        elif location == 1:  # insert at tail
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode
        else:  # insert in middle
            temp = self.head
            index = 0
            while index < location - 1:
                temp = temp.next
                index += 1
            newnode.next = temp.next
            newnode.prev = temp
            temp.next.prev = newnode
            temp.next = newnode
        self.length += 1

    # Traversal
    def traversedll(self):
        if self.head is None:
            print("The list is empty")
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value, end=" ")
                tempnode = tempnode.next
            print()

    # Reverse traversal
    def reversetraverse(self):
        if self.head is None:
            print("The list is empty")
        else:
            tempnode = self.tail
            while tempnode:
                print(tempnode.value, end=" ")
                tempnode = tempnode.prev
            print()

    # Search
    def search(self, nodeValue):
        tempnode = self.head
        while tempnode:
            if tempnode.value == nodeValue:
                return tempnode.value
            tempnode = tempnode.next
        return "Node doesn't exist"

    # Delete node
    def delete(self, location):
        if self.length == 0:
            print("The list is empty")
            return
        if location == 0:  # delete head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif location == 1:  # delete tail
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        else:  # delete middle
            curnode = self.head
            index = 0
            while index < location - 1:
                curnode = curnode.next
                index += 1
            curnode.next = curnode.next.next
            if curnode.next:
                curnode.next.prev = curnode
        self.length -= 1
        print("Node has been deleted")

    # Append at tail
    def append(self, value):
        newnode = Node(value)
        if not self.head:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
        self.length += 1

    # Prepend at head
    def prepend(self, value):
        newnode = Node(value)
        if not self.head:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        self.length += 1

    # Get node at index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:  # search from head
            curnode = self.head
            for _ in range(index):
                curnode = curnode.next
        else:  # search from tail
            curnode = self.tail
            for _ in range(self.length - 1, index, -1):
                curnode = curnode.prev
        return curnode

    # Set value at index
    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    # Pop last
    def pop(self):
        if self.length == 0:
            return None
        removed = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            removed.prev = None
        self.length -= 1
        return removed.value

    # Pop first
    def pop_first(self):
        if self.length == 0:
            return None
        removed = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            removed.next = None
        self.length -= 1
        return removed.value

    # Remove at index
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            curnode = self.get(index)
            curnode.prev.next = curnode.next
            curnode.next.prev = curnode.prev
            removed = curnode
            removed.next = None
            removed.prev = None
            self.length -= 1
            return removed.value


# ----------------- TEST -----------------
DLL = DLL()
DLL.createdll(5)
DLL.append(10)
DLL.append(20)
DLL.append(30)
print([n.value for n in DLL])   # [5, 10, 20, 30]

print("Pop:", DLL.pop())        # removes 30
print([n.value for n in DLL])   # [5, 10, 20]

print("Pop first:", DLL.pop_first())  # removes 5
print([n.value for n in DLL])         # [10, 20]

DLL.remove(0)                   # removes 10
print([n.value for n in DLL])   # [20]
