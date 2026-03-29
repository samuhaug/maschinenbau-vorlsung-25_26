# V19 – Datenbanken – Teil 1

**Vorlesungsinhalte:**
- Informatik-Theorie: Datenbanken – Teil 1 (Relationale Datenbanken, SQL-Grundlagen)
- Python-Praxis: Datenbankverbindung & SQL – Teil 1 (SQLite-Grundlagen)

---

## 📚 Informatik-Theorie: Datenbanken – Teil 1

### Einführung in Datenbanksysteme

Datenbanksysteme sind das Rückgrat moderner Anwendungen. In nahezu jedem professionellen Software-System werden Daten dauerhaft gespeichert, abgefragt und verwaltet. Eine **Datenbank** ist eine strukturierte Sammlung von Daten, die effizient gespeichert, abgefragt und verwaltet werden kann. Ein **Datenbankmanagementsystem (DBMS)** ist die Software, die den Zugriff auf die Datenbank koordiniert, Datenintegrität sicherstellt und Mehrbenutzerzugriff ermöglicht.

> [!NOTE]
> Ein **Datenbankmanagementsystem (DBMS)** ist eine Softwareschicht zwischen Anwendungen und den physischen Datendateien. Es verwaltet Speicherung, Abfrage, Sicherheit und Transaktionen. Beispiele sind PostgreSQL, MySQL, Oracle Database, Microsoft SQL Server und SQLite.

Datenbanksysteme lösen fundamentale Probleme, die bei dateibasierter Speicherung auftreten:

**Datenredundanz**: Bei Verwendung separater Dateien (z.B. Excel-Tabellen für verschiedene Abteilungen) werden dieselben Daten oft mehrfach gespeichert. Dies führt zu Inkonsistenzen, wenn Updates nur in einer Kopie vorgenommen werden. Ein DBMS zentralisiert Daten und vermeidet Redundanz durch **Normalisierung**.

**Datenintegrität**: Ohne zentrale Kontrolle können ungültige Daten in das System gelangen (z.B. negative Stückzahlen, Verweise auf nicht-existierende Datensätze). Ein DBMS erzwingt **Integritätsbedingungen** automatisch.

**Gleichzeitiger Zugriff**: Wenn mehrere Benutzer gleichzeitig dieselbe Datei bearbeiten, können Konflikte entstehen (z.B. verlorene Updates). DBMS bieten **Transaktionsverwaltung** mit ACID-Eigenschaften.

**Zugriffskontrolle**: Nicht jeder Benutzer soll alle Daten sehen oder ändern dürfen. DBMS bieten feingranulare **Berechtigungssysteme**.

**Datenwiederherstellung**: Bei Systemabstürzen können Daten verloren gehen. DBMS bieten **Backup-Mechanismen** und **Recovery-Funktionen**.

### Das Relationale Datenbankmodell

Das **relationale Datenbankmodell** wurde 1970 von Edgar F. Codd eingeführt und ist heute das dominierende Modell. Es basiert auf mathematischer Mengenlehre und Relationen-Algebra.

> [!NOTE]
> Eine **Relation** (umgangssprachlich: **Tabelle**) ist eine Menge von Tupeln (Zeilen), die alle dieselbe Struktur haben. Jedes Tupel besteht aus Attributen (Spalten) mit definierten Datentypen.

#### Grundbegriffe

**Tabelle (Table)**: Eine Tabelle repräsentiert eine Entitätsmenge (z.B. alle Maschinen, alle Aufträge, alle Mitarbeiter). Jede Zeile ist ein konkretes Objekt dieser Menge.

**Zeile (Row / Tuple)**: Eine Zeile enthält alle Informationen zu einem einzelnen Datenobjekt. Beispiel: Eine Maschine mit ID, Typ, Baujahr, Standort.

**Spalte (Column / Attribute)**: Eine Spalte definiert eine Eigenschaft, die alle Objekte der Tabelle haben. Beispiel: `Maschinentyp`, `Baujahr`, `Wartungsintervall_Tage`.

**Primärschlüssel (Primary Key)**: Ein Attribut (oder eine Kombination von Attributen), das jede Zeile eindeutig identifiziert. Primärschlüssel dürfen nicht `NULL` sein und müssen unique sein. Beispiel: `Maschinen_ID` in der Tabelle `Maschinen`.

> [!WARNING]
> Ein guter Primärschlüssel ist unveränderlich. Verwende keine natürlichen Schlüssel wie "Mitarbeiternummer", wenn diese sich ändern könnte. Bevorzuge **künstliche Schlüssel** (Surrogate Keys) wie Auto-Increment-IDs.

**Fremdschlüssel (Foreign Key)**: Ein Attribut in einer Tabelle, das auf den Primärschlüssel einer anderen Tabelle verweist. Dies modelliert Beziehungen zwischen Tabellen. Beispiel: `Maschinen_ID` in der Tabelle `Wartungsprotokolle` verweist auf `Maschinen_ID` in `Maschinen`.

> [!NOTE]
> Ein **Fremdschlüssel** stellt **referentielle Integrität** sicher: Es können keine Wartungsprotokolle für nicht-existierende Maschinen angelegt werden. Das DBMS erzwingt dies automatisch.

#### Beispiel: Produktionsüberwachung

Wir modellieren ein System zur Überwachung von CNC-Maschinen:

**Tabelle: Maschinen**
| Maschinen_ID | Maschinentyp       | Baujahr | Standort      | Wartungsintervall_Tage |
|--------------|-------------------|---------|---------------|------------------------|
| 1            | CNC-Fräse DMU 50  | 2018    | Halle A1      | 90                     |
| 2            | Drehmaschine CTX  | 2020    | Halle B2      | 120                    |
| 3            | Laserschneider    | 2019    | Halle C3      | 60                     |

**Tabelle: Wartungsprotokolle**
| Protokoll_ID | Maschinen_ID | Wartungsdatum | Wartungstyp           | Dauer_Stunden | Kosten_Euro |
|--------------|--------------|---------------|-----------------------|---------------|-------------|
| 1            | 1            | 2024-01-15    | Routineinspektion     | 2.5           | 350.00      |
| 2            | 1            | 2024-04-20    | Öl- und Filterwechsel | 1.0           | 180.00      |
| 3            | 2            | 2024-02-10    | Routineinspektion     | 3.0           | 420.00      |
| 4            | 3            | 2024-03-05    | Laserreinigung        | 0.5           | 90.00       |

In diesem Modell ist `Maschinen_ID` der Primärschlüssel in `Maschinen` und ein Fremdschlüssel in `Wartungsprotokolle`. Jedes Wartungsprotokoll ist genau einer Maschine zugeordnet.

### Beziehungstypen (Kardinalitäten)

Relationale Datenbanken modellieren drei Arten von Beziehungen:

**1:1 (Eins-zu-Eins)**: Jedem Datensatz in Tabelle A ist höchstens ein Datensatz in Tabelle B zugeordnet und umgekehrt. Beispiel: Jede Maschine hat genau ein elektronisches Typenschild mit erweiterten Metadaten. Diese Beziehung ist selten; oft werden 1:1-Tabellen zusammengelegt.

**1:n (Eins-zu-Viele)**: Jedem Datensatz in Tabelle A können mehrere Datensätze in Tabelle B zugeordnet sein, aber jeder Datensatz in B gehört zu genau einem Datensatz in A. Beispiel: Eine Maschine (1) hat viele Wartungsprotokolle (n). Dies ist der häufigste Beziehungstyp.

**m:n (Viele-zu-Viele)**: Jedem Datensatz in A können mehrere Datensätze in B zugeordnet sein und umgekehrt. Beispiel: Mitarbeiter (m) können an mehreren Projekten (n) arbeiten, und Projekte haben mehrere Mitarbeiter. Diese Beziehung wird durch eine **Zwischentabelle** (Junction Table) modelliert.

> [!TIP]
> **m:n-Beziehung auflösen**: Erstelle eine Zwischentabelle mit Fremdschlüsseln zu beiden Tabellen.
> 
> Beispiel: `Mitarbeiter` ↔ `Projektzuordnung` ↔ `Projekte`
> 
> Tabelle `Projektzuordnung`:
> | Mitarbeiter_ID | Projekt_ID | Rolle              | Anteil_Prozent |
> |----------------|------------|--------------------|----------------|
> | 1              | 10         | Projektleiter      | 50             |
> | 1              | 11         | Berater            | 20             |
> | 2              | 10         | Entwickler         | 100            |

### SQL: Structured Query Language

**SQL** ist die Standardsprache zur Interaktion mit relationalen Datenbanken. Sie wurde in den 1970er Jahren bei IBM entwickelt und ist heute ein ISO/IEC-Standard (SQL:2023 ist die aktuelle Version). SQL ist **deklarativ**: Man beschreibt, *was* man haben möchte, nicht *wie* das DBMS es berechnen soll.

> [!NOTE]
> **SQL** (Structured Query Language) ist eine deklarative Sprache für relationale Datenbanken. SQL-Anweisungen werden in Kategorien eingeteilt: **DDL** (Data Definition Language) für Schema-Definition, **DML** (Data Manipulation Language) für Datenänderungen, **DQL** (Data Query Language) für Abfragen und **DCL** (Data Control Language) für Berechtigungen.

#### SQL-Sprachkategorien

**DDL (Data Definition Language)**: Befehle zur Definition von Datenbankstrukturen (Tabellen, Indizes, Views).
- `CREATE TABLE`: Neue Tabelle erstellen
- `ALTER TABLE`: Tabellenstruktur ändern
- `DROP TABLE`: Tabelle löschen
- `CREATE INDEX`: Index erstellen

**DML (Data Manipulation Language)**: Befehle zur Änderung von Daten.
- `INSERT`: Neue Zeilen einfügen
- `UPDATE`: Bestehende Zeilen ändern
- `DELETE`: Zeilen löschen

**DQL (Data Query Language)**: Befehle zum Abfragen von Daten.
- `SELECT`: Daten abfragen (mit `FROM`, `WHERE`, `JOIN`, `GROUP BY`, `HAVING`, `ORDER BY`)

**DCL (Data Control Language)**: Befehle zur Berechtigungsverwaltung.
- `GRANT`: Berechtigungen erteilen
- `REVOKE`: Berechtigungen entziehen

### CREATE TABLE: Tabellen definieren

Die `CREATE TABLE`-Anweisung definiert eine neue Tabelle mit ihrem Schema (Spalten, Datentypen, Constraints).

**Syntax (vereinfacht)**:
```sql
CREATE TABLE Tabellenname (
    Spalte1 Datentyp [Constraints],
    Spalte2 Datentyp [Constraints],
    ...
    [Tabellenconstraints]
);
```

**Datentypen (SQLite-Syntax, andere DBMS haben mehr Typen)**:
- `INTEGER`: Ganzzahl (SQLite speichert 1-8 Bytes je nach Größe)
- `REAL`: Fließkommazahl (8 Bytes, IEEE 754)
- `TEXT`: Zeichenkette (UTF-8, unbegrenzte Länge in SQLite)
- `BLOB`: Binary Large Object (Binärdaten wie Bilder, PDFs)
- `NUMERIC`: Numerischer Wert (SQLite konvertiert automatisch)

> [!WARNING]
> SQLite hat ein sehr flexibles Typsystem (Dynamic Typing). Andere SQL-Datenbanken wie PostgreSQL oder MySQL sind strikter. Achte auf **Portabilität**, wenn du später migrieren musst.

**Constraints (Integritätsbedingungen)**:
- `PRIMARY KEY`: Primärschlüssel (eindeutig, nicht NULL)
- `UNIQUE`: Wert muss unique sein (aber NULL ist erlaubt)
- `NOT NULL`: Wert darf nicht NULL sein
- `DEFAULT wert`: Standardwert, wenn kein Wert angegeben wird
- `CHECK (bedingung)`: Prüft eine Bedingung (z.B. `CHECK (Temperatur >= -273.15)`)
- `FOREIGN KEY`: Fremdschlüssel (referentielle Integrität)

> [!TIP]
> **Beispiel: Maschinen-Tabelle erstellen**
> ```sql
> CREATE TABLE Maschinen (
>     Maschinen_ID INTEGER PRIMARY KEY,
>     Maschinentyp TEXT NOT NULL,
>     Baujahr INTEGER CHECK (Baujahr >= 1900 AND Baujahr <= 2100),
>     Standort TEXT NOT NULL,
>     Wartungsintervall_Tage INTEGER DEFAULT 90,
>     Anschaffungsdatum DATE,
>     Anschaffungskosten_Euro REAL CHECK (Anschaffungskosten_Euro >= 0)
> );
> ```

#### AUTO_INCREMENT / AUTOINCREMENT

Primärschlüssel werden oft automatisch vergeben. In SQLite verwendet man `INTEGER PRIMARY KEY`, was automatisch auto-increment aktiviert (in anderen SQL-Dialekten: `AUTO_INCREMENT`, `SERIAL`, `IDENTITY`).

```sql
CREATE TABLE Wartungsprotokolle (
    Protokoll_ID INTEGER PRIMARY KEY,  -- Auto-Increment in SQLite
    Maschinen_ID INTEGER NOT NULL,
    Wartungsdatum DATE NOT NULL,
    Wartungstyp TEXT NOT NULL,
    Dauer_Stunden REAL CHECK (Dauer_Stunden > 0),
    Kosten_Euro REAL CHECK (Kosten_Euro >= 0),
    Notizen TEXT,
    FOREIGN KEY (Maschinen_ID) REFERENCES Maschinen(Maschinen_ID)
);
```

> [!NOTE]
> Der Constraint `FOREIGN KEY (Maschinen_ID) REFERENCES Maschinen(Maschinen_ID)` stellt sicher, dass jedes Wartungsprotokoll nur auf eine existierende Maschine verweisen kann. Versucht man, ein Protokoll mit einer nicht-existierenden `Maschinen_ID` einzufügen, wird ein Fehler geworfen.

### INSERT: Daten einfügen

Die `INSERT`-Anweisung fügt neue Zeilen in eine Tabelle ein.

**Syntax 1: Alle Spalten angeben**
```sql
INSERT INTO Tabellenname (Spalte1, Spalte2, ...)
VALUES (Wert1, Wert2, ...);
```

**Syntax 2: Alle Spalten in Tabellenreihenfolge (nicht empfohlen)**
```sql
INSERT INTO Tabellenname
VALUES (Wert1, Wert2, ...);
```

**Syntax 3: Mehrere Zeilen gleichzeitig (Performance-Vorteil)**
```sql
INSERT INTO Tabellenname (Spalte1, Spalte2, ...)
VALUES 
    (Wert1a, Wert2a, ...),
    (Wert1b, Wert2b, ...),
    (Wert1c, Wert2c, ...);
```

> [!TIP]
> **Beispiel: Maschinen einfügen**
> ```sql
> INSERT INTO Maschinen (Maschinentyp, Baujahr, Standort, Anschaffungsdatum, Anschaffungskosten_Euro)
> VALUES 
>     ('CNC-Fräse DMU 50', 2018, 'Halle A1', '2018-03-15', 285000.00),
>     ('Drehmaschine CTX 450', 2020, 'Halle B2', '2020-07-22', 198000.00),
>     ('Laserschneider TruLaser 3030', 2019, 'Halle C3', '2019-11-08', 412000.00);
> ```
> 
> Die `Maschinen_ID` wird automatisch vergeben (Auto-Increment).

### SELECT: Daten abfragen

Die `SELECT`-Anweisung ist das Herzstück von SQL. Sie erlaubt es, Daten aus einer oder mehreren Tabellen zu lesen, zu filtern, zu sortieren und zu aggregieren.

**Basis-Syntax**:
```sql
SELECT Spalte1, Spalte2, ...
FROM Tabellenname
WHERE Bedingung
ORDER BY Spalte [ASC|DESC];
```

**Alle Spalten auswählen**:
```sql
SELECT * FROM Maschinen;
```

> [!WARNING]
> `SELECT *` ist bequem, aber in Produktionscode solltest du immer explizit die benötigten Spalten auflisten. Gründe: (1) Performance (nicht alle Spalten werden immer benötigt), (2) Wartbarkeit (wenn sich die Tabellenstruktur ändert, bricht der Code nicht), (3) Lesbarkeit.

**Bestimmte Spalten auswählen**:
```sql
SELECT Maschinentyp, Standort, Baujahr
FROM Maschinen;
```

**WHERE-Klausel: Zeilen filtern**:
```sql
SELECT Maschinentyp, Standort
FROM Maschinen
WHERE Baujahr >= 2019;
```

**Vergleichsoperatoren in WHERE**:
- `=`: Gleichheit (`Baujahr = 2020`)
- `!=` oder `<>`: Ungleichheit
- `<`, `>`, `<=`, `>=`: Kleiner, größer, kleiner-gleich, größer-gleich
- `BETWEEN x AND y`: Bereichsabfrage (`Baujahr BETWEEN 2018 AND 2020`)
- `IN (wert1, wert2, ...)`: Wert in Liste (`Standort IN ('Halle A1', 'Halle B2')`)
- `LIKE 'muster'`: Textmuster mit Wildcards (`%` = beliebig viele Zeichen, `_` = genau ein Zeichen)
- `IS NULL` / `IS NOT NULL`: NULL-Prüfung

> [!TIP]
> **LIKE-Musterabgleich**:
> ```sql
> -- Alle CNC-Maschinen:
> SELECT * FROM Maschinen WHERE Maschinentyp LIKE 'CNC%';
> 
> -- Alle Maschinen mit "Laser" im Namen:
> SELECT * FROM Maschinen WHERE Maschinentyp LIKE '%Laser%';
> ```

**Logische Operatoren: AND, OR, NOT**:
```sql
SELECT * FROM Maschinen
WHERE Baujahr >= 2019 AND Standort = 'Halle A1';

SELECT * FROM Maschinen
WHERE Baujahr < 2019 OR Anschaffungskosten_Euro > 300000;

SELECT * FROM Maschinen
WHERE NOT (Standort = 'Halle C3');
```

**ORDER BY: Ergebnisse sortieren**:
```sql
-- Aufsteigend (Standard):
SELECT * FROM Maschinen ORDER BY Baujahr;

-- Absteigend:
SELECT * FROM Maschinen ORDER BY Anschaffungskosten_Euro DESC;

-- Mehrere Spalten:
SELECT * FROM Maschinen 
ORDER BY Standort ASC, Baujahr DESC;
```

> [!NOTE]
> Bei `ORDER BY` mit mehreren Spalten wird zuerst nach der ersten Spalte sortiert, bei Gleichheit dann nach der zweiten, usw.

**LIMIT: Anzahl der Ergebnisse begrenzen** (SQLite, MySQL, PostgreSQL):
```sql
-- Nur die 5 teuersten Maschinen:
SELECT * FROM Maschinen
ORDER BY Anschaffungskosten_Euro DESC
LIMIT 5;

-- Mit Offset (überspringe die ersten 10 Ergebnisse):
SELECT * FROM Maschinen
ORDER BY Baujahr
LIMIT 5 OFFSET 10;
```

### UPDATE: Daten ändern

Die `UPDATE`-Anweisung ändert bestehende Zeilen.

**Syntax**:
```sql
UPDATE Tabellenname
SET Spalte1 = Wert1, Spalte2 = Wert2, ...
WHERE Bedingung;
```

> [!WARNING]
> **Vorsicht**: Ohne `WHERE`-Klausel werden **alle** Zeilen geändert! Teste kritische Updates immer zuerst mit `SELECT`, um die betroffenen Zeilen zu prüfen.

> [!TIP]
> **Beispiele**:
> ```sql
> -- Wartungsintervall für eine spezifische Maschine ändern:
> UPDATE Maschinen
> SET Wartungsintervall_Tage = 60
> WHERE Maschinen_ID = 3;
> 
> -- Standort für alle CNC-Maschinen ändern:
> UPDATE Maschinen
> SET Standort = 'Halle D1'
> WHERE Maschinentyp LIKE 'CNC%';
> 
> -- Anschaffungskosten um 10% erhöhen (Inflation):
> UPDATE Maschinen
> SET Anschaffungskosten_Euro = Anschaffungskosten_Euro * 1.10;
> ```

### DELETE: Daten löschen

Die `DELETE`-Anweisung löscht Zeilen aus einer Tabelle.

**Syntax**:
```sql
DELETE FROM Tabellenname
WHERE Bedingung;
```

> [!WARNING]
> **Vorsicht**: Ohne `WHERE`-Klausel werden **alle** Zeilen gelöscht! Erstelle vorher ein Backup, wenn du unsicher bist.

> [!TIP]
> **Beispiele**:
> ```sql
> -- Eine spezifische Maschine löschen:
> DELETE FROM Maschinen WHERE Maschinen_ID = 5;
> 
> -- Alle Maschinen vor Baujahr 2010 löschen:
> DELETE FROM Maschinen WHERE Baujahr < 2010;
> 
> -- Alle Zeilen löschen (Tabelle bleibt bestehen):
> DELETE FROM Maschinen;
> ```

**Referentielle Integrität beim Löschen**: Wenn eine Maschine gelöscht wird, die noch Wartungsprotokolle hat, schlägt das Löschen fehl (wegen Fremdschlüssel-Constraint). Lösungsoptionen:
1. Zuerst alle abhängigen Wartungsprotokolle löschen
2. `ON DELETE CASCADE` im Foreign Key definieren (automatisches Mitlöschen)
3. `ON DELETE SET NULL` (Fremdschlüssel wird auf NULL gesetzt)

### Aggregatfunktionen: Daten zusammenfassen

Aggregatfunktionen berechnen einen einzelnen Wert aus mehreren Zeilen. Sie sind essentiell für statistische Auswertungen und Berichte.

**COUNT()**: Zählt Zeilen.
```sql
-- Anzahl aller Maschinen:
SELECT COUNT(*) FROM Maschinen;

-- Anzahl Maschinen in Halle A1:
SELECT COUNT(*) FROM Maschinen WHERE Standort = 'Halle A1';

-- Anzahl unterschiedlicher Standorte:
SELECT COUNT(DISTINCT Standort) FROM Maschinen;
```

> [!NOTE]
> **COUNT(*)** zählt alle Zeilen (auch mit NULL-Werten). **COUNT(Spaltenname)** zählt nur Zeilen, wo die Spalte nicht NULL ist. **COUNT(DISTINCT Spalte)** zählt nur eindeutige Werte.

**SUM()**: Summe numerischer Werte.
```sql
-- Gesamtanschaffungskosten aller Maschinen:
SELECT SUM(Anschaffungskosten_Euro) AS Gesamtkosten
FROM Maschinen;

-- Gesamtkosten aller Wartungen für Maschine 1:
SELECT SUM(Kosten_Euro) AS Gesamtwartungskosten
FROM Wartungsprotokolle
WHERE Maschinen_ID = 1;
```

**AVG()**: Durchschnitt.
```sql
-- Durchschnittliches Baujahr:
SELECT AVG(Baujahr) AS Durchschnittsbaujahr FROM Maschinen;

-- Durchschnittliche Wartungskosten pro Protokoll:
SELECT AVG(Kosten_Euro) AS Durchschnittskosten FROM Wartungsprotokolle;
```

**MIN() / MAX()**: Minimum / Maximum.
```sql
-- Älteste und neueste Maschine:
SELECT MIN(Baujahr) AS Aelteste, MAX(Baujahr) AS Neueste
FROM Maschinen;

-- Teuerste Wartung:
SELECT MAX(Kosten_Euro) AS Teuerste_Wartung FROM Wartungsprotokolle;
```

> [!TIP]
> **Kombination von Aggregatfunktionen**:
> ```sql
> SELECT 
>     COUNT(*) AS Anzahl_Maschinen,
>     SUM(Anschaffungskosten_Euro) AS Gesamtkosten,
>     AVG(Anschaffungskosten_Euro) AS Durchschnittskosten,
>     MIN(Baujahr) AS Aelteste,
>     MAX(Baujahr) AS Neueste
> FROM Maschinen;
> ```

### GROUP BY: Gruppierte Aggregation

`GROUP BY` gruppiert Zeilen nach gemeinsamen Werten und wendet Aggregatfunktionen auf jede Gruppe an.

**Syntax**:
```sql
SELECT Spalte1, AGGREGAT(Spalte2)
FROM Tabelle
WHERE Bedingung
GROUP BY Spalte1;
```

> [!NOTE]
> Alle Spalten in `SELECT`, die **nicht** in einer Aggregatfunktion stehen, müssen in `GROUP BY` aufgeführt werden. Andernfalls ist unklar, welcher Wert angezeigt werden soll.

> [!TIP]
> **Beispiele**:
> ```sql
> -- Anzahl Maschinen pro Standort:
> SELECT Standort, COUNT(*) AS Anzahl
> FROM Maschinen
> GROUP BY Standort;
> 
> -- Durchschnittliche Anschaffungskosten pro Baujahr:
> SELECT Baujahr, AVG(Anschaffungskosten_Euro) AS Durchschnittskosten
> FROM Maschinen
> GROUP BY Baujahr
> ORDER BY Baujahr;
> 
> -- Gesamtkosten und Anzahl Wartungen pro Maschine:
> SELECT 
>     Maschinen_ID,
>     COUNT(*) AS Anzahl_Wartungen,
>     SUM(Kosten_Euro) AS Gesamtkosten,
>     AVG(Kosten_Euro) AS Durchschnittskosten
> FROM Wartungsprotokolle
> GROUP BY Maschinen_ID
> ORDER BY Gesamtkosten DESC;
> ```

**Ergebnis-Beispiel** (Gesamtkosten pro Maschine):
| Maschinen_ID | Anzahl_Wartungen | Gesamtkosten | Durchschnittskosten |
|--------------|------------------|--------------|---------------------|
| 1            | 2                | 530.00       | 265.00              |
| 2            | 1                | 420.00       | 420.00              |
| 3            | 1                | 90.00        | 90.00               |

### HAVING: Gruppen filtern

`HAVING` filtert **nach** der Aggregation. `WHERE` filtert **vor** der Aggregation.

> [!NOTE]
> **WHERE vs. HAVING**: `WHERE` filtert einzelne Zeilen, bevor Gruppen gebildet werden. `HAVING` filtert Gruppen, nachdem Aggregatfunktionen angewendet wurden.

**Syntax**:
```sql
SELECT Spalte1, AGGREGAT(Spalte2)
FROM Tabelle
WHERE Bedingung_vor_Aggregation
GROUP BY Spalte1
HAVING Bedingung_nach_Aggregation;
```

> [!TIP]
> **Beispiele**:
> ```sql
> -- Nur Maschinen mit mehr als 1 Wartung:
> SELECT Maschinen_ID, COUNT(*) AS Anzahl_Wartungen
> FROM Wartungsprotokolle
> GROUP BY Maschinen_ID
> HAVING COUNT(*) > 1;
> 
> -- Standorte mit durchschnittlichen Anschaffungskosten über 250.000 Euro:
> SELECT Standort, AVG(Anschaffungskosten_Euro) AS Durchschnitt
> FROM Maschinen
> GROUP BY Standort
> HAVING AVG(Anschaffungskosten_Euro) > 250000;
> 
> -- Maschinen, die seit 2020 mindestens 500 Euro Wartungskosten hatten:
> SELECT Maschinen_ID, SUM(Kosten_Euro) AS Gesamtkosten
> FROM Wartungsprotokolle
> WHERE Wartungsdatum >= '2020-01-01'
> GROUP BY Maschinen_ID
> HAVING SUM(Kosten_Euro) >= 500
> ORDER BY Gesamtkosten DESC;
> ```

### JOINs: Tabellen verknüpfen

Relationale Datenbanken verteilen Daten auf mehrere Tabellen, um Redundanz zu vermeiden. `JOIN`-Operationen verknüpfen Tabellen über Fremdschlüssel.

#### INNER JOIN

`INNER JOIN` gibt nur Zeilen zurück, für die in **beiden** Tabellen passende Einträge existieren.

**Syntax**:
```sql
SELECT Tabelle1.Spalte1, Tabelle2.Spalte2, ...
FROM Tabelle1
INNER JOIN Tabelle2 ON Tabelle1.Fremdschlüssel = Tabelle2.Primärschlüssel;
```

> [!TIP]
> **Beispiel: Wartungsprotokolle mit Maschinennamen**:
> ```sql
> SELECT 
>     Maschinen.Maschinentyp,
>     Wartungsprotokolle.Wartungsdatum,
>     Wartungsprotokolle.Wartungstyp,
>     Wartungsprotokolle.Kosten_Euro
> FROM Wartungsprotokolle
> INNER JOIN Maschinen ON Wartungsprotokolle.Maschinen_ID = Maschinen.Maschinen_ID
> ORDER BY Wartungsprotokolle.Wartungsdatum DESC;
> ```
> 
> Ergebnis:
> | Maschinentyp           | Wartungsdatum | Wartungstyp               | Kosten_Euro |
> |------------------------|---------------|---------------------------|-------------|
> | CNC-Fräse DMU 50       | 2024-04-20    | Öl- und Filterwechsel     | 180.00      |
> | Laserschneider TruLaser| 2024-03-05    | Laserreinigung            | 90.00       |
> | Drehmaschine CTX 450   | 2024-02-10    | Routineinspektion         | 420.00      |
> | CNC-Fräse DMU 50       | 2024-01-15    | Routineinspektion         | 350.00      |

**Table Aliases** (Abkürzungen für Tabellennamen):
```sql
SELECT 
    m.Maschinentyp,
    w.Wartungsdatum,
    w.Kosten_Euro
FROM Wartungsprotokolle AS w
INNER JOIN Maschinen AS m ON w.Maschinen_ID = m.Maschinen_ID;
```

> [!NOTE]
> Table Aliases machen Queries lesbarer, besonders bei mehreren JOINs. Das Schlüsselwort `AS` ist optional: `FROM Maschinen m` ist gleichbedeutend mit `FROM Maschinen AS m`.

#### LEFT JOIN (LEFT OUTER JOIN)

`LEFT JOIN` gibt **alle** Zeilen der linken Tabelle zurück. Wenn keine passende Zeile in der rechten Tabelle existiert, werden NULL-Werte eingesetzt.

**Anwendungsfall**: Zeige alle Maschinen, auch die ohne Wartungsprotokolle.

```sql
SELECT 
    m.Maschinen_ID,
    m.Maschinentyp,
    COUNT(w.Protokoll_ID) AS Anzahl_Wartungen,
    COALESCE(SUM(w.Kosten_Euro), 0) AS Gesamtkosten
FROM Maschinen AS m
LEFT JOIN Wartungsprotokolle AS w ON m.Maschinen_ID = w.Maschinen_ID
GROUP BY m.Maschinen_ID, m.Maschinentyp
ORDER BY Anzahl_Wartungen DESC;
```

> [!NOTE]
> `COALESCE(Wert1, Wert2, ...)` gibt den ersten Nicht-NULL-Wert zurück. Hier wird `NULL` (wenn keine Wartungen existieren) durch `0` ersetzt.

**Ergebnis-Beispiel**:
| Maschinen_ID | Maschinentyp           | Anzahl_Wartungen | Gesamtkosten |
|--------------|------------------------|------------------|--------------|
| 1            | CNC-Fräse DMU 50       | 2                | 530.00       |
| 2            | Drehmaschine CTX 450   | 1                | 420.00       |
| 3            | Laserschneider TruLaser| 1                | 90.00        |
| 4            | Bohrmaschine XYZ       | 0                | 0.00         |

Maschine 4 hat keine Wartungsprotokolle, wird aber trotzdem angezeigt (wegen `LEFT JOIN`).

#### RIGHT JOIN und FULL OUTER JOIN

**RIGHT JOIN**: Spiegelbild von LEFT JOIN (alle Zeilen der rechten Tabelle). In der Praxis selten verwendet (kann als LEFT JOIN mit vertauschten Tabellen geschrieben werden).

**FULL OUTER JOIN**: Kombiniert LEFT und RIGHT JOIN (alle Zeilen beider Tabellen). Wird in SQLite **nicht unterstützt** (aber in PostgreSQL, MySQL 8+, SQL Server).

### Subqueries (Unterabfragen)

Subqueries sind SELECT-Anweisungen innerhalb von SELECT-Anweisungen. Sie können in `WHERE`, `FROM` oder `SELECT` verwendet werden.

**Subquery in WHERE**:
```sql
-- Alle Maschinen, die teurer als der Durchschnitt sind:
SELECT Maschinentyp, Anschaffungskosten_Euro
FROM Maschinen
WHERE Anschaffungskosten_Euro > (
    SELECT AVG(Anschaffungskosten_Euro) FROM Maschinen
);
```

**Subquery mit IN**:
```sql
-- Alle Maschinen, die mindestens eine Wartung hatten:
SELECT Maschinentyp
FROM Maschinen
WHERE Maschinen_ID IN (
    SELECT DISTINCT Maschinen_ID FROM Wartungsprotokolle
);
```

**Correlated Subquery** (bezieht sich auf äußere Query):
```sql
-- Für jede Maschine: Anzahl Wartungen:
SELECT 
    m.Maschinentyp,
    (SELECT COUNT(*) FROM Wartungsprotokolle w 
     WHERE w.Maschinen_ID = m.Maschinen_ID) AS Anzahl_Wartungen
FROM Maschinen m;
```

> [!WARNING]
> Correlated Subqueries sind langsam, da sie für jede Zeile der äußeren Query ausgeführt werden. Bevorzuge JOINs oder Subqueries in `FROM` wenn möglich.

### Indizes: Performance-Optimierung

Ein **Index** ist eine Datenstruktur (meist B-Tree), die schnelles Suchen ermöglicht. Ohne Index muss die Datenbank eine **Full Table Scan** durchführen (O(n) Zeit). Mit Index ist Suchen oft O(log n).

**Index erstellen**:
```sql
CREATE INDEX idx_maschinen_standort ON Maschinen(Standort);
CREATE INDEX idx_wartung_datum ON Wartungsprotokolle(Wartungsdatum);
```

**Wann Indizes sinnvoll sind**:
- Spalten in `WHERE`-Klauseln (häufige Filter)
- Spalten in `JOIN`-Bedingungen (Fremdschlüssel)
- Spalten in `ORDER BY` (Sortierung)

**Wann Indizes problematisch sind**:
- Verlangsamen `INSERT`, `UPDATE`, `DELETE` (Index muss aktualisiert werden)
- Verbrauchen Speicherplatz
- Zu viele Indizes können kontraproduktiv sein

> [!NOTE]
> Primärschlüssel haben automatisch einen Index. Fremdschlüssel oft nicht (je nach DBMS) – erstelle sie explizit für bessere JOIN-Performance.

### Transaktionen und ACID-Prinzipien

Eine **Transaktion** ist eine Folge von SQL-Operationen, die als atomare Einheit behandelt werden. Entweder werden alle Operationen ausgeführt (Commit) oder keine (Rollback).

**ACID-Eigenschaften**:
- **Atomicity (Atomarität)**: Alles oder nichts – Transaktion wird vollständig oder gar nicht ausgeführt.
- **Consistency (Konsistenz)**: Datenbank bleibt in gültigem Zustand (Constraints bleiben erfüllt).
- **Isolation (Isolation)**: Parallele Transaktionen beeinflussen sich nicht (verschiedene Isolation Levels möglich).
- **Durability (Dauerhaftigkeit)**: Nach Commit sind Änderungen permanent, auch bei Systemabsturz.

**Transaktion in SQL**:
```sql
BEGIN TRANSACTION;

UPDATE Maschinen SET Standort = 'Halle D1' WHERE Maschinen_ID = 1;
INSERT INTO Wartungsprotokolle (Maschinen_ID, Wartungsdatum, Wartungstyp, Dauer_Stunden, Kosten_Euro)
VALUES (1, '2024-05-10', 'Umzug', 4.0, 600.00);

COMMIT;  -- Änderungen speichern
-- Oder: ROLLBACK;  -- Änderungen verwerfen
```

> [!TIP]
> In SQLite ist jede SQL-Anweisung automatisch eine Transaktion (Auto-Commit). Mit `BEGIN TRANSACTION` können mehrere Statements zu einer Transaktion zusammengefasst werden.

### Normalisierung: Redundanz vermeiden

**Normalisierung** ist der Prozess, Datenbankschemata so zu entwerfen, dass Redundanz minimiert und Anomalien vermieden werden.

**Erste Normalform (1NF)**: Jede Zelle enthält einen atomaren Wert (keine Listen, keine zusammengesetzten Werte).

❌ **Nicht 1NF**:
| Maschinen_ID | Maschinentyp | Standorte              |
|--------------|--------------|------------------------|
| 1            | CNC-Fräse    | Halle A1, Halle B2     |

✅ **1NF**:
| Maschinen_ID | Maschinentyp | Standort   |
|--------------|--------------|------------|
| 1            | CNC-Fräse    | Halle A1   |
| 1            | CNC-Fräse    | Halle B2   |

**Zweite Normalform (2NF)**: 1NF + keine partiellen Abhängigkeiten (alle Nicht-Schlüssel-Attribute hängen vom **gesamten** Primärschlüssel ab).

**Dritte Normalform (3NF)**: 2NF + keine transitiven Abhängigkeiten (Nicht-Schlüssel-Attribute hängen nicht von anderen Nicht-Schlüssel-Attributen ab).

> [!NOTE]
> In der Praxis reicht oft **3NF**. Höhere Normalformen (BCNF, 4NF, 5NF) existieren, sind aber selten notwendig. Über-Normalisierung kann zu vielen JOINs und schlechter Performance führen – ein Kompromiss ist manchmal sinnvoll.

### Zusammenfassung: SQL-Abfrage-Reihenfolge

SQL-Statements werden in dieser Reihenfolge ausgeführt (nicht in der Schreib-Reihenfolge!):

1. **FROM** + **JOIN**: Tabellen verknüpfen
2. **WHERE**: Zeilen filtern (vor Aggregation)
3. **GROUP BY**: Gruppen bilden
4. **HAVING**: Gruppen filtern (nach Aggregation)
5. **SELECT**: Spalten auswählen und berechnen
6. **ORDER BY**: Ergebnisse sortieren
7. **LIMIT/OFFSET**: Anzahl begrenzen

> [!TIP]
> **Vollständiges Beispiel**:
> ```sql
> SELECT 
>     m.Standort,
>     COUNT(*) AS Anzahl_Maschinen,
>     AVG(m.Anschaffungskosten_Euro) AS Durchschnittskosten,
>     SUM(w.Kosten_Euro) AS Wartungskosten_Gesamt
> FROM Maschinen m
> LEFT JOIN Wartungsprotokolle w ON m.Maschinen_ID = w.Maschinen_ID
> WHERE m.Baujahr >= 2015
> GROUP BY m.Standort
> HAVING COUNT(*) >= 2
> ORDER BY Wartungskosten_Gesamt DESC
> LIMIT 3;
> ```

---

## 🐍 Python-Praxis: Datenbankverbindung & SQL – Teil 1

### Das sqlite3-Modul

Python enthält das **sqlite3-Modul** in der Standard-Library. SQLite ist eine dateibasierte, serverlose SQL-Datenbank, die perfekt für Prototyping, kleine bis mittlere Anwendungen und Embedded Systems geeignet ist.

> [!NOTE]
> **sqlite3** ist seit Python 2.5 Teil der Standard-Library. SQLite-Datenbanken sind einzelne Dateien (z.B. `maschinen.db`), die portabel sind und keine Server-Installation benötigen. Für Production-Systeme mit vielen gleichzeitigen Schreibzugriffen sind PostgreSQL, MySQL oder andere Client-Server-DBMS oft besser geeignet.

**Import**:
```python
import sqlite3
```

### Verbindung herstellen und schließen

Eine Datenbankverbindung wird mit `sqlite3.connect()` hergestellt. Dies erstellt ein **Connection-Objekt**.

```python
import sqlite3

# Verbindung zu Datei (wird erstellt, falls nicht vorhanden):
conn = sqlite3.connect('maschinen.db')

# ... Datenbankoperationen ...

# Verbindung schließen:
conn.close()
```

> [!TIP]
> **In-Memory-Datenbank** für Tests (Daten gehen verloren beim Schließen):
> ```python
> conn = sqlite3.connect(':memory:')
> ```

**Best Practice: Context Manager verwenden**:
```python
import sqlite3

with sqlite3.connect('maschinen.db') as conn:
    # Datenbankoperationen
    pass
# Verbindung wird automatisch geschlossen
```

> [!NOTE]
> Der Context Manager mit `with` garantiert, dass `conn.close()` auch bei Exceptions ausgeführt wird. Außerdem wird `conn.commit()` automatisch aufgerufen bei Erfolg, und `conn.rollback()` bei Exceptions.

### Cursor erstellen und SQL ausführen

Um SQL-Befehle auszuführen, benötigt man ein **Cursor-Objekt**. Der Cursor verwaltet den aktuellen Zustand einer Abfrage.

```python
import sqlite3

conn = sqlite3.connect('maschinen.db')
cursor = conn.cursor()

# SQL ausführen:
cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)")

conn.commit()  # Änderungen speichern
conn.close()
```

> [!NOTE]
> **`cursor.execute(sql, parameters)`** führt ein einzelnes SQL-Statement aus. **`conn.commit()`** speichert Änderungen permanent. Ohne `commit()` gehen INSERT/UPDATE/DELETE verloren beim Schließen.

### Tabellen erstellen

```python
import sqlite3

with sqlite3.connect('maschinen.db') as conn:
    cursor = conn.cursor()
    
    # Maschinen-Tabelle erstellen:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Maschinen (
            Maschinen_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Maschinentyp TEXT NOT NULL,
            Baujahr INTEGER CHECK (Baujahr >= 1900 AND Baujahr <= 2100),
            Standort TEXT NOT NULL,
            Wartungsintervall_Tage INTEGER DEFAULT 90,
            Anschaffungsdatum TEXT,
            Anschaffungskosten_Euro REAL CHECK (Anschaffungskosten_Euro >= 0)
        )
    """)
    
    # Wartungsprotokolle-Tabelle erstellen:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Wartungsprotokolle (
            Protokoll_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Maschinen_ID INTEGER NOT NULL,
            Wartungsdatum TEXT NOT NULL,
            Wartungstyp TEXT NOT NULL,
            Dauer_Stunden REAL CHECK (Dauer_Stunden > 0),
            Kosten_Euro REAL CHECK (Kosten_Euro >= 0),
            Notizen TEXT,
            FOREIGN KEY (Maschinen_ID) REFERENCES Maschinen(Maschinen_ID)
        )
    """)
    
    conn.commit()
    print("Tabellen erfolgreich erstellt!")
```

> [!WARNING]
> `CREATE TABLE IF NOT EXISTS` verhindert Fehler, wenn die Tabelle bereits existiert. Ohne `IF NOT EXISTS` würde ein Fehler geworfen werden.

### Daten einfügen (INSERT)

**Einzelne Zeile einfügen**:
```python
import sqlite3

with sqlite3.connect('maschinen.db') as conn:
    cursor = conn.cursor()
    
    # FALSCH: SQL-Injection-Gefahr!
    # maschinentyp = "CNC-Fräse'; DROP TABLE Maschinen; --"
    # cursor.execute(f"INSERT INTO Maschinen (Maschinentyp) VALUES ('{maschinentyp}')")
    
    # RICHTIG: Prepared Statements mit ? Platzhaltern
    cursor.execute("""
        INSERT INTO Maschinen (Maschinentyp, Baujahr, Standort, Anschaffungsdatum, Anschaffungskosten_Euro)
        VALUES (?, ?, ?, ?, ?)
    """, ('CNC-Fräse DMU 50', 2018, 'Halle A1', '2018-03-15', 285000.00))
    
    conn.commit()
    print(f"Maschine eingefügt mit ID: {cursor.lastrowid}")
```

> [!WARNING]
> **SQL-Injection-Sicherheit**: Verwende **niemals** String-Interpolation (`f"{variable}"`) oder Konkatenation (`+`) für SQL-Parameter! Immer Prepared Statements mit `?` Platzhaltern nutzen. Das DBMS behandelt Parameter dann als Werte, nicht als SQL-Code.

**Mehrere Zeilen einfügen**:
```python
import sqlite3

maschinen = [
    ('Drehmaschine CTX 450', 2020, 'Halle B2', '2020-07-22', 198000.00),
    ('Laserschneider TruLaser 3030', 2019, 'Halle C3', '2019-11-08', 412000.00),
    ('Bohrmaschine DMC 635 V', 2021, 'Halle A1', '2021-02-14', 156000.00)
]

with sqlite3.connect('maschinen.db') as conn:
    cursor = conn.cursor()
    
    cursor.executemany("""
        INSERT INTO Maschinen (Maschinentyp, Baujahr, Standort, Anschaffungsdatum, Anschaffungskosten_Euro)
        VALUES (?, ?, ?, ?, ?)
    """, maschinen)
    
    conn.commit()
    print(f"{cursor.rowcount} Maschinen eingefügt.")
```

> [!NOTE]
> **`cursor.executemany(sql, seq_of_parameters)`** führt SQL für jedes Tupel in der Sequenz aus. Dies ist effizienter als individuelle `execute()`-Aufrufe in einer Schleife.

### Daten abfragen (SELECT)

**Alle Zeilen abrufen**:
```python
import sqlite3

with sqlite3.connect('maschinen.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Maschinen")
    
    # Alle Zeilen als Liste von Tupeln:
    zeilen = cursor.fetchall()
    
    for zeile in zeilen:
        print(zeile)
```

**Ausgabe**:
```
(1, 'CNC-Fräse DMU 50', 2018, 'Halle A1', 90, '2018-03-15', 285000.0)
(2, 'Drehmaschine CTX 450', 2020, 'Halle B2', 90, '2020-07-22', 198000.0)
...
```

> [!NOTE]
> **`cursor.fetchall()`** gibt eine Liste aller Ergebniszeilen zurück. Jede Zeile ist ein Tupel. Bei großen Ergebnismengen kann dies viel Speicher verbrauchen.

**Einzelne Zeile abrufen**:
```python
cursor.execute("SELECT * FROM Maschinen WHERE Maschinen_ID = ?", (1,))
zeile = cursor.fetchone()

if zeile:
    print(f"Gefunden: {zeile}")
else:
    print("Keine Maschine mit dieser ID gefunden.")
```

> [!NOTE]
> **`cursor.fetchone()`** gibt die nächste Zeile zurück oder `None`, wenn keine mehr vorhanden ist. Nützlich, wenn nur ein Ergebnis erwartet wird.

**Zeilenweise iterieren** (speicher-effizient):
```python
cursor.execute("SELECT Maschinentyp, Standort FROM Maschinen WHERE Baujahr >= ?", (2019,))

for zeile in cursor:
    maschinentyp, standort = zeile
    print(f"{maschinentyp} @ {standort}")
```

> [!TIP]
> Der Cursor ist ein Iterator. Iteration ist speicher-effizienter als `fetchall()`, da Zeilen nacheinander abgerufen werden (lazy loading).

**Spaltennamen erhalten**:
```python
cursor.execute("SELECT Maschinentyp, Baujahr FROM Maschinen")

# Spaltennamen extrahieren:
spaltennamen = [description[0] for description in cursor.description]
print(spaltennamen)  # ['Maschinentyp', 'Baujahr']

for zeile in cursor:
    print(dict(zip(spaltennamen, zeile)))
```

**Ausgabe**:
```
{'Maschinentyp': 'CNC-Fräse DMU 50', 'Baujahr': 2018}
{'Maschinentyp': 'Drehmaschine CTX 450', 'Baujahr': 2020}
...
```

> [!NOTE]
> **`cursor.description`** enthält Metadaten über die Spalten (Name, Typ, etc.). `cursor.description[i][0]` ist der Spaltenname der i-ten Spalte.

**Row Factory: Ergebnisse als Dictionaries**:
```python
import sqlite3

conn = sqlite3.connect('maschinen.db')
conn.row_factory = sqlite3.Row  # Aktiviert Dictionary-ähnlichen Zugriff
cursor = conn.cursor()

cursor.execute("SELECT Maschinentyp, Baujahr FROM Maschinen")

for zeile in cursor:
    print(f"{zeile['Maschinentyp']} (Baujahr: {zeile['Baujahr']})")
    # Oder als Dictionary:
    print(dict(zeile))

conn.close()
```

> [!NOTE]
> **`sqlite3.Row`** ermöglicht Zugriff auf Spalten per Namen **und** per Index. `zeile['Maschinentyp']` und `zeile[0]` funktionieren beide. Dies macht Code lesbarer.

### Daten ändern (UPDATE)

```python
import sqlite3

with sqlite3.connect('maschinen.db') as conn:
    cursor = conn.cursor()
    
    # Wartungsintervall für eine Maschine ändern:
    cursor.execute("""
        UPDATE Maschinen
        SET Wartungsintervall_Tage = ?
        WHERE Maschinen_ID = ?
    """, (60, 3))
    
    conn.commit()
    print(f"{cursor.rowcount} Zeile(n) aktualisiert.")
```

> [!NOTE]
> **`cursor.rowcount`** enthält die Anzahl der betroffenen Zeilen nach INSERT, UPDATE oder DELETE. Bei SELECT ist der Wert oft -1 (nicht definiert).

### Daten löschen (DELETE)

```python
import sqlite3

with sqlite3.connect('maschinen.db') as conn:
    cursor = conn.cursor()
    
    # Lösche alle Maschinen vor Baujahr 2015:
    cursor.execute("DELETE FROM Maschinen WHERE Baujahr < ?", (2015,))
    
    conn.commit()
    print(f"{cursor.rowcount} Maschine(n) gelöscht.")
```

> [!WARNING]
> Ohne `WHERE`-Klausel werden **alle** Zeilen gelöscht! Teste kritische DELETE-Statements zuerst mit `SELECT` mit denselben `WHERE`-Bedingungen.

### Aggregatfunktionen und GROUP BY in Python

```python
import sqlite3

conn = sqlite3.connect('maschinen.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Gesamtkosten und Anzahl Wartungen pro Maschine:
cursor.execute("""
    SELECT 
        m.Maschinentyp,
        COUNT(w.Protokoll_ID) AS Anzahl_Wartungen,
        COALESCE(SUM(w.Kosten_Euro), 0) AS Gesamtkosten
    FROM Maschinen m
    LEFT JOIN Wartungsprotokolle w ON m.Maschinen_ID = w.Maschinen_ID
    GROUP BY m.Maschinen_ID, m.Maschinentyp
    ORDER BY Gesamtkosten DESC
""")

for zeile in cursor:
    print(f"{zeile['Maschinentyp']}: {zeile['Anzahl_Wartungen']} Wartungen, {zeile['Gesamtkosten']:.2f} €")

conn.close()
```

### Transaktionen in Python

Standardmäßig ist Auto-Commit in sqlite3 **deaktiviert** (Isolation Level). Jede SQL-Anweisung ist Teil einer Transaktion. `conn.commit()` speichert Änderungen, `conn.rollback()` verwirft sie.

```python
import sqlite3

conn = sqlite3.connect('maschinen.db')
cursor = conn.cursor()

try:
    # Mehrere Operationen als atomare Transaktion:
    cursor.execute("UPDATE Maschinen SET Standort = ? WHERE Maschinen_ID = ?", ('Halle D1', 1))
    cursor.execute("""
        INSERT INTO Wartungsprotokolle (Maschinen_ID, Wartungsdatum, Wartungstyp, Dauer_Stunden, Kosten_Euro)
        VALUES (?, ?, ?, ?, ?)
    """, (1, '2024-05-10', 'Umzug', 4.0, 600.00))
    
    conn.commit()  # Beide Operationen werden gespeichert
    print("Transaktion erfolgreich abgeschlossen.")
    
except sqlite3.Error as e:
    conn.rollback()  # Keine der Operationen wird gespeichert
    print(f"Fehler: {e}")
    
finally:
    conn.close()
```

> [!NOTE]
> Bei Verwendung des Context Managers (`with sqlite3.connect(...) as conn`) wird `commit()` automatisch bei Erfolg und `rollback()` bei Exceptions aufgerufen.

### Fehlerbehandlung

**Häufige Exceptions**:
- **`sqlite3.Error`**: Basis-Exception für alle sqlite3-Fehler
- **`sqlite3.IntegrityError`**: Constraint-Verletzung (z.B. Fremdschlüssel, PRIMARY KEY, UNIQUE, CHECK)
- **`sqlite3.OperationalError`**: Datenbankoperations-Fehler (z.B. Tabelle existiert nicht, Locked Database)
- **`sqlite3.DatabaseError`**: Allgemeiner Datenbankfehler

```python
import sqlite3

try:
    conn = sqlite3.connect('maschinen.db')
    cursor = conn.cursor()
    
    # Versuche, Maschine mit Duplikat-ID einzufügen:
    cursor.execute("INSERT INTO Maschinen (Maschinen_ID, Maschinentyp, Standort) VALUES (?, ?, ?)",
                   (1, 'Test', 'Halle X'))
    conn.commit()
    
except sqlite3.IntegrityError as e:
    print(f"Integritätsfehler: {e}")
    # Ausgabe: UNIQUE constraint failed: Maschinen.Maschinen_ID
    
except sqlite3.OperationalError as e:
    print(f"Operationsfehler: {e}")
    
except sqlite3.Error as e:
    print(f"Allgemeiner Datenbankfehler: {e}")
    
finally:
    conn.close()
```

> [!TIP]
> Fange spezifische Exceptions vor allgemeinen. `IntegrityError` ist eine Unterklasse von `DatabaseError`, die wiederum eine Unterklasse von `Error` ist.

### Praktisches Beispiel: Maschinenverwaltungs-System

```python
import sqlite3
from datetime import date

class MaschinenDB:
    def __init__(self, db_datei='maschinen.db'):
        self.db_datei = db_datei
        self._erstelle_tabellen()
    
    def _erstelle_tabellen(self):
        with sqlite3.connect(self.db_datei) as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Maschinen (
                    Maschinen_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Maschinentyp TEXT NOT NULL,
                    Baujahr INTEGER CHECK (Baujahr >= 1900),
                    Standort TEXT NOT NULL,
                    Wartungsintervall_Tage INTEGER DEFAULT 90
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Wartungsprotokolle (
                    Protokoll_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Maschinen_ID INTEGER NOT NULL,
                    Wartungsdatum TEXT NOT NULL,
                    Wartungstyp TEXT NOT NULL,
                    Kosten_Euro REAL CHECK (Kosten_Euro >= 0),
                    FOREIGN KEY (Maschinen_ID) REFERENCES Maschinen(Maschinen_ID)
                )
            """)
            
            conn.commit()
    
    def maschine_hinzufuegen(self, maschinentyp, baujahr, standort, wartungsintervall=90):
        with sqlite3.connect(self.db_datei) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Maschinen (Maschinentyp, Baujahr, Standort, Wartungsintervall_Tage)
                VALUES (?, ?, ?, ?)
            """, (maschinentyp, baujahr, standort, wartungsintervall))
            conn.commit()
            return cursor.lastrowid
    
    def wartung_hinzufuegen(self, maschinen_id, wartungstyp, kosten, datum=None):
        if datum is None:
            datum = date.today().isoformat()
        
        with sqlite3.connect(self.db_datei) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Wartungsprotokolle (Maschinen_ID, Wartungsdatum, Wartungstyp, Kosten_Euro)
                VALUES (?, ?, ?, ?)
            """, (maschinen_id, datum, wartungstyp, kosten))
            conn.commit()
            return cursor.lastrowid
    
    def alle_maschinen(self):
        conn = sqlite3.connect(self.db_datei)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Maschinen ORDER BY Maschinentyp")
        ergebnisse = cursor.fetchall()
        conn.close()
        return [dict(zeile) for zeile in ergebnisse]
    
    def wartungshistorie(self, maschinen_id):
        conn = sqlite3.connect(self.db_datei)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM Wartungsprotokolle
            WHERE Maschinen_ID = ?
            ORDER BY Wartungsdatum DESC
        """, (maschinen_id,))
        ergebnisse = cursor.fetchall()
        conn.close()
        return [dict(zeile) for zeile in ergebnisse]


# Verwendung:
if __name__ == "__main__":
    db = MaschinenDB()
    
    # Maschinen hinzufügen:
    id1 = db.maschine_hinzufuegen('CNC-Fräse DMU 50', 2018, 'Halle A1')
    id2 = db.maschine_hinzufuegen('Drehmaschine CTX 450', 2020, 'Halle B2', wartungsintervall=120)
    
    print(f"Maschinen hinzugefügt: {id1}, {id2}")
    
    # Wartungen hinzufügen:
    db.wartung_hinzufuegen(id1, 'Routineinspektion', 350.00, '2024-01-15')
    db.wartung_hinzufuegen(id1, 'Öl- und Filterwechsel', 180.00, '2024-04-20')
    
    # Alle Maschinen abrufen:
    print("\nAlle Maschinen:")
    for maschine in db.alle_maschinen():
        print(f"  - {maschine['Maschinentyp']} (ID: {maschine['Maschinen_ID']})")
    
    # Wartungshistorie:
    print(f"\nWartungshistorie für Maschine {id1}:")
    for wartung in db.wartungshistorie(id1):
        print(f"  - {wartung['Wartungsdatum']}: {wartung['Wartungstyp']} ({wartung['Kosten_Euro']:.2f} €)")
```

---

## 📝 Zusammenfassung

**Theorie: Datenbanken – Teil 1**
- Relationale Datenbanken strukturieren Daten in Tabellen mit Zeilen (Tupeln) und Spalten (Attributen).
- Primärschlüssel identifizieren Zeilen eindeutig, Fremdschlüssel verknüpfen Tabellen.
- SQL ist die Standardsprache für relationale Datenbanken (DDL, DML, DQL, DCL).
- `CREATE TABLE` definiert Tabellen mit Datentypen und Constraints (PRIMARY KEY, FOREIGN KEY, NOT NULL, CHECK).
- `INSERT` fügt Zeilen ein, `SELECT` fragt Daten ab, `UPDATE` ändert Daten, `DELETE` löscht Daten.
- Aggregatfunktionen (COUNT, SUM, AVG, MIN, MAX) fassen Daten zusammen.
- `GROUP BY` gruppiert Zeilen für Aggregation, `HAVING` filtert Gruppen.
- `JOIN` verknüpft Tabellen: INNER JOIN (nur passende Zeilen), LEFT JOIN (alle Zeilen linker Tabelle).
- Indizes beschleunigen Abfragen, Transaktionen garantieren ACID-Eigenschaften, Normalisierung vermeidet Redundanz.

**Praxis: SQLite & Python**
- `sqlite3`-Modul ist Teil der Python-Standard-Library (dateibasierte SQL-Datenbank).
- Verbindung mit `sqlite3.connect(datei)`, Cursor mit `conn.cursor()`.
- SQL ausführen mit `cursor.execute(sql, parameter)`, immer Prepared Statements (?) verwenden.
- Daten abrufen mit `cursor.fetchall()` (alle Zeilen), `cursor.fetchone()` (eine Zeile) oder Iteration über Cursor.
- `conn.commit()` speichert Änderungen, `conn.rollback()` verwirft sie, Context Manager (`with`) automatisiert dies.
- `sqlite3.Row` als `row_factory` ermöglicht Dictionary-ähnlichen Zugriff auf Spalten.
- Fehlerbehandlung: `sqlite3.IntegrityError` (Constraints), `sqlite3.OperationalError` (DB-Operationen), `sqlite3.Error` (alle Fehler).
- Objektorientiertes Design mit Klassen für Datenbank-Operationen verbessert Wartbarkeit.

