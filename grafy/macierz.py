from graf import Graph

# n - liczba wierzchołków
# u, v - wierzchołki

class MatrixGraph(Graph):

    def __init__(self, n):
        self.n = n
        self.matrix = [[0] * n for _ in range(n)]

    def neighbors(self, v):
        result = []

        for i in range(self.n):
            if self.matrix[v][i]:
                result.append(i)

        return result

    def has_edge(self, u, v):
        return self.matrix[u][v] == 1

    def vertices(self):
        return range(self.n)
    
    def __str__(self):
        result = ""

        for i in range(self.n):
            for j in range(self.n):
                result += str(self.matrix[i][j]) + " "
            result += "\n"

        return result