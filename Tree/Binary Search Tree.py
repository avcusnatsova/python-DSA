from collections import deque
def levelordertraversal(rootnode):
    if not rootnode:
        return
    customqueue = deque()
    customqueue.append(rootnode)

    while customqueue:
        root = customqueue.popleft()
        print(root.data)

        if root.leftchild:
            customqueue.append(root.leftchild)
        if root.rightchild:
            customqueue.append(root.rightchild)

class bstnode:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
    
#insert a node
def insertnode(rootnode, nodevalue):
    if rootnode is None:
        return bstnode(nodevalue)
    
    if nodevalue <= rootnode.data:
        rootnode.leftchild = insertnode(rootnode.leftchild, nodevalue)
    else:
        rootnode.rightchild = insertnode(rootnode.rightchild, nodevalue)
    return rootnode

def preordertraversal(rootnode):
    if not rootnode:
        return 
    print(rootnode.data)
    preordertraversal(rootnode.leftchild)
    preordertraversal(rootnode.rightchild)

def inordertraversal(rootnode):
    if not rootnode:
        return
    inordertraversal(rootnode.leftchild)
    print(rootnode.data)
    inordertraversal(rootnode.rightchild)

def postordertraversal(rootnode):
    if not rootnode:
        return
    postordertraversal(rootnode.leftchild)
    postordertraversal(rootnode.rightchild)
    print(rootnode.data)

def levelordertraversal(rootnode):
    if not rootnode:
        return
    customqueue = deque()
    customqueue.append(rootnode)
    while customqueue:
        root = customqueue.popleft()
        print(root.data)
        if root.leftchild:
            customqueue.append(root.leftchild)
        if root.rightchild:
            customqueue.append(root.rightchild)

def searchnode(rootnode, nodevalue):
    if rootnode is None:
        print("value not found")
        return
    if rootnode.data == nodevalue:
        print("value is found")
    elif nodevalue < rootnode.data:
        searchnode(rootnode.leftchild, nodevalue)
    else:
        searchnode(rootnode.rightchild, nodevalue)

def minvaluenode(bstnode):
    current = bstnode
    while current and current.leftchild is not None:
        current = current.leftchild
    return current
def deletenode(rootnode, nodevalue):
    if rootnode is None:
        return rootnode
    if nodevalue < rootnode.data:
        rootnode.leftchild = deletenode(rootnode.leftchild, nodevalue)
    elif nodevalue > rootnode.data:
        rootnode.rightchild = deletenode(rootnode.rightchild, nodevalue)
    else:
        #has a single child which is right child
        if rootnode.leftchild is None:
            temp = rootnode.rightchild
            rootnode = None
            return temp
        elif rootnode.rightchild is None:
            temp = rootnode.leftchild
            rootnode = None
            return temp
        temp = minvaluenode(rootnode.rightchild)
        rootnode.data = temp.data
        rootnode.rightchild = deletenode(rootnode.rightchild, temp.data)
    return rootnode
def deletebst(rootnode):
    rootnode.data = None
    rootnode.leftchild = None
    rootnode.rightchild = None
    return "bst has been deleted"
# BST
root = bstnode(70)
insertnode(root, 50)
insertnode(root, 90)
insertnode(root, 30)
insertnode(root, 60)
insertnode(root, 80)
insertnode(root, 100)
print(levelordertraversal(root))
print("Searching for 60:")
searchnode(root, 60)   
print("Searching for 25:")
searchnode(root, 25)   
print("\nMinimum value in BST:")
min_node = minvaluenode(root)
print(min_node.data)   
print("\nDeleting 50:")
root = deletenode(root, 50)

print("Inorder traversal after deleting 50:")
inordertraversal(root)  

print("\nDeleting entire BST:")
print(deletebst(root))   
print("Trying inorder traversal after deletion:")
inordertraversal(root)  


'''# Build a BST
root = bstnode(70)
insertnode(root, 50)
insertnode(root, 90)
insertnode(root, 30)
insertnode(root, 60)
insertnode(root, 80)
insertnode(root, 100)

print("Preorder Traversal:")
preordertraversal(root)

print("\nInorder Traversal:")
inordertraversal(root)

print("\nPostorder Traversal:")
postordertraversal(root)

print("\nLevel Order Traversal:")
levelordertraversal(root)
'''
