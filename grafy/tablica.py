from grafy.graf import Graph

# n - liczba wierzchołków
# u, v - wierzchołki

class EdgeTableGraph(Graph):

    def __init__(self, n):
        self.n = n
        self.edges = []

    def neighbors(self, v):
        result = []

        for u, w in self.edges:
            if u == v:
                result.append(w)

        return result

    def add_edge(self, u, v):
        self.edges.append((u, v))

    def has_edge(self, u, v):
        return (u, v) in self.edges

    def vertices(self):
        return range(self.n)

    def __str__(self):
        result = ""

        for u, v in self.edges:
            result += f"{u} -> {v}\n"

        return result