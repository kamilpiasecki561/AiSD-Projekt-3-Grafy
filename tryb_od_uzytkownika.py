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
        nastepnicy_bez_duplikatow = set()
        
        for j in range(len(czesci)):
            jeden_tekst = czesci[j]
            try:
                numer_od_1 = int(jeden_tekst)
            except ValueError:
                print("Niepoprawna lista nastepnikow - uzyj liczb calkowitych", file=sys.stderr)
                sys.exit(1)
            if numer_od_1 < 1 or numer_od_1 > liczba_wierzcholkow:
                print(f"Numer wierzcholka musi byc od 1 do {liczba_wierzcholkow}.", file=sys.stderr)
                sys.exit(1)
                
            nastepnicy_bez_duplikatow.add(numer_od_1 - 1)
            
        lista_nastepnikow.append(sorted(list(nastepnicy_bez_duplikatow)))
    return lista_nastepnikow

def uruchom_tryb_od_uzytkownika():
    typ = wspolne.wczytaj_typ_reprezentacji()
    liczba_wierzcholkow = wspolne.wczytaj_calkowita("nodes> ")
    if liczba_wierzcholkow == 0:
        print("Brak wierzchołków - koniec", file=sys.stderr)
        return
    lista_nastepnikow = wczytaj_listy_nastepnikow(liczba_wierzcholkow)
    wspolne.petla_operacji(lista_nastepnikow, typ)