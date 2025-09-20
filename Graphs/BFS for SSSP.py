class graph:
    def __init__(self, gdict):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    def BFS(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
# Create adjacency list for the graph
customDict = {
    "a": ["b", "c"],
    "b": ["d", "g"],
    "c": ["d", "e"],
    "d": ["f"],
    "e": ["f"],
    "g": ["f"]
}

# Initialize graph
g = graph(customDict)

# Find path from 'a' to 'f'
print("Path from a to f:", g.BFS("a", "f"))

# Find path from 'a' to 'g'
print("Path from a to g:", g.BFS("a", "g"))

# Try path to a node that doesn't exist
print("Path from a to z:", g.BFS("a", "z"))
