def uruchom_dfs(lista_nastepnikow, start):
    # Przeszukiwanie w głąb (iteracyjnie, z użyciem stosu)
    visited = set()
    stack = [start]
    wynik = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            wynik.append(node)
            visited.add(node)
            # Odwracamy sąsiadów, by odwiedzać od najmniejszego do największego
            for neighbor in reversed(lista_nastepnikow[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    # Konwersja indeksowania od 0 do 1 dla użytkownika
    print(f"Kolejność odwiedzania DFS (od węzła {start + 1}): {[x + 1 for x in wynik]}")
    return wynik


def sortowanie_tarjana(lista_nastepnikow):
    # Implementacja Sortowania Topologicznego Tarjana z PDF (Znaczniki)
    n = len(lista_nastepnikow)
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
        for neighbor in lista_nastepnikow[node]:
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