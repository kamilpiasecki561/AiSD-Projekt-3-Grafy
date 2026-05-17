import sys

def wczytaj_typ_reprezentacji():
    while True:
        try:
            typ = input("type> ").strip().lower()
            if typ in ['matrix', 'list', 'table']:
                return typ
            else:
                print("Dozwolone typy to: 'matrix', 'list', 'table'. Spróbuj jeszcze raz", file=sys.stderr)
        except EOFError:
            sys.exit(0)

def wczytaj_calkowita():
    while True:
        try:
            linia = input("nodes> ")
            linia = linia.strip()
            wartosc = int(linia)
            if wartosc < 0:
                print("Podaj nieujemną liczbę całkowitą", file=sys.stderr)
            else:
                return wartosc
        except ValueError:
            print("To nie jest poprawna liczba całkowita, spróbuj jeszcze raz", file=sys.stderr)
        except EOFError:
            sys.exit(0)

def wczytaj_nasycenie_procent():
    while True:
        linia = input("saturation> ")
        linia = linia.strip()
        try:
            procent = int(linia)
            if procent < 0 or procent > 100:
                print("Nasycenie musi byc liczba calkowita od 0 do 100", file=sys.stderr)
            else:
                ulamek = procent / 100.0
                return ulamek
        except ValueError:
            print("To nie jest poprawna liczba calkowita, sprobuj jeszcze raz", file=sys.stderr)
        except EOFError:
            sys.exit(0)

def dane_do_uruchomienia():
    typ = wczytaj_typ_reprezentacji()
    liczba_wierzcholkow = wczytaj_calkowita()
    if liczba_wierzcholkow == 0:
        print("Graf pusty — koniec.", file=sys.stderr)
        return
    nasycenie = wczytaj_nasycenie_procent()
    return typ, liczba_wierzcholkow, nasycenie