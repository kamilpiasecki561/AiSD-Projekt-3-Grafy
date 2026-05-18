import sys
import dfs_tarjan
import bfs_kahn
import eksport_tikz

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

def konwertuj_na_strukture(lista_nastepnikow, typ):
    n = len(lista_nastepnikow)
    if typ == 'list':
        return lista_nastepnikow
    elif typ == 'matrix':
        macierz = [[0] * n for _ in range(n)]
        for skad in range(n):
            for dokad in lista_nastepnikow[skad]:
                macierz[skad][dokad] = 1
        return macierz
    elif typ == 'table':
        tabela = []
        for skad in range(n):
            for dokad in lista_nastepnikow[skad]:
                tabela.append((skad, dokad))
        return tabela

def pobierz_sasiadow(graf, typ, wezel, n):
    if typ == 'list':
        return graf[wezel]
    elif typ == 'matrix':
        return [i for i in range(n) if graf[wezel][i] == 1]
    elif typ == 'table':
        return [krawedz[1] for krawedz in graf if krawedz[0] == wezel]

def wypisz_graf(graf, typ, n):
    print("")
    if typ == 'list':
        print("--- Lista nastepnikow ---")
        for i in range(n):
            sasiedzi = graf[i]
            if len(sasiedzi) == 0:
                print(f"  {i+1} -> (brak)")
            else:
                print(f"  {i+1} -> {', '.join(str(x+1) for x in sasiedzi)}")
    elif typ == 'matrix':
        print("--- Macierz sasiedztwa ---")
        naglowek = "    " + "".join([str(x + 1).rjust(4) for x in range(n)])
        print(naglowek)
        for i in range(n):
            linia = str(i+1).rjust(3) + " "
            for wartosc in graf[i]:
                linia += str(wartosc).rjust(4)
            print(linia)
    elif typ == 'table':
        print("--- Tabela krawedzi ---")
        print("  Skąd | Dokąd")
        print("  -------------")
        if len(graf) == 0:
             print("  (brak krawedzi)")
        else:
            for krawedz in graf:
                print(f"  {str(krawedz[0] + 1).rjust(4)} | {krawedz[1] + 1}")
    print("")


def petla_operacji(lista_nastepnikow, typ_reprezentacji):
    n = len(lista_nastepnikow)
    
    graf = konwertuj_na_strukture(lista_nastepnikow, typ_reprezentacji)
    
    def sasiedzi(wezel):
        return pobierz_sasiadow(graf, typ_reprezentacji, wezel, n)

    while True:
        try:
            akcja = input("action> ").strip().lower()
        except EOFError:
            break
            
        if akcja == "print":
            wypisz_graf(graf, typ_reprezentacji, n)
            
        elif akcja == "find":
            skad = wczytaj_calkowita("from> ")
            dokad = wczytaj_calkowita("to> ")
            if skad < 1 or skad > n or dokad < 1 or dokad > n:
                print(f"Falsz: wezel ({skad},{dokad}) nie istnieje w grafie")
            else:
                if (dokad - 1) in sasiedzi(skad - 1):
                    print(f"Prawda: krawedz ({skad},{dokad}) istnieje w grafie")
                else:
                    print(f"Falsz: krawedz ({skad},{dokad}) nie istnieje w grafie")
                    
        elif akcja == "bfs":
            start = wczytaj_calkowita("start_node> ")
            if 1 <= start <= n:
                bfs_kahn.uruchom_bfs(n, start - 1, sasiedzi)
            else:
                print(f"Węzeł {start} nie istnieje!")

        elif akcja == "dfs":
            start = wczytaj_calkowita("start_node> ")
            if 1 <= start <= n:
                dfs_tarjan.uruchom_dfs(n, start - 1, sasiedzi)
            else:
                print(f"Węzeł {start} nie istnieje!")

        elif akcja == "kahn":
            bfs_kahn.sortowanie_kahna(n, sasiedzi)

        elif akcja == "tarjan":
            dfs_tarjan.sortowanie_tarjana(n, sasiedzi)

        elif akcja == "tikz":
            eksport_tikz.eksportuj_do_tikz(n, sasiedzi)

        elif akcja in ["exit", "quit", "q"]:
            print("Koniec programu.")
            break
        elif akcja == "":
            continue
        else:
            print("Nieznana akcja. Dostępne: print, find, bfs, dfs, kahn, tarjan, tikz, exit")