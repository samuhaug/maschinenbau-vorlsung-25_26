# V19: Daten organisieren mit SQL — Datenbanken Teil 1

> **Lernziele dieser Vorlesung:**
> - Verstehen, was eine Datenbank ist und wofür man sie braucht
> - Tabellen, Zeilen und Spalten kennen
> - Die wichtigsten SQL-Befehle: SELECT, INSERT, UPDATE, DELETE
> - Python: Mit `sqlite3` eine Datenbank erstellen und abfragen

---

## Teil 1: Theorie — Was ist eine Datenbank?

### Das Problem: Daten organisieren

Stell dir vor, du verwaltest 500 Maschinen in einer Fabrik. Du brauchst:
- Name, Typ und Standort jeder Maschine
- Letzte Wartung und nächster Termin
- Aktuelle Temperatur und Status

Das alles in eine Excel-Tabelle? Geht — aber wird schnell unübersichtlich und fehleranfällig.

> **Lösung:** Eine Datenbank — professionell, schnell, fehlerfrei.

### Tabellen = Organisierte Daten

Eine Datenbank besteht aus **Tabellen**. Jede Tabelle ist wie eine Excel-Tabelle:

| id | name | typ | standort | temperatur |
|----|------|-----|----------|------------|
| 1 | CNC-01 | Fräse | Halle A | 42.5 |
| 2 | CNC-02 | Fräse | Halle A | 38.1 |
| 3 | ROBO-01 | Roboter | Halle B | 55.0 |

- **Spalten** = Eigenschaften (name, typ, ...)
- **Zeilen** = Einzelne Einträge (eine Maschine pro Zeile)
- **id** = Eindeutige Nummer (Primärschlüssel)

### SQL: Die Sprache für Datenbanken

**SQL** (Structured Query Language) ist die Standardsprache für Datenbanken. Du brauchst nur 4 Befehle:

| SQL-Befehl | Was er tut | Analogie |
|-----------|-----------|----------|
| `SELECT` | Daten abfragen | "Zeig mir alle Maschinen" |
| `INSERT` | Daten einfügen | "Neue Maschine hinzufügen" |
| `UPDATE` | Daten ändern | "Temperatur aktualisieren" |
| `DELETE` | Daten löschen | "Maschine entfernen" |

### Die 4 wichtigsten SQL-Befehle

**1. SELECT — Daten abfragen:**
```sql
SELECT * FROM maschinen;                          -- Alle Maschinen
SELECT name, temperatur FROM maschinen;            -- Nur Name und Temperatur
SELECT * FROM maschinen WHERE temperatur > 40;     -- Nur heiße Maschinen
```

**2. INSERT — Neue Daten einfügen:**
```sql
INSERT INTO maschinen (name, typ, standort, temperatur)
VALUES ('LASER-01', 'Laser', 'Halle C', 28.0);
```

**3. UPDATE — Daten ändern:**
```sql
UPDATE maschinen SET temperatur = 45.0 WHERE name = 'CNC-01';
```

**4. DELETE — Daten löschen:**
```sql
DELETE FROM maschinen WHERE name = 'CNC-02';
```

> **Wichtig:** `WHERE` filtert die Zeilen. Ohne `WHERE` betrifft der Befehl ALLE Zeilen!

---

## Teil 2: Python-Praxis — sqlite3

### SQLite: Eine Datenbank in einer Datei

**SQLite** ist eine einfache Datenbank, die alles in einer einzigen Datei speichert. Python hat `sqlite3` eingebaut — keine Installation nötig!

### Datenbank erstellen und Tabelle anlegen

```python
import sqlite3

# Verbindung zur Datenbank (wird automatisch erstellt)
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

verbindung.commit()  # Änderungen speichern
print("Tabelle erstellt!")
```

### Daten einfügen

```python
cursor.execute("""
    INSERT INTO maschinen (name, typ, standort, temperatur)
    VALUES ('CNC-01', 'Fräse', 'Halle A', 42.5)
""")
verbindung.commit()
print("Maschine hinzugefügt!")
```

### Daten abfragen

```python
cursor.execute("SELECT * FROM maschinen")
ergebnisse = cursor.fetchall()

for zeile in ergebnisse:
    print(zeile)
# (1, 'CNC-01', 'Fräse', 'Halle A', 42.5)
```

### Verbindung schließen

```python
verbindung.close()
```

### Das Grundmuster (immer gleich!)

```python
import sqlite3

# 1. Verbinden
verbindung = sqlite3.connect("meine_datenbank.db")
cursor = verbindung.cursor()

# 2. SQL ausführen
cursor.execute("SELECT * FROM tabelle")
ergebnisse = cursor.fetchall()

# 3. Ergebnisse nutzen
for zeile in ergebnisse:
    print(zeile)

# 4. Schließen
verbindung.close()
```

> **Heute neu:** `sqlite3.connect()`, `cursor.execute()`, `cursor.fetchall()`, `verbindung.commit()`
