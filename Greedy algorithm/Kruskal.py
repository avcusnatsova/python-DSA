import Disjoint as dst

class graph:
    def __init__ (self, vertices):
        self.v = vertices
        self.graph = []
        self.nodes = []
        self.mst = []

    def addedge(self, s, d,w):
        self.graph.append([s,d,w])

    def addnode(self,value):
        self.nodes.append(value)

    def printsolution(self, s, d,w):
        for s,d,w in self.mst:
            print("%s - %s : %s "% (s,d,w))
    
    def kruskalalgo(self):
        i, e = 0,0
        ds = dst.disjointset(self.nodes)

        self.graph = sorted(self.graph, key = lambda item: item[2])

        while e < self.v - 1:
            s,d,w = self.graph[i]
            i+=1
            x=ds.find(s)
            y=ds.find(d)

            if x != y:
                e += 1
                self.mst.append([s,d,w])
                ds.union(x,y)
        self.printsolution(s,d,w)
g = graph(5)

# Add nodes
g.addnode("A")
g.addnode("B")
g.addnode("C")
g.addnode("D")
g.addnode("E")

# Add edges with weights
g.addedge("A", "B", 5)
g.addedge("A", "C", 13)
g.addedge("A", "E", 15)
g.addedge("B", "C", 10)
g.addedge("B", "D", 8)
g.addedge("C", "D", 6)
g.addedge("C", "E", 20)

# Run Kruskal’s algorithm
g.kruskalalgo()
