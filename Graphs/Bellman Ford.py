class graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = []
        self.nodes = []

    
    def addedge(self, s,d,w):
        self.graph.append([s,d,w])
    def addnode(self,value):
        self.nodes.append(value)
    def printsol(self, dist):
        print("vertex distance from source")
        for key, value in dist.items():
            print(f"{key}: {value}")

    def bellmanford(self,src):
        dist = {i: float("inf") for i in self.nodes}
        dist[src] = 0

        for _ in range(self.v-1):
            for s, d,w in self.graph:
                if dist[s] != float("inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        for s, d, w in self.graph:
            if dist[s] != float("inf") and dist[s] + w < dist[d]:
                print("graph contains negative cycle")
                return
        self.printsol(dist)
g = graph(5)

# Add nodes
for node in ["A", "B", "C", "D", "E"]:
    g.addnode(node)

# Add edges
g.addedge("A", "B", -1)
g.addedge("A", "C", 4)
g.addedge("B", "C", 3)
g.addedge("B", "D", 2)
g.addedge("B", "E", 2)
g.addedge("D", "B", 1)
g.addedge("D", "C", 5)
g.addedge("E", "D", -3)

# Run Bellman-Ford
g.bellmanford("A")
