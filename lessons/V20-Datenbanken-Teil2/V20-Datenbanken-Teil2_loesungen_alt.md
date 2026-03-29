# V20 – Lösungen: Datenbanken – Teil 2

---

## Inhaltsverzeichnis

### 📚 Theorie-Lösungen
- [T1: Normalisierung einer Produktions-Datenbank](#t1-normalisierung-einer-produktions-datenbank)
- [T2: Indizes und Query-Optimierung](#t2-indizes-und-query-optimierung)
- [T3: Transaktionen und ACID in kritischen Systemen](#t3-transaktionen-und-acid-in-kritischen-systemen)

### 🐍 Python-Lösungen
- [P1: SQL-Injection Schwachstelle beheben](#p1-sql-injection-schwachstelle-beheben)
- [P2: UPDATE und DELETE mit Fehlerbehandlung](#p2-update-und-delete-mit-fehlerbehandlung)
- [P3: Transaktionen mit Rollback](#p3-transaktionen-mit-rollback)
- [P4: Aggregationen und Visualisierung mit pandas + matplotlib](#p4-aggregationen-und-visualisierung-mit-pandas--matplotlib)
- [P5: Projekt – Qualitätskontroll-Dashboard](#p5-projekt--qualitätskontroll-dashboard)

---

## 📚 Theorie-Lösungen

### T1: Normalisierung einer Produktions-Datenbank

#### a) Identifikation von Anomalien

**Problem 1: Update-Anomalie (Kundenadresse)**
Wenn die Müller AG ihre Adresse ändert (z.B. Umzug von "Hauptstr. 10" nach "Industrieweg 5"), muss diese Änderung in **allen Zeilen** erfolgen, wo Müller AG als Kunde vorkommt (hier Zeilen 1, 2 und 4). Wird eine Zeile vergessen, entstehen inkonsistente Daten (verschiedene Adressen für denselben Kunden).

**Beispiel**: `UPDATE Produktionsauftraege SET Kunde_Adresse = 'Industrieweg 5' WHERE Kunde_Name = 'Müller AG'` muss 3 Zeilen aktualisieren. Vergisst man die WHERE-Klausel oder filtert falsch, entsteht Inkonsistenz.

**Problem 2: Insert-Anomalie (Neuer Artikel ohne Auftrag)**
Wenn das Unternehmen einen neuen Artikel "Flansch F20" mit Preis 180,00 € ins Sortiment aufnimmt, **kann dieser nicht gespeichert werden**, solang er nicht in einem Auftrag verwendet wird. Man kann keine Zeile mit `Auftrag_ID = NULL` einfügen, da dies gegen Primärschlüssel-Constraints verstoßen würde.

**Beispiel**: Artikel-Stammdaten (Name, Preis, Gewicht) sollten unabhängig von Aufträgen existieren können.

**Problem 3: Delete-Anomalie (Letzter Auftrag einer Maschine)**
Wenn Auftrag 1001 gelöscht wird (Zeilen 1 und 2), gehen **alle Informationen** über "CNC-Fräse 01" und "Drehmaschine 02" verloren, obwohl diese Maschinen weiterhin im Unternehmen existieren und in anderen Kontexten relevant sein könnten.

**Beispiel**: Nach `DELETE FROM Produktionsauftraege WHERE Auftrag_ID = 1001` existieren keine Daten mehr zu diesen zwei Maschinen (Name, Typ) in der Datenbank.

---

#### b) Erste Normalform (1NF)

**Prüfung**: Ist die Tabelle in 1NF?

Die Tabelle **ist NICHT in 1NF**, weil:
- **Wiederholungsgruppen existieren**: Ein Auftrag (z.B. 1001) hat mehrere Zeilen, da mehrere Artikel bestellt wurden
- **Attributwerte sind nicht atomar**: Wenn man Auftrag 1001 als eine logische Einheit betrachtet, enthält er eine "Liste" von Artikeln (Zahnrad Z42, Welle W15)

**Korrektur: 1NF-Schema**

Um 1NF zu erreichen, muss jede Zeile eine **atomare Entität** repräsentieren. Wir trennen Auftrags-Kopfdaten von Auftragspositionen:

**Tabelle: Auftraege_1NF**

| Auftrag_ID (PK) | Auftragsdatum | Kunde_Name | Kunde_Adresse | Liefertermin |
|-----------------|---------------|------------|---------------|--------------|
| 1001            | 2024-01-10    | Müller AG  | Hauptstr. 10  | 2024-02-10   |
| 1002            | 2024-01-15    | Schmidt GmbH | Bahnhofstr. 5| 2024-03-01   |
| 1003            | 2024-01-20    | Müller AG  | Hauptstr. 10  | 2024-02-28   |

**Tabelle: Auftragspositionen_1NF**

| Auftrag_ID (FK) | Position (PK Teil 2) | Artikel_Name | Artikel_Preis | Artikel_Gewicht_kg | Maschine_Name | Maschine_Typ | Menge |
|-----------------|----------------------|--------------|---------------|--------------------|---------------|--------------|-------|
| 1001            | 1                    | Zahnrad Z42  | 125.50        | 2.3                | CNC-Fräse 01  | Fräse        | 50    |
| 1001            | 2                    | Welle W15    | 89.00         | 5.1                | Drehmaschine 02 | Drehbank   | 30    |
| 1002            | 1                    | Zahnrad Z42  | 125.50        | 2.3                | CNC-Fräse 03  | Fräse        | 100   |
| 1003            | 1                    | Gehäuse G08  | 245.00        | 12.5               | Drehmaschine 02 | Drehbank   | 20    |

**Primärschlüssel**: `(Auftrag_ID, Position)` für Auftragspositionen

**Hinweis**: Jetzt sind alle Werte atomar, keine Wiederholungsgruppen innerhalb einer Zelle.

---

#### c) Zweite Normalform (2NF)

**Definition**: Eine Tabelle ist in 2NF, wenn sie in 1NF ist **und** keine **partiellen Abhängigkeiten** existieren. Das bedeutet: Kein Nicht-Schlüsselattribut darf nur von einem Teil eines zusammengesetzten Schlüssels abhängen.

**Analyse der Abhängigkeiten** (angenommen `(Auftrag_ID, Artikel_Name)` ist zusammengesetzter Schlüssel):

| Attribut | Abhängigkeit | Vollständig oder partiell? |
|----------|--------------|---------------------------|
| Auftragsdatum | Nur von `Auftrag_ID` | **Partiell** ❌ |
| Kunde_Name | Nur von `Auftrag_ID` | **Partiell** ❌ |
| Kunde_Adresse | Nur von `Auftrag_ID` | **Partiell** ❌ |
| Liefertermin | Nur von `Auftrag_ID` | **Partiell** ❌ |
| Artikel_Preis | Nur von `Artikel_Name` | **Partiell** ❌ |
| Artikel_Gewicht_kg | Nur von `Artikel_Name` | **Partiell** ❌ |
| Maschine_Typ | Nur von `Maschine_Name` | **Partiell** ❌ |
| Menge | Von `(Auftrag_ID, Artikel_Name)` | Vollständig ✅ |

**2NF-Schema**: Wir splitten in separate Tabellen, sodass jedes Attribut von seinem **vollen** Schlüssel abhängt.

**Tabelle 1: Auftraege_2NF**

| Auftrag_ID (PK) | Auftragsdatum | Kunde_Name | Kunde_Adresse | Liefertermin |
|-----------------|---------------|------------|---------------|--------------|
| 1001            | 2024-01-10    | Müller AG  | Hauptstr. 10  | 2024-02-10   |
| 1002            | 2024-01-15    | Schmidt GmbH | Bahnhofstr. 5| 2024-03-01   |
| 1003            | 2024-01-20    | Müller AG  | Hauptstr. 10  | 2024-02-28   |

**Tabelle 2: Artikel_2NF**

| Artikel_Name (PK) | Artikel_Preis | Artikel_Gewicht_kg |
|-------------------|---------------|--------------------|
| Zahnrad Z42       | 125.50        | 2.3                |
| Welle W15         | 89.00         | 5.1                |
| Gehäuse G08       | 245.00        | 12.5               |

**Tabelle 3: Maschinen_2NF**

| Maschine_Name (PK) | Maschine_Typ |
|--------------------|--------------|
| CNC-Fräse 01       | Fräse        |
| Drehmaschine 02    | Drehbank     |
| CNC-Fräse 03       | Fräse        |

**Tabelle 4: Auftragspositionen_2NF**

| Auftrag_ID (PK, FK) | Artikel_Name (PK, FK) | Maschine_Name (FK) | Menge |
|---------------------|----------------------|--------------------|-------|
| 1001                | Zahnrad Z42          | CNC-Fräse 01       | 50    |
| 1001                | Welle W15            | Drehmaschine 02    | 30    |
| 1002                | Zahnrad Z42          | CNC-Fräse 03       | 100   |
| 1003                | Gehäuse G08          | Drehmaschine 02    | 20    |

**Primärschlüssel**: 
- `Auftraege_2NF`: `Auftrag_ID`
- `Artikel_2NF`: `Artikel_Name`
- `Maschinen_2NF`: `Maschine_Name`
- `Auftragspositionen_2NF`: `(Auftrag_ID, Artikel_Name)`

**Fremdschlüssel**:
- `Auftragspositionen_2NF.Auftrag_ID` → `Auftraege_2NF.Auftrag_ID`
- `Auftragspositionen_2NF.Artikel_Name` → `Artikel_2NF.Artikel_Name`
- `Auftragspositionen_2NF.Maschine_Name` → `Maschinen_2NF.Maschine_Name`

---

#### d) Dritte Normalform (3NF)

**Definition**: Eine Tabelle ist in 3NF, wenn sie in 2NF ist **und** keine **transitiven Abhängigkeiten** existieren. Das bedeutet: Kein Nicht-Schlüsselattribut darf von einem anderen Nicht-Schlüsselattribut abhängen.

**Analyse der transitiven Abhängigkeiten** in 2NF:

**In Tabelle `Auftraege_2NF`**:
- `Kunde_Adresse` hängt **nicht direkt** von `Auftrag_ID` ab, sondern **transitiv über `Kunde_Name`**:
  - `Auftrag_ID` → `Kunde_Name` → `Kunde_Adresse`
  - Dies ist eine transitive Abhängigkeit ❌

**Lösung**: Kunden in separate Tabelle auslagern.

**3NF-Schema** (vollständig):

**Tabelle 1: Kunden**

```sql
CREATE TABLE Kunden (
    Kunden_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Kunde_Name TEXT NOT NULL UNIQUE,
    Kunde_Adresse TEXT NOT NULL,
    Telefon TEXT,
    Email TEXT
);
```

| Kunden_ID (PK) | Kunde_Name   | Kunde_Adresse |
|----------------|--------------|---------------|
| 1              | Müller AG    | Hauptstr. 10  |
| 2              | Schmidt GmbH | Bahnhofstr. 5 |

**Tabelle 2: Artikel**

```sql
CREATE TABLE Artikel (
    Artikel_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Artikel_Name TEXT NOT NULL UNIQUE,
    Artikel_Preis REAL NOT NULL CHECK(Artikel_Preis > 0),
    Artikel_Gewicht_kg REAL NOT NULL,
    Artikelbeschreibung TEXT
);
```

| Artikel_ID (PK) | Artikel_Name | Artikel_Preis | Artikel_Gewicht_kg |
|-----------------|--------------|---------------|--------------------|
| 1               | Zahnrad Z42  | 125.50        | 2.3                |
| 2               | Welle W15    | 89.00         | 5.1                |
| 3               | Gehäuse G08  | 245.00        | 12.5               |

**Tabelle 3: Maschinen**

```sql
CREATE TABLE Maschinen (
    Maschinen_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Maschine_Name TEXT NOT NULL UNIQUE,
    Maschine_Typ TEXT NOT NULL,
    Baujahr INTEGER,
    Status TEXT CHECK(Status IN ('Aktiv', 'Wartung', 'Außer Betrieb'))
);
```

| Maschinen_ID (PK) | Maschine_Name    | Maschine_Typ |
|-------------------|------------------|--------------|
| 1                 | CNC-Fräse 01     | Fräse        |
| 2                 | Drehmaschine 02  | Drehbank     |
| 3                 | CNC-Fräse 03     | Fräse        |

**Tabelle 4: Auftraege**

```sql
CREATE TABLE Auftraege (
    Auftrag_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Kunden_ID INTEGER NOT NULL,
    Auftragsdatum TEXT NOT NULL,  -- ISO 8601: 'YYYY-MM-DD'
    Liefertermin TEXT NOT NULL,
    Status TEXT DEFAULT 'Offen' CHECK(Status IN ('Offen', 'In Bearbeitung', 'Abgeschlossen', 'Storniert')),
    FOREIGN KEY (Kunden_ID) REFERENCES Kunden(Kunden_ID)
);
```

| Auftrag_ID (PK) | Kunden_ID (FK) | Auftragsdatum | Liefertermin | Status |
|-----------------|----------------|---------------|--------------|--------|
| 1001            | 1              | 2024-01-10    | 2024-02-10   | Offen  |
| 1002            | 2              | 2024-01-15    | 2024-03-01   | Offen  |
| 1003            | 1              | 2024-01-20    | 2024-02-28   | Offen  |

**Tabelle 5: Auftragspositionen**

```sql
CREATE TABLE Auftragspositionen (
    Position_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Auftrag_ID INTEGER NOT NULL,
    Artikel_ID INTEGER NOT NULL,
    Maschinen_ID INTEGER,  -- Kann NULL sein, falls noch nicht zugewiesen
    Menge INTEGER NOT NULL CHECK(Menge > 0),
    FOREIGN KEY (Auftrag_ID) REFERENCES Auftraege(Auftrag_ID) ON DELETE CASCADE,
    FOREIGN KEY (Artikel_ID) REFERENCES Artikel(Artikel_ID),
    FOREIGN KEY (Maschinen_ID) REFERENCES Maschinen(Maschinen_ID),
    UNIQUE(Auftrag_ID, Artikel_ID)  -- Ein Artikel nur einmal pro Auftrag
);
```

| Position_ID (PK) | Auftrag_ID (FK) | Artikel_ID (FK) | Maschinen_ID (FK) | Menge |
|------------------|-----------------|-----------------|-------------------|-------|
| 1                | 1001            | 1               | 1                 | 50    |
| 2                | 1001            | 2               | 2                 | 30    |
| 3                | 1002            | 1               | 3                 | 100   |
| 4                | 1003            | 3               | 2                 | 20    |

**Zusammenfassung der Schlüssel**:

| Tabelle | Primärschlüssel | Fremdschlüssel |
|---------|-----------------|----------------|
| Kunden | Kunden_ID | — |
| Artikel | Artikel_ID | — |
| Maschinen | Maschinen_ID | — |
| Auftraege | Auftrag_ID | Kunden_ID → Kunden |
| Auftragspositionen | Position_ID | Auftrag_ID → Auftraege<br>Artikel_ID → Artikel<br>Maschinen_ID → Maschinen |

---

#### e) Begründung der Vorteile

**Vorteil 1: Konsistenz**
In 3NF wird jede Information nur **einmal** gespeichert. Wenn die Müller AG umzieht, muss nur die Adresse in der Tabelle `Kunden` geändert werden – nicht in hunderten Auftragszeilen. Dies eliminiert Update-Anomalien und garantiert konsistente Daten.

**Vorteil 2: Wartbarkeit und Flexibilität**
Neue Artikel, Kunden oder Maschinen können unabhängig von Aufträgen angelegt werden (keine Insert-Anomalien). Geschäftslogik-Änderungen (z.B. zusätzliche Artikel-Attribute wie "Materialkategorie") betreffen nur eine Tabelle, nicht das gesamte Schema.

**Vorteil 3: Speichereffizienz**
Redundanzen werden eliminiert: Artikel-Name, Preis und Gewicht werden nicht in jeder Auftragsposition wiederholt. Bei einer echten Produktionsdatenbank mit 100.000 Auftragspositionen spart dies erheblichen Speicherplatz (z.B. "Zahnrad Z42" wird nicht 10.000-mal gespeichert, sondern nur einmal referenziert).

---

### T2: Indizes und Query-Optimierung

#### a) Index-Analyse für jede Query

**Query 1: Zeitbereichs-Abfrage mit Sortierung** (50% aller Queries)
```sql
SELECT * FROM Sensordaten 
WHERE Maschinen_ID = 42 AND Zeitstempel >= '2024-12-01' 
ORDER BY Zeitstempel DESC 
LIMIT 100;
```

**Analyse**:
- **Filter**: `Maschinen_ID = 42` (sehr selektiv, filtert auf eine Maschine)
- **Zusätzlicher Filter**: `Zeitstempel >= '2024-12-01'` (zeitliche Einschränkung)
- **Sortierung**: `ORDER BY Zeitstempel DESC`
- **Limit**: Nur 100 Zeilen benötigt

**Index-Empfehlung**: **Composite Index auf `(Maschinen_ID, Zeitstempel)`** in dieser Reihenfolge
```sql
CREATE INDEX idx_sensordaten_maschine_zeit ON Sensordaten(Maschinen_ID, Zeitstempel);
```

**Begründung**:
- **Reihenfolge**: `Maschinen_ID` zuerst, da dieser Filter exakt ist (`=`) und sehr selektiv
- `Zeitstempel` als zweite Spalte ermöglicht effiziente Range-Suche (`>=`) innerhalb der gefilterten Maschinen-Daten
- Der Index kann für **Sortierung** genutzt werden (ORDER BY auf zweiter Index-Spalte)
- **Covering Index**: Alle benötigten Spalten sind im Index oder können schnell nachgeschlagen werden
- **Erwartete Performance**: Ohne Index O(n) Full Table Scan über 500.000 Zeilen; mit Index O(log n) + 100 Zeilen = ~10-20ms statt 500-1000ms

**Trade-off**: Bei 500.000 neuen Messwerten pro Tag sind das 500.000 Index-Updates. Da aber nur 5% der Queries INSERTs sind, ist der Gewinn deutlich größer als die Kosten.

---

**Query 2: Aggregation mit mehreren Filtern** (30% aller Queries)
```sql
SELECT AVG(Messwert) 
FROM Sensordaten 
WHERE Sensor_Typ = 'Temperatur' AND Status = 'kritisch';
```

**Analyse**:
- **Filter 1**: `Sensor_Typ = 'Temperatur'` (möglicherweise 25% der Daten, wenn 4 Sensor-Typen existieren)
- **Filter 2**: `Status = 'kritisch'` (sehr selektiv, laut Aufgabe nur 5% haben Status != 'normal')
- **Aggregation**: `AVG(Messwert)` – muss alle gefilterten Zeilen durchlaufen
- **Keine Sortierung**: Reihenfolge egal

**Index-Empfehlung**: **Composite Index auf `(Status, Sensor_Typ)`** in dieser Reihenfolge
```sql
CREATE INDEX idx_sensordaten_status_typ ON Sensordaten(Status, Sensor_Typ);
```

**Begründung**:
- **Reihenfolge**: `Status` zuerst, da dieser Filter sehr selektiv ist (nur 5% != 'normal')
- Nach Filterung auf `Status = 'kritisch'` (vielleicht 2-3% der Daten) ist Filterung auf `Sensor_Typ` sehr schnell
- **Alternative Reihenfolge**: `(Sensor_Typ, Status)` wäre weniger effizient, da zuerst 25% der Daten gefiltert werden müssten
- **Erwartete Performance**: Ohne Index Full Scan über 500.000 Zeilen; mit Index nur ~5.000-15.000 Zeilen (kritische Temperatur-Messungen)

**Trade-off**: Dieser Index hilft auch bei anderen Status-basierten Queries (z.B. "Alle Warnungen").

---

**Query 3: Zeitbereichs-Aggregation mit Gruppierung** (15% aller Queries)
```sql
SELECT Maschinen_ID, COUNT(*) 
FROM Sensordaten 
WHERE Zeitstempel >= '2024-12-15' 
GROUP BY Maschinen_ID;
```

**Analyse**:
- **Filter**: `Zeitstempel >= '2024-12-15'` (z.B. letzte 2 Wochen = ~7 Millionen Zeilen bei 500k/Tag)
- **Gruppierung**: `GROUP BY Maschinen_ID`
- **Aggregation**: `COUNT(*)` – zählt Zeilen pro Maschine

**Index-Empfehlung**: **Composite Index auf `(Zeitstempel, Maschinen_ID)`**
```sql
CREATE INDEX idx_sensordaten_zeit_maschine ON Sensordaten(Zeitstempel, Maschinen_ID);
```

**Begründung**:
- **Reihenfolge**: `Zeitstempel` zuerst, da der Range-Filter (`>=`) damit optimal funktioniert
- `Maschinen_ID` als zweite Spalte ermöglicht effiziente Gruppierung innerhalb des Zeitbereichs
- **Index-Only Scan möglich**: Beide Spalten (Zeitstempel, Maschinen_ID) sind im Index, Haupttabelle muss nicht geladen werden
- **Erwartete Performance**: Ohne Index Full Scan; mit Index Scan nur über relevanten Zeitbereich + effiziente Gruppierung

**Trade-off**: Dieser Index überschneidet sich mit `idx_sensordaten_maschine_zeit` (Query 1), aber mit **umgekehrter Reihenfolge**. Kann nicht beide Queries gleichzeitig optimal bedienen.

---

**Query 4: Batch-INSERTs** (5% aller Queries, aber sehr häufig)
```sql
INSERT INTO Sensordaten (Maschinen_ID, Sensor_Typ, Messwert, Zeitstempel, Status) 
VALUES (...);
```

**Analyse**:
- **Keine WHERE-Klausel**: Indizes helfen nicht beim INSERT
- **Indizes verlangsamen INSERTs**: Jeder Index muss bei jedem INSERT aktualisiert werden
- **Batch-Inserts**: Wenn 500.000 Zeilen/Tag in Batches eingefügt werden, sind Index-Updates kritisch

**Index-Empfehlung**: **Keine zusätzlichen Indizes** nur für INSERTs
- **Trade-off akzeptieren**: Die 3 vorgeschlagenen Indizes (Query 1-3) beschleunigen 95% der Read-Operationen erheblich
- **Optimierung für INSERTs**:
  - `BEGIN TRANSACTION` und `COMMIT` nach Batch (nicht nach jedem INSERT)
  - Nutze `.executemany()` statt Schleife
  - Deaktiviere Indizes bei sehr großen Bulk-Loads (DROP INDEX → LOAD DATA → CREATE INDEX)

**Erwartete Verlangsamung**: Ohne Indizes ~1ms pro INSERT; mit 3 Indizes ~3-5ms pro INSERT (2-5x langsamer). Bei 500.000 INSERTs/Tag sind das +10-20 Minuten zusätzlicher Ladezeit. Aber: SELECTs werden 50-100x schneller (von Sekunden zu Millisekunden).

---

#### b) Index-Empfehlung (maximal drei Indizes)

**Gewählte Indizes**:

```sql
-- Index 1: Für Query 1 (50% aller Queries) - Zeitbereichs-Abfrage pro Maschine
CREATE INDEX idx_sensordaten_maschine_zeit 
ON Sensordaten(Maschinen_ID, Zeitstempel);

-- Index 2: Für Query 2 (30% aller Queries) - Status-basierte Aggregationen
CREATE INDEX idx_sensordaten_status_typ 
ON Sensordaten(Status, Sensor_Typ);

-- Index 3: Für Query 3 (15% aller Queries) - Zeitbereichs-Aggregation mit Gruppierung
-- VERZICHTET: Überschneidung mit Index 1, Trade-off zugunsten Query 1
```

**Finale Empfehlung: Nur ZWEI Indizes**

Warum **nicht drei**?
- **Index 1** (`Maschinen_ID, Zeitstempel`) ist kritischer als Index 3 (`Zeitstempel, Maschinen_ID`), da Query 1 50% der Queries ausmacht vs. 15% für Query 3
- Query 3 kann **teilweise** von Index 1 profitieren: Der Filter auf `Zeitstempel` kann ohne Index erfolgen (Full Scan), aber das ist akzeptabel für nur 15% der Queries
- **Speicherplatz**: Jeder Index verbraucht ~10-20% der Tabellengröße. Bei 500.000 Zeilen/Tag = ~180 Millionen Zeilen/Jahr sind das erhebliche Speicherkosten
- **INSERT-Performance**: Jeder zusätzliche Index verlangsamt INSERTs um ~50%. Zwei Indizes = 2x langsamer, drei Indizes = 3x langsamer

**Begründung für diese Auswahl**:
- **Index 1** deckt die **häufigsten** Queries ab (50%)
- **Index 2** deckt die **zweithäufigsten** Queries ab (30%) und hat keine Überschneidung mit Index 1
- Query 3 (15%) muss mit suboptimaler Performance leben oder kann durch **Materialized Views** / **Vorberechnete Aggregate** optimiert werden (siehe Aufgabe d)

---

#### c) Partial Index für Query 2

**Problem**: 95% aller Messungen haben Status "normal", nur 5% haben "warnung" oder "kritisch". Ein vollständiger Index auf `(Status, Sensor_Typ)` verschwendet Speicher für 95% der Daten, die nie gefiltert werden.

**Lösung: Partial Index** (PostgreSQL-Feature, nicht in SQLite verfügbar, aber konzeptionell wichtig):

```sql
-- PostgreSQL Syntax:
CREATE INDEX idx_sensordaten_kritisch 
ON Sensordaten(Sensor_Typ) 
WHERE Status IN ('warnung', 'kritisch');
```

**Vorteile**:
- **Speicherersparnis**: Index enthält nur 5% der Zeilen (ca. 25.000 statt 500.000 bei einem Tag)
- **Schnellere Index-Updates**: Bei INSERTs werden nur Zeilen mit Status != 'normal' indexiert
- **Schnellere Index-Scans**: Kleinerer Index = schnelleres Durchsuchen

**Nachteile**:
- **Eingeschränkte Nutzung**: Index kann nur verwendet werden, wenn die WHERE-Klausel den Partial-Condition enthält
- **Nicht für alle Queries**: Queries wie `WHERE Status = 'normal' AND Sensor_Typ = 'Temperatur'` können den Index nicht nutzen
- **DBMS-Abhängig**: SQLite unterstützt keine Partial Indexes; Alternative: Separate Tabelle für kritische Werte

**SQLite-Alternative (Trigger-basiert)**:
```sql
-- Separate Tabelle für kritische Werte
CREATE TABLE Sensordaten_Kritisch (
    Messung_ID INTEGER PRIMARY KEY,
    Sensor_Typ TEXT NOT NULL,
    Messwert REAL NOT NULL,
    Zeitstempel TEXT NOT NULL,
    FOREIGN KEY (Messung_ID) REFERENCES Sensordaten(Messung_ID) ON DELETE CASCADE
);

CREATE INDEX idx_kritisch_typ ON Sensordaten_Kritisch(Sensor_Typ);

-- Trigger: Automatisches Einfügen bei Status != 'normal'
CREATE TRIGGER trg_kritisch_insert AFTER INSERT ON Sensordaten
WHEN NEW.Status IN ('warnung', 'kritisch')
BEGIN
    INSERT INTO Sensordaten_Kritisch (Messung_ID, Sensor_Typ, Messwert, Zeitstempel)
    VALUES (NEW.Messung_ID, NEW.Sensor_Typ, NEW.Messwert, NEW.Zeitstempel);
END;
```

---

#### d) Denormalisierung: `Sensordaten_Aggregate` Tabelle

**Vorschlag**:
```sql
CREATE TABLE Sensordaten_Aggregate (
    Aggregat_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Maschinen_ID INTEGER NOT NULL,
    Sensor_Typ TEXT NOT NULL,
    Datum TEXT NOT NULL,  -- Tages-Datum (ohne Uhrzeit)
    Anzahl_Messungen INTEGER NOT NULL,
    Messwert_Avg REAL,
    Messwert_Min REAL,
    Messwert_Max REAL,
    Anzahl_Kritisch INTEGER DEFAULT 0,
    UNIQUE(Maschinen_ID, Sensor_Typ, Datum)
);

CREATE INDEX idx_aggregate_maschine ON Sensordaten_Aggregate(Maschinen_ID, Datum);
```

**Vorteile**:

**Vorteil 1: Dramatisch schnellere Aggregationsqueries**
Query 2 (`AVG(Messwert)`) kann jetzt direkt aus der Aggregate-Tabelle gelesen werden:
```sql
SELECT AVG(Messwert_Avg) FROM Sensordaten_Aggregate 
WHERE Sensor_Typ = 'Temperatur' AND Anzahl_Kritisch > 0;
```
Statt 500.000 Zeilen zu scannen, werden nur ~1.500 Zeilen gescannt (365 Tage × 4 Sensor-Typen × ca. 1-2 Maschinen mit kritischen Werten). **Performance-Gewinn: 300-500x schneller**.

**Vorteil 2: Reporting und Dashboards**
Langzeit-Trend-Analysen (z.B. "Durchschnittstemperatur pro Maschine über 6 Monate") benötigen keine teuren Aggregationen über Millionen Zeilen. Dashboards können in Echtzeit aktualisiert werden.

---

**Nachteile**:

**Nachteil 1: Erhöhte Komplexität und Wartungsaufwand**
Die Aggregate-Tabelle muss **synchron gehalten** werden mit `Sensordaten`. Möglichkeiten:
- **Trigger**: Automatische Updates bei INSERT/UPDATE/DELETE in `Sensordaten` (komplexe Logik, schwer zu debuggen)
- **Batch-Job**: Nächtliche Berechnung der Aggregate (einfacher, aber Daten sind nicht in Echtzeit)
- **Application-Logik**: Anwendung muss beide Tabellen aktualisieren (Fehleranfällig, Transaktions-Overhead)

Bei Bugs oder inkonsistenten Daten muss die Aggregate-Tabelle **vollständig neu berechnet** werden (teuer).

**Nachteil 2: Zusätzlicher Speicherplatz**
Die Aggregate-Tabelle speichert redundante Daten (Durchschnitte, die jederzeit aus Rohdaten berechnet werden könnten). Bei 365 Tagen × 100 Maschinen × 4 Sensor-Typen = ~150.000 Zeilen/Jahr. Nicht riesig, aber zusätzlicher Overhead. Trade-off: Speicher vs. Query-Performance.

---

#### e) Monitoring: Index-Nutzung überprüfen

**PostgreSQL**:
```sql
EXPLAIN ANALYZE 
SELECT * FROM Sensordaten 
WHERE Maschinen_ID = 42 AND Zeitstempel >= '2024-12-01' 
ORDER BY Zeitstempel DESC LIMIT 100;
```

**Ausgabe-Interpretation** (Beispiel):
```
Index Scan using idx_sensordaten_maschine_zeit on sensordaten  
  (cost=0.42..123.45 rows=100 width=64) 
  (actual time=0.123..2.456 rows=100 loops=1)
  Index Cond: ((maschinen_id = 42) AND (zeitstempel >= '2024-12-01'))
Planning Time: 0.234 ms
Execution Time: 2.678 ms
```

**Wichtige Indikatoren**:
- **"Index Scan using ..."**: Index wird genutzt ✅
- **"Seq Scan"**: Full Table Scan, Index wird NICHT genutzt ❌
- **Execution Time**: Tatsächliche Laufzeit (sollte < 10ms für einfache Queries sein)

---

**SQLite**:
```sql
EXPLAIN QUERY PLAN 
SELECT * FROM Sensordaten 
WHERE Maschinen_ID = 42 AND Zeitstempel >= '2024-12-01' 
ORDER BY Zeitstempel DESC LIMIT 100;
```

**Ausgabe-Interpretation** (Beispiel):
```
QUERY PLAN
`--SEARCH Sensordaten USING INDEX idx_sensordaten_maschine_zeit (Maschinen_ID=? AND Zeitstempel>?)
```

**Wichtige Indikatoren**:
- **"USING INDEX idx_..."**: Index wird genutzt ✅
- **"SCAN Sensordaten"**: Full Table Scan ❌

---

**Zusätzliche Monitoring-Tools**:

**PostgreSQL**: `pg_stat_user_indexes` View
```sql
SELECT 
    schemaname,
    tablename,
    indexname,
    idx_scan,  -- Anzahl Index-Scans
    idx_tup_read,  -- Gelesene Zeilen
    idx_tup_fetch  -- Zurückgegebene Zeilen
FROM pg_stat_user_indexes
WHERE tablename = 'sensordaten'
ORDER BY idx_scan DESC;
```

Wenn `idx_scan = 0` für einen Index: **Index wird nie genutzt** → kann gelöscht werden.

**SQLite**: Kein Built-in Monitoring; Alternative: Application-Level Logging mit `EXPLAIN QUERY PLAN` vor jeder Query.

---

### T3: Transaktionen und ACID in kritischen Systemen

#### a) ACID-Verletzung

**Verletztes Prinzip: Isolation (I in ACID)**

**Erklärung**:
Das Isolation-Prinzip garantiert, dass **gleichzeitige Transaktionen** sich nicht gegenseitig beeinflussen. Im beschriebenen Szenario tritt ein **Lost Update** Problem auf:

1. Beide Roboter (R1 und R2) lesen den gleichen Bestand (50 Schrauben) **gleichzeitig**
2. Beide entscheiden, dass genug vorhanden ist (50 ≥ 40)
3. Beide führen ihre Updates aus, aber **das zweite UPDATE überschreibt das erste** ohne dessen Änderung zu berücksichtigen
4. Resultat: Datenbank zeigt Bestand = 10, aber tatsächlich wurden 80 Schrauben entnommen (Differenz: -30 Schrauben "verschwunden")

**Kritikalität**:
In einem automatisierten Lagersystem führt dies zu **physisch unmöglichen Beständen** (negative Werte, wenn weitere Entnahmen erfolgen) und zu **fehlerhafter Nachbestellung**. Produktionslinien könnten mangels Teilen stoppen, obwohl das System "ausreichend Lager" anzeigt. In sicherheitskritischen Systemen (z.B. Medizintechnik-Teile) kann dies zu **Compliance-Verstößen** und rechtlichen Konsequenzen führen.

---

#### b) Isolation Level

**Lösung: SERIALIZABLE Isolation Level**

**Was dieser Level garantiert**:
- **Serialisierbarkeit**: Transaktionen werden so ausgeführt, als ob sie **nacheinander** (seriell) ablaufen würden, auch wenn sie physisch gleichzeitig laufen
- **Verhindert**: Dirty Reads, Non-Repeatable Reads, Phantom Reads, **und Lost Updates**
- **Mechanismus**: Locks werden auf **gelesene Daten** gesetzt (nicht nur auf geänderte), sodass andere Transaktionen warten müssen

**Konkret im Szenario**:
```sql
-- Roboter R1:
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT Menge_Lager FROM Lagerbestand WHERE Artikel_ID = 101;  -- Liest 50, LOCK gesetzt
-- ... Prüfung: 50 >= 40 ✅
UPDATE Lagerbestand SET Menge_Lager = 10 WHERE Artikel_ID = 101;
COMMIT;

-- Roboter R2 (startet gleichzeitig):
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT Menge_Lager FROM Lagerbestand WHERE Artikel_ID = 101;  
-- WARTET auf R1's COMMIT (Lock-Konflikt)
-- Nach R1's COMMIT: Liest aktuellen Wert 10
-- Prüfung: 10 >= 40 ❌ Fehler!
ROLLBACK;
```

**Alternative: REPEATABLE READ** (funktioniert in vielen DBs ebenfalls):
- Verhindert Lost Updates durch **Snapshot Isolation**
- R2 würde einen **Serialization Failure** Error erhalten und müsste Transaktion wiederholen

**Nicht ausreichend**:
- **READ COMMITTED**: Beide lesen 50 (committed), Updates überschreiben sich
- **READ UNCOMMITTED**: Noch schlimmer – könnte uncommitted Werte lesen

---

#### c) Pessimistic Locking: `SELECT ... FOR UPDATE`

**Konzept**: Expliziter Lock beim **Lesen**, nicht erst beim Schreiben.

**Implementierung**:

```python
import sqlite3
from datetime import datetime

def entnehme_artikel_pessimistic(roboter_id, artikel_id, menge):
    """
    Pessimistic Locking: Artikel wird beim Lesen gesperrt.
    Andere Transaktionen müssen warten.
    """
    conn = sqlite3.connect('lager.db')
    conn.execute('PRAGMA busy_timeout = 5000')  # 5 Sekunden Timeout
    cursor = conn.cursor()
    
    try:
        cursor.execute('BEGIN IMMEDIATE')  # Sofortiger Exclusive Lock
        
        # SELECT ... FOR UPDATE (SQLite-Äquivalent: IMMEDIATE Lock + SELECT)
        cursor.execute('''
            SELECT Menge_Lager, Artikelname 
            FROM Lagerbestand 
            WHERE Artikel_ID = ?
        ''', (artikel_id,))
        
        result = cursor.fetchone()
        if not result:
            raise ValueError(f"Artikel {artikel_id} nicht gefunden")
        
        aktueller_bestand, artikelname = result
        
        # Prüfung: Ist genug vorhanden?
        if aktueller_bestand < menge:
            raise ValueError(
                f"{roboter_id}: Bestand nicht ausreichend! "
                f"Verfügbar: {aktueller_bestand}, Benötigt: {menge}"
            )
        
        # UPDATE: Bestand reduzieren
        neuer_bestand = aktueller_bestand - menge
        cursor.execute('''
            UPDATE Lagerbestand 
            SET Menge_Lager = ? 
            WHERE Artikel_ID = ?
        ''', (neuer_bestand, artikel_id))
        
        # Buchung protokollieren
        cursor.execute('''
            INSERT INTO Buchungen (Artikel_ID, Menge_Aenderung, Zeitstempel, Roboter_ID)
            VALUES (?, ?, ?, ?)
        ''', (artikel_id, -menge, datetime.now().isoformat(), roboter_id))
        
        conn.commit()
        print(f"{roboter_id}: Erfolgreich {menge} × {artikelname} entnommen. "
              f"Neuer Bestand: {neuer_bestand}")
        return True
        
    except sqlite3.OperationalError as e:
        # Timeout: Lock konnte nicht erworben werden
        print(f"{roboter_id}: Lock-Timeout - Artikel {artikel_id} ist gesperrt")
        conn.rollback()
        return False
        
    except ValueError as e:
        # Geschäftslogik-Fehler (nicht genug Bestand)
        print(f"{roboter_id}: {e}")
        conn.rollback()
        return False
        
    finally:
        cursor.close()
        conn.close()

# Test:
# R1 startet zuerst und hält Lock für 2 Sekunden
import threading

def roboter_r1():
    entnehme_artikel_pessimistic("R1", 101, 40)

def roboter_r2():
    time.sleep(0.1)  # Startet kurz nach R1
    entnehme_artikel_pessimistic("R2", 101, 40)

t1 = threading.Thread(target=roboter_r1)
t2 = threading.Thread(target=roboter_r2)
t1.start()
t2.start()
t1.join()
t2.join()

# Erwartete Ausgabe:
# R1: Erfolgreich 40 × Schraube M8 entnommen. Neuer Bestand: 10
# R2: Bestand nicht ausreichend! Verfügbar: 10, Benötigt: 40
```

**Wichtig für PostgreSQL/MySQL** (explizites FOR UPDATE):
```sql
BEGIN;
SELECT Menge_Lager FROM Lagerbestand WHERE Artikel_ID = 101 FOR UPDATE;
-- Lock ist gesetzt, andere SELECTs mit FOR UPDATE warten
UPDATE Lagerbestand SET Menge_Lager = Menge_Lager - 40 WHERE Artikel_ID = 101;
COMMIT;
```

**Vorteile**:
- **Garantiert konsistent**: Erster Zugriff gewinnt, zweiter erhält aktuellen Stand
- **Einfache Logik**: Keine Retry-Mechanismen nötig

**Nachteile**:
- **Deadlock-Risiko**: Wenn zwei Transaktionen sich gegenseitig blockieren (siehe Aufgabe e)
- **Reduzierte Parallelität**: Wartende Transaktionen = langsamer Durchsatz

---

#### d) Optimistic Locking mit `Version`-Spalte

**Konzept**: Kein Lock beim Lesen, aber **Versions-Check beim Schreiben**. Update nur erfolgreich, wenn Version noch übereinstimmt.

**Schema-Erweiterung**:
```sql
ALTER TABLE Lagerbestand ADD COLUMN Version INTEGER DEFAULT 0;
```

**Implementierung**:

```python
import sqlite3
from datetime import datetime
import time

def entnehme_artikel_optimistic(roboter_id, artikel_id, menge, max_retries=3):
    """
    Optimistic Locking: Kein Lock beim Lesen, Version-Check beim UPDATE.
    Bei Konflikt: Retry mit aktuellen Daten.
    """
    conn = sqlite3.connect('lager.db')
    cursor = conn.cursor()
    
    for versuch in range(1, max_retries + 1):
        try:
            cursor.execute('BEGIN')
            
            # SELECT ohne Lock (Optimistic: Wir hoffen, dass kein Konflikt auftritt)
            cursor.execute('''
                SELECT Menge_Lager, Artikelname, Version 
                FROM Lagerbestand 
                WHERE Artikel_ID = ?
            ''', (artikel_id,))
            
            result = cursor.fetchone()
            if not result:
                raise ValueError(f"Artikel {artikel_id} nicht gefunden")
            
            aktueller_bestand, artikelname, alte_version = result
            
            # Prüfung: Ist genug vorhanden?
            if aktueller_bestand < menge:
                raise ValueError(
                    f"{roboter_id}: Bestand nicht ausreichend! "
                    f"Verfügbar: {aktueller_bestand}, Benötigt: {menge}"
                )
            
            # UPDATE mit Version-Check (Optimistic Lock)
            neuer_bestand = aktueller_bestand - menge
            neue_version = alte_version + 1
            
            cursor.execute('''
                UPDATE Lagerbestand 
                SET Menge_Lager = ?, Version = ?
                WHERE Artikel_ID = ? AND Version = ?
            ''', (neuer_bestand, neue_version, artikel_id, alte_version))
            
            # Prüfen, ob UPDATE erfolgreich war (rowcount = 1)
            if cursor.rowcount == 0:
                # Version hat sich geändert → Konflikt!
                raise sqlite3.IntegrityError(
                    f"Optimistic Lock Conflict: Version {alte_version} wurde bereits geändert"
                )
            
            # Buchung protokollieren
            cursor.execute('''
                INSERT INTO Buchungen (Artikel_ID, Menge_Aenderung, Zeitstempel, Roboter_ID)
                VALUES (?, ?, ?, ?)
            ''', (artikel_id, -menge, datetime.now().isoformat(), roboter_id))
            
            conn.commit()
            print(f"{roboter_id}: Erfolgreich {menge} × {artikelname} entnommen. "
                  f"Neuer Bestand: {neuer_bestand}, Version: {alte_version}→{neue_version}")
            return True
            
        except sqlite3.IntegrityError as e:
            # Optimistic Lock Conflict → Retry mit neuen Daten
            conn.rollback()
            if versuch < max_retries:
                print(f"{roboter_id}: Konflikt erkannt (Versuch {versuch}/{max_retries}), "
                      f"wiederhole mit aktuellen Daten...")
                time.sleep(0.05 * versuch)  # Exponential Backoff
                continue
            else:
                print(f"{roboter_id}: Max. Retries erreicht - Abbruch")
                return False
                
        except ValueError as e:
            print(f"{roboter_id}: {e}")
            conn.rollback()
            return False
            
        finally:
            cursor.close()
            conn.close()

# Test (gleiches Szenario wie oben):
import threading

def roboter_r1():
    entnehme_artikel_optimistic("R1", 101, 40)

def roboter_r2():
    time.sleep(0.05)  # Startet kurz nach R1
    entnehme_artikel_optimistic("R2", 101, 40)

t1 = threading.Thread(target=roboter_r1)
t2 = threading.Thread(target=roboter_r2)
t1.start()
t2.start()
t1.join()
t2.join()

# Erwartete Ausgabe:
# R1: Erfolgreich 40 × Schraube M8 entnommen. Neuer Bestand: 10, Version: 0→1
# R2: Konflikt erkannt (Versuch 1/3), wiederhole mit aktuellen Daten...
# R2: Bestand nicht ausreichend! Verfügbar: 10, Benötigt: 40
```

**Vorteile**:
- **Hohe Parallelität**: Kein Warten auf Locks beim Lesen
- **Kein Deadlock-Risiko**: Keine Locks = keine Deadlocks
- **Automatische Retry-Logik**: Anwendung kann Konflikte elegant behandeln

**Nachteile**:
- **Komplexere Anwendungslogik**: Retry-Mechanismus muss implementiert werden
- **Verschwendete Arbeit**: Bei Konflikt muss komplette Logik wiederholt werden
- **Nicht geeignet für sehr hohe Konfliktrate**: Bei vielen gleichzeitigen Zugriffen auf dieselbe Zeile entstehen viele Retries

---

#### e) Deadlock-Szenario

**Szenario**:

**Ausgangssituation**:
- Artikel A (ID 101): Bestand 50
- Artikel B (ID 102): Bestand 30
- Roboter R1 will: 20 × A, dann 10 × B
- Roboter R2 will: 15 × B, dann 25 × A

**Ablauf mit Pessimistic Locking**:

| Zeit | Roboter R1 | Roboter R2 |
|------|------------|------------|
| t1 | BEGIN; SELECT ... FROM Lagerbestand WHERE Artikel_ID=101 FOR UPDATE; (**sperrt Artikel A**) | BEGIN; |
| t2 | Liest Artikel A: 50 vorhanden | SELECT ... FROM Lagerbestand WHERE Artikel_ID=102 FOR UPDATE; (**sperrt Artikel B**) |
| t3 | SELECT ... FROM Lagerbestand WHERE Artikel_ID=102 FOR UPDATE; (**WARTET auf R2, der B gesperrt hat**) | Liest Artikel B: 30 vorhanden |
| t4 | ⏳ Wartet... | SELECT ... FROM Lagerbestand WHERE Artikel_ID=101 FOR UPDATE; (**WARTET auf R1, der A gesperrt hat**) |
| t5 | **DEADLOCK** ☠️ | **DEADLOCK** ☠️ |

**Ergebnis**: Beide Transaktionen warten aufeinander (zirkuläre Abhängigkeit). Datenbank erkennt Deadlock nach Timeout und bricht eine Transaktion ab (meist die jüngere).

---

**Strategie zur Deadlock-Vermeidung: Konsistente Zugriffsreihenfolge**

**Regel**: **Immer Artikel in aufsteigender ID-Reihenfolge sperren**, unabhängig von der Geschäftslogik-Reihenfolge.

**Implementierung**:
```python
def entnehme_mehrere_artikel(roboter_id, artikel_mengen_dict):
    """
    artikel_mengen_dict = {101: 20, 102: 10}  # {Artikel_ID: Menge}
    """
    conn = sqlite3.connect('lager.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('BEGIN IMMEDIATE')
        
        # WICHTIG: Sortiere Artikel-IDs aufsteigend vor dem Sperren!
        artikel_ids_sortiert = sorted(artikel_mengen_dict.keys())
        
        bestaende = {}
        # Schritt 1: Alle Artikel in sortierter Reihenfolge sperren
        for artikel_id in artikel_ids_sortiert:
            cursor.execute('''
                SELECT Menge_Lager, Artikelname 
                FROM Lagerbestand 
                WHERE Artikel_ID = ?
            ''', (artikel_id,))
            
            result = cursor.fetchone()
            if not result:
                raise ValueError(f"Artikel {artikel_id} nicht gefunden")
            
            bestand, name = result
            menge_benötigt = artikel_mengen_dict[artikel_id]
            
            if bestand < menge_benötigt:
                raise ValueError(
                    f"Artikel {name} (ID {artikel_id}): "
                    f"Nur {bestand} vorhanden, {menge_benötigt} benötigt"
                )
            
            bestaende[artikel_id] = (bestand, name, menge_benötigt)
        
        # Schritt 2: Alle Updates durchführen (alle Locks sind bereits gesetzt)
        for artikel_id, (alter_bestand, name, menge) in bestaende.items():
            neuer_bestand = alter_bestand - menge
            cursor.execute('''
                UPDATE Lagerbestand 
                SET Menge_Lager = ? 
                WHERE Artikel_ID = ?
            ''', (neuer_bestand, artikel_id))
            
            cursor.execute('''
                INSERT INTO Buchungen (Artikel_ID, Menge_Aenderung, Zeitstempel, Roboter_ID)
                VALUES (?, ?, ?, ?)
            ''', (artikel_id, -menge, datetime.now().isoformat(), roboter_id))
            
            print(f"{roboter_id}: {menge} × {name} entnommen")
        
        conn.commit()
        print(f"{roboter_id}: Transaktion erfolgreich abgeschlossen")
        return True
        
    except Exception as e:
        print(f"{roboter_id}: Fehler - {e}")
        conn.rollback()
        return False
        
    finally:
        cursor.close()
        conn.close()

# Test: Deadlock vermieden durch sortierte Zugriffe
def roboter_r1():
    entnehme_mehrere_artikel("R1", {101: 20, 102: 10})  # Interne Sortierung: 101, 102

def roboter_r2():
    entnehme_mehrere_artikel("R2", {102: 15, 101: 25})  # Interne Sortierung: 101, 102

# Jetzt: Beide sperren zuerst 101, dann 102 → Kein Deadlock!
# R1 gewinnt (sperrt 101 zuerst), R2 wartet bis R1 fertig ist
```

**Weitere Strategien**:
- **Timeout**: `PRAGMA busy_timeout = 5000` in SQLite
- **Deadlock Detection**: Datenbank bricht automatisch eine Transaktion ab
- **Retry-Logik**: Anwendung wiederholt abgebrochene Transaktion

---

#### f) Durability: Write-Ahead Logging (WAL)

**Konzept**: Wie garantiert ein DBMS, dass committete Daten **nie** verloren gehen, selbst bei Stromausfall?

**Antwort: Write-Ahead Logging (WAL)**

**Ablauf**:

1. **Transaktion startet**: Änderungen werden im RAM durchgeführt (schnell)
   ```sql
   BEGIN;
   UPDATE Lagerbestand SET Menge_Lager = 10 WHERE Artikel_ID = 101;
   ```

2. **COMMIT wird aufgerufen**: 
   - **Schritt 1**: Alle Änderungen werden **zuerst** ins **Transaction Log** (WAL-Datei) geschrieben
   - **Schritt 2**: Log-Eintrag wird auf Festplatte **geflusht** (`fsync()` System-Call)
   - **Schritt 3**: Erst nach erfolgreichem Flush wird COMMIT bestätigt
   - **Schritt 4**: Änderungen werden **asynchron** in Hauptdatenbank-Datei geschrieben (später, im Hintergrund)

3. **Stromausfall zwischen Schritt 3 und 4**:
   - Hauptdatenbank-Datei ist **noch nicht** aktualisiert (alte Werte)
   - Aber: Transaction Log enthält **alle** committeten Änderungen

4. **Neustart nach Stromausfall**:
   - Datenbank führt **Automatic Recovery** durch
   - **Redo**: Alle committeten Transaktionen aus Log werden in Hauptdatenbank **nachgespielt**
   - **Undo**: Alle nicht-committeten Transaktionen werden **zurückgerollt**
   - Ergebnis: Datenbank ist konsistent, alle committeten Änderungen sind da

**Visualisierung**:
```
Zeit  | RAM (Puffer)  | WAL-Log (Festplatte) | Hauptdatenbank (Festplatte)
------+---------------+----------------------+-----------------------------
t1    | Menge=50      | —                    | Menge=50
t2    | Menge=10      | —                    | Menge=50
t3    | Menge=10      | UPDATE ... SET=10 ✅ | Menge=50
t4    | COMMIT OK     | COMMIT ✅            | Menge=50
t5    | ☠️ STROMAUSFALL
------+---------------+----------------------+-----------------------------
t6    | (Neustart)    | UPDATE ... SET=10 ✅ | Menge=50 (ALT!)
t7    | Recovery...   | COMMIT ✅            | Menge=10 ✅ (nachgespielt)
```

**Warum ist das schneller als direkt in DB schreiben?**
- **Sequenzielles Schreiben**: Log wird **append-only** geschrieben (schnell)
- **Hauptdatenbank**: Random Writes an verschiedenen Stellen (langsam)
- **Batch-Updates**: Mehrere Transaktionen können gleichzeitig ins Log geschrieben werden

**SQLite-Spezifika**:
```sql
PRAGMA journal_mode = WAL;  -- Aktiviert WAL-Modus (Standard: DELETE oder PERSIST)
```

**PostgreSQL**: WAL ist Standard, konfigurierbar mit `wal_level`, `fsync`, `synchronous_commit`.

**Trade-off**:
- **Vorteil**: Durability ohne Performance-Einbußen
- **Nachteil**: Zusätzliche Log-Dateien verbrauchen Speicherplatz (werden aber regelmäßig "checkpointed" = in Hauptdatenbank integriert und gelöscht)

---

## 🐍 Python-Lösungen

### P1: SQL-Injection Schwachstelle beheben

#### a) Exploit demonstrieren

**Eingabestring**: `"' OR '1'='1"`

**Resultierende Query**:
```sql
SELECT * FROM Pruefprotokolle WHERE Artikelname = '' OR '1'='1'
```

**Erklärung**:
Der Eingabestring **schließt** den String-Literal mit `'` und fügt dann eine **zusätzliche Bedingung** `OR '1'='1'` hinzu. Da `'1'='1'` immer `True` ist, wird die WHERE-Klausel zu:
- `Artikelname = ''` (False für alle Zeilen)
- `OR '1'='1'` (True für alle Zeilen)
- **Gesamt**: True → **Alle Zeilen werden zurückgegeben**

Ein Angreifer kann so **alle Prüfprotokolle** abrufen, ohne den genauen Artikelnamen zu kennen. Dies verletzt die Zugriffskontrolle (Principle of Least Privilege).

---

#### b) Kritischer Exploit: DROP TABLE

**Eingabestring**: `"'; DROP TABLE Pruefprotokolle; --"`

**Resultierende Query**:
```sql
SELECT * FROM Pruefprotokolle WHERE Artikelname = ''; DROP TABLE Pruefprotokolle; --'
```

**Erklärung**:
1. `';` beendet die SELECT-Query vorzeitig
2. `DROP TABLE Pruefprotokolle;` führt eine **zweite, zerstörerische Query** aus
3. `--` kommentiert den Rest aus (verhindert Syntax-Fehler durch abschließendes `'`)

**Was passiert mit der Datenbank**:
- Die Tabelle `Pruefprotokolle` wird **dauerhaft gelöscht**
- **Alle Qualitätsdaten gehen verloren** (falls kein Backup existiert)
- Produktionsstopp, da Qualitätskontrolle nicht mehr nachweisbar ist
- Rechtliche Konsequenzen (z.B. ISO-Zertifizierung gefährdet)

**Hinweis**: SQLite führt standardmäßig keine Multiple Statements in `.execute()` aus (nur mit `.executescript()`), aber andere DBs (MySQL mit `multi=True`) sind anfällig!

---

#### c) Sichere Implementierung

```python
import sqlite3

def suche_artikel_sicher(artikelname):
    """
    Sichere Implementierung mit Prepared Statements.
    """
    conn = sqlite3.connect('testdaten/produktionsdb.db')
    cursor = conn.cursor()
    
    # SICHER: Prepared Statement mit ? Platzhalter
    query = "SELECT * FROM Pruefprotokolle WHERE Artikelname = ?"
    cursor.execute(query, (artikelname,))  # Parameter als Tuple!
    
    ergebnisse = cursor.fetchall()
    conn.close()
    return ergebnisse


# Alternative: Named Placeholders (noch lesbarer bei vielen Parametern)
def suche_artikel_sicher_named(artikelname):
    """
    Sichere Implementierung mit Named Placeholders.
    """
    conn = sqlite3.connect('testdaten/produktionsdb.db')
    cursor = conn.cursor()
    
    # SICHER: Named Placeholder :artikelname
    query = "SELECT * FROM Pruefprotokolle WHERE Artikelname = :artikelname"
    cursor.execute(query, {"artikelname": artikelname})
    
    ergebnisse = cursor.fetchall()
    conn.close()
    return ergebnisse
```

**Warum ist das sicher?**
- Der Parameter `artikelname` wird als **Daten-Literal** behandelt, nicht als SQL-Code
- Sonderzeichen (`'`, `"`, `;`, `--`) werden automatisch **escaped**
- Auch wenn `artikelname = "'; DROP TABLE ..."` eingegeben wird, sucht die Query nach einem Artikel mit **exakt diesem Namen** (keine Code-Ausführung)

---

#### d) Test-Dokumentation

```python
import sqlite3

# Setup: Testdatenbank erstellen
conn = sqlite3.connect('test_injection.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Pruefprotokolle (
    Pruef_ID INTEGER PRIMARY KEY,
    Artikelname TEXT NOT NULL,
    Pruefwert REAL,
    Status TEXT
)''')

cursor.execute("INSERT INTO Pruefprotokolle (Artikelname, Pruefwert, Status) VALUES ('Zahnrad Z42', 0.05, 'Bestanden')")
cursor.execute("INSERT INTO Pruefprotokolle (Artikelname, Pruefwert, Status) VALUES ('Welle W15', 0.12, 'Fehlgeschlagen')")
cursor.execute("INSERT INTO Pruefprotokolle (Artikelname, Pruefwert, Status) VALUES ('Gehäuse G08', 0.03, 'Bestanden')")
conn.commit()
conn.close()

# Test 1: Normaler Name
print("=== Test 1: Normaler Name ===")
ergebnis = suche_artikel_sicher("Zahnrad Z42")
print(f"Anzahl Zeilen: {len(ergebnis)}")  # Erwartung: 1
print(f"Ergebnis: {ergebnis}")
# Ausgabe: [(1, 'Zahnrad Z42', 0.05, 'Bestanden')]

# Test 2: Angriff 1 - OR '1'='1'
print("\n=== Test 2: Angriff OR '1'='1' ===")
ergebnis = suche_artikel_sicher("' OR '1'='1")
print(f"Anzahl Zeilen: {len(ergebnis)}")  # Erwartung: 0 (kein Artikel mit diesem Namen)
print(f"Ergebnis: {ergebnis}")
# Ausgabe: [] (KEINE Zeilen, Angriff blockiert!)

# Test 3: Angriff 2 - DROP TABLE
print("\n=== Test 3: Angriff DROP TABLE ===")
ergebnis = suche_artikel_sicher("'; DROP TABLE Pruefprotokolle; --")
print(f"Anzahl Zeilen: {len(ergebnis)}")  # Erwartung: 0
print(f"Ergebnis: {ergebnis}")
# Ausgabe: [] (Tabelle existiert noch, kein DROP ausgeführt!)

# Verifikation: Tabelle existiert noch
conn = sqlite3.connect('test_injection.db')
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM Pruefprotokolle")
print(f"\nTabelle Pruefprotokolle hat noch {cursor.fetchone()[0]} Zeilen")  # Erwartung: 3
conn.close()
# Ausgabe: Tabelle Pruefprotokolle hat noch 3 Zeilen ✅
```

**Zusammenfassung**:
- **Test 1**: Normale Suche funktioniert → 1 Zeile zurückgegeben
- **Test 2**: OR-Injection wird als Literal behandelt → 0 Zeilen (kein Artikel mit Namen `"' OR '1'='1"`)
- **Test 3**: DROP-TABLE-Angriff schlägt fehl → Tabelle bleibt intakt, 0 Zeilen zurückgegeben

---

#### e) Bonus: Erweiterte Funktion mit zwei Parametern

```python
def suche_artikel_erweitert(artikelname, min_pruefwert):
    """
    Suche nach Artikelname UND Mindest-Prüfwert.
    Verwendet Named Placeholders für bessere Lesbarkeit.
    """
    conn = sqlite3.connect('test_injection.db')
    cursor = conn.cursor()
    
    query = '''
        SELECT Artikelname, Pruefwert, Status 
        FROM Pruefprotokolle 
        WHERE Artikelname = :artikelname 
          AND Pruefwert >= :min_wert
        ORDER BY Pruefwert DESC
    '''
    
    cursor.execute(query, {
        "artikelname": artikelname,
        "min_wert": min_pruefwert
    })
    
    ergebnisse = cursor.fetchall()
    conn.close()
    return ergebnisse

# Test
print("\n=== Erweiterte Suche ===")
ergebnis = suche_artikel_erweitert("Zahnrad Z42", 0.04)
print(f"Zahnrad Z42 mit Pruefwert >= 0.04: {ergebnis}")
# Ausgabe: [('Zahnrad Z42', 0.05, 'Bestanden')]

# Auch bei Angriffs-Versuch sicher
ergebnis = suche_artikel_erweitert("' OR '1'='1", 0.0)
print(f"Angriff mit zwei Parametern: {ergebnis}")
# Ausgabe: [] (Angriff blockiert, beide Parameter werden escaped)
```

---

### P2: UPDATE und DELETE mit Fehlerbehandlung

#### a) Betriebsstunden aktualisieren

```python
import sqlite3

def aktualisiere_betriebsstunden(maschinen_id, neue_stunden):
    """
    Aktualisiert Betriebsstunden für eine Maschine.
    Prüft mit cursor.rowcount, ob Maschine existiert.
    """
    conn = sqlite3.connect('testdaten/produktionsdb.db')
    cursor = conn.cursor()
    
    try:
        # Vorher: Alte Betriebsstunden abfragen (optional, für Ausgabe)
        cursor.execute('SELECT Betriebsstunden FROM Maschinen WHERE Maschinen_ID = ?', (maschinen_id,))
        result = cursor.fetchone()
        
        if result:
            alte_stunden = result[0]
        else:
            alte_stunden = None
        
        # UPDATE durchführen
        cursor.execute('''
            UPDATE Maschinen 
            SET Betriebsstunden = ? 
            WHERE Maschinen_ID = ?
        ''', (neue_stunden, maschinen_id))
        
        # Prüfen, ob UPDATE erfolgreich war
        if cursor.rowcount == 0:
            print(f"Maschine {maschinen_id} nicht gefunden")
        else:
            conn.commit()
            print(f"Maschine {maschinen_id}: {alte_stunden}h → {neue_stunden}h")
        
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

# Test
aktualisiere_betriebsstunden(1, 15000)  # Existiert
aktualisiere_betriebsstunden(999, 5000)  # Existiert nicht
```

---

#### b) Wartungen löschen

```python
from datetime import datetime, timedelta

def loesche_alte_wartungen(tage_alt):
    """
    Löscht Wartungen älter als tage_alt Tage.
    Gibt Anzahl gelöschter Zeilen zurück.
    """
    conn = sqlite3.connect('testdaten/produktionsdb.db')
    conn.execute('PRAGMA foreign_keys = ON')  # FK-Constraints aktivieren
    cursor = conn.cursor()
    
    try:
        # Berechne Stichtag
        stichtag = (datetime.now() - timedelta(days=tage_alt)).strftime('%Y-%m-%d')
        
        # DELETE mit Datum-Filter
        cursor.execute('''
            DELETE FROM Wartungen 
            WHERE Datum < ?
        ''', (stichtag,))
        
        anzahl_geloescht = cursor.rowcount
        conn.commit()
        
        print(f"{anzahl_geloescht} Wartungen älter als {tage_alt} Tage gelöscht (vor {stichtag})")
        return anzahl_geloescht
        
    except sqlite3.IntegrityError as e:
        print(f"Foreign Key Constraint verletzt: {e}")
        print("Hinweis: Andere Tabellen verweisen noch auf diese Wartungen")
        conn.rollback()
        return 0
        
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        conn.rollback()
        return 0
        
    finally:
        cursor.close()
        conn.close()

# Test
anzahl = loesche_alte_wartungen(365)  # Lösche Wartungen älter als 1 Jahr
```

---

#### c) Maschine außer Betrieb setzen (Transaktion)

```python
from datetime import datetime

def deaktiviere_maschine_mit_wartungen(maschinen_id):
    """
    Setzt Maschine auf Inaktiv UND erstellt Wartungseintrag.
    Beide Operationen in EINER Transaktion (Atomicity).
    """
    conn = sqlite3.connect('testdaten/produktionsdb.db')
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()
    
    try:
        cursor.execute('BEGIN')
        
        # Operation 1: Maschine deaktivieren
        cursor.execute('''
            UPDATE Maschinen 
            SET Status = 'Außer Betrieb'
            WHERE Maschinen_ID = ?
        ''', (maschinen_id,))
        
        if cursor.rowcount == 0:
            raise ValueError(f"Maschine {maschinen_id} nicht gefunden")
        
        # Operation 2: Wartungseintrag erstellen
        cursor.execute('''
            INSERT INTO Wartungen (Maschinen_ID, Datum, Typ, Beschreibung, Kosten)
            VALUES (?, ?, 'Stilllegung', 'Maschine außer Betrieb gesetzt', 0.0)
        ''', (maschinen_id, datetime.now().strftime('%Y-%m-%d')))
        
        conn.commit()
        print(f"Maschine {maschinen_id} wurde deaktiviert und Wartungseintrag erstellt")
        
    except ValueError as e:
        print(f"Fehler: {e}")
        conn.rollback()
        
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        print("Rollback: Keine der beiden Operationen wurde durchgeführt")
        conn.rollback()
        
    finally:
        cursor.close()
        conn.close()

# Test
deaktiviere_maschine_mit_wartungen(2)  # Erfolgreich
deaktiviere_maschine_mit_wartungen(999)  # Fehler: Maschine nicht gefunden
```

---

#### d) + e) Fehlerbehandlung testen & CASCADE DELETE

**Test-Setup mit CASCADE**:

```python
# Schema mit CASCADE (in init_produktionsdb.py bereits vorhanden)
CREATE TABLE Wartungen (
    Wartungs_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Maschinen_ID INTEGER NOT NULL,
    Datum TEXT NOT NULL,
    Typ TEXT NOT NULL,
    Kosten REAL,
    Beschreibung TEXT,
    FOREIGN KEY (Maschinen_ID) REFERENCES Maschinen(Maschinen_ID) 
        ON DELETE CASCADE  -- Automatisches Löschen bei Maschinen-Löschung
);

# Test: Maschine mit zugehörigen Wartungen löschen
conn = sqlite3.connect('testdaten/produktionsdb.db')
conn.execute('PRAGMA foreign_keys = ON')  # WICHTIG!
cursor = conn.cursor()

# Zähle Wartungen vor dem Löschen
cursor.execute('SELECT COUNT(*) FROM Wartungen WHERE Maschinen_ID = 1')
print(f"Wartungen für Maschine 1 (vorher): {cursor.fetchone()[0]}")

# Lösche Maschine → Wartungen werden automatisch gelöscht
cursor.execute('DELETE FROM Maschinen WHERE Maschinen_ID = 1')
conn.commit()

# Zähle Wartungen nach dem Löschen
cursor.execute('SELECT COUNT(*) FROM Wartungen WHERE Maschinen_ID = 1')
print(f"Wartungen für Maschine 1 (nachher): {cursor.fetchone()[0]}")  # 0

conn.close()
```

**Ohne CASCADE** (Fehler-Test):

```sql
-- Ohne ON DELETE CASCADE:
CREATE TABLE Wartungen_NoCascade (
    ...
    FOREIGN KEY (Maschinen_ID) REFERENCES Maschinen(Maschinen_ID)
    -- Kein CASCADE!
);

-- Versuch, Maschine zu löschen:
DELETE FROM Maschinen WHERE Maschinen_ID = 1;
-- Fehler: FOREIGN KEY constraint failed
-- Wartungen existieren noch und verweisen auf Maschine 1!
```

---

### P3: Transaktionen mit Rollback

Aufgrund der Komplexität hier eine kompakte, vollständige Lösung für Teil a-b:

```python
import sqlite3
from datetime import datetime

def starte_produktionslauf(maschinen_id, artikel, menge, material_verbrauch):
    """
    Startet Produktionslauf mit atomarer Transaktion.
    material_verbrauch = {Material_ID: menge, ...}
    """
    conn = sqlite3.connect('testdaten/produktionsdb.db')
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()
    
    try:
        cursor.execute('BEGIN')
        
        # Operation 1: Prüfe Maschinenstatus
        cursor.execute('SELECT Status FROM Maschinen WHERE Maschinen_ID = ?', (maschinen_id,))
        result = cursor.fetchone()
        
        if not result:
            raise ValueError(f"Maschine {maschinen_id} nicht gefunden")
        
        if result[0] != 'Bereit':
            raise ValueError(f"Maschine nicht bereit (Status: {result[0]})")
        
        # Operation 2: Materialbestand reduzieren
        for material_id, menge_verbraucht in material_verbrauch.items():
            cursor.execute('SELECT Menge_Lager FROM Materialbestand WHERE Material_ID = ?', (material_id,))
            result = cursor.fetchone()
            
            if not result:
                raise ValueError(f"Material {material_id} nicht gefunden")
            
            if result[0] < menge_verbraucht:
                raise ValueError(
                    f"Materialbestand nicht ausreichend (ID {material_id}): "
                    f"{result[0]} vorhanden, {menge_verbraucht} benötigt"
                )
            
            cursor.execute('''
                UPDATE Materialbestand 
                SET Menge_Lager = Menge_Lager - ? 
                WHERE Material_ID = ?
            ''', (menge_verbraucht, material_id))
        
        # Operation 3: Maschinenstatus aktualisieren
        cursor.execute('''
            UPDATE Maschinen 
            SET Status = 'Produktion' 
            WHERE Maschinen_ID = ?
        ''', (maschinen_id,))
        
        # Operation 4: Produktionslauf einfügen
        cursor.execute('''
            INSERT INTO Produktionslaeufe (Maschinen_ID, Artikel, Menge_Geplant, Start_Zeit, Status)
            VALUES (?, ?, ?, ?, 'Laufend')
        ''', (maschinen_id, artikel, menge, datetime.now().isoformat()))
        
        lauf_id = cursor.lastrowid
        
        conn.commit()
        print(f"Produktionslauf {lauf_id} gestartet auf Maschine {maschinen_id}")
        return lauf_id
        
    except ValueError as e:
        print(f"Fehler: {e}")
        print("ROLLBACK: Keine Änderungen an Datenbank")
        conn.rollback()
        return None
        
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        conn.rollback()
        return None
        
    finally:
        cursor.close()
        conn.close()

# Test-Szenarien
# Erfolg: Maschine bereit, Material vorhanden
starte_produktionslauf(1, "Zahnrad Z42", 100, {101: 50, 102: 20})

# Fehler 1: Maschine nicht bereit
starte_produktionslauf(2, "Welle W15", 50, {101: 30})  # Falls Status != 'Bereit'

# Fehler 2: Material nicht ausreichend
starte_produktionslauf(1, "Gehäuse G08", 200, {101: 9999})  # Zu viel Material
```

Die Lösungen für P3c-e (Savepoints, Logging, Context Manager), P4 (vollständiges pandas+matplotlib Skript) und P5 (komplettes Dashboard-Projekt) würden weitere ~400-500 Zeilen Code umfassen. Soll ich diese auch noch vollständig ausarbeiten?

---

### P4: Aggregationen und Visualisierung mit pandas + matplotlib

**Vollständiges Skript**:

```python
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Verbindung zur Datenbank
conn = sqlite3.connect('testdaten/produktionsdb.db')

# a) Daten abfragen mit JOIN und Quartal-Extraktion
query = '''
SELECT 
    m.Typ,
    strftime('%Y', w.Datum) || '-Q' || 
        ((CAST(strftime('%m', w.Datum) AS INTEGER) - 1) / 3 + 1) AS Quartal,
    SUM(w.Kosten) AS Gesamt_Kosten,
    COUNT(*) AS Anzahl_Wartungen
FROM Maschinen m
INNER JOIN Wartungen w ON m.Maschinen_ID = w.Maschinen_ID
WHERE strftime('%Y', w.Datum) IN ('2023', '2024')
GROUP BY m.Typ, Quartal
ORDER BY Quartal, m.Typ
'''

# b) pandas DataFrame laden
df = pd.read_sql_query(query, conn)
conn.close()

print("=== Rohdaten ===")
print(df.head(10))

# c) Datenbereinigung
df['Gesamt_Kosten'] = df['Gesamt_Kosten'].astype(float)
df = df.sort_values(['Quartal', 'Typ'])

# d) Pivot-Tabelle erstellen
pivot = pd.pivot_table(
    df,
    values='Gesamt_Kosten',
    index='Quartal',
    columns='Typ',
    aggfunc='sum',
    fill_value=0
)

print("\n=== Pivot-Tabelle ===")
print(pivot)

# e) Visualisierung 1: Gestapeltes Balkendiagramm
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Plot 1: Gestapeltes Balkendiagramm
pivot.plot(kind='bar', stacked=True, ax=ax1, colormap='tab10')
ax1.set_title('Wartungskosten nach Quartal und Maschinentyp', fontsize=14, fontweight='bold')
ax1.set_xlabel('Quartal', fontsize=12)
ax1.set_ylabel('Wartungskosten (€)', fontsize=12)
ax1.legend(title='Maschinentyp', bbox_to_anchor=(1.05, 1), loc='upper left')
ax1.grid(axis='y', alpha=0.3)
ax1.tick_params(axis='x', rotation=45)

# Plot 2: Liniendiagramm für Trend-Analyse
pivot.plot(kind='line', ax=ax2, marker='o', linewidth=2)
ax2.set_title('Wartungskosten-Trend nach Maschinentyp', fontsize=14, fontweight='bold')
ax2.set_xlabel('Quartal', fontsize=12)
ax2.set_ylabel('Wartungskosten (€)', fontsize=12)
ax2.legend(title='Maschinentyp', bbox_to_anchor=(1.05, 1), loc='upper left')
ax2.grid(alpha=0.3)

# Maximalwerte markieren
for col in pivot.columns:
    max_idx = pivot[col].idxmax()
    max_val = pivot[col].max()
    if max_val > 0:
        ax2.annotate(
            f'{max_val:.0f}€',
            xy=(pivot.index.get_loc(max_idx), max_val),
            xytext=(10, 10),
            textcoords='offset points',
            fontsize=9,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5)
        )

plt.tight_layout()
plt.savefig('wartungskosten_analyse.png', dpi=300, bbox_inches='tight')
print("\n✅ Plots gespeichert: wartungskosten_analyse.png")
plt.close()

# f) Statistik-Ausgabe
print("\n=== Statistik ===")

# Durchschnittliche Kosten pro Wartung nach Typ
df_stats = df.copy()
df_stats['Kosten_pro_Wartung'] = df_stats['Gesamt_Kosten'] / df_stats['Anzahl_Wartungen']
avg_kosten = df_stats.groupby('Typ')['Kosten_pro_Wartung'].mean()
print("\nDurchschnittliche Kosten pro Wartung nach Typ:")
print(avg_kosten.sort_values(ascending=False))

# Typ mit höchsten Gesamtkosten
typ_max = df.groupby('Typ')['Gesamt_Kosten'].sum().idxmax()
kosten_max = df.groupby('Typ')['Gesamt_Kosten'].sum().max()
print(f"\nTyp mit höchsten Gesamtkosten: {typ_max} ({kosten_max:.2f}€)")

# Quartal mit höchsten Gesamtkosten
quartal_max = df.groupby('Quartal')['Gesamt_Kosten'].sum().idxmax()
kosten_quartal_max = df.groupby('Quartal')['Gesamt_Kosten'].sum().max()
print(f"Quartal mit höchsten Gesamtkosten: {quartal_max} ({kosten_quartal_max:.2f}€)")

# g) Export als Excel
pivot.to_excel('wartungskosten_analyse.xlsx', sheet_name='Kosten_Quartal', engine='openpyxl')
print("\n✅ Excel-Export: wartungskosten_analyse.xlsx")
```

**Erwartete Ausgabe**:
- 2 PNG-Dateien (gestapeltes Balkendiagramm + Liniendiagramm mit Annotationen)
- Excel-Datei mit Pivot-Tabelle
- Konsolen-Ausgabe mit Statistiken

---

### P5: Projekt – Qualitätskontroll-Dashboard

**Vollständiges Lösungsskript** (gekürzt auf Kernkomponenten):

```python
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# ==================== a) Schema und Beispieldaten ====================

conn = sqlite3.connect('testdaten/produktionsdb.db')
conn.execute('PRAGMA foreign_keys = ON')
cursor = conn.cursor()

# Tabellen erstellen
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pruefprotokolle (
    Pruef_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Lauf_ID INTEGER NOT NULL,
    Artikel TEXT NOT NULL,
    Pruef_Datum TEXT NOT NULL,
    Pruef_Typ TEXT NOT NULL,
    Pruef_Wert REAL,
    Soll_Wert REAL,
    Toleranz REAL,
    Status TEXT CHECK(Status IN ('Bestanden', 'Fehlgeschlagen', 'Nacharbeit')),
    Pruefer_Name TEXT,
    Bemerkung TEXT,
    FOREIGN KEY (Lauf_ID) REFERENCES Produktionslaeufe(Lauf_ID) ON DELETE CASCADE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Fehlerarten (
    Fehler_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Pruef_ID INTEGER NOT NULL,
    Fehlerart TEXT NOT NULL,
    Schweregrad INTEGER CHECK(Schweregrad BETWEEN 1 AND 5),
    Beschreibung TEXT,
    FOREIGN KEY (Pruef_ID) REFERENCES Pruefprotokolle(Pruef_ID) ON DELETE CASCADE
)
''')

# Indizes erstellen
cursor.execute('CREATE INDEX IF NOT EXISTS idx_pruef_lauf ON Pruefprotokolle(Lauf_ID)')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_pruef_status ON Pruefprotokolle(Status)')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_fehler_pruef ON Fehlerarten(Pruef_ID)')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_fehler_art ON Fehlerarten(Fehlerart)')

# 30+ Prüfprotokolle generieren
import random
artikel_liste = ['Zahnrad Z42', 'Welle W15', 'Gehäuse G08']
pruef_typen = ['Sichtprüfung', 'Maßprüfung', 'Funktionstest']
pruefer = ['Anna Schmidt', 'Ben Müller', 'Clara Wagner']
status_weights = [0.7, 0.2, 0.1]  # 70% bestanden, 20% fehlgeschlagen, 10% nacharbeit

for i in range(35):
    lauf_id = random.randint(1, 10)
    artikel = random.choice(artikel_liste)
    pruef_typ = random.choice(pruef_typen)
    soll_wert = 50.0 if pruef_typ == 'Maßprüfung' else 100.0
    toleranz = 0.05 if pruef_typ == 'Maßprüfung' else 5.0
    pruef_wert = soll_wert + random.uniform(-toleranz*2, toleranz*2)
    
    # Status bestimmen
    abweichung = abs(pruef_wert - soll_wert)
    if abweichung <= toleranz:
        status = 'Bestanden'
    elif abweichung <= toleranz * 1.5:
        status = 'Nacharbeit'
    else:
        status = 'Fehlgeschlagen'
    
    # Gewichtete Status-Verteilung erzwingen
    status = random.choices(['Bestanden', 'Fehlgeschlagen', 'Nacharbeit'], weights=status_weights)[0]
    
    datum = (datetime.now() - timedelta(days=random.randint(0, 90))).strftime('%Y-%m-%d')
    
    cursor.execute('''
        INSERT INTO Pruefprotokolle 
        (Lauf_ID, Artikel, Pruef_Datum, Pruef_Typ, Pruef_Wert, Soll_Wert, Toleranz, Status, Pruefer_Name)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (lauf_id, artikel, datum, pruef_typ, pruef_wert, soll_wert, toleranz, status, random.choice(pruefer)))
    
    # Fehlerarten für fehlgeschlagene Tests
    if status == 'Fehlgeschlagen':
        pruef_id = cursor.lastrowid
        fehlerarten_liste = ['Maßabweichung', 'Oberflächenfehler', 'Funktionsstörung']
        cursor.execute('''
            INSERT INTO Fehlerarten (Pruef_ID, Fehlerart, Schweregrad, Beschreibung)
            VALUES (?, ?, ?, ?)
        ''', (pruef_id, random.choice(fehlerarten_liste), random.randint(2, 5), 'Automatisch generiert'))

conn.commit()
print("✅ Schema und Testdaten erstellt")

# ==================== b) Komplexe JOIN-Queries ====================

# Query 1: Qualitätsübersicht nach Maschine
query1 = '''
SELECT 
    m.Name AS Maschine,
    m.Typ,
    COUNT(DISTINCT pl.Lauf_ID) AS Anzahl_Laeufe,
    COUNT(pp.Pruef_ID) AS Anzahl_Pruefungen,
    SUM(CASE WHEN pp.Status = 'Bestanden' THEN 1 ELSE 0 END) AS Bestanden,
    SUM(CASE WHEN pp.Status = 'Fehlgeschlagen' THEN 1 ELSE 0 END) AS Fehlgeschlagen,
    ROUND(
        SUM(CASE WHEN pp.Status = 'Fehlgeschlagen' THEN 1 ELSE 0 END) * 100.0 / COUNT(pp.Pruef_ID),
        2
    ) AS Fehlerquote_Prozent
FROM Maschinen m
LEFT JOIN Produktionslaeufe pl ON m.Maschinen_ID = pl.Maschinen_ID
LEFT JOIN Pruefprotokolle pp ON pl.Lauf_ID = pp.Lauf_ID
GROUP BY m.Maschinen_ID
HAVING COUNT(pp.Pruef_ID) > 0
ORDER BY Fehlerquote_Prozent DESC
'''

df_qualitaet = pd.read_sql_query(query1, conn)
print("\n=== Query 1: Qualitätsübersicht ===")
print(df_qualitaet)

# Query 2: Problem-Artikel identifizieren
query2 = '''
SELECT 
    pp.Artikel,
    COUNT(*) AS Anzahl_Pruefungen,
    SUM(CASE WHEN pp.Status = 'Fehlgeschlagen' THEN 1 ELSE 0 END) AS Anzahl_Fehler,
    (SELECT fa.Fehlerart 
     FROM Fehlerarten fa 
     JOIN Pruefprotokolle pp2 ON fa.Pruef_ID = pp2.Pruef_ID
     WHERE pp2.Artikel = pp.Artikel
     GROUP BY fa.Fehlerart
     ORDER BY COUNT(*) DESC LIMIT 1) AS Haeufigste_Fehlerart,
    AVG(fa.Schweregrad) AS Durchschn_Schweregrad
FROM Pruefprotokolle pp
LEFT JOIN Fehlerarten fa ON pp.Pruef_ID = fa.Pruef_ID
WHERE pp.Status = 'Fehlgeschlagen'
GROUP BY pp.Artikel
HAVING COUNT(*) > 3
ORDER BY Anzahl_Fehler DESC
'''

df_probleme = pd.read_sql_query(query2, conn)
print("\n=== Query 2: Problem-Artikel ===")
print(df_probleme)

# ==================== c) + d) Subqueries und pandas Aggregationen ====================

# Query 4: Maschinen mit überdurchschnittlicher Fehlerquote (Subquery)
query4 = '''
WITH Fehlerquoten AS (
    SELECT 
        m.Name,
        ROUND(
            SUM(CASE WHEN pp.Status = 'Fehlgeschlagen' THEN 1 ELSE 0 END) * 100.0 / COUNT(pp.Pruef_ID),
            2
        ) AS Fehlerquote
    FROM Maschinen m
    JOIN Produktionslaeufe pl ON m.Maschinen_ID = pl.Maschinen_ID
    JOIN Pruefprotokolle pp ON pl.Lauf_ID = pp.Lauf_ID
    GROUP BY m.Maschinen_ID
)
SELECT Name, Fehlerquote
FROM Fehlerquoten
WHERE Fehlerquote > (SELECT AVG(Fehlerquote) FROM Fehlerquoten)
ORDER BY Fehlerquote DESC
'''

df_ueberdurchschnitt = pd.read_sql_query(query4, conn)
print("\n=== Query 4: Überdurchschnittliche Fehlerquote ===")
print(df_ueberdurchschnitt)

# pandas: First Pass Yield berechnen
df_qualitaet['FPY'] = (df_qualitaet['Bestanden'] / df_qualitaet['Anzahl_Pruefungen'] * 100).round(2)
kritische_maschinen = df_qualitaet[df_qualitaet['FPY'] < 80]
print("\n=== Kritische Maschinen (FPY < 80%) ===")
print(kritische_maschinen)

# CSV-Export
df_qualitaet.to_csv('qualitaetsuebersicht.csv', index=False, encoding='utf-8')
print("\n✅ CSV-Export: qualitaetsuebersicht.csv")

# ==================== e) Visualisierung (3 Plots) ====================

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 14))

# Plot 1: Fehlerquote nach Maschine (Balkendiagramm mit Farben)
colors = ['green' if fq < 5 else 'yellow' if fq < 10 else 'red' 
          for fq in df_qualitaet['Fehlerquote_Prozent']]
ax1.barh(df_qualitaet['Maschine'], df_qualitaet['Fehlerquote_Prozent'], color=colors)
ax1.axvline(x=5, color='orange', linestyle='--', linewidth=2, label='Soll-Wert (5%)')
ax1.set_xlabel('Fehlerquote (%)', fontsize=11)
ax1.set_ylabel('Maschine', fontsize=11)
ax1.set_title('Fehlerquote nach Maschine', fontsize=13, fontweight='bold')
ax1.legend()
ax1.grid(axis='x', alpha=0.3)

# Plot 2: Heatmap - Fehlerarten nach Artikel (vereinfacht)
query_heatmap = '''
SELECT pp.Artikel, fa.Fehlerart, COUNT(*) AS Anzahl
FROM Pruefprotokolle pp
JOIN Fehlerarten fa ON pp.Pruef_ID = fa.Pruef_ID
GROUP BY pp.Artikel, fa.Fehlerart
'''
df_heatmap = pd.read_sql_query(query_heatmap, conn)
heatmap_pivot = df_heatmap.pivot(index='Artikel', columns='Fehlerart', values='Anzahl').fillna(0)

im = ax2.imshow(heatmap_pivot.values, cmap='YlOrRd', aspect='auto')
ax2.set_xticks(range(len(heatmap_pivot.columns)))
ax2.set_yticks(range(len(heatmap_pivot.index)))
ax2.set_xticklabels(heatmap_pivot.columns, rotation=45, ha='right')
ax2.set_yticklabels(heatmap_pivot.index)
ax2.set_title('Fehlerarten nach Artikel (Heatmap)', fontsize=13, fontweight='bold')
plt.colorbar(im, ax=ax2, label='Anzahl Fehler')

# Plot 3: Zeitreihe - Fehlerquote über Zeit (Wochen)
query_zeitreihe = '''
SELECT 
    pp.Artikel,
    strftime('%Y-W%W', pp.Pruef_Datum) AS Woche,
    COUNT(*) AS Gesamt,
    SUM(CASE WHEN pp.Status = 'Fehlgeschlagen' THEN 1 ELSE 0 END) AS Fehler
FROM Pruefprotokolle pp
GROUP BY pp.Artikel, Woche
ORDER BY Woche
'''
df_zeit = pd.read_sql_query(query_zeitreihe, conn)
df_zeit['Fehlerquote'] = (df_zeit['Fehler'] / df_zeit['Gesamt'] * 100).round(2)

for artikel in df_zeit['Artikel'].unique():
    df_artikel = df_zeit[df_zeit['Artikel'] == artikel]
    ax3.plot(df_artikel['Woche'], df_artikel['Fehlerquote'], marker='o', label=artikel, linewidth=2)
    
    # Markiere Wochen mit >15% Fehlerquote
    kritisch = df_artikel[df_artikel['Fehlerquote'] > 15]
    if not kritisch.empty:
        ax3.scatter(kritisch['Woche'], kritisch['Fehlerquote'], 
                   color='red', s=100, zorder=5, marker='X')

ax3.axhline(y=15, color='red', linestyle='--', linewidth=1.5, alpha=0.7, label='Kritisch (>15%)')
ax3.set_xlabel('Woche', fontsize=11)
ax3.set_ylabel('Fehlerquote (%)', fontsize=11)
ax3.set_title('Fehlerquote-Trend über Zeit', fontsize=13, fontweight='bold')
ax3.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax3.grid(alpha=0.3)
ax3.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('qualitaetskontrolle_dashboard.png', dpi=300, bbox_inches='tight')
print("\n✅ Dashboard-Plots gespeichert: qualitaetskontrolle_dashboard.png")
plt.close()

conn.close()
print("\n✅ Projekt P5 abgeschlossen!")
```

**Abgabe-Dateien**:
- `p5_qualitaetskontrolle.py` (obiges Skript)
- `qualitaetsuebersicht.csv`
- `qualitaetskontrolle_dashboard.png` (3 Plots)
- `produktionsdb.db` (erweiterte Datenbank)

---

