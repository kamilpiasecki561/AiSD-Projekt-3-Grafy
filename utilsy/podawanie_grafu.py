from utilsy.dane_od_uzytkownika import wczytaj_calkowita, wczytaj_typ_reprezentacji
from grafy.macierz import MatrixGraph
from grafy.lista import ListGraph
from grafy.tablica import EdgeTableGraph

def reczne_podawanie_grafu():
    typ = wczytaj_typ_reprezentacji()
    liczba_wierzcholkow = wczytaj_calkowita()
    if typ == 'matrix':
        graf = MatrixGraph(liczba_wierzcholkow)
    elif typ == 'list':
        graf = ListGraph(liczba_wierzcholkow)
    elif typ == 'edge-table':
        graf = EdgeTableGraph(liczba_wierzcholkow)

    for i in range(liczba_wierzcholkow):
        print(f"Podaj sąsiadów wierzchołka {i+1} (oddzielonych spacją):")
        sasiedzi = set(input().strip().split())
        for sasied in sasiedzi:
            if sasied.isdigit():
                v = int(sasied) - 1
                if i < v < liczba_wierzcholkow:
                    graf.add_edge(i, v)
                else:
                    print(f"Nieprawidłowy wierzchołek: {v + 1}. Ignoruję.")
            else:
                print(f"Nieprawidłowy input: {sasied}. Ignoruję.")
    

#   ^ to zle bo wczytuje graf, bo nie sprawdza czy krawędź już istnieje, a w przypadku listy sąsiadów może się zdarzyć że użytkownik poda ten sam sąsiad więcej niż raz, co spowoduje że w liście sąsiadów będzie on występował wielokrotnie, a to jest niepoprawne. Trzeba dodać sprawdzanie czy krawędź już istnieje przed dodaniem jej do grafu. ^
# ten debil wlasnie sam wygenerowal co zrobil zle i trzeba poprawic xd
# jak sie poda cos zle to przechodzi do nastepnego wierzchołka, a powinno sie powtarzac pytanie o tego samego wierzchołka az do skutku, czyli az uzytkownik poda poprawne dane, albo az dojdzie do EOF, wtedy program powinien sie zakonczyc. Trzeba dodac petle while True z odpowiednimi warunkami wyjscia. ^
# znowu sobie dokonczyl sam xd