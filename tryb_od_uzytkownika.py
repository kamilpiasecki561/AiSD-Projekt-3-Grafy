"""Tryb -user-provided / --user-provided: graf z list nastepnikow (stdin)."""

import sys

import wspolne


def wczytaj_listy_nastepnikow(liczba_wierzcholkow):
    lista_nastepnikow = []
    for wierzcholek_od_1 in range(1, liczba_wierzcholkow + 1):
        zacheta = str(wierzcholek_od_1) + "> "
        linia = input(zacheta)
        linia = linia.strip()
        if linia == "":
            pusta = []
            lista_nastepnikow.append(pusta)
            continue
        czesci = linia.split()
        nastepnicy = []
        for j in range(len(czesci)):
            jeden_tekst = czesci[j]
            try:
                numer_od_1 = int(jeden_tekst)
            except ValueError:
                print("Niepoprawna lista nastepnikow — uzyj liczb calkowitych.", file=sys.stderr)
                sys.exit(1)
            if numer_od_1 < 1 or numer_od_1 > liczba_wierzcholkow:
                print(
                    "Numer wierzcholka musi byc od 1 do "
                    + str(liczba_wierzcholkow)
                    + ".",
                    file=sys.stderr,
                )
                sys.exit(1)
            nastepnicy.append(numer_od_1 - 1)
        lista_nastepnikow.append(nastepnicy)
    return lista_nastepnikow


def uruchom_tryb_od_uzytkownika():
    liczba_wierzcholkow = wspolne.wczytaj_calkowita("nodes> ")
    if liczba_wierzcholkow == 0:
        print("Brak wierzchołków — koniec.", file=sys.stderr)
        return
    lista_nastepnikow = wczytaj_listy_nastepnikow(liczba_wierzcholkow)
    wspolne.wypisz_graf(lista_nastepnikow)
