# V19: Daten organisieren mit SQL — Lösungen

---

## Aufgabe 1: Theorie-Check

**a)**
- **Tabelle:** Eine strukturierte Sammlung von Daten mit Spalten (Eigenschaften) und Zeilen (Einträge), wie eine Excel-Tabelle.
- **Zeile:** Ein einzelner Datensatz in der Tabelle (z.B. eine Maschine).
- **Spalte:** Eine Eigenschaft, die für jeden Eintrag gespeichert wird (z.B. Name, Temperatur).
- **Primärschlüssel (id):** Eine eindeutige Nummer, die jeden Eintrag identifiziert.

**b)**
- `SELECT name FROM maschinen WHERE temperatur > 50;` → Gibt die Namen aller Maschinen aus, deren Temperatur über 50°C liegt.
- `INSERT INTO maschinen (name, typ) VALUES ('ROBO-02', 'Roboter');` → Fügt eine neue Maschine "ROBO-02" vom Typ "Roboter" ein.
- `DELETE FROM maschinen WHERE id = 3;` → Löscht die Maschine mit der ID 3.

---

## Aufgabe 2: Maschinen-Datenbank

```python
import sqlite3

verbindung = sqlite3.connect("fabrik.db")
cursor = verbindung.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS maschinen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        typ TEXT,
        standort TEXT,
        temperatur REAL
    )
""")

# 3 Maschinen einfügen
cursor.execute("""
    INSERT INTO maschinen (name, typ, standort, temperatur)
    VALUES ('CNC-01', 'Fräse', 'Halle A', 42.5)
""")

cursor.execute("""
    INSERT INTO maschinen (name, typ, standort, temperatur)
    VALUES ('CNC-02', 'Fräse', 'Halle A', 38.1)
""")

cursor.execute("""
    INSERT INTO maschinen (name, typ, standort, temperatur)
    VALUES ('ROBO-01', 'Roboter', 'Halle B', 55.0)
""")

verbindung.commit()

# Alle Maschinen anzeigen
cursor.execute("SELECT * FROM maschinen")
ergebnisse = cursor.fetchall()

print("Alle Maschinen:")
for zeile in ergebnisse:
    print(f"  {zeile}")

# Heiße Maschinen
cursor.execute("SELECT * FROM maschinen WHERE temperatur > 40")
heisse = cursor.fetchall()

print("\nHeiße Maschinen (>40°C):")
for zeile in heisse:
    print(f"  {zeile}")

verbindung.close()
```

---

## Aufgabe 3: Maschinen-Verwaltung

```python
import sqlite3

verbindung = sqlite3.connect("verwaltung.db")
cursor = verbindung.cursor()

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
        cursor.execute("SELECT * FROM maschinen")
        ergebnisse = cursor.fetchall()
        if len(ergebnisse) == 0:
            print("Keine Maschinen vorhanden.")
        else:
            for zeile in ergebnisse:
                print(f"  ID:{zeile[0]} | {zeile[1]} | {zeile[2]} | {zeile[3]}°C")

    elif wahl == "2":
        name = input("Name: ")
        typ = input("Typ: ")
        temp = float(input("Temperatur: "))
        cursor.execute(
            "INSERT INTO maschinen (name, typ, temperatur) VALUES (?, ?, ?)",
            (name, typ, temp)
        )
        verbindung.commit()
        print(f"{name} wurde hinzugefügt!")

    elif wahl == "3":
        maschinen_id = input("ID der Maschine: ")
        neue_temp = float(input("Neue Temperatur: "))
        cursor.execute(
            "UPDATE maschinen SET temperatur = ? WHERE id = ?",
            (neue_temp, maschinen_id)
        )
        verbindung.commit()
        print("Temperatur aktualisiert!")

    elif wahl == "4":
        print("Auf Wiedersehen!")
        break

verbindung.close()
```

### Bonus: Maschine löschen

Zusätzliche Option im Menü:

```python
    elif wahl == "5":
        maschinen_id = input("ID der zu löschenden Maschine: ")
        cursor.execute(
            "DELETE FROM maschinen WHERE id = ?",
            (maschinen_id,)
        )
        verbindung.commit()
        print("Maschine gelöscht!")
```
