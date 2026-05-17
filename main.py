import sys
from utilsy.generator import wygeneruj_graf
from utilsy.podawanie_grafu import reczne_podawanie_grafu

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
        graf = wygeneruj_graf()
        print(graf)
    elif tryb == "-user-provided" or tryb == "--user-provided":
        reczne_podawanie_grafu()
        print(graf)
    else:
        print(
            "Nieznany argument. Uzyj -generate / --generate albo -user-provided / --user-provided.",
            file=sys.stderr,
        )
        sys.exit(1)

if __name__ == "__main__":
    main()