def erstelle_spielfeld():
    print(" ", end=" ")
    for buchstabe in "ABCDE":
        print(f"{buchstabe}", end=" ")
    print()

    for zeile in range(1, 6):
        print(f"{zeile}", end=" ")
        for i in range(5):
            print("~", end=" ")
        print()

def spielfeld_ausgeben(spielfeld)


# ── Schiffspositionen festlegen ──────────────────────────────────────────────
schiff_1 = "B2"
schiff_2 = "D4"

# ── Schritt 1: Koordinate einlesen ───────────────────────────────────────────
eingabe = "B3"

buchstabe = eingabe[0]       # erstes Zeichen  → Spalte,  z.B. "B"
zahl      = int(eingabe[1])  # zweites Zeichen → Zeile,   z.B. 2

# ── Schritt 2: Eingabe validieren ────────────────────────────────────────────
ist_gueltige_spalte = "A" <= buchstabe <= "E"
ist_gueltige_zeile  = 1 <= zahl <= 5

if ist_gueltige_spalte and ist_gueltige_zeile:

    # ── Schritt 3: Treffer oder Wasser? ──────────────────────────────────────
    if eingabe == schiff_1 or eingabe == schiff_2:
        print("Treffer!")
    else:
        print("Wasser!")

else:
    print("Ungültige Eingabe!")