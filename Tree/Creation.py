class treenode:
    def __init__(self, data, children = None):
        self.data = data
        self.children = children if children is not None else []
    def __str__(self, level = 0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    def addchild(self, node):
        self.children.append(node)
root = treenode("root")

child1 = treenode("child1")
child2 = treenode("child2")

root.addchild(child1)
root.addchild(child2)

child1.addchild(treenode("grandchildren1"))

print(root)

