class graph:
    def __init__(self):
        self.adjacency_list = {}
    def addvertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False
    def BFS(self,vertex):
        visited = set()
        visited.add(vertex)

        queue = [vertex]
        while queue:
            currentvertex = queue.pop(0)
            print(currentvertex)

            for adjacentvertex in self.adjacency_list[currentvertex]:
                if adjacentvertex not in visited:
                    visited.add(adjacentvertex)
                    queue.append(adjacentvertex)
g = graph()
g.addvertex("A")
g.addvertex("B")
g.addvertex("C")
g.addvertex("D")
g.add_edge("A","B")
g.add_edge("A","C")
g.add_edge("B","D")

g.print_graph()
print("BFS traversal")
g.BFS("A")
print("BFS traversal")
g.BFS("B")