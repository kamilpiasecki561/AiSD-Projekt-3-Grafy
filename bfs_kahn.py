from collections import deque

def uruchom_bfs(n, start_node, sasiedzi_func):
    if n == 0:
        print("Graf jest pusty!")
        return []
        
    odwiedzone = set([start_node])
    kolejka = deque([start_node])
    wynik = []
    
    while kolejka:
        aktualny = kolejka.popleft()
        wynik.append(aktualny)
        for sasiad in sasiedzi_func(aktualny):
            if sasiad not in odwiedzone:
                odwiedzone.add(sasiad)
                kolejka.append(sasiad)
                
    print(f"Kolejność odwiedzania BFS (od węzła {start_node + 1}): {[x + 1 for x in wynik]}")
    return wynik


def sortowanie_kahna(n, sasiedzi_func):
    if n == 0:
        print("Graf jest pusty!")
        return []
        
    stopnie_wejsciowe = [0] * n
    for i in range(n):
        for sasiad in sasiedzi_func(i):
            stopnie_wejsciowe[sasiad] += 1
            
    kolejka = deque([i for i in range(n) if stopnie_wejsciowe[i] == 0])
    posortowane = []
    
    while kolejka:
        aktualny = kolejka.popleft()
        posortowane.append(aktualny)
        for sasiad in sasiedzi_func(aktualny):
            stopnie_wejsciowe[sasiad] -= 1
            if stopnie_wejsciowe[sasiad] == 0:
                kolejka.append(sasiad)
                
    if len(posortowane) != n:
        print("Błąd (Kahn): Graf zawiera cykl! Sortowanie topologiczne jest niemożliwe.")
        return []
        
    wynik_1_based = [x + 1 for x in posortowane]
    print(f"Wynik sortowania Kahna: {wynik_1_based}")
    return posortowane