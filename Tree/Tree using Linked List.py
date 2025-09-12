class treenode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
root = treenode("root")

#print(root.data)

#PREORDER TRAVERSAL R-L-RI

'''def preorder(node):
    if node is None:
        return 
    else:
        print(node.data, end=" ")
        #recursion
        preorder(node.leftchild)
        preorder(node.rightchild)'''

# Build tree
'''root = treenode("Root")
root.leftchild = treenode("Left")
root.rightchild = treenode("Right")
root.leftchild.leftchild = treenode("Left.Left")
root.leftchild.rightchild = treenode("Left.Right")
root.rightchild.leftchild = treenode("Right.Left")
root.rightchild.rightchild = treenode("Right.Right")'''

# Perform preorder traversal
'''print("Preorder Traversal:")
preorder(root)'''

#INORDER TRAVERSAL L-R-RI

def inordertraversal(node):
    if node is None:
        return
    
    inordertraversal(node.leftchild)
    print(node.data, end =" ")
    inordertraversal(node.rightchild)
print("inorder traversal")
inordertraversal(root)

#POSTORDER TRAVERSAL L-RI-R

'''def postordertraversal(node):
    if node is None:
        return
    postordertraversal(node.leftchild)
    postordertraversal(node.rightchild)
    print(node.data, end =" ")
print("postorder traversal")
postordertraversal(root)'''

#LEVEL ORDER TRAVERSAL
from collections import deque
class solution:
    def levelorder(self,root):
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level =[]
            for _ in range(len(queue)):
                node =queue.popleft()
                level.append(node.data)

                if node.leftchild:
                    queue.append(node.leftchild)
                if node.rightchild:
                    queue.append(node.rightchild)
            result.append(level)
        return result
sol = solution()
result = sol.levelorder(root)
print(result)

def search(root, target):
    if not root:
        return False
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node.data == target:
            return True
        
        if node.leftchild:
            queue.append(node.leftchild)
        if node.rightchild:
            queue.append(node.rightchild)
    return False

def insert(root, value):
    newnode = treenode(value)

    if not root:
        return newnode
    
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if not node.leftchild:
            node.leftchild = newnode
            return root
        else:
            queue.append(node.leftchild)

        if not node.rightchild:
            node.rightchild = newnode
            return root
        else:
            queue.append(node.rightchild)
root = treenode(1)

def get_deepest(root):
    if not root:
        return None
    queue = deque([root])
    node = None

    while queue:
        node = queue.popleft()
        if node.leftchild:
            queue.append(node.leftchild)
        if node.rightchild:
            queue.append(node.rightchild)
    return node
def delete_deepest(root, dnode):
    if not root:
        return
    
    queue = deque([root])
    while queue:
        node = queue.popleft()

        if node is dnode:
            node = None
            return
        
        if node.rightchild:
            if node.rightchild is dnode:
                node.rightchild = None
                return
            else:
                queue.append(node.rightchild)

        if node.leftchild:
            if node.leftchild is dnode:
                node.leftchild = None
                return
            else:
                queue.append(node.leftchild)
def deletespnode(root, value):
    if not root:
        return "the binary tree doesnot exist"
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.data == value:
            dnode = get_deepest(root)
            node.data = dnode.data
            delete_deepest(root, dnode)
            return "the node has been successfully deleted"
        if node.leftchild:
            queue.append(node.leftchild)
        if node.rightchild:
            queue.append(node.rightchild)
    return "failed to delete"
def deletebt(root):
    root.data = None
    root.leftchild = None
    root.rightchild = None
    return"bt deleted"
#for deleting specific node and entire tree
root = treenode(1)
root.leftchild = treenode(2)
root.rightchild = treenode(3)
root.leftchild.leftchild = treenode(4)
root.leftchild.rightchild = treenode(5)

print("Inorder before deletion:", inordertraversal(root))

print(deletespnode(root, 2))   

print("Inorder after deletion:", inordertraversal(root))

print(deletebt(root))          # delete entire tree

print("Inorder after deleting whole tree:", inordertraversal(root))

#for deleting deepest node
'''root = treenode(1)
root.leftchild = treenode(2)
root.rightchild = treenode(3)
root.leftchild.leftchild = treenode(4)
root.leftchild.rightchild = treenode(5)
root.rightchild.leftchild = treenode(6)
root.rightchild.rightchild = treenode(7)
sol = solution()
print("Before deletion:", sol.levelorder(root))

deepest = get_deepest(root)
print("Deepest node is:", deepest.data)

delete_deepest(root, deepest)

print("After deletion:", sol.levelorder(root))'''

'''# Example tree for finding deepest
root = treenode(1)
root.leftchild = treenode(2)
root.rightchild = treenode(3)
root.leftchild.leftchild = treenode(4)
root.leftchild.rightchild = treenode(5)
root.rightchild.leftchild = treenode(6)
root.rightchild.rightchild = treenode(7)

deepest = get_deepest(root)
print("Deepest node is:", deepest.data)'''



'''# Insert more nodes
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 4)
root = insert(root, 5)
root = insert(root, 6)
root = insert(root, 7)

# Print tree level order after insertions
print("Level Order Traversal after insertions:")
sol = solution()
result = sol.levelorder(root)
print(result)'''

'''root = treenode(1)
root.leftchild = treenode(2)
root.rightchild = treenode(3)
root.leftchild.leftchild = treenode(4)
root.leftchild.rightchild = treenode(5)
root.rightchild.leftchild = treenode(6)
root.rightchild.rightchild = treenode(7)

sol = solution()
result = sol.levelorder(root)
print("Level Order Traversal by levels:")
print(result)

print("Searching for 5:", search(root, 5))   
print("Searching for 10:", search(root, 10))'''