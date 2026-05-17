import sys
from utilsy.dane_od_uzytkownika import dane_do_uruchomienia
from utilsy.generator import przenies_do_grafu

def main():
    if len(sys.argv) < 2:
        print(
            "Uzycie: python3 main.py -generate          --generate  \n"
            "LUB     python3 main.py -user-provided     --user-provided \n",
            file=sys.stderr,
        )
        sys.exit(1)

    tryb = sys.argv[1]

    if tryb == "-generate" or tryb == "--generate":
        graf = przenies_do_grafu()
        print(graf)
#    elif tryb == "-user-provided" or tryb == "--user-provided":
#        tryb_od_uzytkownika.uruchom_tryb_od_uzytkownika()
    else:
        print(
            "Nieznany argument. Uzyj -generate / --generate albo -user-provided / --user-provided.",
            file=sys.stderr,
        )
        sys.exit(1)

if __name__ == "__main__":
    main()