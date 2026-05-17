import random
import sys
from utilsy.dane_od_uzytkownika import dane_do_uruchomienia
from grafy.macierz import MatrixGraph
from grafy.lista import ListGraph
from grafy.tablica import EdgeTableGraph

def czy_krawedz_juz_jest(lista_krawedzi, skad, dokad):
    for i in range(len(lista_krawedzi)):
        para = lista_krawedzi[i]
        od_wierzcholka = para[0]
        do_wierzcholka = para[1]
        if od_wierzcholka == skad and do_wierzcholka == dokad:
            return True
    return False

def zrob_liste_wszystkich_mozliwych_krawedzi_w_gornym_trojkacie(liczba_wierzcholkow):
    wynik = []
    for skad in range(liczba_wierzcholkow):
        for dokad in range(skad + 1, liczba_wierzcholkow):
            para = [skad, dokad]
            wynik.append(para)
    return wynik

def wygeneruj_spojny_dag(liczba_wierzcholkow, nasycenie):
    if liczba_wierzcholkow <= 0:
        print("Liczba wierzchołków musi być dodatnia", file=sys.stderr)
        sys.exit(1)

    if liczba_wierzcholkow == 1:
        graf_pusty = []
        graf_pusty.append([])
        return graf_pusty

    wszystkie_mozliwe = zrob_liste_wszystkich_mozliwych_krawedzi_w_gornym_trojkacie(liczba_wierzcholkow)
    ile_mozna_max = len(wszystkie_mozliwe)

    wybrane_krawedzie = []
    for i in range(liczba_wierzcholkow - 1):
        skad = i
        dokad = i + 1
        wybrane_krawedzie.append([skad, dokad])

    ile_chcemy = round(nasycenie * ile_mozna_max)
    if ile_chcemy < liczba_wierzcholkow - 1:
        ile_chcemy = liczba_wierzcholkow - 1
    if ile_chcemy > ile_mozna_max:
        ile_chcemy = ile_mozna_max

    kandydaci = []
    for i in range(len(wszystkie_mozliwe)):
        para = wszystkie_mozliwe[i]
        skad = para[0]
        dokad = para[1]
        if czy_krawedz_juz_jest(wybrane_krawedzie, skad, dokad):
            pass
        else:
            kandydaci.append(para)

    random.shuffle(kandydaci)

    for i in range(len(kandydaci)):
        if len(wybrane_krawedzie) >= ile_chcemy:
            break
        para = kandydaci[i]
        wybrane_krawedzie.append(para)

    lista_nastepnikow = []
    for i in range(liczba_wierzcholkow):
        pusta_lista = []
        lista_nastepnikow.append(pusta_lista)

    for i in range(len(wybrane_krawedzie)):
        para = wybrane_krawedzie[i]
        skad = para[0]
        dokad = para[1]
        lista_nastepnikow[skad].append(dokad)

    for i in range(len(lista_nastepnikow)):
        lista_nastepnikow[i].sort()

    return lista_nastepnikow

def uruchom_tryb_generowania():
    typ, liczba_wierzcholkow, nasycenie = dane_do_uruchomienia()
    lista_nastepnikow = wygeneruj_spojny_dag(liczba_wierzcholkow, nasycenie)
    return typ, lista_nastepnikow, liczba_wierzcholkow

def przenies_do_grafu():
    typ, lista_nastepnikow, liczba_wierzcholkow = uruchom_tryb_generowania()
    if typ == 'matrix':
        graf = MatrixGraph(liczba_wierzcholkow)
    elif typ == 'list':
        graf = ListGraph(liczba_wierzcholkow)
    elif typ == 'table':
        graf = EdgeTableGraph(liczba_wierzcholkow)

    for i in range(len(lista_nastepnikow)):
        nastepnik = lista_nastepnikow[i]
        for j in range(len(nastepnik)):
            dokad = nastepnik[j]
            graf.add_edge(i, dokad)

    return graf