class binarytree:
    def __init__(self, size):
        self.customlist = size * [None]
        self.lastusedindex = 0
        self.maxsize = size
    def insertnode(self, value):
        if self.lastusedindex + 1 == self.maxsize:
            return " bt is full "
        self.customlist[self.lastusedindex + 1] = value
        self.lastusedindex += 1
        return " the value has been inserted"
    
    def searchnode(self, nodevalue):
        for i in range(len(self.customlist)):
            if self.customlist[i] == nodevalue:
                return "found"
        return "not found"
    def preordertraversal(self,index):
        if index > self.lastusedindex:
            return
        print(self.customlist[index])
        self.preordertraversal(index * 2)
        self.preordertraversal(index * 2 + 1)

    def inordertraversal(self,index):
        if index > self.lastusedindex:
            return
        self.inordertraversal(index * 2)
        print(self.customlist[index])
        self.inordertraversal(index * 2 + 1)

    def postordertraversal(self, index):
        if index > self.lastusedindex:
            return
        self.postordertraversal(index * 2)
        self.postordertraversal(index * 2 + 1)
        print(self.customlist[index])
    
    def levelordertraversal(self, index):
        for i in range(index, self.lastusedindex + 1):
            print(self.customlist[i])
    def deletenode(self, value):
        if self.lastusedindex == 0:
            return "tree empty"
        for i in range(1, self.lastusedindex + 1):
            if self.customlist[i] == value:
                self.customlist[i] = self.customlist[self.lastusedindex]
                self.customlist[self.lastusedindex] = None
                self.lastusedindex -= 1

                return "deleted"
            return "not found"
    def deletebt(self):
        self.customlist = None
        return "tree deleted"
# Create a binary tree of size 10
bt = binarytree(10)

# Insert nodes
print(bt.insertnode(10))  # value inserted
print(bt.insertnode(20))
print(bt.insertnode(30))
print(bt.insertnode(40))
print(bt.insertnode(50))

# Search for a node
print(bt.searchnode(30))  # found
print(bt.searchnode(60))  # not found

# Traversals
print("Pre-order Traversal:")
bt.preordertraversal(1)

print("In-order Traversal:")
bt.inordertraversal(1)

print("Post-order Traversal:")
bt.postordertraversal(1)

print("Level-order Traversal:")
bt.levelordertraversal(1)

# Delete a node
print(bt.deletenode(20))  # deleted
print(bt.levelordertraversal(1))  # Check tree after deletion

# Delete the entire tree
print(bt.deletebt())
print(bt.customlist)  # None


