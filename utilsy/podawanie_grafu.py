from utilsy.dane_od_uzytkownika import dane_do_uruchomienia
from grafy.macierz import MatrixGraph
from grafy.lista import ListGraph
from grafy.tablica import EdgeTableGraph

def reczne_podawanie_grafu():
    typ, liczba_wierzcholkow = dane_do_uruchomienia()
    if typ == 'matrix':
        graf = MatrixGraph(liczba_wierzcholkow)
    elif typ == 'list':
        graf = ListGraph(liczba_wierzcholkow)
    elif typ == 'edge-table':
        graf = EdgeTableGraph(liczba_wierzcholkow)

    for i in range(liczba_wierzcholkow):
        print(f"Podaj sąsiadów wierzchołka {i} (oddzielonych spacją):")
        sasiedzi = input().strip().split()
        for sasied in sasiedzi:
            if sasied.isdigit():
                v = int(sasied)
                if 0 <= v < liczba_wierzcholkow:
                    graf.add_edge(i, v)
                else:
                    print(f"Nieprawidłowy wierzchołek: {v}. Ignoruję.")
            else:
                print(f"Nieprawidłowy input: {sasied}. Ignoruję.")