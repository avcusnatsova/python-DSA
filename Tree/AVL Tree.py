from QueueLinkedlist import queue


class avlnode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1
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
    q = queue()
    q.enqueue(rootnode)

    while not q.isempty():
        node = q.dequeue()
        print(node.data)
        if node.leftchild:
            q.enqueue(node.leftchild)
        if node.rightchild:
             q.enqueue(node.rightchild)

def searchnode(rootnode, nodevalue):
    if not rootnode:
        print("value not found")
        return
    if rootnode.data == nodevalue:
        print("value found")
        return
    elif nodevalue<rootnode.data:
        searchnode(rootnode.leftchild, nodevalue)
    else: 
        searchnode(rootnode.rightchild, nodevalue)
def getheight(rootnode):
    if not rootnode:
        return 0
    return rootnode.height

def rightrotate(disbalancednode):
    newroot = disbalancednode.leftchild
    disbalancednode.leftchild = newroot.rightchild
    newroot.rightchild = disbalancednode

    disbalancednode.height = 1 + max(getheight(disbalancednode.leftchild), getheight(disbalancednode.rightchild))
    newroot.height = 1 + max(getheight(newroot.leftchild), getheight(newroot.rightchild))
    return newroot
def leftrotate(disbalancednode):
    newroot = disbalancednode.rightchild
    disbalancednode.rightchild = newroot.leftchild
    newroot.leftchild = disbalancednode

    disbalancednode.height = 1+ max(getheight(disbalancednode.leftchild), getheight(disbalancednode.rightchild))
    newroot.height = 1+ max(getheight(newroot.leftchild), getheight(newroot.rightchild))
    return newroot
def getbalance(rootnode):
    if not rootnode:
        return 0
    return getheight(rootnode.leftchild) - getheight(rootnode.rightchild)
def insertnode(rootnode, nodevalue):
    if not rootnode:
        return avlnode(nodevalue)
    elif nodevalue < rootnode.data:
        rootnode.leftchild = insertnode(rootnode.leftchild, nodevalue)
    else:
        rootnode.rightchild = insertnode(rootnode.rightchild, nodevalue)
    rootnode.height = 1 + max(getheight(rootnode.leftchild), getheight(rootnode.rightchild))
    balance = getbalance(rootnode)
    if balance > 1 and nodevalue < rootnode.leftchild.data:
        return rightrotate(rootnode)
    if balance > 1 and nodevalue > rootnode.leftchild.data:
        rootnode.leftchild = leftrotate(rootnode.leftchild)
        return rightrotate(rootnode)
    if balance < -1 and nodevalue > rootnode.rightchild.data:
        return leftrotate(rootnode)
    if balance < -1 and nodevalue < rootnode.rightchild.data:
        rootnode.rightchild = rightrotate(rootnode.rightchild)
        return leftrotate(rootnode)
    return rootnode
def getminvaluenode(rootnode):
    if rootnode is None or rootnode.leftchild is None:
        return rootnode
    return getminvaluenode(rootnode.leftchild)

def deletenode(rootnode, nodevalue):
    if not rootnode:
        return rootnode
    elif nodevalue< rootnode.data:
        rootnode.leftchild = deletenode(rootnode.leftchild, nodevalue)
    elif nodevalue> rootnode.data:
        rootnode.rightchild = deletenode(rootnode.rightchild, nodevalue)
    #rootnode is the node to be deleted
    else:
        if rootnode.leftchild is None:
            temp = rootnode.rightchild
            rootnode = None
            return temp
        elif rootnode.rightchild is None:
            temp = rootnode.leftchild
            rootnode = None
            return temp
        temp = getminvaluenode(rootnode.rightchild)
        rootnode.data = temp.data
        rootnode.rightchild = deletenode(rootnode.rightchild, temp.data)
    balance = getbalance(rootnode)
    if balance> 1 and getbalance(rootnode.leftchild) >= 0:
        return rightrotate(rootnode)
    if balance <-1 and getbalance(rootnode.rightchild) <=0:
        return leftrotate(rootnode)
    if balance> 1 and getbalance(rootnode.leftchild) < 0:
        rootnode.leftchild = leftrotate(rootnode.leftchild)
        return rightrotate(rootnode)
    if balance < -1 and getbalance(rootnode.rightchild)>0:
        rootnode.rightchikd = rightrotate(rootnode.leftchild)
        return leftrotate(rootnode)
    return rootnode
def deleteavl(rootnode):
    rootnode.data = None
    rootnode.leftchild = None
    rootnode.rightchild = None
    return "AVL TREE DELETED"
# 1️⃣ Create root
root = avlnode(50)

# 2️⃣ Insert nodes
root = insertnode(root, 30)
root = insertnode(root, 70)
root = insertnode(root, 20)
root = insertnode(root, 40)
root = insertnode(root, 60)
root = insertnode(root, 80)

# 3️⃣ Traversals
print("Preorder Traversal:")
preordertraversal(root)

print("\nInorder Traversal:")
inordertraversal(root)

print("\nPostorder Traversal:")
postordertraversal(root)

print("\nLevel Order Traversal:")
levelordertraversal(root)

# 4️⃣ Search for a node
print("\nSearch for 40:")
searchnode(root, 40)

print("Search for 100:")
searchnode(root, 100)

# 5️⃣ Delete a node
print("\nDelete 20 (leaf node):")
root = deletenode(root, 20)
inordertraversal(root)

print("\nDelete 30 (node with one child):")
root = deletenode(root, 30)
inordertraversal(root)

print("\nDelete 50 (node with two children):")
root = deletenode(root, 50)
inordertraversal(root)

# 6️⃣ Delete entire AVL tree
print("\nDelete AVL Tree:")
print(deleteavl(root))
