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

'''#INORDER TRAVERSAL L-R-RI

def inordertraversal(node):
    if node is None:
        return
    
    inordertraversal(node.leftchild)
    print(node.data, end =" ")
    inordertraversal(node.rightchild)
print("inorder traversal")
inordertraversal(root)'''

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

root = treenode(1)
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
print("Searching for 10:", search(root, 10)) 