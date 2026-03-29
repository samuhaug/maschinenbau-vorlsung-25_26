# V20: Daten verknüpfen — Lösungen

---

## Aufgabe 1: Theorie-Check

**a)** Ein **Fremdschlüssel** ist eine Spalte in einer Tabelle, die auf den Primärschlüssel (id) einer anderen Tabelle verweist. Beispiel: `hallen_id` in der Tabelle `maschinen` verweist auf `id` in der Tabelle `hallen`. So weiß man, in welcher Halle jede Maschine steht.

**b)** Der Befehl:
- Verbindet die Tabellen `maschinen` und `hallen` über den Fremdschlüssel
- Filtert nur Maschinen mit Temperatur über 40°C
- Zeigt den Maschinennamen und den Hallennamen an

**c)**
- `COUNT(*)` zählt die Anzahl der Zeilen
- `GROUP BY` gruppiert die Ergebnisse nach einer Spalte (z.B. pro Halle)
- Zusammen: `COUNT(*)` zählt, wie viele Einträge es pro Gruppe gibt

---

## Aufgabe 2: Fabrik-Datenbank mit JOIN

```python
import sqlite3

verbindung = sqlite3.connect("fabrik_aufgabe.db")
cursor = verbindung.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS hallen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        adresse TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS maschinen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        typ TEXT,
        temperatur REAL,
        hallen_id INTEGER
    )
""")

cursor.execute("INSERT INTO hallen (name, adresse) VALUES ('Halle A', 'Industriestr. 1')")
cursor.execute("INSERT INTO hallen (name, adresse) VALUES ('Halle B', 'Industriestr. 3')")
cursor.execute("INSERT INTO hallen (name, adresse) VALUES ('Halle C', 'Fabrikweg 5')")

cursor.execute("INSERT INTO maschinen (name, typ, temperatur, hallen_id) VALUES ('CNC-01', 'Fräse', 42.5, 1)")
cursor.execute("INSERT INTO maschinen (name, typ, temperatur, hallen_id) VALUES ('CNC-02', 'Fräse', 38.1, 1)")
cursor.execute("INSERT INTO maschinen (name, typ, temperatur, hallen_id) VALUES ('ROBO-01', 'Roboter', 55.0, 2)")
cursor.execute("INSERT INTO maschinen (name, typ, temperatur, hallen_id) VALUES ('LASER-01', 'Laser', 28.0, 3)")
cursor.execute("INSERT INTO maschinen (name, typ, temperatur, hallen_id) VALUES ('ROBO-02', 'Roboter', 60.0, 2)")

verbindung.commit()

# JOIN-Abfrage
cursor.execute("""
    SELECT maschinen.name, maschinen.typ, maschinen.temperatur, hallen.name
    FROM maschinen
    JOIN hallen ON maschinen.hallen_id = hallen.id
""")

print("Alle Maschinen mit Halle:")
for zeile in cursor.fetchall():
    print(f"  {zeile[0]} ({zeile[1]}) | {zeile[2]}°C | {zeile[3]}")

# Heiße Maschinen
cursor.execute("""
    SELECT maschinen.name, maschinen.temperatur, hallen.name
    FROM maschinen
    JOIN hallen ON maschinen.hallen_id = hallen.id
    WHERE maschinen.temperatur > 40
""")

print("\nHeiße Maschinen:")
for zeile in cursor.fetchall():
    print(f"  {zeile[0]}: {zeile[1]}°C in {zeile[2]}")

verbindung.close()
```

---

## Aufgabe 3: Datenbank-Detektiv

```python
import sqlite3

verbindung = sqlite3.connect("detektiv.db")
cursor = verbindung.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS hallen (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS maschinen (id INTEGER PRIMARY KEY, name TEXT, typ TEXT, temperatur REAL, hallen_id INTEGER)")

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

# Frage 1: Maschinen pro Halle
cursor.execute("""
    SELECT hallen.name, COUNT(*) as anzahl
    FROM maschinen
    JOIN hallen ON maschinen.hallen_id = hallen.id
    GROUP BY hallen.name
""")
print("Maschinen pro Halle:")
for zeile in cursor.fetchall():
    print(f"  {zeile[0]}: {zeile[1]} Maschinen")

# Frage 2: Durchschnittstemperatur pro Halle
cursor.execute("""
    SELECT hallen.name, AVG(maschinen.temperatur) as durchschnitt
    FROM maschinen
    JOIN hallen ON maschinen.hallen_id = hallen.id
    GROUP BY hallen.name
""")
print("\nDurchschnittstemperatur pro Halle:")
for zeile in cursor.fetchall():
    print(f"  {zeile[0]}: {zeile[1]:.1f}°C")

# Frage 3: Heißeste Maschine
cursor.execute("""
    SELECT maschinen.name, maschinen.temperatur, hallen.name
    FROM maschinen
    JOIN hallen ON maschinen.hallen_id = hallen.id
    ORDER BY maschinen.temperatur DESC
    LIMIT 1
""")
zeile = cursor.fetchone()
print(f"\nHeißeste Maschine: {zeile[0]} mit {zeile[1]}°C in {zeile[2]}")

verbindung.close()
```

### Bonus: Wartungs-Tabelle

```python
import sqlite3

verbindung = sqlite3.connect("detektiv.db")
cursor = verbindung.cursor()

# Wartungs-Tabelle erstellen
cursor.execute("""
    CREATE TABLE IF NOT EXISTS wartungen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        maschinen_id INTEGER,
        datum TEXT,
        beschreibung TEXT
    )
""")

# Wartungen einfügen
cursor.execute("INSERT INTO wartungen (maschinen_id, datum, beschreibung) VALUES (1, '2024-01-15', 'Ölwechsel')")
cursor.execute("INSERT INTO wartungen (maschinen_id, datum, beschreibung) VALUES (1, '2024-06-20', 'Lager getauscht')")
cursor.execute("INSERT INTO wartungen (maschinen_id, datum, beschreibung) VALUES (4, '2024-03-10', 'Software-Update')")
cursor.execute("INSERT INTO wartungen (maschinen_id, datum, beschreibung) VALUES (7, '2024-05-01', 'Linse gereinigt')")
verbindung.commit()

# JOIN über maschinen und wartungen
cursor.execute("""
    SELECT maschinen.name, wartungen.datum, wartungen.beschreibung
    FROM wartungen
    JOIN maschinen ON wartungen.maschinen_id = maschinen.id
    ORDER BY wartungen.datum
""")

print("Wartungsprotokoll:")
for zeile in cursor.fetchall():
    print(f"  {zeile[1]} | {zeile[0]}: {zeile[2]}")

verbindung.close()
```
