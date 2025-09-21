class disjointset:
    def __init__(self,vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)
    def find(self,item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    def union(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
vertices = ["A","B","C","D"]
ds = disjointset(vertices)

ds.union("A", "B")  # merge A and B
ds.union("C", "D")  # merge C and D
ds.union("A", "C")  # merge {A,B} with {C,D}

print(ds.find("A"))
print(ds.find("B"))
print(ds.find("C"))
print(ds.find("D"))
