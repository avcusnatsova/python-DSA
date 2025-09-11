class treenode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
root = treenode("root")

print(root.data)