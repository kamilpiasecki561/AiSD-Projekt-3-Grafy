from collections import deque

def uruchom_bfs(lista_nastepnikow, start_node):
    if not lista_nastepnikow:
        print("Graf jest pusty!")
        return []
        
    odwiedzone = set([start_node])
    kolejka = deque([start_node])
    wynik = []
    
    while kolejka:
        aktualny = kolejka.popleft()
        wynik.append(aktualny)
        for sasiad in lista_nastepnikow[aktualny]:
            if sasiad not in odwiedzone:
                odwiedzone.add(sasiad)
                kolejka.append(sasiad)
                
    # Konwersja z indeksów 0 na 1
    print(f"Kolejność odwiedzania BFS (od węzła {start_node + 1}): {[x + 1 for x in wynik]}")
    return wynik


def sortowanie_kahna(lista_nastepnikow):
    n = len(lista_nastepnikow)
    if n == 0:
        print("Graf jest pusty!")
        return []
        
    # Inicjalizacja stopni wejściowych na zerach
    stopnie_wejsciowe = [0] * n
    for sasiedzi in lista_nastepnikow:
        for sasiad in sasiedzi:
            stopnie_wejsciowe[sasiad] += 1
            
    # Znalezienie wierzchołków bez krawędzi wejściowych
    kolejka = deque([i for i in range(n) if stopnie_wejsciowe[i] == 0])
    posortowane = []
    
    while kolejka:
        aktualny = kolejka.popleft()
        posortowane.append(aktualny)
        for sasiad in lista_nastepnikow[aktualny]:
            stopnie_wejsciowe[sasiad] -= 1
            if stopnie_wejsciowe[sasiad] == 0:
                kolejka.append(sasiad)
                
    if len(posortowane) != n:
        print("Błąd (Kahn): Graf zawiera cykl! Sortowanie topologiczne jest niemożliwe.")
        return []
        
    wynik_1_based = [x + 1 for x in posortowane]
    print(f"Wynik sortowania Kahna: {wynik_1_based}")
    return posortowane