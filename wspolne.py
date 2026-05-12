"""Funkcje wspolne dla obu trybow programu (wczytywanie, wypis grafu)."""

import sys


def wczytaj_calkowita(zacheta):
    while True:
        linia = input(zacheta)
        linia = linia.strip()
        try:
            wartosc = int(linia)
            if wartosc < 0:
                print("Podaj nieujemną liczbę całkowitą", file=sys.stderr)
            else:
                return wartosc
        except ValueError:
            print("To nie jest poprawna liczba całkowita, spróbuj jeszcze raz", file=sys.stderr)


def zbuduj_macierz_sasiedztwa(lista_nastepnikow):
    n = len(lista_nastepnikow)
    macierz = []
    for wiersz_nr in range(n):
        wiersz = []
        for kolumna_nr in range(n):
            wiersz.append(0)
        macierz.append(wiersz)

    for skad in range(n):
        nastepnicy = lista_nastepnikow[skad]
        for i in range(len(nastepnicy)):
            dokad = nastepnicy[i]
            if dokad >= 0 and dokad < n:
                macierz[skad][dokad] = 1
    return macierz


def wypisz_graf(lista_nastepnikow):
    n = len(lista_nastepnikow)
    print("")
    print("--- Lista nastepnikow (numeracja 1..n) ---")
    for i in range(n):
        etykieta = i + 1
        nastepnicy = lista_nastepnikow[i]
        if len(nastepnicy) == 0:
            print("  " + str(etykieta) + " -> (brak)")
        else:
            tekst = ""
            for j in range(len(nastepnicy)):
                if j > 0:
                    tekst = tekst + ", "
                numer_wyjscia = nastepnicy[j] + 1
                tekst = tekst + str(numer_wyjscia)
            print("  " + str(etykieta) + " -> " + tekst)

    print("")
    print("--- Macierz sasiedztwa (wiersz i kolumna: wierzcholki 1..n) ---")
    macierz = zbuduj_macierz_sasiedztwa(lista_nastepnikow)

    naglowek = "    "
    for kolumna in range(n):
        etykieta_kolumny = kolumna + 1
        naglowek = naglowek + str(etykieta_kolumny).rjust(4)
    print(naglowek)

    for wiersz_nr in range(n):
        etykieta_wiersza = wiersz_nr + 1
        linia_wyjscia = str(etykieta_wiersza).rjust(3) + " "
        wiersz = macierz[wiersz_nr]
        for i in range(len(wiersz)):
            linia_wyjscia = linia_wyjscia + str(wiersz[i]).rjust(4)
        print(linia_wyjscia)
