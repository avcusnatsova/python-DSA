from collections import defaultdict

class graph:
    def __init__(self, numberofvertices):
        self.graph = defaultdict(list)
        self.numberofvertices = numberofvertices
    def addedge(self, vertex, edge):
        self.graph[vertex].append(edge)
    def topologicalsortutil(self, v, visited, stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalsortutil(i, visited, stack)
        stack.insert(0, v)

    def topologicalsort(self):
        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topologicalsortutil(k, visited, stack)
        print(stack)
# Create graph with 8 vertices
customGraph = graph(8)

# Add directed edges
customGraph.addedge("A", "C")
customGraph.addedge("C", "E")
customGraph.addedge("E", "H")
customGraph.addedge("E", "F")
customGraph.addedge("F", "G")
customGraph.addedge("B", "D")
customGraph.addedge("B", "C")
customGraph.addedge("D", "F")

# Perform Topological Sort
customGraph.topologicalsort()
