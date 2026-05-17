def uruchom_dfs(n, start, sasiedzi_func):
    visited = set()
    stack = [start]
    wynik = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            wynik.append(node)
            visited.add(node)
            for neighbor in reversed(sasiedzi_func(node)):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    print(f"Kolejność odwiedzania DFS (od węzła {start + 1}): {[x + 1 for x in wynik]}")
    return wynik


def sortowanie_tarjana(n, sasiedzi_func):
    if n == 0:
        print("Graf jest pusty!")
        return []

    UNMARKED = 0
    TEMPORARY = 1
    PERMANENT = 2
    
    marks = [UNMARKED] * n
    L = []
    cykl_znaleziony = False

    def visit(node):
        nonlocal cykl_znaleziony
        if cykl_znaleziony: 
            return
        if marks[node] == PERMANENT: 
            return
        if marks[node] == TEMPORARY:
            cykl_znaleziony = True
            return

        marks[node] = TEMPORARY
        for neighbor in sasiedzi_func(node):
            visit(neighbor)

        marks[node] = PERMANENT
        L.insert(0, node)

    for i in range(n):
        if marks[i] == UNMARKED and not cykl_znaleziony:
            visit(i)

    if cykl_znaleziony:
        print("Błąd (Tarjan): Graf zawiera co najmniej jeden cykl! Sortowanie niemożliwe.")
        return []

    wynik_1_based = [x + 1 for x in L]
    print(f"Wynik sortowania Tarjana: {wynik_1_based}")
    return L