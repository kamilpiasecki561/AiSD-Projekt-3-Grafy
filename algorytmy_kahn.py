from collections import deque
def sortowanie_kahna(lista_nastepnikow):
    if not lista_nastepnikow:
        print("Graf jest pusty!")
        return []
    # Inicjalizacja słownika stopni wejściowych
    stopnie_wejsciowe = {wezel: 0 for wezel in lista_nastepnikow.keys()}
    
    # Węzły, które są tylko sąsiadami też są w słowniku
    for wezel, sasiedzi in lista_nastepnikow.items():
        for sasiad in sasiedzi:
            if sasiad not in stopnie_wejsciowe:
                stopnie_wejsciowe[sasiad] = 0
            stopnie_wejsciowe[sasiad] += 1
    # Znalezienie wierzchołków bez krawędzi wejściowych
    kolejka = deque([wezel for wezel, stopien in stopnie_wejsciowe.items() if stopien == 0])
    posortowane = []
    # Przetwarzanie kolejki
    while kolejka:
        aktualny = kolejka.popleft()
        posortowane.append(aktualny)
        # Zmniejszamy stopień wejściowy dla sąsiadów
        for sasiad in lista_nastepnikow.get(aktualny, []):
            stopnie_wejsciowe[sasiad] -= 1
            if stopnie_wejsciowe[sasiad] == 0:
                kolejka.append(sasiad)
    # Sprawdzenie czy graf nie ma cykli
    if len(posortowane) != len(stopnie_wejsciowe):
        print("Błąd: Graf zawiera cykl! Sortowanie topologiczne jest niemożliwe.")
        return []
    print(f"Wynik sortowania Kahna: {posortowane}")
    return posortowane