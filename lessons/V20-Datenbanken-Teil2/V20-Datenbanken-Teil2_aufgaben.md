# V20: Daten verknüpfen — Aufgaben

> **Punkte-System:** Sammle Punkte für die Klausurvorbereitung!

---

## Aufgabe 1: Theorie-Check (2 Punkte)

**a)** Was ist ein Fremdschlüssel? Erkläre an einem Beispiel.

**b)** Erkläre in eigenen Worten, was dieser SQL-Befehl tut:

```sql
SELECT maschinen.name, hallen.name
FROM maschinen
JOIN hallen ON maschinen.hallen_id = hallen.id
WHERE maschinen.temperatur > 40;
```

**c)** Was ist der Unterschied zwischen `COUNT(*)` und `GROUP BY`?

---

## Aufgabe 2: Fabrik-Datenbank mit JOIN (4 Punkte)

Erstelle eine Datenbank mit zwei Tabellen und verknüpfe sie.

```python
import sqlite3

verbindung = sqlite3.connect("fabrik_aufgabe.db")
cursor = verbindung.cursor()

# Tabelle 1: Hallen
cursor.execute("""
    CREATE TABLE IF NOT EXISTS hallen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        adresse TEXT
    )
""")

# Tabelle 2: Maschinen
cursor.execute("""
    CREATE TABLE IF NOT EXISTS maschinen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        typ TEXT,
        temperatur REAL,
        hallen_id INTEGER
    )
""")

# Hallen einfügen
cursor.execute("INSERT INTO hallen (name, adresse) VALUES ('Halle A', 'Industriestr. 1')")
cursor.execute("INSERT INTO hallen (name, adresse) VALUES ('Halle B', 'Industriestr. 3')")
cursor.execute("INSERT INTO hallen (name, adresse) VALUES ('Halle C', 'Fabrikweg 5')")

# TODO: Füge 5 Maschinen ein (verteilt auf die 3 Hallen)
# Tipp: hallen_id 1 = Halle A, 2 = Halle B, 3 = Halle C
cursor.execute("INSERT INTO maschinen (name, typ, temperatur, hallen_id) VALUES ('CNC-01', 'Fräse', 42.5, 1)")
cursor.execute("INSERT INTO maschinen (name, typ, temperatur, hallen_id) VALUES ('CNC-02', 'Fräse', 38.1, 1)")
cursor.execute("INSERT INTO maschinen (name, typ, temperatur, hallen_id) VALUES ('ROBO-01', 'Roboter', 55.0, 2)")
# TODO: Füge 2 weitere Maschinen ein
___
___

verbindung.commit()

# TODO: JOIN-Abfrage — Zeige Maschinenname, Typ und Hallenname
cursor.execute("""
    SELECT maschinen.name, maschinen.typ, maschinen.temperatur, hallen.name
    FROM maschinen
    JOIN hallen ON ___
""")

print("Alle Maschinen mit Halle:")
for zeile in cursor.fetchall():
    print(f"  {zeile[0]} ({zeile[1]}) | {zeile[2]}°C | {zeile[3]}")

# TODO: Zeige nur Maschinen mit Temperatur > 40 (füge WHERE hinzu)
cursor.execute("""
    SELECT maschinen.name, maschinen.temperatur, hallen.name
    FROM maschinen
    JOIN hallen ON maschinen.hallen_id = hallen.id
    WHERE ___
""")

print("\nHeiße Maschinen:")
for zeile in cursor.fetchall():
    print(f"  {zeile[0]}: {zeile[1]}°C in {zeile[2]}")

verbindung.close()
```

---

## Aufgabe 3: Datenbank-Detektiv (5 Punkte)

Du hast eine fertige Datenbank. Beantworte die Fragen mit SQL-Abfragen!

```python
import sqlite3

# Datenbank vorbereiten
verbindung = sqlite3.connect("detektiv.db")
cursor = verbindung.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS hallen (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS maschinen (id INTEGER PRIMARY KEY, name TEXT, typ TEXT, temperatur REAL, hallen_id INTEGER)")

# Testdaten
cursor.execute("DELETE FROM hallen")
cursor.execute("DELETE FROM maschinen")
cursor.executemany("INSERT INTO hallen VALUES (?, ?)", [
    (1, "Halle A"), (2, "Halle B"), (3, "Halle C")
])
cursor.executemany("INSERT INTO maschinen VALUES (?, ?, ?, ?, ?)", [
    (1, "CNC-01", "Fräse", 42.5, 1),
    (2, "CNC-02", "Fräse", 38.1, 1),
    (3, "CNC-03", "Fräse", 51.0, 2),
    (4, "ROBO-01", "Roboter", 55.0, 2),
    (5, "ROBO-02", "Roboter", 33.0, 3),
    (6, "LASER-01", "Laser", 28.0, 3),
    (7, "LASER-02", "Laser", 62.0, 1),
])
verbindung.commit()

# Frage 1: Wie viele Maschinen stehen in jeder Halle?
# TODO: GROUP BY + COUNT
cursor.execute("""___""")
print("Maschinen pro Halle:")
for zeile in cursor.fetchall():
    print(f"  {zeile[0]}: {zeile[1]} Maschinen")

# Frage 2: Welche Halle hat die höchste Durchschnittstemperatur?
# Tipp: SELECT hallen.name, AVG(maschinen.temperatur) ... GROUP BY hallen.name
cursor.execute("""___""")
print("\nDurchschnittstemperatur pro Halle:")
for zeile in cursor.fetchall():
    print(f"  {zeile[0]}: {zeile[1]:.1f}°C")

# Frage 3: Welche Maschine ist am heißesten und in welcher Halle steht sie?
# Tipp: ORDER BY temperatur DESC LIMIT 1
cursor.execute("""___""")
zeile = cursor.fetchone()
print(f"\nHeißeste Maschine: {zeile[0]} mit {zeile[1]}°C in {zeile[2]}")

verbindung.close()
```

**Bonus (+ 2 Punkte):** Erstelle eine dritte Tabelle `wartungen` mit Spalten (id, maschinen_id, datum, beschreibung). Füge Wartungseinträge hinzu und zeige mit einem JOIN an, welche Maschine wann gewartet wurde.

---

## Punkte-Übersicht

| Aufgabe | Thema | Punkte |
|---------|-------|--------|
| 1 | Theorie-Check | 2 |
| 2 | Fabrik-DB mit JOIN | 4 |
| 3 | Datenbank-Detektiv | 5 |
| Bonus | Wartungs-Tabelle | +2 |
| **Gesamt** | | **max. 13** |
