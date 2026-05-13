class Tarjan:
    def __init__(self, lista_nastepnikow):
        self.graph = lista_nastepnikow

        self.index = 0

        self.stack = []
        self.on_stack = set()

        self.indices = [-1] * len(lista_nastepnikow)
        self.lowlink = [-1] * len(lista_nastepnikow)

        self.sccs = []

    def dfs(self, v):

        # ustawienie indeksu
        self.indices[v] = self.index
        self.lowlink[v] = self.index

        self.index += 1

        self.stack.append(v)
        self.on_stack.add(v)

        # przechodzenie po sasiadach
        for neighbor in self.graph[v]:

            # jesli nieodwiedzony
            if self.indices[neighbor] == -1:

                self.dfs(neighbor)

                self.lowlink[v] = min(
                    self.lowlink[v],
                    self.lowlink[neighbor]
                )

            # jesli jest na stosie
            elif neighbor in self.on_stack:

                self.lowlink[v] = min(
                    self.lowlink[v],
                    self.indices[neighbor]
                )

        # znaleziono SCC
        if self.lowlink[v] == self.indices[v]:

            scc = []

            while True:

                w = self.stack.pop()

                self.on_stack.remove(w)

                scc.append(w)

                if w == v:
                    break

            self.sccs.append(scc)

    def find_scc(self):

        for v in range(len(self.graph)):

            if self.indices[v] == -1:
                self.dfs(v)

        return self.sccs