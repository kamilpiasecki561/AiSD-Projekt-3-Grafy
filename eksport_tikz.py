def eksportuj_do_tikz(n, sasiedzi_func):
    if n == 0:
        print("% Graf jest pusty")
        return

    krawedzie = set()
    for u in range(n):
        for v in sasiedzi_func(u):
            krawedzie.add((u + 1, v + 1))
            
    print("\\begin{tikzpicture}[>=stealth,")
    print("  every node/.style={circle, draw, minimum size=8mm, font=\\sffamily}]")
    print("")
    
    print("  % Wezly")
    promien = max(3.0, n * 0.6)
    for i in range(1, n + 1):
        kat = 90 - (360 / n) * (i - 1)
        print(f"  \\node ({i}) at ({kat:.1f}:{promien:.1f}cm) {{{i}}};")
        
    print("")
    print("  % Krawedzie")
    
    for u, v in sorted(krawedzie):
        if u == v:
            print(f"  \\draw[->] ({u}) to[loop above] ({v});")
        else:
            if (v, u) in krawedzie:
                # Krawedz dwukierunkowa
                print(f"  \\draw[->] ({u}) to[bend left=15] ({v});")
            else:
                # Krawedz jednokierunkowa
                print(f"  \\draw[->] ({u}) -- ({v});")

    print("\\end{tikzpicture}")
