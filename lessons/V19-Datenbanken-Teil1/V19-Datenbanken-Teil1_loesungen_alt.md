# V19 – Datenbanken – Teil 1: Lösungen

---

## 📚 Theorie-Lösungen

### T1: Entity-Relationship-Modellierung

**a) Kardinalität**

Die Beziehung zwischen Werkstücken und Maschinen ist **n:m (many-to-many)**.

> [!NOTE]
> **Begründung**: Laut Aufgabenstellung kann "jede Maschine mehrere Werkstücktypen bearbeiten" (1:n von Maschine zu Werkstück) **und** "jedes Werkstück kann auf mehreren Maschinen gefertigt werden" (1:n von Werkstück zu Maschine). Die Kombination zweier 1:n-Beziehungen ergibt eine n:m-Beziehung.

**b) Tabellenschema**

```sql
CREATE TABLE Werkstuecke (
    Werkstueck_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Bezeichnung TEXT NOT NULL,
    Materialnummer TEXT NOT NULL,
    Gewicht_kg REAL CHECK (Gewicht_kg > 0),
    Zielstueckzahl_pro_Monat INTEGER CHECK (Zielstueckzahl_pro_Monat > 0)
);

CREATE TABLE Maschinen (
    Maschinen_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Maschinentyp TEXT NOT NULL,
    Baujahr INTEGER CHECK (Baujahr >= 1900 AND Baujahr <= 2100),
    Standort TEXT NOT NULL,
    Max_Betriebsstunden_pro_Tag REAL CHECK (Max_Betriebsstunden_pro_Tag > 0 AND Max_Betriebsstunden_pro_Tag <= 24)
);

CREATE TABLE Produktionsauftraege (
    Auftrags_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Werkstueck_ID INTEGER NOT NULL,
    Maschinen_ID INTEGER NOT NULL,
    Auftragsdatum TEXT NOT NULL,  -- ISO-Format: YYYY-MM-DD
    Produzierte_Stueckzahl INTEGER CHECK (Produzierte_Stueckzahl >= 0),
    Tatsaechliche_Betriebsstunden REAL CHECK (Tatsaechliche_Betriebsstunden >= 0),
    Ausschussrate_Prozent REAL CHECK (Ausschussrate_Prozent >= 0 AND Ausschussrate_Prozent <= 100),
    FOREIGN KEY (Werkstueck_ID) REFERENCES Werkstuecke(Werkstueck_ID),
    FOREIGN KEY (Maschinen_ID) REFERENCES Maschinen(Maschinen_ID)
);
```

> [!TIP]
> **Constraints-Erklärung**:
> - `PRIMARY KEY AUTOINCREMENT`: Auto-inkrementierende ID als Primärschlüssel
> - `NOT NULL`: Wert muss angegeben werden (Pflichtfeld)
> - `CHECK (...)`: Validierungsbedingung (z.B. Gewicht > 0, Betriebsstunden ≤ 24h)
> - `FOREIGN KEY`: Referenzielle Integrität zur Eltern-Tabelle

**c) Normalisierung (3NF-Prüfung)**

Das Schema erfüllt **3NF**:

1. **1NF (Erste Normalform)**: ✅ Alle Attribute sind atomar (keine Listen/Arrays in Zellen)
2. **2NF (Zweite Normalform)**: ✅ Keine partiellen Abhängigkeiten (alle Nicht-Schlüssel-Attribute sind vollständig vom Primärschlüssel abhängig)
3. **3NF (Dritte Normalform)**: ✅ Keine transitiven Abhängigkeiten (kein Nicht-Schlüssel-Attribut ist von anderem Nicht-Schlüssel-Attribut abhängig)

> [!NOTE]
> **Potenzielle Redundanz**: In `Produktionsauftraege` könnten theoretisch Materialnummer/Gewicht redundant gespeichert werden, wenn man sie denormalisiert. Das ist aber hier nicht der Fall – alle Werkstück-Details stehen nur in `Werkstuecke`.

**d) Beispiel-INSERT-Statements**

```sql
-- Werkstück einfügen
INSERT INTO Werkstuecke (Bezeichnung, Materialnummer, Gewicht_kg, Zielstueckzahl_pro_Monat)
VALUES ('Zahnrad Z24', 'M-1234', 2.5, 500);

-- Maschine einfügen
INSERT INTO Maschinen (Maschinentyp, Baujahr, Standort, Max_Betriebsstunden_pro_Tag)
VALUES ('CNC-Drehmaschine Index G220', 2019, 'Halle 3', 20.0);

-- Produktionsauftrag einfügen (IDs 1 und 1 annehmen)
INSERT INTO Produktionsauftraege (Werkstueck_ID, Maschinen_ID, Auftragsdatum, Produzierte_Stueckzahl, Tatsaechliche_Betriebsstunden, Ausschussrate_Prozent)
VALUES (1, 1, '2024-03-15', 120, 8.5, 2.5);
```

> [!WARNING]
> **Wichtig**: Die Reihenfolge ist entscheidend! Erst `Werkstuecke` und `Maschinen` einfügen (Eltern-Tabellen), dann `Produktionsauftraege` (Kind-Tabelle mit Fremdschlüsseln).

---

### T2: SQL-Abfragen formulieren

**a) Abweichungsberechnung**

```sql
SELECT
    m.Mess_ID,
    b.Bezeichnung AS Bauteil,
    b.Sollmasse_mm,
    m.Istmasse_mm,
    ABS(m.Istmasse_mm - b.Sollmasse_mm) AS Abweichung_mm
FROM Messungen m
JOIN Bauteile b ON m.Bauteil_ID = b.Bauteil_ID
ORDER BY Abweichung_mm DESC;
```

**Erwartete Ausgabe (Auszug):**
```
Mess_ID | Bauteil      | Sollmasse_mm | Istmasse_mm | Abweichung_mm
--------|--------------|--------------|-------------|---------------
4       | Flansch F-90 | 220.00       | 220.15      | 0.15
2       | Welle W-42   | 150.00       | 150.07      | 0.07
1       | Welle W-42   | 150.00       | 150.02      | 0.02
5       | Welle W-42   | 150.00       | 149.98      | 0.02
3       | Buchse B-18  | 25.00        | 24.99       | 0.01
```

**b) Ausschuss-Identifikation**

```sql
SELECT
    m.Mess_ID,
    b.Bezeichnung AS Bauteil,
    b.Sollmasse_mm,
    m.Istmasse_mm,
    ABS(m.Istmasse_mm - b.Sollmasse_mm) AS Abweichung_mm,
    b.Toleranz_mm,
    'AUSSCHUSS' AS Status
FROM Messungen m
JOIN Bauteile b ON m.Bauteil_ID = b.Bauteil_ID
WHERE ABS(m.Istmasse_mm - b.Sollmasse_mm) > b.Toleranz_mm
ORDER BY Abweichung_mm DESC;
```

**Erwartete Ausgabe:**
```
Mess_ID | Bauteil      | Sollmasse_mm | Istmasse_mm | Abweichung_mm | Toleranz_mm | Status
--------|--------------|--------------|-------------|---------------|-------------|--------
4       | Flansch F-90 | 220.00       | 220.15      | 0.15          | 0.10        | AUSSCHUSS
2       | Welle W-42   | 150.00       | 150.07      | 0.07          | 0.05        | AUSSCHUSS
```

**c) Aggregation nach Bauteil**

```sql
SELECT
    b.Bezeichnung AS Bauteil,
    COUNT(*) AS Anzahl_Messungen,
    AVG(m.Istmasse_mm) AS Durchschnitt_Istmasse_mm,
    MIN(m.Istmasse_mm) AS Min_Istmasse_mm,
    MAX(m.Istmasse_mm) AS Max_Istmasse_mm,
    SUM(CASE WHEN ABS(m.Istmasse_mm - b.Sollmasse_mm) > b.Toleranz_mm THEN 1 ELSE 0 END) AS Anzahl_Ausschuss
FROM Messungen m
JOIN Bauteile b ON m.Bauteil_ID = b.Bauteil_ID
GROUP BY b.Bauteil_ID, b.Bezeichnung
ORDER BY Anzahl_Messungen DESC;
```

> [!NOTE]
> **CASE WHEN**: Zählt nur Messungen, bei denen die Abweichung die Toleranz überschreitet. `SUM(CASE WHEN ... THEN 1 ELSE 0 END)` ist ein Idiom zum konditionalen Zählen.

**Erwartete Ausgabe:**
```
Bauteil      | Anzahl_Messungen | Durchschnitt_Istmasse_mm | Min_Istmasse_mm | Max_Istmasse_mm | Anzahl_Ausschuss
-------------|------------------|--------------------------|-----------------|-----------------|------------------
Welle W-42   | 3                | 150.0233                 | 149.98          | 150.07          | 1
Flansch F-90 | 1                | 220.15                   | 220.15          | 220.15          | 1
Buchse B-18  | 1                | 24.99                    | 24.99           | 24.99           | 0
```

**d) Prüfgeräte-Analyse**

```sql
SELECT
    Pruefgeraet,
    COUNT(*) AS Anzahl_Messungen
FROM Messungen
GROUP BY Pruefgeraet
HAVING COUNT(*) > 1
ORDER BY Anzahl_Messungen DESC;
```

**Erwartete Ausgabe:**
```
Pruefgeraet     | Anzahl_Messungen
----------------|------------------
Messschieber-A1 | 3
```

> [!TIP]
> **HAVING vs. WHERE**: `WHERE` filtert Zeilen vor der Gruppierung, `HAVING` filtert Gruppen nach der Aggregation. Hier benötigen wir `HAVING`, weil wir auf `COUNT(*)` filtern.

---

### T3: Datenbankdesign-Entscheidungen

**Frage 1**

**Korrekte Antwort: d) `Email TEXT NOT NULL UNIQUE`**

> [!NOTE]
> **Begründung**:
> - `NOT NULL`: Jeder Mitarbeiter **muss** eine E-Mail haben (Pflichtfeld)
> - `UNIQUE`: Keine zwei Mitarbeiter dürfen dieselbe E-Mail haben (Eindeutigkeit)
> - Beide Constraints sind notwendig: `NOT NULL` verhindert leere Werte, `UNIQUE` verhindert Duplikate

**Falsche Antworten**:
- a) Erlaubt `NULL` und Duplikate
- b) Erlaubt Duplikate (mehrere Mitarbeiter mit derselben E-Mail)
- c) Erlaubt `NULL` (Mitarbeiter ohne E-Mail)

---

**Frage 2**

**Korrekte Antwort: a) `CREATE INDEX` auf `Sensor_ID` und separaten Index auf `Zeitstempel`**

> [!NOTE]
> **Begründung**:
> - **Separate Indizes** erlauben dem Query Optimizer, je nach Query den passenden Index zu wählen
> - Bei Abfragen nur nach `Sensor_ID` wird nur dieser Index verwendet
> - Bei Abfragen nur nach `Zeitstempel` wird nur dieser Index verwendet
> - Bei Abfragen nach beiden kann der Optimizer einen Index wählen oder Index Merge verwenden

**Falsche Antworten**:
- b) **Kombinierter Index** `(Sensor_ID, Zeitstempel)` ist nur effizient bei Queries, die **beide** Spalten in dieser Reihenfolge filtern. Bei Abfragen nur nach `Zeitstempel` wird der Index nicht verwendet (Left-Prefix Rule).
- c) Keine Indizes verlangsamen SELECTs drastisch (10.000 INSERTs/Sekunde sind performant genug)
- d) Normalisierung hat nichts mit Indizes zu tun

> [!WARNING]
> **Trade-off**: Indizes verlangsamen INSERTs minimal (ca. 5-15%), aber beschleunigen SELECTs um Faktor 100-1000. Bei 10.000 INSERTs/Sekunde ist das vertretbar.

---

**Frage 3**

**Korrekte Antwort: c) n:m – Junction Table mit zwei Fremdschlüsseln**

> [!NOTE]
> **Begründung**:
> - **n:m-Beziehung**: Ein Auftrag kann mehrere Werkstücke enthalten **und** ein Werkstück kann in mehreren Aufträgen vorkommen
> - **Junction Table** (auch: Assoziationstabelle, Join-Table) ist das Standard-Implementierungsmuster:
>   ```sql
>   CREATE TABLE Auftrag_Werkstueck (
>       Auftrag_ID INTEGER,
>       Werkstueck_ID INTEGER,
>       Menge INTEGER,
>       PRIMARY KEY (Auftrag_ID, Werkstueck_ID),
>       FOREIGN KEY (Auftrag_ID) REFERENCES Auftraege(Auftrag_ID),
>       FOREIGN KEY (Werkstueck_ID) REFERENCES Werkstuecke(Werkstueck_ID)
>   );
>   ```

**JSON-Speicherung (Antwort d):**
- **Vorteil**: Weniger Tabellen, einfacheres Schema
- **Nachteile**:
  - Keine referenzielle Integrität (FOREIGN KEY Constraints funktionieren nicht)
  - Schwierig zu querien (JSON-Funktionen notwendig, keine Standard-SQL-JOINs)
  - Verletzt Normalisierung (Redundanz)
  - Performance-Probleme bei großen Arrays

> [!TIP]
> **Faustregel**: JSON nur für Daten ohne Beziehungen verwenden (z.B. Konfigurationsdaten, Metadaten). Für relationale Daten immer Junction Table bevorzugen.

---

## 🐍 Python-Lösungen

### P1: Temperatur-Monitoring-System

**Datei: `loesungen/aufgabe_p1.py`**

```python
import sqlite3
import csv
from datetime import datetime

DB_NAME = 'kuehlueberwachung.db'

def erstelle_datenbank():
    """Erstellt Datenbank und Tabellen falls nicht vorhanden."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Tabelle Kuehlschraenke
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Kuehlschraenke (
            Kuehlschrank_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Bezeichnung TEXT NOT NULL,
            Standort TEXT NOT NULL,
            Soll_Temperatur_Celsius REAL NOT NULL,
            Toleranz_Celsius REAL DEFAULT 2.0,
            Aktiv INTEGER DEFAULT 1
        )
    ''')
    
    # Tabelle Temperaturmessungen
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Temperaturmessungen (
            Mess_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Kuehlschrank_ID INTEGER NOT NULL,
            Zeitstempel TEXT NOT NULL,
            Temperatur_Celsius REAL NOT NULL,
            Alarm INTEGER DEFAULT 0,
            FOREIGN KEY (Kuehlschrank_ID) REFERENCES Kuehlschraenke(Kuehlschrank_ID)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Datenbank und Tabellen erstellt")

def initialisiere_kuehlschraenke():
    """Fügt Kühlschränke ein."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    kuehlschraenke = [
        ("Kühlraum A1", "Produktionshalle 1", 4.0, 1.5),
        ("Gefrierschrank B2", "Lager Gebäude 2", -18.0, 3.0),
        ("Kühlzelle C3", "Versandhalle", 2.0, 1.0)
    ]
    
    cursor.executemany('''
        INSERT INTO Kuehlschraenke (Bezeichnung, Standort, Soll_Temperatur_Celsius, Toleranz_Celsius)
        VALUES (?, ?, ?, ?)
    ''', kuehlschraenke)
    
    conn.commit()
    conn.close()
    print(f"✅ {len(kuehlschraenke)} Kühlschränke eingefügt")

def importiere_messwerte(csv_datei='testdaten/temperaturmessungen.csv'):
    """Importiert Messwerte aus CSV und berechnet Alarm-Flag."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Kühlschrank-Daten abrufen
    cursor.execute('SELECT Kuehlschrank_ID, Soll_Temperatur_Celsius, Toleranz_Celsius FROM Kuehlschraenke')
    kuehlschraenke = {row[0]: (row[1], row[2]) for row in cursor.fetchall()}
    
    with open(csv_datei, 'r', encoding='utf-8') as datei:
        reader = csv.DictReader(datei)
        messungen = []
        
        for zeile in reader:
            kuehl_id = int(zeile['Kuehlschrank_ID'])
            zeitstempel = zeile['Zeitstempel']
            temperatur = float(zeile['Temperatur_Celsius'])
            
            # Alarm berechnen
            soll_temp, toleranz = kuehlschraenke[kuehl_id]
            abweichung = abs(temperatur - soll_temp)
            alarm = 1 if abweichung > toleranz else 0
            
            messungen.append((kuehl_id, zeitstempel, temperatur, alarm))
    
    cursor.executemany('''
        INSERT INTO Temperaturmessungen (Kuehlschrank_ID, Zeitstempel, Temperatur_Celsius, Alarm)
        VALUES (?, ?, ?, ?)
    ''', messungen)
    
    conn.commit()
    conn.close()
    print(f"✅ {len(messungen)} Messwerte importiert")

def alarm_report():
    """Zeigt alle Alarme an."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT k.Bezeichnung, k.Soll_Temperatur_Celsius, k.Toleranz_Celsius,
               m.Zeitstempel, m.Temperatur_Celsius
        FROM Temperaturmessungen m
        JOIN Kuehlschraenke k ON m.Kuehlschrank_ID = k.Kuehlschrank_ID
        WHERE m.Alarm = 1
        ORDER BY m.Zeitstempel DESC
    ''')
    
    print("\n🚨 ALARM-REPORT 🚨")
    print("-" * 80)
    
    for row in cursor:
        soll = row['Soll_Temperatur_Celsius']
        toleranz = row['Toleranz_Celsius']
        ist = row['Temperatur_Celsius']
        status = "ÜBERHITZT" if ist > soll else "ZU WARM" if ist > soll - toleranz else "ZU KALT"
        
        print(f"ALARM: {row['Bezeichnung']} (Soll: {soll}°C ±{toleranz}°C) – "
              f"{row['Zeitstempel']} – IST: {ist}°C [{status}]")
    
    conn.close()

def statistik_pro_kuehlschrank():
    """Berechnet Statistiken pro Kühlschrank."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT k.Bezeichnung,
               COUNT(*) AS Anzahl_Messungen,
               AVG(m.Temperatur_Celsius) AS Durchschnitt,
               MIN(m.Temperatur_Celsius) AS Minimum,
               MAX(m.Temperatur_Celsius) AS Maximum,
               SUM(m.Alarm) AS Anzahl_Alarme,
               ROUND(100.0 * SUM(m.Alarm) / COUNT(*), 2) AS Alarmrate_Prozent
        FROM Temperaturmessungen m
        JOIN Kuehlschraenke k ON m.Kuehlschrank_ID = k.Kuehlschrank_ID
        GROUP BY k.Kuehlschrank_ID, k.Bezeichnung
    ''')
    
    print("\n📊 STATISTIK PRO KÜHLSCHRANK")
    print("=" * 80)
    
    for row in cursor:
        print(f"\n{row['Bezeichnung']}")
        print(f"  Anzahl Messungen: {row['Anzahl_Messungen']}")
        print(f"  Ø Temperatur: {row['Durchschnitt']:.2f}°C")
        print(f"  Min/Max: {row['Minimum']}°C / {row['Maximum']}°C")
        print(f"  Anzahl Alarme: {row['Anzahl_Alarme']}")
        print(f"  Alarmrate: {row['Alarmrate_Prozent']}%")
    
    conn.close()

if __name__ == '__main__':
    print("🔧 Temperatur-Monitoring-System")
    print("=" * 80)
    
    erstelle_datenbank()
    initialisiere_kuehlschraenke()
    importiere_messwerte()
    alarm_report()
    statistik_pro_kuehlschrank()
```

---

### P2: Werkstoff-Prüfdatenbank mit JOINs

**Datei: `loesungen/aufgabe_p2.py`** (Auszug)

```python
import sqlite3
import csv

DB_NAME = 'werkstoffpruefung.db'

def erstelle_datenbank():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Werkstoffe (
        Werkstoff_ID INTEGER PRIMARY KEY,
        Bezeichnung TEXT NOT NULL,
        Werkstoffnummer TEXT UNIQUE NOT NULL,
        Dichte_g_cm3 REAL,
        E_Modul_GPa REAL
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Proben (
        Proben_ID INTEGER PRIMARY KEY,
        Werkstoff_ID INTEGER NOT NULL,
        Probendurchmesser_mm REAL NOT NULL,
        Probenlaenge_mm REAL NOT NULL,
        Herstellungsdatum TEXT,
        FOREIGN KEY (Werkstoff_ID) REFERENCES Werkstoffe(Werkstoff_ID)
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Zugversuche (
        Versuchs_ID INTEGER PRIMARY KEY,
        Proben_ID INTEGER NOT NULL,
        Versuchsdatum TEXT NOT NULL,
        Streckgrenze_MPa REAL,
        Zugfestigkeit_MPa REAL,
        Bruchdehnung_Prozent REAL,
        Pruefgeraet TEXT NOT NULL,
        FOREIGN KEY (Proben_ID) REFERENCES Proben(Proben_ID)
    )''')
    
    conn.commit()
    conn.close()

def importiere_csv(tabelle, csv_datei):
    """Generische CSV-Import-Funktion."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    with open(csv_datei, 'r', encoding='utf-8') as datei:
        reader = csv.DictReader(datei)
        spalten = reader.fieldnames
        platzhalter = ', '.join(['?'] * len(spalten))
        
        zeilen = []
        for zeile in reader:
            werte = [zeile[spalte] for spalte in spalten]
            zeilen.append(tuple(werte))
        
        cursor.executemany(f'INSERT INTO {tabelle} VALUES ({platzhalter})', zeilen)
    
    conn.commit()
    conn.close()
    print(f"✅ {len(zeilen)} Zeilen in {tabelle} eingefügt")

def vollstaendige_versuchsdaten():
    """JOIN-Query: Alle Versuchsdaten mit Werkstoff-Info."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT z.Versuchs_ID, z.Versuchsdatum,
               w.Bezeichnung AS Werkstoff, w.Werkstoffnummer,
               p.Probendurchmesser_mm,
               z.Streckgrenze_MPa, z.Zugfestigkeit_MPa, z.Bruchdehnung_Prozent,
               z.Pruefgeraet
        FROM Zugversuche z
        INNER JOIN Proben p ON z.Proben_ID = p.Proben_ID
        INNER JOIN Werkstoffe w ON p.Werkstoff_ID = w.Werkstoff_ID
        ORDER BY z.Versuchs_ID
    ''')
    
    print("\n📋 Vollständige Versuchsdaten (mit JOINs)")
    print("=" * 100)
    
    for row in cursor:
        print(f"Versuch {row['Versuchs_ID']:3d} | {row['Versuchsdatum']} | {row['Werkstoff']:20s} ({row['Werkstoffnummer']}) | "
              f"Ø {row['Probendurchmesser_mm']:4.1f}mm | Re={row['Streckgrenze_MPa']:6.1f} MPa | "
              f"Rm={row['Zugfestigkeit_MPa']:6.1f} MPa | A={row['Bruchdehnung_Prozent']:5.1f}% | {row['Pruefgeraet']}")
    
    conn.close()

def durchschnittswerte_pro_werkstoff():
    """Aggregation: Durchschnittswerte gruppiert nach Werkstoff."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT w.Bezeichnung, w.Werkstoffnummer,
               COUNT(*) AS Anzahl_Versuche,
               AVG(z.Streckgrenze_MPa) AS Avg_Streckgrenze,
               AVG(z.Zugfestigkeit_MPa) AS Avg_Zugfestigkeit,
               AVG(z.Bruchdehnung_Prozent) AS Avg_Bruchdehnung
        FROM Zugversuche z
        JOIN Proben p ON z.Proben_ID = p.Proben_ID
        JOIN Werkstoffe w ON p.Werkstoff_ID = w.Werkstoff_ID
        GROUP BY w.Werkstoff_ID, w.Bezeichnung, w.Werkstoffnummer
        ORDER BY Anzahl_Versuche DESC
    ''')
    
    print("\n📊 Durchschnittswerte pro Werkstoff")
    print("=" * 100)
    
    for row in cursor:
        print(f"\nWerkstoff: {row['Bezeichnung']} (Werkstoffnummer {row['Werkstoffnummer']})")
        print(f"  Anzahl Versuche: {row['Anzahl_Versuche']}")
        print(f"  Ø Streckgrenze: {row['Avg_Streckgrenze']:.1f} MPa")
        print(f"  Ø Zugfestigkeit: {row['Avg_Zugfestigkeit']:.1f} MPa")
        print(f"  Ø Bruchdehnung: {row['Avg_Bruchdehnung']:.1f}%")
    
    conn.close()

if __name__ == '__main__':
    erstelle_datenbank()
    importiere_csv('Werkstoffe', 'testdaten/werkstoffe.csv')
    importiere_csv('Proben', 'testdaten/proben.csv')
    importiere_csv('Zugversuche', 'testdaten/zugversuche.csv')
    vollstaendige_versuchsdaten()
    durchschnittswerte_pro_werkstoff()
```

---

### P3: Fertigungsauftragsverwaltung (Transaktionen)

**Datei: `loesungen/aufgabe_p3.py`** (Auszug – Fokus auf Transaktionen)

```python
import sqlite3
import json

DB_NAME = 'fertigungsauftraege.db'

# ... (Tabellenerstellung wie in P1/P2) ...

def material_buchen(auftrags_id, material_id, menge_kg):
    """Bucht Material mit Transaktion (Atomicity)."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        # 1. Prüfen ob genug Material vorhanden
        cursor.execute('SELECT Lagerbestand_kg FROM Materialbestand WHERE Material_ID = ?', (material_id,))
        row = cursor.fetchone()
        
        if not row:
            raise ValueError(f"Material-ID {material_id} existiert nicht")
        
        lagerbestand = row[0]
        
        if lagerbestand < menge_kg:
            raise ValueError(f"Nicht genug Material im Lager (Bestand: {lagerbestand} kg, benötigt: {menge_kg} kg)")
        
        # 2. Lagerbestand reduzieren
        cursor.execute('''
            UPDATE Materialbestand
            SET Lagerbestand_kg = Lagerbestand_kg - ?
            WHERE Material_ID = ?
        ''', (menge_kg, material_id))
        
        # 3. Buchung eintragen
        cursor.execute('''
            INSERT INTO Materialbuchungen (Auftrags_ID, Material_ID, Menge_kg, Buchungsdatum)
            VALUES (?, ?, ?, DATE('now'))
        ''', (auftrags_id, material_id, menge_kg))
        
        # Commit: Beide Operationen erfolgreich
        conn.commit()
        print(f"✅ Material erfolgreich gebucht: {menge_kg} kg von Material-ID {material_id}")
        
    except ValueError as e:
        # Rollback: Bei Fehler alle Änderungen rückgängig machen
        conn.rollback()
        print(f"❌ Fehler: {e}")
        raise
    
    except sqlite3.IntegrityError as e:
        conn.rollback()
        print(f"❌ Datenbankfehler: {e}")
        raise
    
    finally:
        conn.close()

def testfall_transaktion():
    """Testfall: Versuche, mehr Material zu buchen als vorhanden."""
    print("\n🧪 TESTFALL: Transaktion mit zu wenig Lagerbestand")
    print("-" * 80)
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Vorher-Zustand
    cursor.execute('SELECT Lagerbestand_kg FROM Materialbestand WHERE Material_ID = 1')
    bestand_vorher = cursor.fetchone()[0]
    print(f"Lagerbestand vorher (Material-ID 1): {bestand_vorher} kg")
    
    # Versuch, 1000 kg zu buchen (mehr als vorhanden)
    try:
        material_buchen(auftrags_id=1, material_id=1, menge_kg=1000.0)
    except ValueError:
        print("✅ Exception korrekt geworfen")
    
    # Nachher-Zustand (sollte unverändert sein)
    cursor.execute('SELECT Lagerbestand_kg FROM Materialbestand WHERE Material_ID = 1')
    bestand_nachher = cursor.fetchone()[0]
    print(f"Lagerbestand nachher: {bestand_nachher} kg")
    
    if bestand_vorher == bestand_nachher:
        print("✅ Transaktion erfolgreich zurückgerollt (Rollback)")
    else:
        print("❌ FEHLER: Lagerbestand wurde verändert (kein Rollback!)")
    
    conn.close()

if __name__ == '__main__':
    # ... Setup ...
    testfall_transaktion()
```

> [!NOTE]
> **Transaktion**: Die Kombination aus `cursor.execute()` (UPDATE + INSERT) in einem `try`-Block mit `conn.commit()` bei Erfolg und `conn.rollback()` bei Fehler garantiert **Atomicity** (ACID). Entweder werden beide Operationen ausgeführt oder keine.

---

### P4: Sensor-Datenbank mit pandas

**Datei: `loesungen/aufgabe_p4.py`** (Auszug – Fokus auf pandas + matplotlib)

```python
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

DB_NAME = 'sensor_datenbank.db'

def export_zu_pandas(sensor_id):
    """Exportiert Sensordaten als pandas DataFrame."""
    conn = sqlite3.connect(DB_NAME)
    
    query = '''
        SELECT s.Sensorname, s.Einheit, m.Zeitstempel, m.Wert
        FROM Sensormesswerte m
        JOIN Sensoren s ON m.Sensor_ID = s.Sensor_ID
        WHERE m.Sensor_ID = ?
        ORDER BY m.Zeitstempel
    '''
    
    df = pd.read_sql_query(query, conn, params=(sensor_id,))
    
    # Zeitstempel als datetime konvertieren
    df['Zeitstempel'] = pd.to_datetime(df['Zeitstempel'])
    
    conn.close()
    return df

def zeitreihen_plot(sensor_id):
    """Erstellt Zeitreihen-Plot mit Min/Max/Durchschnitt."""
    df = export_zu_pandas(sensor_id)
    
    if df.empty:
        print(f"Keine Daten für Sensor-ID {sensor_id}")
        return
    
    sensorname = df['Sensorname'].iloc[0]
    einheit = df['Einheit'].iloc[0]
    
    # Statistiken berechnen
    mittelwert = df['Wert'].mean()
    minimum = df['Wert'].min()
    maximum = df['Wert'].max()
    
    # Plot erstellen
    plt.figure(figsize=(12, 6))
    plt.plot(df['Zeitstempel'], df['Wert'], 'o-', label='Messwerte', linewidth=2, markersize=5)
    
    # Horizontale Linien für Statistiken
    plt.axhline(y=mittelwert, color='green', linestyle='--', linewidth=2, label=f'Mittelwert ({mittelwert:.2f} {einheit})')
    plt.axhline(y=minimum, color='blue', linestyle=':', linewidth=1.5, label=f'Minimum ({minimum:.2f} {einheit})')
    plt.axhline(y=maximum, color='red', linestyle=':', linewidth=1.5, label=f'Maximum ({maximum:.2f} {einheit})')
    
    plt.xlabel('Zeitstempel', fontsize=12)
    plt.ylabel(f'Wert ({einheit})', fontsize=12)
    plt.title(f'Zeitreihe: {sensorname}', fontsize=14, fontweight='bold')
    plt.legend(loc='best')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'zeitreihe_sensor_{sensor_id}.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"✅ Plot gespeichert: zeitreihe_sensor_{sensor_id}.png")

def anomalie_detektion(sensor_id):
    """Erkennt Anomalien (> 2 Standardabweichungen)."""
    df = export_zu_pandas(sensor_id)
    
    mittelwert = df['Wert'].mean()
    std_abweichung = df['Wert'].std()
    
    # Anomalien identifizieren
    df['Anomalie'] = np.abs(df['Wert'] - mittelwert) > (2 * std_abweichung)
    anomalien = df[df['Anomalie']]
    
    print(f"\n🔍 Anomalie-Detektion für {df['Sensorname'].iloc[0]}")
    print(f"  Mittelwert: {mittelwert:.2f} {df['Einheit'].iloc[0]}")
    print(f"  Standardabweichung: {std_abweichung:.2f} {df['Einheit'].iloc[0]}")
    print(f"  Anomalien erkannt: {len(anomalien)} (von {len(df)} Messungen)")
    
    if not anomalien.empty:
        print("\n  Zeitpunkte:")
        for _, row in anomalien.iterrows():
            print(f"    {row['Zeitstempel']}: {row['Wert']:.2f} {row['Einheit']}")
    
    # Scatter-Plot
    plt.figure(figsize=(12, 6))
    normal = df[~df['Anomalie']]
    plt.scatter(normal['Zeitstempel'], normal['Wert'], c='blue', label='Normal', s=50, alpha=0.7)
    plt.scatter(anomalien['Zeitstempel'], anomalien['Wert'], c='red', label='Anomalie', s=100, marker='X')
    
    plt.xlabel('Zeitstempel', fontsize=12)
    plt.ylabel(f'Wert ({df["Einheit"].iloc[0]})', fontsize=12)
    plt.title(f'Anomalie-Detektion: {df["Sensorname"].iloc[0]}', fontsize=14, fontweight='bold')
    plt.legend(loc='best')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'anomalien_sensor_{sensor_id}.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    # ... Setup ...
    zeitreihen_plot(sensor_id=1)
    anomalie_detektion(sensor_id=3)
```

> [!TIP]
> **pandas Integration**: `pd.read_sql_query()` lädt SQL-Ergebnisse direkt in DataFrame. Zeitreihen-Operationen wie `.rolling()` (gleitender Durchschnitt) sind einfach: `df['Wert'].rolling(window=10).mean()`.

---

### P5: Produktionsplanungs-Tool (CSV-Export)

**Datei: `loesungen/aufgabe_p5.py`** (Auszug – Fokus auf komplexen JOIN + CSV-Export)

```python
import sqlite3
import csv
import xml.etree.ElementTree as ET

DB_NAME = 'produktionsplanung.db'

def produktionsplan_report():
    """Komplexer JOIN für Produktionsplan-Report."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT pa.Auftrag_ID,
               p.Produktname,
               pa.Stueckzahl AS Geplante_Stueckzahl,
               pa.Prioritaet,
               pa.Zieltermin,
               pa.Status,
               COUNT(mb.Belegungs_ID) AS Anzahl_Maschinenbelegungen,
               COALESCE(SUM(mb.Tatsaechliche_Stueckzahl), 0) AS Produzierte_Stueckzahl,
               ROUND(100.0 * COALESCE(SUM(mb.Tatsaechliche_Stueckzahl), 0) / pa.Stueckzahl, 1) AS Fortschritt_Prozent
        FROM Produktionsauftraege pa
        JOIN Produkte p ON pa.Produkt_ID = p.Produkt_ID
        LEFT JOIN Maschinenbelegung mb ON pa.Auftrag_ID = mb.Auftrag_ID
        GROUP BY pa.Auftrag_ID, p.Produktname, pa.Stueckzahl, pa.Prioritaet, pa.Zieltermin, pa.Status
        ORDER BY pa.Prioritaet ASC, pa.Zieltermin ASC
    ''')
    
    zeilen = cursor.fetchall()
    conn.close()
    return zeilen

def export_produktionsplan(ausgabedatei='produktionsplan_export.csv'):
    """Exportiert Produktionsplan als CSV (Excel-kompatibel)."""
    zeilen = produktionsplan_report()
    
    with open(ausgabedatei, 'w', newline='', encoding='utf-8') as datei:
        writer = csv.writer(datei, delimiter=';')  # Semikolon für deutsche Excel-Version
        
        # Header
        writer.writerow([
            'Auftrag_ID', 'Produktname', 'Geplante_Stückzahl', 'Priorität',
            'Zieltermin', 'Status', 'Anzahl_Maschinenbelegungen',
            'Produzierte_Stückzahl', 'Fortschritt_%'
        ])
        
        # Datenzeilen
        for zeile in zeilen:
            writer.writerow([
                zeile['Auftrag_ID'],
                zeile['Produktname'],
                zeile['Geplante_Stueckzahl'],
                zeile['Prioritaet'],
                zeile['Zieltermin'],
                zeile['Status'],
                zeile['Anzahl_Maschinenbelegungen'],
                zeile['Produzierte_Stueckzahl'],
                str(zeile['Fortschritt_Prozent']).replace('.', ',')  # Dezimaltrennzeichen: Komma
            ])
    
    print(f"✅ Produktionsplan exportiert: {ausgabedatei}")

if __name__ == '__main__':
    # ... Setup (Import aus XML, JSON, CSV) ...
    export_produktionsplan()
```

> [!NOTE]
> **CSV für Excel**: Für deutsche Excel-Versionen: Separator `;` (Semikolon) und Dezimaltrennzeichen `,` (Komma). Mit `newline=''` unter Windows.

---

## 📝 Zusammenfassung

Diese Lösungen demonstrieren:
- **SQL-Grundlagen**: CREATE TABLE, INSERT, SELECT mit WHERE/GROUP BY/HAVING/JOIN
- **Python-SQLite**: Verbindungen, Cursor, Prepared Statements (`?`), `row_factory`
- **Fehlerbehandlung**: `try-except-finally`, `conn.commit()`, `conn.rollback()`
- **Transaktionen**: Atomicity durch Commit/Rollback
- **pandas**: SQL → DataFrame mit `pd.read_sql_query()`, Zeitreihen-Operationen
- **matplotlib**: Zeitreihen-Plots, Scatter-Plots, Annotationen
- **CSV/JSON/XML-Import**: `csv.DictReader()`, `json.load()`, `xml.etree.ElementTree`
