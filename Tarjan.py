from DFS import dfs


class Tarjan:
    """Algorytm Tarjana do znajdowania silnie spójnych składowych (SCC)"""
    
    def __init__(self, graph):
        """
        Inicjalizacja algorytmu Tarjana
        
        Args:
            graph: słownik reprezentujący graf {wierzchołek: [lista sąsiadów]}
        """
        self.graph = graph
        self.index_counter = 0
        self.stack = []
        self.indices = {}
        self.lowlinks = {}
        self.on_stack = {}
        self.sccs = []
    
    def stronglyConnectedComponents(self):
        """
        Znajduje wszystkie silnie spójne składowe w grafie
        
        Returns:
            Lista list reprezentujących silnie spójne składowe
        """
        for v in self.graph:
            if v not in self.indices:
                self._tarjan_dfs(v)
        
        return self.sccs
    
    def _tarjan_dfs(self, v):
        """
        Głębokie przeszukiwanie z algorytmu Tarjana
        
        Args:
            v: bieżący wierzchołek
        """
        self.indices[v] = self.index_counter
        self.lowlinks[v] = self.index_counter
        self.index_counter += 1
        self.stack.append(v)
        self.on_stack[v] = True
        
        # Przejdź wszystkie krawędzie v -> w
        if v in self.graph:
            for w in self.graph[v]:
                if w not in self.indices:
                    # Wierzchołek nie był odwiedzony
                    self._tarjan_dfs(w)
                    self.lowlinks[v] = min(self.lowlinks[v], self.lowlinks[w])
                elif self.on_stack.get(w, False):
                    # Krawędź zwrotna do wierzchołka na stosie
                    self.lowlinks[v] = min(self.lowlinks[v], self.indices[w])
        
        # Jeśli v jest wierzchołkiem głównym, wypakuj stos i utwórz SCC
        if self.lowlinks[v] == self.indices[v]:
            scc = []
            while True:
                w = self.stack.pop()
                self.on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            
            self.sccs.append(scc)


# Przykład użycia
if __name__ == "__main__":
    # Przykładowy graf
    graph = {
        0: [1],
        1: [2],
        2: [0, 3],
        3: [1, 4],
        4: [2, 5],
        5: [5, 6],
        6: [5, 7],
        7: [6, 8],
        8: [7, 3]
    }
    
    tarjan = Tarjan(graph)
    sccs = tarjan.stronglyConnectedComponents()
    
    print("Silnie spójne składowe:")
    for i, scc in enumerate(sccs):
        print(f"SCC {i+1}: {scc}")