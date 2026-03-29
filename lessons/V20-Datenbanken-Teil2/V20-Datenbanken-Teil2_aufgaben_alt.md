# V20 – Aufgaben: Datenbanken – Teil 2

---

## 📚 Theorie-Aufgaben

### T1: Normalisierung einer Produktions-Datenbank ⭐⭐

**Kontext**: Ein Maschinenbau-Unternehmen hat eine unnormalisierte Tabelle `Produktionsauftraege`, die Informationen über Fertigungsaufträge, Artikel und Maschinen mischt.

**Tabelle `Produktionsauftraege` (unnormalisiert)**:

| Auftrag_ID | Auftragsdatum | Kunde_Name | Kunde_Adresse | Artikel_Name | Artikel_Preis | Artikel_Gewicht_kg | Maschine_Name | Maschine_Typ | Menge | Liefertermin |
|------------|---------------|------------|---------------|--------------|---------------|-------------------|---------------|--------------|-------|--------------|
| 1001       | 2024-01-10    | Müller AG  | Hauptstr. 10  | Zahnrad Z42  | 125.50        | 2.3               | CNC-Fräse 01  | Fräse        | 50    | 2024-02-10   |
| 1001       | 2024-01-10    | Müller AG  | Hauptstr. 10  | Welle W15    | 89.00         | 5.1               | Drehmaschine 02 | Drehbank   | 30    | 2024-02-10   |
| 1002       | 2024-01-15    | Schmidt GmbH | Bahnhofstr. 5| Zahnrad Z42  | 125.50        | 2.3               | CNC-Fräse 03  | Fräse        | 100   | 2024-03-01   |
| 1003       | 2024-01-20    | Müller AG  | Hauptstr. 10  | Gehäuse G08  | 245.00        | 12.5              | Drehmaschine 02 | Drehbank   | 20    | 2024-02-28   |

**Aufgaben**:

a) **Identifikation von Anomalien**: Beschreibe mindestens **drei Probleme** (Update-, Insert- oder Delete-Anomalien), die in dieser Tabelle auftreten können. Gib für jede Anomalie ein konkretes Beispiel.

b) **Erste Normalform (1NF)**: Zeige, ob die Tabelle in 1NF ist. Falls nicht, beschreibe, was verletzt wird, und erstelle ein Schema in 1NF.

c) **Zweite Normalform (2NF)**: Analysiere, ob partielle Abhängigkeiten existieren (nehme an, `Auftrag_ID` alleine ist **nicht** ausreichend als Primärschlüssel, sondern `(Auftrag_ID, Artikel_Name)` bildet den zusammengesetzten Schlüssel für Auftragspositionen). Welche Spalten hängen nur von einem Teil des Schlüssels ab? Erstelle ein Schema in 2NF mit mindestens **zwei separaten Tabellen**.

d) **Dritte Normalform (3NF)**: Identifiziere transitive Abhängigkeiten in deinem 2NF-Schema. Erstelle ein vollständiges 3NF-Schema mit **mindestens vier Tabellen** (`Kunden`, `Artikel`, `Maschinen`, `Auftraege`, `Auftragspositionen` o.ä.). Gib für jede Tabelle Primärschlüssel und Fremdschlüssel an.

e) **Begründung**: Erkläre in 2-3 Sätzen, warum das 3NF-Schema praktische Vorteile gegenüber der unnormalisierten Tabelle hat (z.B. Konsistenz, Wartbarkeit, Speicherplatz).

---

### T2: Indizes und Query-Optimierung ⭐⭐⭐

**Kontext**: Eine Produktionsdatenbank mit 500.000 Maschinen-Messwerten pro Tag (Tabelle `Sensordaten`) leidet unter langsamen Abfragen. Die Datenbank-Administratorin möchte Indizes strategisch einsetzen.

**Tabelle `Sensordaten`**:
```sql
CREATE TABLE Sensordaten (
    Messung_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Maschinen_ID INTEGER NOT NULL,
    Sensor_Typ TEXT NOT NULL,
    Messwert REAL NOT NULL,
    Zeitstempel TEXT NOT NULL,
    Status TEXT CHECK(Status IN ('normal', 'warnung', 'kritisch'))
);
```

**Typische Abfragen** (sortiert nach Häufigkeit):

1. `SELECT * FROM Sensordaten WHERE Maschinen_ID = 42 AND Zeitstempel >= '2024-12-01' ORDER BY Zeitstempel DESC LIMIT 100;` (50% aller Queries)
2. `SELECT AVG(Messwert) FROM Sensordaten WHERE Sensor_Typ = 'Temperatur' AND Status = 'kritisch';` (30% aller Queries)
3. `SELECT Maschinen_ID, COUNT(*) FROM Sensordaten WHERE Zeitstempel >= '2024-12-15' GROUP BY Maschinen_ID;` (15% aller Queries)
4. `INSERT INTO Sensordaten (Maschinen_ID, Sensor_Typ, Messwert, Zeitstempel, Status) VALUES (...);` (5% aller Queries, aber sehr häufig – Batch-Inserts)

**Aufgaben**:

a) **Index-Analyse**: Für jede der vier Queries, begründe, ob ein Index helfen würde und **welcher Index** am besten geeignet wäre. Berücksichtige:
   - Einspalten- vs. Mehrspaltiger Index
   - Reihenfolge der Spalten bei Composite Index
   - Trade-offs (schnellere SELECTs vs. langsamere INSERTs)

b) **Index-Empfehlung**: Erstelle **maximal drei Indizes**, die das Gesamtsystem optimieren. Schreibe die `CREATE INDEX`-Statements. Begründe, warum du genau diese Indizes gewählt hast und warum du nicht mehr erstellst.

c) **Partial Index (PostgreSQL-Feature)**: Angenommen, 95% aller Messungen haben Status "normal", nur 5% haben "warnung" oder "kritisch". Schlage einen Partial Index vor, der Query 2 beschleunigt, aber weniger Speicher verbraucht als ein vollständiger Index auf `(Sensor_Typ, Status)`.

d) **Denormalisierung**: Die Datenbank-Administratorin schlägt vor, eine zusätzliche Tabelle `Sensordaten_Aggregate` zu erstellen, die täglich vorbere vorberechnete Durchschnittswerte pro Maschine und Sensor speichert. Diskutiere **zwei Vorteile** und **zwei Nachteile** dieser Denormalisierung (je 1-2 Sätze).

e) **Monitoring**: Wie würdest du überprüfen, ob deine Indizes tatsächlich genutzt werden? Nenne das SQL-Keyword/Command für PostgreSQL oder SQLite.

---

### T3: Transaktionen und ACID in kritischen Systemen ⭐⭐⭐

**Kontext**: Ein automatisiertes Lagerverwaltungssystem für Maschinenbauteile muss sicherstellen, dass Lagerbestände immer korrekt sind, selbst bei gleichzeitigen Zugriffen von mehreren Robotern.

**Datenbank-Schema**:
```sql
CREATE TABLE Lagerbestand (
    Artikel_ID INTEGER PRIMARY KEY,
    Artikelname TEXT NOT NULL,
    Menge_Lager INTEGER NOT NULL CHECK(Menge_Lager >= 0),
    Mindestbestand INTEGER NOT NULL
);

CREATE TABLE Buchungen (
    Buchung_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Artikel_ID INTEGER NOT NULL,
    Menge_Aenderung INTEGER NOT NULL,  -- Positiv bei Einlagerung, negativ bei Entnahme
    Zeitstempel TEXT NOT NULL,
    Roboter_ID TEXT,
    FOREIGN KEY (Artikel_ID) REFERENCES Lagerbestand(Artikel_ID)
);
```

**Szenario**: Zwei Roboter (R1 und R2) greifen gleichzeitig auf dieselbe Schraube (Artikel-ID 101, aktueller Bestand: 50) zu. Beide wollen 40 Schrauben entnehmen.

**Transaktions-Ablauf ohne Isolation**:
1. R1 liest Bestand: 50 (ausreichend für 40)
2. R2 liest Bestand: 50 (ausreichend für 40)
3. R1 entnimmt 40 → aktualisiert Bestand auf 10
4. R2 entnimmt 40 → aktualisiert Bestand auf 10 (überschreibt R1's Update!)
5. **Problem**: 80 Schrauben wurden entnommen, aber nur 40 sind im System verbucht!

**Aufgaben**:

a) **ACID-Verletzung**: Welche der vier ACID-Eigenschaften wird in diesem Szenario verletzt? Erkläre in 2-3 Sätzen, warum dies kritisch ist.

b) **Isolation Level**: Beschreibe, welcher **Isolation Level** (READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE) dieses Problem lösen würde. Was garantiert dieser Level konkret?

c) **Pessimistische Lösung**: Entwerfe eine Transaktion mit **Pessimistic Locking** (verwende `SELECT ... FOR UPDATE` in SQL-Pseudocode), die sicherstellt, dass nur der erste Roboter erfolgreich ist, und der zweite eine Fehlermeldung erhält ("Bestand nicht ausreichend").

d) **Optimistische Lösung**: Füge eine Spalte `Version` zur `Lagerbestand`-Tabelle hinzu. Entwerfe eine Transaktion, die Optimistic Locking verwendet: Der UPDATE erfolgt nur, wenn die `Version` noch übereinstimmt. Bei Konflikt muss die Anwendung neu lesen und erneut versuchen. Zeige SQL-Pseudocode für dieses Pattern.

e) **Deadlock-Szenario**: Beschreibe ein Szenario mit **zwei** Robotern und **zwei** Artikeln, bei dem ein Deadlock entstehen kann (R1 sperrt Artikel A und wartet auf B, R2 sperrt B und wartet auf A). Schlage eine Strategie vor, um Deadlocks zu vermeiden (Tipp: Zugriffsreihenfolge).

f) **Durability**: Erkläre, wie ein DBMS Durability garantiert, wenn während einer Transaktion (nach Bestandsupdate, aber vor COMMIT) der Strom ausfällt. Nenne das verwendete Konzept.

---

## 🐍 Python-Aufgaben

**Hinweis**: Alle Python-Aufgaben arbeiten mit der Datenbank `produktionsdb.db` aus dem Ordner `testdaten/`. Diese Datenbank enthält Tabellen für Maschinen, Sensordaten, Wartungen und Produktionsläufe. Die Struktur findest du in `testdaten/TESTDATEN_README.md`.

---

### P1: SQL-Injection Schwachstelle beheben ⭐⭐

**Szenario**: Ein Legacy-System für die Qualitätskontrolle hat eine Sicherheitslücke. Der folgende Code erlaubt SQL-Injection-Angriffe:

```python
import sqlite3

def suche_artikel(artikelname):
    """
    UNSICHERER CODE - NUR ZU DEMONSTRATIONSZWECKEN!
    Sucht Artikel nach Name und gibt Prüfprotokolle zurück.
    """
    conn = sqlite3.connect('testdaten/produktionsdb.db')
    cursor = conn.cursor()
    
    # GEFÄHRLICH: String-Formatierung in SQL!
    query = f"SELECT * FROM Pruefprotokolle WHERE Artikelname = '{artikelname}'"
    cursor.execute(query)
    
    ergebnisse = cursor.fetchall()
    conn.close()
    return ergebnisse

# Beispiel-Aufruf (normal):
print(suche_artikel("Zahnrad Z42"))

# ANGRIFF: Ein böswilliger Benutzer gibt ein:
# artikelname = "' OR '1'='1"
# Query wird zu: SELECT * FROM Pruefprotokolle WHERE Artikelname = '' OR '1'='1'
# -> Gibt ALLE Protokolle zurück, nicht nur das gesuchte!
```

**Aufgaben**:

a) **Exploit demonstrieren**: Erkläre in 2-3 Sätzen, wie ein Angreifer mit dem Eingabestring `"' OR '1'='1"` **alle** Prüfprotokolle abrufen könnte, obwohl er nur Zugriff auf einen Artikel haben sollte.

b) **Kritischer Exploit**: Beschreibe einen noch gefährlicheren Angriff, bei dem der Eingabestring `"'; DROP TABLE Pruefprotokolle; --"` verwendet wird. Was passiert mit der Datenbank?

c) **Sichere Implementierung**: Schreibe die Funktion `suche_artikel_sicher(artikelname)` neu, die **Prepared Statements** mit `?` Platzhaltern verwendet. Stelle sicher, dass auch bei bösartigen Eingaben keine SQL-Injection möglich ist.

d) **Test**: Teste deine sichere Funktion mit den Eingaben:
   - Normaler Name: `"Zahnrad Z42"`
   - Angriff 1: `"' OR '1'='1"`
   - Angriff 2: `"'; DROP TABLE Pruefprotokolle; --"`
   
   Dokumentiere die Ausgabe (wie viele Zeilen werden jeweils zurückgegeben, und tritt ein Fehler auf?).

e) **Bonus**: Implementiere eine zusätzliche Funktion `suche_artikel_erweitert(artikelname, min_pruefwert)`, die nach Artikelname **und** einem Mindest-Prüfwert filtert. Verwende **Named Placeholders** (`:artikelname`, `:min_wert`).

---

### P2: UPDATE und DELETE mit Fehlerbehandlung ⭐⭐

**Szenario**: Eine Wartungs-Management-Anwendung muss Maschinendaten aktualisieren und alte Wartungsprotokolle löschen.

**Aufgaben**:

a) **Betriebsstunden aktualisieren**: Schreibe eine Funktion `aktualisiere_betriebsstunden(maschinen_id, neue_stunden)`, die:
   - Die Spalte `Betriebsstunden` in der Tabelle `Maschinen` für die gegebene `maschinen_id` aktualisiert
   - Prüft, ob die Maschine existiert (nutze `cursor.rowcount` nach dem UPDATE)
   - Bei Erfolg: `"Maschine {id}: {alte_stunden}h → {neue_stunden}h"` ausgibt
   - Bei Misserfolg: `"Maschine {id} nicht gefunden"` ausgibt
   - Die Transaktion committed

b) **Wartungen löschen**: Schreibe eine Funktion `loesche_alte_wartungen(tage_alt)`, die:
   - Alle Einträge aus der Tabelle `Wartungen` löscht, deren `Datum` älter als `tage_alt` Tage ist
   - Die Anzahl gelöschter Zeilen zurückgibt (`cursor.rowcount`)
   - `sqlite3.IntegrityError` abfängt (falls Foreign Key Constraints verletzt werden)
   - Bei Fehler: Transaktion rollbackt und eine Fehlermeldung ausgibt

c) **Maschine außer Betrieb setzen**: Schreibe eine Funktion `deaktiviere_maschine_mit_wartungen(maschinen_id)`, die:
   - Die Spalte `Aktiv` in `Maschinen` auf `0` setzt
   - **Zusätzlich** einen Eintrag in `Wartungen` erstellt mit:
     - `Maschinen_ID = maschinen_id`
     - `Wartungstyp = 'Stilllegung'`
     - `Datum = datetime.now().strftime('%Y-%m-%d')`
     - `Beschreibung = 'Maschine außer Betrieb gesetzt'`
   - Beide Operationen in **einer Transaktion** durchführt (beide müssen erfolgreich sein, sonst Rollback)
   - Bei Erfolg: `"Maschine {id} wurde deaktiviert und Wartungseintrag erstellt"` ausgibt
   - Bei Fehler: Rollback + Fehlermeldung

d) **Fehlerbehandlung testen**: Teste `loesche_alte_wartungen(365)` und provoziere bewusst einen `IntegrityError`:
   - Aktiviere Foreign Keys: `PRAGMA foreign_keys = ON;`
   - Versuche, Wartungen zu löschen, die über Foreign Keys mit anderen Tabellen verknüpft sind
   - Dokumentiere, welcher Fehler auftritt und wie deine Funktion damit umgeht

e) **Cascade DELETE**: Ändere das Schema der Tabelle `Wartungen` so, dass beim Löschen einer Maschine **automatisch** alle zugehörigen Wartungen gelöscht werden. Gib das `ALTER TABLE`- oder `CREATE TABLE`-Statement mit `ON DELETE CASCADE` an.

---

### P3: Transaktionen mit Rollback ⭐⭐⭐

**Szenario**: Ein automatisiertes Produktionsplanungssystem muss einen Produktionslauf starten. Dabei werden mehrere Tabellen gleichzeitig geändert: Materialverbrauch wird gebucht, Maschinenstatus wird aktualisiert, und ein neuer Produktionslauf wird angelegt. **Alle drei Operationen müssen erfolgreich sein** – bei einem Fehler darf **keine** der Änderungen persistiert werden.

**Tabellen** (siehe `testdaten/produktionsdb.db`):
- `Materialbestand` (Material_ID, Materialname, Menge_Lager, Einheit)
- `Maschinen` (Maschinen_ID, Name, Status TEXT)  -- Status: 'Bereit', 'Produktion', 'Wartung'
- `Produktionslaeufe` (Lauf_ID, Maschinen_ID, Artikel, Menge_Geplant, Start_Zeit, Status TEXT)

**Aufgaben**:

a) **Transaktion implementieren**: Schreibe eine Funktion `starte_produktionslauf(maschinen_id, artikel, menge, material_verbrauch)`, die:
   - Parameter `material_verbrauch` ist ein Dictionary: `{'Material_ID': menge_verbraucht, ...}`
   - **Operation 1**: Prüft, ob die Maschine im Status "Bereit" ist (sonst Exception `ValueError("Maschine nicht bereit")`)
   - **Operation 2**: Reduziert den `Materialbestand` für alle Materialien in `material_verbrauch`. Wirft `ValueError("Materialbestand nicht ausreichend")`, falls Menge negativ werden würde.
   - **Operation 3**: Aktualisiert Maschinenstatus auf "Produktion"
   - **Operation 4**: Fügt einen neuen Eintrag in `Produktionslaeufe` ein (Start_Zeit = aktuelles Datum, Status = 'Laufend')
   - Bei **jedem Fehler**: Komplettes Rollback aller vier Operationen
   - Bei Erfolg: Commit und Ausgabe `"Produktionslauf {lauf_id} gestartet auf Maschine {maschinen_id}"`

b) **Rollback testen**: Teste deine Funktion mit den folgenden Szenarien:
   - **Erfolgsfall**: Maschine 1 ist bereit, Material ausreichend vorhanden → Alle Operationen erfolgreich
   - **Fehlerfall 1**: Maschine 1 ist bereits in "Produktion" → Rollback, keine Änderungen in DB
   - **Fehlerfall 2**: Material-ID 101 hat nur 50 Einheiten, aber du versuchst 100 zu verbrauchen → Rollback
   
   Prüfe nach jedem Test mit SELECT-Queries, ob die Datenbank unverändert bleibt bei Fehlern.

c) **Nested Transactions (Savepoints)**: Erweitere die Funktion um **Savepoints**: Falls Material-Operation fehlschlägt, rollback nur bis zu einem Savepoint nach der Maschinen-Prüfung (nicht komplett). Nutze `SAVEPOINT` und `ROLLBACK TO` in SQL.

d) **Logging**: Füge eine Tabelle `Transaktions_Log` hinzu (Log_ID, Zeitstempel, Operation, Status TEXT, Fehler TEXT). Protokolliere **jeden** Versuch (erfolgreich oder fehlgeschlagen) mit Commit/Rollback-Status.

e) **Context Manager**: Erstelle eine eigene Context Manager Klasse `ProduktionsTransaktion`, die automatisch Rollback bei Exceptions durchführt:
   ```python
   with ProduktionsTransaktion('testdaten/produktionsdb.db') as db:
       db.cursor.execute(...)
       # Bei Exception automatisch Rollback
   ```

---

### P4: Aggregationen und Visualisierung mit pandas + matplotlib ⭐⭐⭐

**Szenario**: Die Produktionsleitung möchte die **Wartungskosten** nach Maschinentyp und Quartal analysieren, um Budgets für 2025 zu planen.

**Datenbank**: `testdaten/produktionsdb.db`

**Tabellen**:
- `Maschinen` (Maschinen_ID, Name, Typ TEXT, Baujahr, Aktiv)
- `Wartungen` (Wartung_ID, Maschinen_ID FK, Wartungstyp TEXT, Datum TEXT, Kosten REAL, Beschreibung)

**Aufgaben**:

a) **Daten abfragen**: Schreibe eine SQL-Query mit JOIN, die folgende Informationen extrahiert:
   - Maschinentyp (`Typ` aus `Maschinen`)
   - Quartal aus Wartungsdatum (extrahiere Jahr und Quartal aus `Datum`)
   - Summe der Wartungskosten (`SUM(Kosten)`)
   - Anzahl der Wartungen (`COUNT(*)`)
   
   Gruppiere nach Typ und Quartal. Die Query sollte etwa so aussehen:
   ```sql
   SELECT 
       m.Typ,
       strftime('%Y', w.Datum) || '-Q' || ((CAST(strftime('%m', w.Datum) AS INTEGER) - 1) / 3 + 1) AS Quartal,
       SUM(w.Kosten) AS Gesamt_Kosten,
       COUNT(*) AS Anzahl_Wartungen
   FROM Maschinen m
   INNER JOIN Wartungen w ON m.Maschinen_ID = w.Maschinen_ID
   WHERE ...
   GROUP BY ...
   ```

b) **pandas DataFrame**: Lade die Ergebnisse in einen pandas DataFrame:
   ```python
   import pandas as pd
   import sqlite3
   
   conn = sqlite3.connect('testdaten/produktionsdb.db')
   df = pd.read_sql_query(query, conn)
   ```

c) **Datenbereinigung**: 
   - Konvertiere die Spalte `Gesamt_Kosten` zu `float`
   - Filtere nur Quartale aus 2023 und 2024
   - Sortiere nach Typ und Quartal

d) **Pivot-Tabelle**: Erstelle eine Pivot-Tabelle mit:
   - Index: Quartal (z.B. "2023-Q1", "2023-Q2", ...)
   - Spalten: Maschinentyp (z.B. "Fräse", "Drehbank", "Roboter")
   - Werte: Summe der Wartungskosten
   
   Verwende `pd.pivot_table()` mit `aggfunc='sum'` und `fill_value=0`.

e) **Visualisierung**: Erstelle **zwei Plots** mit matplotlib:
   
   **Plot 1**: Gestapeltes Balkendiagramm (`plt.bar()` mit `bottom`-Parameter)
   - X-Achse: Quartale (2023-Q1 bis 2024-Q4)
   - Y-Achse: Wartungskosten in Euro
   - Gestapelt nach Maschinentyp (unterschiedliche Farben)
   - Titel: "Wartungskosten nach Quartal und Maschinentyp"
   - Legende mit Maschinentypen
   - Speichere als `wartungskosten_quartal.png`
   
   **Plot 2**: Liniendiagramm für Trend-Analyse
   - Gruppiere nach Typ, zeige Gesamtkosten über Zeit
   - Mehrere Linien (eine pro Maschinentyp)
   - Markiere Maximalwerte mit `plt.annotate()`
   - Speichere als `wartungskosten_trend.png`

f) **Statistik-Ausgabe**: Berechne und ausgebe:
   - Durchschnittliche Kosten pro Wartung nach Typ (Gesamt_Kosten / Anzahl_Wartungen)
   - Typ mit höchsten Gesamtkosten
   - Quartal mit höchsten Gesamtkosten über alle Typen
   
   Nutze pandas-Methoden wie `.mean()`, `.max()`, `.idxmax()`.

g) **Export**: Exportiere die Pivot-Tabelle als Excel-Datei `wartungskosten_analyse.xlsx` (nutze `df.to_excel()`).

---

### P5: Projekt – Qualitätskontroll-Dashboard mit JOINs und Subqueries ⭐⭐⭐⭐

**Szenario**: Du sollst ein **Qualitätskontroll-Dashboard** für eine Fertigungslinie entwickeln, das Prüfprotokolle, Maschinen und Produktionsläufe verknüpft. Das System muss folgende Anforderungen erfüllen:

1. **Datenbank-Schema erweitern**: Ergänze die bestehende `produktionsdb.db` um Qualitätsdaten
2. **Komplexe Queries mit JOINs**: Verknüpfe mehrere Tabellen für Reports
3. **Subqueries für Analysen**: Finde "Problem-Maschinen" und "Top-Artikel"
4. **Visualisierung**: Erstelle ein Dashboard mit pandas + matplotlib

**Bestehende Tabellen** (siehe `testdaten/produktionsdb.db`):
- `Maschinen` (Maschinen_ID, Name, Typ, Baujahr, Aktiv)
- `Produktionslaeufe` (Lauf_ID, Maschinen_ID FK, Artikel, Menge_Geplant, Start_Zeit, Status)

**Neue Tabellen** (erstelle diese):

```sql
CREATE TABLE Pruefprotokolle (
    Pruef_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Lauf_ID INTEGER NOT NULL,
    Artikel TEXT NOT NULL,
    Pruef_Datum TEXT NOT NULL,
    Pruef_Typ TEXT NOT NULL,  -- 'Sichtprüfung', 'Maßprüfung', 'Funktionstest'
    Pruef_Wert REAL,           -- Z.B. gemessene Länge in mm, Härte HRC, etc.
    Soll_Wert REAL,            -- Sollwert laut Spezifikation
    Toleranz REAL,             -- Zulässige Abweichung (+/-)
    Status TEXT CHECK(Status IN ('Bestanden', 'Fehlgeschlagen', 'Nacharbeit')),
    Pruefer_Name TEXT,
    Bemerkung TEXT,
    FOREIGN KEY (Lauf_ID) REFERENCES Produktionslaeufe(Lauf_ID) ON DELETE CASCADE
);

CREATE TABLE Fehlerarten (
    Fehler_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Pruef_ID INTEGER NOT NULL,
    Fehlerart TEXT NOT NULL,  -- 'Maßabweichung', 'Oberflächenfehler', 'Funktionsstörung'
    Schweregrad INTEGER CHECK(Schweregrad BETWEEN 1 AND 5),  -- 1=gering, 5=kritisch
    Beschreibung TEXT,
    FOREIGN KEY (Pruef_ID) REFERENCES Pruefprotokolle(Pruef_ID) ON DELETE CASCADE
);
```

**Aufgaben**:

#### a) Schema und Beispieldaten (20 Punkte)

1. Erstelle die beiden neuen Tabellen `Pruefprotokolle` und `Fehlerarten` in `produktionsdb.db`
2. Erstelle Indizes auf:
   - `Pruefprotokolle(Lauf_ID)`
   - `Pruefprotokolle(Status)`
   - `Fehlerarten(Pruef_ID)`
   - `Fehlerarten(Fehlerart)`
3. Füge mindestens **30 Prüfprotokolle** für verschiedene Produktionsläufe ein:
   - Mindestens 3 verschiedene Artikel ("Zahnrad Z42", "Welle W15", "Gehäuse G08")
   - Mindestens 3 verschiedene Prüftypen
   - Status-Verteilung: ca. 70% "Bestanden", 20% "Fehlgeschlagen", 10% "Nacharbeit"
   - Realistische Werte mit Toleranzen (z.B. Soll: 50.00mm, Toleranz: ±0.05mm, Ist: 50.03mm → "Bestanden")
4. Füge für jeden fehlgeschlagenen Test mindestens einen Eintrag in `Fehlerarten` ein

#### b) Komplexe JOIN-Queries (30 Punkte)

Schreibe folgende Queries:

**Query 1**: **Qualitätsübersicht nach Maschine**
- Zeige: Maschinen-Name, Maschinen-Typ, Anzahl Produktionsläufe, Anzahl Prüfungen, Anzahl bestandene/fehlgeschlagene Tests, Fehlerquote (%)
- Verknüpfe: `Maschinen` → `Produktionslaeufe` → `Pruefprotokolle`
- Gruppiere nach Maschine
- Sortiere nach Fehlerquote absteigend (schlechteste Maschinen zuerst)

**Query 2**: **Problem-Artikel identifizieren**
- Zeige: Artikel-Name, Gesamtanzahl Prüfungen, Anzahl Fehler, Häufigste Fehlerart, Durchschnittlicher Schweregrad
- Nutze Subquery: Finde die häufigste Fehlerart mit `GROUP BY` und `COUNT(*)`, dann `MAX()`
- Filtere nur Artikel mit mehr als 3 fehlgeschlagenen Tests

**Query 3**: **Prüfer-Performance**
- Zeige: Prüfer-Name, Anzahl Prüfungen, Anzahl Fehlerfunde, Durchschnittliche Prüf-Zeit (falls Zeitstempel vorhanden)
- Sortiere nach Anzahl Fehlerfunde absteigend

#### c) Subqueries für Analyse (20 Punkte)

**Query 4**: **Maschinen mit überdurchschnittlicher Fehlerquote**
- Nutze Subquery, um zuerst die durchschnittliche Fehlerquote **über alle Maschinen** zu berechnen
- Hauptquery: Zeige nur Maschinen, deren Fehlerquote darüber liegt
- Beispiel-Struktur:
  ```sql
  SELECT m.Name, (Fehler / Total * 100.0) AS Fehlerquote
  FROM ...
  WHERE (Fehler / Total * 100.0) > (
      SELECT AVG(Fehler / Total * 100.0) FROM ...
  )
  ```

**Query 5**: **Artikel, die auf allen Maschinen getestet wurden**
- Nutze Subquery oder `HAVING COUNT(DISTINCT Maschinen_ID) = (SELECT COUNT(*) FROM Maschinen WHERE Aktiv = 1)`
- Zeige nur Artikel, die auf mindestens 3 verschiedenen Maschinen produziert wurden

#### d) pandas DataFrame und Aggregationen (15 Punkte)

1. Lade Query 1 (Qualitätsübersicht) in pandas DataFrame
2. Berechne zusätzliche Kennzahlen:
   - First Pass Yield (FPY): Anteil bestandene Tests beim ersten Versuch
   - Mean Time Between Failures (MTBF): Durchschnittliche Anzahl bestandene Tests zwischen Fehlern
3. Filtere Maschinen mit FPY < 80% (kritische Maschinen)
4. Exportiere als CSV: `qualitaetsuebersicht.csv`

#### e) Visualisierung (15 Punkte)

Erstelle **drei Plots**:

**Plot 1**: Balkendiagramm – Fehlerquote nach Maschine
- X-Achse: Maschinen-Name
- Y-Achse: Fehlerquote in %
- Farbe: Grün (<5%), Gelb (5-10%), Rot (>10%)
- Horizontale Linie bei 5% als Soll-Wert

**Plot 2**: Heatmap – Fehlerarten nach Artikel
- Zeilen: Artikel-Namen
- Spalten: Fehlerarten
- Farbe: Anzahl Fehler (verwende `plt.imshow()` mit Colorbar)

**Plot 3**: Zeitreihe – Fehlerquote über Zeit
- X-Achse: Wochen oder Monate
- Y-Achse: Fehlerquote %
- Mehrere Linien für verschiedene Artikel
- Markiere Wochen mit >15% Fehlerquote

Speichere alle Plots als PNG-Dateien.

---

**Abgabe**:
- `p5_qualitaetskontrolle.py` (Hauptskript mit allen Funktionen)
- `qualitaetsuebersicht.csv` (Export aus pandas)
- `fehlerquote_maschinen.png`, `fehlerarten_heatmap.png`, `fehlerquote_zeit.png` (Plots)
- `testdaten/produktionsdb.db` (erweiterte Datenbank mit neuen Tabellen und Daten)

**Bonus** (5 Punkte): Erstelle eine interaktive Streamlit-App, die die Queries ausführt und Plots anzeigt.

---

