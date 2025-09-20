import heapq

class Edge:
    def __init__(self, weight, startvertex, targetvertex):
        self.weight = weight
        self.startvertex = startvertex
        self.targetvertex = targetvertex

class node:
    def __init__(self,name):
        self.name = name
        self.visited = False

        self.predecessor = None
        self.neighbors = []
        self.min_distance = float("inf")
    
    def __lt__(self, othernode):
        return self.min_distance < othernode.min_distance
    
    def addedge(self, weight, destinationvertex):
        edge = Edge(weight, self, destinationvertex)
        self.neighbors.append(edge)
class dijkstra:
    def __init__(self):
        self.heap = []
    def calculate(self, startvertex):
        startvertex.min_distance = 0
        heapq.heappush(self.heap, startvertex)

        while self.heap:

            actualvertex = heapq.heappop(self.heap)
            if actualvertex.visited:
                continue
            for edge in actualvertex.neighbors:
                start = edge.startvertex
                target = edge.targetvertex
                newdistance = start.min_distance + edge.weight
                if newdistance < target.min_distance:
                    target.min_distance = newdistance
                    target.predecessor = start

                    heapq.heappush(self.heap, target)
            actualvertex.visited = True
    def getshortestpath(self,vertex):
        print(f"the shortes path to the vertex is: {vertex.min_distance}")
        actualvertex = vertex
        while actualvertex is not None:
            print(actualvertex.name, end=" ")
            actualvertex = actualvertex.predecessor

# Create nodes
A = node("A")
B = node("B")
C = node("C")
D = node("D")
E = node("E")
# A → B (weight 4), A → C (weight 2)
A.addedge(4, B)
A.addedge(2, C)

# B → C (weight 5), B → D (weight 10)
B.addedge(5, C)
B.addedge(10, D)

# C → E (weight 3)
C.addedge(3, E)

# E → D (weight 4)
E.addedge(4, D)

# D → F (weight 11)
F = node("F")
D.addedge(11, F)

algo = dijkstra()
algo.calculate(A)   # Start from A

print("\nPath to D:")
algo.getshortestpath(D)

print("\n\nPath to F:")
algo.getshortestpath(F)
