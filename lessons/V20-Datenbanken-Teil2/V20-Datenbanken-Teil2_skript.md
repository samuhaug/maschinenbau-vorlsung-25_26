# V20: Daten verknüpfen — Datenbanken Teil 2

> **Lernziele dieser Vorlesung:**
> - Verstehen, warum man Daten auf mehrere Tabellen verteilt
> - Fremdschlüssel (Foreign Keys) kennen
> - JOIN verwenden, um Tabellen zu verknüpfen
> - GROUP BY und COUNT für einfache Statistiken nutzen

---

## Teil 1: Theorie — Warum mehrere Tabellen?

### Das Problem: Doppelte Daten

Eine einzige Tabelle für alles führt zu Wiederholungen:

| id | maschine | typ | halle | halle_adresse | wartung_datum |
|----|---------|-----|-------|---------------|---------------|
| 1 | CNC-01 | Fräse | Halle A | Industriestr. 1 | 2024-01-15 |
| 2 | CNC-02 | Fräse | Halle A | Industriestr. 1 | 2024-02-20 |
| 3 | CNC-01 | Fräse | Halle A | Industriestr. 1 | 2024-03-10 |

**Problem:** "Halle A" und "Industriestr. 1" stehen dreimal drin. Wenn sich die Adresse ändert, muss man jede Zeile einzeln ändern!

### Die Lösung: Zwei Tabellen + Fremdschlüssel

**Tabelle `hallen`:**
| id | name | adresse |
|----|------|---------|
| 1 | Halle A | Industriestr. 1 |
| 2 | Halle B | Industriestr. 3 |

**Tabelle `maschinen`:**
| id | name | typ | hallen_id | temperatur |
|----|------|-----|-----------|------------|
| 1 | CNC-01 | Fräse | 1 | 42.5 |
| 2 | CNC-02 | Fräse | 1 | 38.1 |
| 3 | ROBO-01 | Roboter | 2 | 55.0 |

> **`hallen_id`** ist ein **Fremdschlüssel** — er verweist auf die `id` in der Tabelle `hallen`.

### JOIN: Tabellen zusammenführen

Mit `JOIN` kombiniert man die Daten aus beiden Tabellen:

```sql
SELECT maschinen.name, maschinen.typ, hallen.name
FROM maschinen
JOIN hallen ON maschinen.hallen_id = hallen.id;
```

**Ergebnis:**
| maschinen.name | maschinen.typ | hallen.name |
|-------|-----|---------|
| CNC-01 | Fräse | Halle A |
| CNC-02 | Fräse | Halle A |
| ROBO-01 | Roboter | Halle B |

> **JOIN ON** sagt: "Verbinde Zeilen, bei denen `maschinen.hallen_id = hallen.id`"

### GROUP BY und COUNT: Zusammenfassen

**Wie viele Maschinen stehen in jeder Halle?**

```sql
SELECT hallen.name, COUNT(*) as anzahl
FROM maschinen
JOIN hallen ON maschinen.hallen_id = hallen.id
GROUP BY hallen.name;
```

**Ergebnis:**
| hallen.name | anzahl |
|-------------|--------|
| Halle A | 2 |
| Halle B | 1 |

### Zusammenfassung Theorie

| Konzept | Bedeutung |
|---------|-----------|
| **Fremdschlüssel** | Spalte, die auf eine ID in einer anderen Tabelle verweist |
| **JOIN** | Kombiniert Daten aus zwei Tabellen |
| **ON** | Bedingung, welche Zeilen zusammengehören |
| **GROUP BY** | Gruppiert Ergebnisse (z.B. pro Halle) |
| **COUNT(*)** | Zählt die Zeilen pro Gruppe |

---

## Teil 2: Python-Praxis — JOIN und GROUP BY mit sqlite3

### Zwei Tabellen erstellen

```python
import sqlite3

verbindung = sqlite3.connect("fabrik_v2.db")
cursor = verbindung.cursor()

# Tabelle 1: Hallen
cursor.execute("""
    CREATE TABLE IF NOT EXISTS hallen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        adresse TEXT
    )
""")

# Tabelle 2: Maschinen mit Fremdschlüssel
cursor.execute("""
    CREATE TABLE IF NOT EXISTS maschinen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        typ TEXT,
        temperatur REAL,
        hallen_id INTEGER
    )
""")
verbindung.commit()
```

### Daten einfügen und mit JOIN abfragen

```python
# Hallen einfügen
cursor.execute("INSERT INTO hallen (name, adresse) VALUES ('Halle A', 'Industriestr. 1')")
cursor.execute("INSERT INTO hallen (name, adresse) VALUES ('Halle B', 'Industriestr. 3')")

# Maschinen mit hallen_id einfügen
cursor.execute("INSERT INTO maschinen (name, typ, temperatur, hallen_id) VALUES ('CNC-01', 'Fräse', 42.5, 1)")
cursor.execute("INSERT INTO maschinen (name, typ, temperatur, hallen_id) VALUES ('ROBO-01', 'Roboter', 55.0, 2)")
verbindung.commit()

# JOIN-Abfrage
cursor.execute("""
    SELECT maschinen.name, maschinen.typ, hallen.name
    FROM maschinen
    JOIN hallen ON maschinen.hallen_id = hallen.id
""")

for zeile in cursor.fetchall():
    print(f"{zeile[0]} ({zeile[1]}) → {zeile[2]}")
```

### GROUP BY: Statistik

```python
cursor.execute("""
    SELECT hallen.name, COUNT(*) as anzahl
    FROM maschinen
    JOIN hallen ON maschinen.hallen_id = hallen.id
    GROUP BY hallen.name
""")

for zeile in cursor.fetchall():
    print(f"{zeile[0]}: {zeile[1]} Maschinen")
```

> **Heute neu:** `JOIN ... ON ...`, `GROUP BY`, `COUNT(*)`
