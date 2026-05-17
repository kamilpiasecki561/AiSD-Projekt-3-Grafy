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

def wczytaj_calkowita(zacheta):
    while True:
        try:
            linia = input(zacheta)
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