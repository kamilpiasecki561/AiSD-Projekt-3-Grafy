#   Uruchomienie (obie formy flag, jak w poleceniu):
#   python main.py -generate         albo    python main.py --generate
#   python main.py -user-provided    albo    python main.py --user-provided
#
#   Heredoc (bash), przyklad:
#   python main.py --user-provided << EOF
#   4
#   2
#
#   2
#   2 3
#   EOF

import sys

import tryb_generowania
import tryb_od_uzytkownika


def glowna():
    if len(sys.argv) < 2:
        print(
            "Uzycie: python main.py -generate | --generate  "
            "LUB  python main.py -user-provided | --user-provided",
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
    glowna()
