# V19: Daten organisieren mit SQL — Aufgaben

> **Punkte-System:** Sammle Punkte für die Klausurvorbereitung!

---

## Aufgabe 1: Theorie-Check (2 Punkte)

**a)** Erkläre die folgenden Begriffe in je einem Satz:
- Tabelle
- Zeile
- Spalte
- Primärschlüssel (id)

**b)** Was machen diese SQL-Befehle?

```sql
SELECT name FROM maschinen WHERE temperatur > 50;

INSERT INTO maschinen (name, typ) VALUES ('ROBO-02', 'Roboter');

DELETE FROM maschinen WHERE id = 3;
```

---

## Aufgabe 2: Maschinen-Datenbank (4 Punkte)

Erstelle eine Datenbank für eine Fabrik und füge Maschinen hinzu.

```python
import sqlite3

# Verbindung erstellen
verbindung = sqlite3.connect("fabrik.db")
cursor = verbindung.cursor()

# Tabelle erstellen
cursor.execute("""
    CREATE TABLE IF NOT EXISTS maschinen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        typ TEXT,
        standort TEXT,
        temperatur REAL
    )
""")

# TODO: Füge 3 Maschinen ein
# Tipp: cursor.execute("INSERT INTO maschinen (name, typ, standort, temperatur) VALUES (...)")

# Maschine 1: CNC-01, Fräse, Halle A, 42.5
cursor.execute("""___""")

# Maschine 2: CNC-02, Fräse, Halle A, 38.1
cursor.execute("""___""")

# Maschine 3: ROBO-01, Roboter, Halle B, 55.0
cursor.execute("""___""")

verbindung.commit()

# TODO: Alle Maschinen anzeigen
# Tipp: cursor.execute("SELECT * FROM maschinen")
cursor.execute("""___""")
ergebnisse = cursor.fetchall()

print("Alle Maschinen:")
for zeile in ergebnisse:
    print(f"  {zeile}")

# TODO: Nur Maschinen mit Temperatur > 40 anzeigen
# Tipp: SELECT * FROM maschinen WHERE temperatur > 40
cursor.execute("""___""")
heisse = cursor.fetchall()

print("\nHeiße Maschinen (>40°C):")
for zeile in heisse:
    print(f"  {zeile}")

verbindung.close()
```

---

## Aufgabe 3: Maschinen-Verwaltung (5 Punkte)

Erstelle ein interaktives Programm, mit dem man Maschinen hinzufügen und anzeigen kann.

```python
import sqlite3

verbindung = sqlite3.connect("verwaltung.db")
cursor = verbindung.cursor()

# Tabelle erstellen
cursor.execute("""
    CREATE TABLE IF NOT EXISTS maschinen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        typ TEXT,
        temperatur REAL
    )
""")
verbindung.commit()

while True:
    print("\n=== MASCHINEN-VERWALTUNG ===")
    print("1 - Alle Maschinen anzeigen")
    print("2 - Neue Maschine hinzufügen")
    print("3 - Temperatur aktualisieren")
    print("4 - Beenden")

    wahl = input("Deine Wahl: ")

    if wahl == "1":
        # TODO: Alle Maschinen anzeigen
        cursor.execute("SELECT * FROM maschinen")
        ergebnisse = cursor.fetchall()
        if len(ergebnisse) == 0:
            print("Keine Maschinen vorhanden.")
        else:
            for zeile in ergebnisse:
                print(f"  ID:{zeile[0]} | {zeile[1]} | {zeile[2]} | {zeile[3]}°C")

    elif wahl == "2":
        # TODO: Neue Maschine per input() hinzufügen
        name = input("Name: ")
        typ = input("Typ: ")
        temp = float(input("Temperatur: "))
        # TODO: INSERT-Befehl ausführen
        cursor.execute("""___""", ___)
        verbindung.commit()
        print(f"{name} wurde hinzugefügt!")

    elif wahl == "3":
        # TODO: Temperatur einer Maschine aktualisieren
        maschinen_id = input("ID der Maschine: ")
        neue_temp = float(input("Neue Temperatur: "))
        # TODO: UPDATE-Befehl ausführen
        cursor.execute("""___""", ___)
        verbindung.commit()
        print("Temperatur aktualisiert!")

    elif wahl == "4":
        print("Auf Wiedersehen!")
        break

verbindung.close()
```

**Bonus (+ 2 Punkte):** Füge eine Option 5 hinzu: "Maschine löschen" — der Benutzer gibt die ID ein und die Maschine wird mit `DELETE` entfernt.

---

## Punkte-Übersicht

| Aufgabe | Thema | Punkte |
|---------|-------|--------|
| 1 | Theorie-Check | 2 |
| 2 | Maschinen-Datenbank | 4 |
| 3 | Maschinen-Verwaltung | 5 |
| Bonus | Maschine löschen | +2 |
| **Gesamt** | | **max. 13** |
