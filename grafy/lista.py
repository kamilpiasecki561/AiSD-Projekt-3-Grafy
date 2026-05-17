from grafy.graf import Graph

# n - liczba wierzchołków
# u, v - wierzchołki

class ListGraph(Graph):

    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def neighbors(self, v):
        return self.adj[v]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[u].sort()

    def has_edge(self, u, v):
        return v in self.adj[u]

    def vertices(self):
        return range(self.n)
    
    def __str__(self):
        result = ""

        for i in range(self.n):
            result += str(i) + ": " + str(self.adj[i]) + "\n"

        return result