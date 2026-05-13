from collections import deque
def uruchom_bfs(lista_nastepnikow, start_node=None):
    if not lista_nastepnikow:
        print("Graf jest pusty!")
        return
    # Jeśli nie podano startu, bierzemy pierwszy klucz ze słownika
    if start_node is None:
        start_node = list(lista_nastepnikow.keys())[0]
    if start_node not in lista_nastepnikow:
        print(f"Węzeł {start_node} nie istnieje w grafie.")
        return
    odwiedzone = set([start_node])
    kolejka = deque([start_node])
    wynik = []
    while kolejka:
        aktualny = kolejka.popleft()
        wynik.append(aktualny)
        for sasiad in lista_nastepnikow.get(aktualny, []):
            if sasiad not in odwiedzone:
                odwiedzone.add(sasiad)
                kolejka.append(sasiad)
    print(f"Kolejność odwiedzania BFS (od węzła {start_node}): {wynik}")
    return wynik