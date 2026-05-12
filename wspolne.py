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

def wypisz_graf(lista_nastepnikow, typ_reprezentacji):
    n = len(lista_nastepnikow)
    print("")
    
    if typ_reprezentacji == 'list':
        print("--- Lista nastepnikow ---")
        for i in range(n):
            etykieta = i + 1
            nastepnicy = lista_nastepnikow[i]
            if len(nastepnicy) == 0:
                print(f"  {etykieta} -> (brak)")
            else:
                tekst = ", ".join([str(x + 1) for x in nastepnicy])
                print(f"  {etykieta} -> {tekst}")
                
    elif typ_reprezentacji == 'matrix':
        print("--- Macierz sasiedztwa ---")
        macierz = zbuduj_macierz_sasiedztwa(lista_nastepnikow)
        naglowek = "    " + "".join([str(x + 1).rjust(4) for x in range(n)])
        print(naglowek)
        for wiersz_nr in range(n):
            etykieta_wiersza = wiersz_nr + 1
            linia_wyjscia = str(etykieta_wiersza).rjust(3) + " "
            for wartosc in macierz[wiersz_nr]:
                linia_wyjscia += str(wartosc).rjust(4)
            print(linia_wyjscia)
            
    elif typ_reprezentacji == 'table':
        print("--- Tabela krawedzi ---")
        print("  Skąd | Dokąd")
        print("  -------------")
        for i in range(n):
            skad = i + 1
            nastepnicy = lista_nastepnikow[i]
            if not nastepnicy:
                print(f"  {str(skad).rjust(4)} | -")
            for dokad in nastepnicy:
                print(f"  {str(skad).rjust(4)} | {dokad + 1}")
    print("")

def petla_operacji(lista_nastepnikow, typ_reprezentacji):
    while True:
        try:
            akcja = input("action> ").strip().lower()
        except EOFError:
            break
            
        if akcja == "print":
            wypisz_graf(lista_nastepnikow, typ_reprezentacji)
            
        elif akcja == "find":
            skad = wczytaj_calkowita("from> ")
            dokad = wczytaj_calkowita("to> ")
            
            n = len(lista_nastepnikow)
            if skad < 1 or skad > n or dokad < 1 or dokad > n:
                print(f"Falsz: krawedz ({skad},{dokad}) nie istnieje w grafie")
            else:
                if (dokad - 1) in lista_nastepnikow[skad - 1]:
                    print(f"Prawda: krawedz ({skad},{dokad}) istnieje w grafie")
                else:
                    print(f"Falsz: krawedz ({skad},{dokad}) nie istnieje w grafie")
                    
        elif akcja in ["exit", "quit", "q"]:
            break
        elif akcja == "":
            continue
        else:
            print("Nieznana akcja. Dostępne: Print, find, exit")