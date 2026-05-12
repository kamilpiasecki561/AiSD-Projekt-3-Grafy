import sys
import tryb_generowania
import tryb_od_uzytkownika

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
        tryb_generowania.uruchom_tryb_generowania()
    elif tryb == "-user-provided" or tryb == "--user-provided":
        tryb_od_uzytkownika.uruchom_tryb_od_uzytkownika()
    else:
        print(
            "Nieznany argument. Uzyj -generate / --generate albo -user-provided / --user-provided.",
            file=sys.stderr,
        )
        sys.exit(1)

if __name__ == "__main__":
    main()
