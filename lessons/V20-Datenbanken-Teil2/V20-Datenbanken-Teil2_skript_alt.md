# V20 – Datenbanken – Teil 2

**Vorlesungsinhalte:**
- Informatik-Theorie: Datenbanken – Teil 2 (Normalisierung, Indizes, Transaktionen, NoSQL)
- Python-Praxis: Datenbankverbindung & SQL – Teil 2 (Prepared Statements, UPDATE/DELETE, Transaktionen, Context Manager)

---

## 📚 Informatik-Theorie: Datenbanken – Teil 2

### Normalisierung relationaler Datenbanken

Die **Normalisierung** ist ein systematischer Prozess zur Strukturierung relationaler Datenbanken, um Redundanz zu minimieren und Datenintegrität zu maximieren. Ziel ist es, Anomalien bei INSERT, UPDATE und DELETE zu vermeiden. Edgar F. Codd definierte die ersten drei Normalformen (1NF, 2NF, 3NF), die in der Praxis am häufigsten angewendet werden. Weitere Normalformen (BCNF, 4NF, 5NF) existieren, werden aber seltener benötigt.

> [!NOTE]
> **Normalisierung** bedeutet, Datenstrukturen so zu organisieren, dass jede Information nur einmal gespeichert wird. Dies geschieht durch Aufteilung von Tabellen und Verwendung von Fremdschlüsseln. Der Prozess folgt strengen Regeln, die schrittweise angewendet werden.

#### Warum Normalisierung wichtig ist

Unnormalisierte Datenbanken leiden unter drei Hauptproblemen:

**Update-Anomalie**: Wenn dieselbe Information mehrfach gespeichert ist, muss sie an mehreren Stellen geändert werden. Wird eine Stelle vergessen, entsteht Inkonsistenz.

**Insert-Anomalie**: Manchmal können Daten nicht eingefügt werden, weil abhängige Daten fehlen. Beispiel: Ein Lieferant kann nicht gespeichert werden, bevor ein Produkt existiert, das er liefert.

**Delete-Anomalie**: Das Löschen eines Datensatzes kann unbeabsichtigt andere Informationen entfernen. Beispiel: Wird das letzte Produkt eines Lieferanten gelöscht, gehen alle Lieferanteninformationen verloren.

> [!TIP]
> **Praktisches Beispiel für Anomalien**:
> 
> Tabelle `Bestellungen` (unnormalisiert):
> 
> | Bestell_ID | Kunde_Name | Kunde_Adresse   | Artikel_Name | Artikel_Preis | Menge |
> |------------|------------|-----------------|--------------|---------------|-------|
> | 1          | Müller AG  | Hauptstr. 10    | Schraube M8  | 0.15          | 1000  |
> | 2          | Müller AG  | Hauptstr. 10    | Mutter M8    | 0.10          | 500   |
> | 3          | Schmidt GmbH | Bahnhofstr. 5 | Schraube M8  | 0.15          | 200   |
> 
> **Update-Anomalie**: Müller AG zieht um → Adresse muss in zwei Zeilen geändert werden.  
> **Delete-Anomalie**: Wird Bestellung 3 gelöscht, verlieren wir Schmidt GmbH komplett.  
> **Insert-Anomalie**: Wir können keinen neuen Kunden anlegen, bevor er etwas bestellt hat.

#### Erste Normalform (1NF)

Eine Tabelle ist in **1NF**, wenn folgende Bedingungen erfüllt sind:

1. **Atomare Werte**: Jede Zelle enthält genau einen Wert (keine Listen, Mengen oder verschachtelten Strukturen).
2. **Eindeutige Spaltennamen**: Jede Spalte hat einen eindeutigen Namen.
3. **Gleicher Datentyp pro Spalte**: Alle Werte in einer Spalte haben denselben Typ.
4. **Eindeutige Zeilen**: Es gibt keine Duplikate (Primärschlüssel vorhanden).

> [!WARNING]
> **Häufiger Fehler**: Mehrere Werte in einer Zelle speichern (z.B. `"Telefon1, Telefon2, Telefon3"`). Dies verletzt 1NF und macht Abfragen extrem umständlich.

**Beispiel für Nicht-1NF**:

Tabelle `Mitarbeiter`:
| Mitarbeiter_ID | Name   | Telefonnummern              |
|----------------|--------|-----------------------------|
| 1              | Müller | +49 123 456, +49 789 012    |
| 2              | Schmidt| +49 555 999                 |

Die Spalte `Telefonnummern` enthält mehrere Werte → **verletzt 1NF**.

**Lösung: In 1NF umwandeln**:

Tabelle `Mitarbeiter`:
| Mitarbeiter_ID | Name    |
|----------------|---------|
| 1              | Müller  |
| 2              | Schmidt |

Tabelle `Telefonnummern`:
| Telefon_ID | Mitarbeiter_ID | Nummer         | Typ     |
|------------|----------------|----------------|---------|
| 1          | 1              | +49 123 456    | Mobil   |
| 2          | 1              | +49 789 012    | Festnetz|
| 3          | 2              | +49 555 999    | Mobil   |

Jetzt ist jede Zelle atomar, und wir können einfach nach Telefonnummern suchen oder filtern.

#### Zweite Normalform (2NF)

Eine Tabelle ist in **2NF**, wenn sie:

1. **In 1NF** ist.
2. **Keine partiellen Abhängigkeiten** hat: Jedes Nicht-Schlüssel-Attribut ist von **allen Teilen** des Primärschlüssels abhängig, nicht nur von einem Teil.

Diese Regel ist nur relevant bei **zusammengesetzten Primärschlüsseln** (bestehend aus mehreren Spalten).

> [!NOTE]
> Eine **partielle Abhängigkeit** liegt vor, wenn ein Nicht-Schlüssel-Attribut nur von einem Teil eines zusammengesetzten Primärschlüssels abhängt. Dies führt zu Redundanz.

**Beispiel für Nicht-2NF**:

Tabelle `Bestellpositionen`:
| Bestell_ID | Artikel_ID | Artikel_Name | Artikel_Preis | Menge |
|------------|------------|--------------|---------------|-------|
| 1          | 10         | Schraube M8  | 0.15          | 1000  |
| 1          | 11         | Mutter M8    | 0.10          | 500   |
| 2          | 10         | Schraube M8  | 0.15          | 200   |

Primärschlüssel: `(Bestell_ID, Artikel_ID)` (zusammengesetzt)

**Problem**: `Artikel_Name` und `Artikel_Preis` hängen nur von `Artikel_ID` ab, nicht von der gesamten Kombination `(Bestell_ID, Artikel_ID)`. Dies ist eine **partielle Abhängigkeit** → verletzt 2NF.

**Folge**: "Schraube M8" und ihr Preis werden mehrfach gespeichert (Zeile 1 und 3). Ändert sich der Preis, muss er in allen Zeilen aktualisiert werden.

**Lösung: In 2NF umwandeln**:

Tabelle `Bestellpositionen`:
| Bestell_ID | Artikel_ID | Menge |
|------------|------------|-------|
| 1          | 10         | 1000  |
| 1          | 11         | 500   |
| 2          | 10         | 200   |

Tabelle `Artikel`:
| Artikel_ID | Artikel_Name | Artikel_Preis |
|------------|--------------|---------------|
| 10         | Schraube M8  | 0.15          |
| 11         | Mutter M8    | 0.10          |

Jetzt sind alle Nicht-Schlüssel-Attribute vom gesamten Primärschlüssel abhängig. Artikelinformationen stehen nur noch einmal in der Tabelle `Artikel`.

#### Dritte Normalform (3NF)

Eine Tabelle ist in **3NF**, wenn sie:

1. **In 2NF** ist.
2. **Keine transitiven Abhängigkeiten** hat: Kein Nicht-Schlüssel-Attribut ist von einem anderen Nicht-Schlüssel-Attribut abhängig.

> [!NOTE]
> Eine **transitive Abhängigkeit** liegt vor, wenn ein Nicht-Schlüssel-Attribut B von einem anderen Nicht-Schlüssel-Attribut A abhängt, das wiederum vom Primärschlüssel abhängt. Schema: Primärschlüssel → A → B. Dies führt zu Redundanz.

**Beispiel für Nicht-3NF**:

Tabelle `Mitarbeiter`:
| Mitarbeiter_ID | Name    | Abteilung_ID | Abteilung_Name | Abteilung_Standort |
|----------------|---------|--------------|----------------|--------------------|
| 1              | Müller  | 10           | Produktion     | Halle A            |
| 2              | Schmidt | 10           | Produktion     | Halle A            |
| 3              | Weber   | 20           | Qualitätssicherung | Gebäude B      |

Primärschlüssel: `Mitarbeiter_ID`

**Problem**: `Abteilung_Name` und `Abteilung_Standort` hängen von `Abteilung_ID` ab, nicht direkt von `Mitarbeiter_ID`. Transitive Abhängigkeit: `Mitarbeiter_ID → Abteilung_ID → Abteilung_Name, Abteilung_Standort` → verletzt 3NF.

**Folge**: "Produktion" und "Halle A" werden mehrfach gespeichert (Zeile 1 und 2). Ändert sich der Standort der Produktion, muss dies in allen Zeilen geändert werden.

**Lösung: In 3NF umwandeln**:

Tabelle `Mitarbeiter`:
| Mitarbeiter_ID | Name    | Abteilung_ID |
|----------------|---------|--------------|
| 1              | Müller  | 10           |
| 2              | Schmidt | 10           |
| 3              | Weber   | 20           |

Tabelle `Abteilungen`:
| Abteilung_ID | Abteilung_Name       | Abteilung_Standort |
|--------------|----------------------|--------------------|
| 10           | Produktion           | Halle A            |
| 20           | Qualitätssicherung   | Gebäude B          |

Jetzt ist jede Information nur einmal gespeichert, und Updates sind konsistent.

> [!TIP]
> **Faustregel für Normalisierung**:
> - **1NF**: Eine Spalte = ein Wert (keine Listen!)
> - **2NF**: Keine halben Schlüssel (bei zusammengesetzten Primärschlüsseln)
> - **3NF**: Nicht-Schlüssel-Attribute hängen nur vom Primärschlüssel ab, nicht voneinander
> 
> In der Praxis sind die meisten gut entworfenen Datenbanken in 3NF.

#### Denormalisierung: Wann macht Abweichung Sinn?

Obwohl Normalisierung Redundanz reduziert, kann sie Performance-Probleme verursachen. Stark normalisierte Datenbanken erfordern viele **JOINs**, um Daten zusammenzufügen. Bei sehr großen Datenmengen oder komplexen Queries kann dies langsam werden.

**Denormalisierung** bedeutet bewusst Redundanz einzuführen, um Abfragen zu beschleunigen. Dies sollte nur nach sorgfältiger Analyse geschehen.

**Typische Szenarien für Denormalisierung**:

**Read-Heavy Workloads**: Wenn Daten sehr viel häufiger gelesen als geschrieben werden, können berechnete Werte oder duplizierte Informationen die Performance verbessern.

**Reporting/Analytics**: Data Warehouses verwenden oft **Star-Schema** oder **Snowflake-Schema**, die teilweise denormalisiert sind, um komplexe Aggregationen zu beschleunigen.

**Caching**: Berechnete Werte (z.B. Summen, Durchschnitte) können vorberechnet und gespeichert werden, statt sie bei jeder Abfrage neu zu berechnen.

> [!WARNING]
> **Denormalisierung ist ein Trade-Off**: Man gewinnt Leseperformance, verliert aber Konsistenzgarantien und erhöht Komplexität bei Updates. Verwende Denormalisierung nur, wenn Performance-Messungen zeigen, dass normalisierte Abfragen zu langsam sind.

**Beispiel**: In einer E-Commerce-Datenbank könnte man `Anzahl_Bestellungen` und `Umsatz_Gesamt` direkt in der `Kunden`-Tabelle speichern, statt sie jedes Mal aus der `Bestellungen`-Tabelle zu berechnen. Dies erfordert aber Trigger oder Anwendungslogik, um diese Felder bei jeder Bestellung zu aktualisieren.

### Indizes zur Performance-Optimierung

Ein **Index** ist eine Datenstruktur, die schnelle Zugriffe auf Zeilen einer Tabelle basierend auf bestimmten Spalten ermöglicht. Ohne Indizes muss das DBMS bei Abfragen die gesamte Tabelle durchsuchen (**Full Table Scan**), was bei großen Tabellen sehr langsam ist.

> [!NOTE]
> Ein **Index** funktioniert ähnlich wie ein Stichwortverzeichnis in einem Buch: Statt das gesamte Buch zu durchsuchen, schlägt man im Index nach und findet direkt die relevanten Seiten. Technisch sind Indizes meist **B-Tree** oder **Hash-Tabellen**.

#### Wie funktionieren Indizes?

Wenn ein Index auf Spalte `X` existiert, erstellt das DBMS eine sortierte Liste aller Werte von `X` zusammen mit Zeigern auf die entsprechenden Zeilen. Bei einer Abfrage `WHERE X = 'Wert'` kann das DBMS binäre Suche verwenden, statt alle Zeilen zu durchlaufen.

**Beispiel ohne Index**:

```sql
SELECT * FROM Maschinen WHERE Maschinentyp = 'CNC-Fräse';
```

Ohne Index: DBMS muss alle Zeilen der Tabelle `Maschinen` durchgehen → O(n) Zeitkomplexität.

**Beispiel mit Index**:

```sql
CREATE INDEX idx_maschinentyp ON Maschinen(Maschinentyp);
SELECT * FROM Maschinen WHERE Maschinentyp = 'CNC-Fräse';
```

Mit Index: DBMS nutzt den Index → O(log n) Zeitkomplexität für Suche, dann direkter Zugriff auf Zeilen.

> [!TIP]
> **B-Tree-Indizes** (der Standard in den meisten DBMS):
> - Sortierte Baumstruktur mit garantiert ausbalancierter Höhe
> - Suche: O(log n)
> - Einfügen/Löschen: O(log n)
> - Gut für Bereichsabfragen (`WHERE X BETWEEN a AND b`)
> - Gut für Sortierungen (`ORDER BY X`)

#### Wann sollte man Indizes erstellen?

Indizes beschleunigen **SELECT**, **WHERE**, **JOIN** und **ORDER BY** Operationen, verlangsamen aber **INSERT**, **UPDATE** und **DELETE**, weil der Index aktualisiert werden muss.

**Gute Kandidaten für Indizes**:

**Primärschlüssel**: Wird automatisch indexiert (in den meisten DBMS).

**Fremdschlüssel**: Beschleunigt JOINs erheblich. Manche DBMS indexieren Fremdschlüssel automatisch, andere nicht.

**Spalten in WHERE-Klauseln**: Wenn eine Spalte häufig gefiltert wird (`WHERE Status = 'aktiv'`), hilft ein Index.

**Spalten in JOIN-Bedingungen**: Wenn Tabellen oft über eine Spalte verknüpft werden, sollte diese indexiert sein.

**Spalten in ORDER BY/GROUP BY**: Indizes können Sortierungen beschleunigen oder überflüssig machen.

**Schlechte Kandidaten für Indizes**:

**Spalten mit wenigen unterschiedlichen Werten** (Low Cardinality): Ein Index auf eine Spalte mit nur zwei Werten (z.B. `Geschlecht: M/F`) bringt kaum Vorteil.

**Selten genutzte Spalten**: Wenn eine Spalte nie in WHERE, JOIN oder ORDER BY vorkommt, ist ein Index verschwendeter Speicher.

**Sehr kleine Tabellen**: Bei Tabellen mit nur wenigen Dutzend Zeilen ist ein Full Table Scan schneller als Index-Zugriff (wegen Overhead).

> [!WARNING]
> **Zu viele Indizes schaden**: Jeder Index benötigt Speicherplatz und verlangsamt Schreiboperationen. Eine Tabelle mit 10 Indizes kann bei INSERT/UPDATE extrem langsam werden. Erstelle Indizes nur basierend auf tatsächlichen Query-Patterns.

#### Index-Typen

**Einspalten-Index (Single-Column Index)**:

```sql
CREATE INDEX idx_baujahr ON Maschinen(Baujahr);
```

Beschleunigt Abfragen wie `WHERE Baujahr > 2015`.

**Mehrspaltiger Index (Composite Index)**:

```sql
CREATE INDEX idx_typ_baujahr ON Maschinen(Maschinentyp, Baujahr);
```

Beschleunigt Abfragen wie `WHERE Maschinentyp = 'Fräse' AND Baujahr > 2015`. Die Reihenfolge der Spalten ist wichtig: Dieser Index hilft auch bei `WHERE Maschinentyp = 'Fräse'`, aber **nicht** bei `WHERE Baujahr > 2015` alleine.

**Unique Index**:

```sql
CREATE UNIQUE INDEX idx_seriennummer ON Maschinen(Seriennummer);
```

Erzwingt Eindeutigkeit (wie ein UNIQUE Constraint) und bietet zusätzliche Performance.

**Partial Index (PostgreSQL)**:

```sql
CREATE INDEX idx_aktive_maschinen ON Maschinen(Maschinen_ID) WHERE Aktiv = true;
```

Indexiert nur Zeilen, die eine Bedingung erfüllen. Spart Speicher und beschleunigt Abfragen auf dieser Teilmenge.

**Volltext-Index (Full-Text Index)**:

```sql
CREATE FULLTEXT INDEX idx_beschreibung ON Artikel(Beschreibung);
```

Für Textsuche in langen Texten (z.B. Produktbeschreibungen). Unterstützt Wortsuche, Stemming, Relevanz-Ranking.

> [!TIP]
> **Index-Analyse**: Die meisten DBMS bieten `EXPLAIN` oder `EXPLAIN ANALYZE`, um zu sehen, ob ein Index genutzt wird:
> 
> ```sql
> EXPLAIN SELECT * FROM Maschinen WHERE Maschinentyp = 'CNC-Fräse';
> ```
> 
> Output zeigt, ob "Index Scan" oder "Sequential Scan" verwendet wird.

### Transaktionen und ACID-Prinzipien

In produktiven Datenbankanwendungen finden oft mehrere Operationen statt, die logisch zusammengehören. Beispiel: Eine Banküberweisung besteht aus zwei Operationen: Geld vom Konto A abbuchen und Geld auf Konto B gutschreiben. Beide Operationen müssen entweder komplett ausgeführt werden oder gar nicht – ein Zwischenzustand (Geld abgebucht, aber nicht gutgeschrieben) wäre katastrophal.

Eine **Transaktion** ist eine Folge von Datenbankoperationen, die als atomare Einheit behandelt wird. Das DBMS garantiert, dass entweder alle Operationen erfolgreich ausgeführt werden (**COMMIT**) oder keine (**ROLLBACK**).

> [!NOTE]
> Eine **Transaktion** ist eine Sequenz von SQL-Statements, die als unteilbare Einheit ausgeführt wird. Transaktionen beginnen mit `BEGIN` (oder implizit beim ersten Statement) und enden mit `COMMIT` (erfolgreich) oder `ROLLBACK` (abgebrochen).

#### Die ACID-Eigenschaften

ACID ist ein Akronym für vier fundamentale Eigenschaften, die ein transaktionales DBMS garantieren muss:

**Atomicity (Atomarität)**: Eine Transaktion ist unteilbar. Entweder werden alle Operationen ausgeführt, oder keine. Bei einem Fehler (z.B. Constraint-Verletzung, Systemabsturz) werden alle bisher durchgeführten Operationen der Transaktion rückgängig gemacht.

**Beispiel**: Überweisung von 100 € von Konto A nach Konto B:

```sql
BEGIN TRANSACTION;
UPDATE Konten SET Saldo = Saldo - 100 WHERE Konto_ID = 1;  -- Konto A
UPDATE Konten SET Saldo = Saldo + 100 WHERE Konto_ID = 2;  -- Konto B
COMMIT;
```

Wenn das zweite UPDATE fehlschlägt (z.B. Konto B existiert nicht), wird das erste UPDATE automatisch rückgängig gemacht. Das Geld verschwindet nicht.

**Consistency (Konsistenz)**: Eine Transaktion überführt die Datenbank von einem konsistenten Zustand in einen anderen konsistenten Zustand. Alle Integritätsbedingungen (Constraints, Foreign Keys, Check Constraints) müssen am Ende der Transaktion erfüllt sein.

**Beispiel**: Ein Fremdschlüssel-Constraint verbietet Referenzen auf nicht-existierende Zeilen. Wenn eine Transaktion versucht, ein Wartungsprotokoll für eine nicht-existierende Maschine zu erstellen, schlägt sie fehl, und die Datenbank bleibt konsistent.

**Isolation (Isolierung)**: Parallele Transaktionen beeinflussen sich nicht gegenseitig. Jede Transaktion sieht die Datenbank so, als wäre sie die einzige Transaktion. Dies verhindert Race Conditions und Inkonsistenzen bei gleichzeitigen Zugriffen.

**Beispiel**: Zwei Benutzer kaufen gleichzeitig das letzte verfügbare Produkt. Ohne Isolation könnten beide die Menge als "verfügbar" sehen und bestellen. Mit Isolation stellt das DBMS sicher, dass nur eine Transaktion erfolgreich ist.

**Isolation Levels** (von schwach zu stark):
- **READ UNCOMMITTED**: Erlaubt "Dirty Reads" (Lesen von nicht-committeten Daten) – kaum verwendet
- **READ COMMITTED**: Liest nur committete Daten – Standard in vielen DBMS
- **REPEATABLE READ**: Garantiert, dass wiederholte Reads denselben Wert liefern
- **SERIALIZABLE**: Stärkste Isolation, als ob Transaktionen nacheinander ablaufen – langsamste Option

**Durability (Dauerhaftigkeit)**: Sobald eine Transaktion erfolgreich committed wurde, sind ihre Änderungen dauerhaft gespeichert. Selbst bei Systemabsturz, Stromausfall oder Hardware-Fehler bleiben die Daten erhalten.

**Implementierung**: DBMS verwenden **Write-Ahead Logging (WAL)**: Änderungen werden zunächst in ein Log geschrieben (auf Festplatte), bevor sie in die eigentlichen Datenbankdateien übernommen werden. Bei einem Crash kann das DBMS aus dem Log wiederherstellen.

> [!WARNING]
> **Transaktions-Overhead**: Transaktionen haben Performance-Kosten (Logging, Locking). Bei sehr vielen kleinen Transaktionen kann dies zum Flaschenhals werden. Gruppiere zusammenhängende Operationen in eine Transaktion, aber halte Transaktionen so kurz wie möglich.

#### Transaktionen in der Praxis

**Explizite Transaktionen**:

```sql
BEGIN TRANSACTION;  -- Startet Transaktion

UPDATE Lagerbestand SET Menge = Menge - 10 WHERE Artikel_ID = 5;
INSERT INTO Buchungen (Artikel_ID, Menge, Datum) VALUES (5, -10, '2024-12-15');

COMMIT;  -- Speichert Änderungen dauerhaft
```

Falls ein Fehler auftritt:

```sql
ROLLBACK;  -- Macht alle Änderungen seit BEGIN rückgängig
```

**Implizite Transaktionen**: Manche DBMS (z.B. SQLite im Default-Modus) wrappen jedes einzelne Statement automatisch in eine Transaktion. Dies ist sicher, aber ineffizient bei mehreren zusammenhängenden Operationen.

**Autocommit-Modus**: In vielen SQL-Clients ist Autocommit standardmäßig aktiviert – jedes Statement wird sofort committed. Für Anwendungen sollte Autocommit deaktiviert werden, um Transaktionen explizit zu kontrollieren.

> [!TIP]
> **Best Practice für Transaktionen**:
> - Beginne Transaktionen so spät wie möglich, committed sie so früh wie möglich (reduziert Locking-Konflikte)
> - Halte Transaktionen kurz (keine langen Berechnungen zwischen BEGIN und COMMIT)
> - Verwende passenden Isolation Level (nicht immer SERIALIZABLE – das ist oft zu restriktiv)
> - In Anwendungen: Verwende Connection Pooling und transaktionale ORM-Features

#### Locks und Concurrency Control

Um Isolation zu garantieren, verwenden DBMS **Locks** (Sperren). Wenn eine Transaktion eine Zeile liest oder ändert, kann sie sie für andere Transaktionen sperren.

**Lock-Typen**:

**Shared Lock (S-Lock, Read Lock)**: Mehrere Transaktionen können gleichzeitig eine Zeile lesen, aber nicht ändern. Wird bei `SELECT` gesetzt (abhängig von Isolation Level).

**Exclusive Lock (X-Lock, Write Lock)**: Nur eine Transaktion kann die Zeile ändern. Wird bei `UPDATE`, `DELETE`, `INSERT` gesetzt. Blockiert andere Lese- und Schreiboperationen.

**Deadlocks**: Zwei Transaktionen warten gegenseitig aufeinander. Beispiel: Transaktion A sperrt Zeile 1 und wartet auf Zeile 2, Transaktion B sperrt Zeile 2 und wartet auf Zeile 1. Das DBMS erkennt Deadlocks und bricht eine Transaktion ab (mit Fehlermeldung).

> [!WARNING]
> **Deadlock-Vermeidung**:
> - Greife immer in derselben Reihenfolge auf Ressourcen zu (z.B. sortiert nach Primärschlüssel)
> - Halte Transaktionen kurz
> - Verwende optimistische Locking statt pessimistische Locks (wenn möglich)

**Optimistisches vs. Pessimistisches Locking**:

**Pessimistisches Locking**: Transaktion sperrt Zeile sofort beim Lesen (`SELECT ... FOR UPDATE`). Andere Transaktionen müssen warten. Sicher, aber langsam bei hohem Parallelitätsgrad.

**Optimistisches Locking**: Transaktion liest Zeile ohne Lock. Beim Update prüft sie, ob die Zeile sich zwischenzeitlich geändert hat (z.B. via Version-Spalte). Falls ja, schlägt Update fehl, und Anwendung muss Konflikt auflösen. Schneller bei geringen Konflikten.

### NoSQL-Datenbanken: Wann und warum?

**NoSQL** (Not Only SQL) ist eine Sammelbezeichnung für Datenbanksysteme, die das relationale Modell aufgeben zugunsten anderer Datenstrukturen. NoSQL-Datenbanken entstanden ab 2000, um Skalierbarkeits- und Flexibilitätsprobleme relationaler Datenbanken bei sehr großen Datenmengen (Big Data) zu lösen.

> [!NOTE]
> **NoSQL** bedeutet **nicht** "kein SQL" (viele NoSQL-Datenbanken bieten SQL-ähnliche Abfragesprachen), sondern "Not Only SQL" – also Datenbanken, die alternative Modelle verwenden.

#### Warum NoSQL?

Relationale Datenbanken haben Grenzen:

**Horizontale Skalierung**: Relationale DBMS sind für vertikale Skalierung optimiert (größerer Server). Horizontale Skalierung (viele Server) ist schwierig wegen ACID-Garantien und JOINs über mehrere Server.

**Schema-Flexibilität**: Relationale Datenbanken erfordern ein festes Schema. Änderungen am Schema (z.B. neue Spalte) können bei großen Tabellen Stunden dauern und Downtime verursachen.

**Komplexe Datenstrukturen**: Hierarchische oder graphartige Daten (z.B. soziale Netzwerke, verschachtelte JSON-Dokumente) sind in relationalen Tabellen umständlich zu modellieren.

**Performance bei spezifischen Workloads**: Bestimmte Zugriffspatterns (z.B. Key-Value-Lookups, Graph-Traversierung) sind in spezialisierten NoSQL-Datenbanken schneller.

> [!WARNING]
> **NoSQL ist kein Allheilmittel**: Viele Probleme, die angeblich NoSQL erfordern, sind in Wirklichkeit schlechtes Design oder fehlende Indizes in relationalen Datenbanken. Verwende NoSQL nur, wenn du **nachweislich** an Grenzen relationaler Systeme stößt.

#### NoSQL-Kategorien

**Key-Value-Stores** (Beispiel: Redis, DynamoDB):
- Einfachstes Modell: Speichert Werte unter Schlüsseln (wie ein riesiges Dictionary)
- Sehr schnell für Lookups (O(1))
- Keine Queries, nur direkter Zugriff per Key
- Verwendung: Caching, Session-Storage, Counters, Echtzeit-Leaderboards

**Document Stores** (Beispiel: MongoDB, CouchDB):
- Speichert semi-strukturierte Dokumente (JSON, BSON, XML)
- Flexibles Schema: Jedes Dokument kann unterschiedliche Felder haben
- Unterstützt verschachtelte Strukturen
- Query-Fähigkeiten (ähnlich SQL, aber für JSON)
- Verwendung: Content Management, Kataloge, User Profiles, Event Logs

**Column-Family Stores** (Beispiel: Apache Cassandra, HBase):
- Speichert Daten spaltenweise statt zeilenweise
- Optimiert für Schreib-intensive Workloads und große Datenmengen
- Horizontal skalierbar (Petabyte-Scale)
- Verwendung: Zeitreihen-Daten, IoT-Sensor-Daten, Logs

**Graph Databases** (Beispiel: Neo4j, Amazon Neptune):
- Speichert Knoten (Entities) und Kanten (Beziehungen)
- Optimiert für Traversierung von Beziehungen
- Query-Sprachen für Graph-Patterns (z.B. Cypher)
- Verwendung: Soziale Netzwerke, Empfehlungssysteme, Fraud Detection, Wissensgraphen

> [!TIP]
> **NoSQL-Auswahl**:
> - **Redis**: Wenn du ein in-Memory-Cache oder Pub/Sub brauchst
> - **MongoDB**: Wenn du flexible Schemas und JSON-artige Dokumente hast
> - **Cassandra**: Wenn du extrem hohe Schreibraten und lineare Skalierung brauchst
> - **Neo4j**: Wenn dein Datenmodell primär aus Beziehungen besteht (z.B. Freundschaften, Abhängigkeiten)

#### MongoDB Beispiel

MongoDB ist eine der populärsten Document Stores. Daten werden als JSON-ähnliche Dokumente (BSON) gespeichert.

**Beispiel-Dokument** (Maschinen-Datenbank):

```json
{
  "_id": ObjectId("507f1f77bcf86cd799439011"),
  "Maschinentyp": "CNC-Fräse DMU 50",
  "Baujahr": 2018,
  "Standort": "Halle A1",
  "Wartungsintervall_Tage": 90,
  "Letzte_Wartung": ISODate("2024-01-15"),
  "Sensoren": [
    {"Typ": "Temperatur", "Einheit": "Celsius", "Grenzwert": 80},
    {"Typ": "Vibration", "Einheit": "mm/s", "Grenzwert": 5.0}
  ],
  "Status": "aktiv"
}
```

Vorteile gegenüber relationaler DB:
- Verschachtelte Arrays (`Sensoren`) direkt speicherbar (keine separate Tabelle)
- Schema kann pro Dokument variieren (manche Maschinen haben andere Sensoren)
- Kein JOIN nötig, um alle Maschineninformationen zu laden

**Query in MongoDB**:

```javascript
db.maschinen.find({ "Baujahr": { "$gt": 2015 }, "Status": "aktiv" })
```

Findet alle aktiven Maschinen mit Baujahr > 2015.

#### CAP-Theorem

Das **CAP-Theorem** (Eric Brewer, 2000) besagt, dass ein verteiltes Datenbanksystem **maximal zwei** der folgenden drei Eigenschaften gleichzeitig garantieren kann:

**Consistency (Konsistenz)**: Alle Knoten sehen dieselben Daten zur selben Zeit. Nach einem Write sehen alle Reads den neuen Wert.

**Availability (Verfügbarkeit)**: Jede Anfrage erhält eine Antwort (erfolgreich oder Fehler), auch wenn Knoten ausfallen.

**Partition Tolerance (Partitionstoleranz)**: System funktioniert auch bei Netzwerkausfällen zwischen Knoten (Kommunikation unterbrochen).

Da Netzwerkpartitionen in verteilten Systemen unvermeidbar sind, muss zwischen **CP** (Consistency + Partition Tolerance) und **AP** (Availability + Partition Tolerance) gewählt werden.

**CP-Systeme** (z.B. HBase, MongoDB im Strong Consistency Mode): Bei Netzwerkpartition werden Writes abgelehnt, um Konsistenz zu garantieren. Manche Knoten sind dann nicht verfügbar.

**AP-Systeme** (z.B. Cassandra, DynamoDB): Bei Netzwerkpartition bleiben alle Knoten verfügbar, aber Daten können temporär inkonsistent sein (Eventual Consistency).

> [!WARNING]
> **Eventual Consistency**: In AP-Systemen können nach einem Write kurzzeitig unterschiedliche Werte auf verschiedenen Knoten existieren. Nach einiger Zeit (Millisekunden bis Sekunden) konvergieren sie. Für kritische Anwendungen (Banking, Bestandsverwaltung) ist dies oft inakzeptabel.

### KI und Datenbanken: Vector Databases für Embeddings

Mit dem Aufstieg von Machine Learning und Large Language Models (LLMs) entstanden spezielle Datenbanken für **Vektor-Embeddings**. Ein **Embedding** ist eine numerische Repräsentation von Daten (Text, Bilder, Audio) als Vektor in hochdimensionalem Raum (z.B. 1536 Dimensionen bei OpenAI's `text-embedding-3-small`).

> [!NOTE]
> Ein **Vector Embedding** ist ein Vektor von Fließkommazahlen, der semantische Bedeutung kodiert. Ähnliche Konzepte haben ähnliche Vektoren (gemessen via Cosinus-Ähnlichkeit oder Euklidischer Distanz).

#### Warum Vector Databases?

Traditionelle Datenbanken sind ineffizient für **Similarity Search** (Ähnlichkeitssuche) in hochdimensionalen Räumen. Eine Abfrage wie "Finde die 10 ähnlichsten Dokumente zu diesem Text" würde in einer relationalen DB Millionen Vektoren durchrechnen müssen.

**Vector Databases** (z.B. Pinecone, Weaviate, Milvus, Chroma) sind für diese Workload optimiert:

**Approximate Nearest Neighbor (ANN)**: Statt exakte nächste Nachbarn zu finden (langsam), verwenden sie Algorithmen wie HNSW (Hierarchical Navigable Small World) oder IVF (Inverted File Index), um schnell approximative Ergebnisse zu liefern.

**Skalierung**: Können Milliarden von Vektoren handhaben und horizontal skalieren.

**Integration mit ML-Pipelines**: Bieten APIs für Embedding-Generierung und speichern Metadaten zusammen mit Vektoren.

#### Anwendungsfälle

**Semantische Suche**: Suche nach "Wartungsanleitung für Hydrauliksysteme" findet Dokumente, die das Wort "Hydraulik" nicht enthalten, aber semantisch verwandt sind (z.B. "Drucksysteme in Pressen").

**Retrieval-Augmented Generation (RAG)**: LLMs werden mit kontextrelevanten Dokumenten aus Vector Database gefüttert, um halluzinationsarme Antworten zu generieren.

**Empfehlungssysteme**: Produkt-Embeddings basierend auf Beschreibungen; finde ähnliche Produkte.

**Duplikat-Erkennung**: Finde ähnliche Datensätze (z.B. doppelte Kundeneinträge, ähnliche Support-Tickets).

**Bilderkennung**: Speichere Bild-Embeddings und finde visuell ähnliche Bilder.

> [!TIP]
> **Vector Database Workflow**:
> 1. Generiere Embeddings mit einem Modell (z.B. OpenAI API, Sentence Transformers)
> 2. Speichere Embeddings + Metadaten in Vector DB
> 3. Bei Query: Generiere Query-Embedding, suche nächste Nachbarn
> 4. Gebe Metadaten der gefundenen Vektoren zurück (z.B. Dokument-IDs, Texte)

**Beispiel: Dokumentensuche mit Embeddings**

```python
import openai
import pinecone  # Vector Database

# 1. Dokumente embedden
dokumente = [
    "Wartungsanleitung für CNC-Fräsen",
    "Sicherheitsvorschriften für Drehmaschinen",
    "Hydrauliksystem-Handbuch"
]

embeddings = [openai.Embedding.create(input=doc, model="text-embedding-3-small")['data'][0]['embedding'] 
              for doc in dokumente]

# 2. In Vector DB speichern
pinecone.init(api_key="...")
index = pinecone.Index("maschinenbau-docs")
index.upsert(vectors=[(f"doc_{i}", emb, {"text": doc}) 
                       for i, (emb, doc) in enumerate(zip(embeddings, dokumente))])

# 3. Suche
query = "Wie warte ich eine Fräsmaschine?"
query_emb = openai.Embedding.create(input=query, model="text-embedding-3-small")['data'][0]['embedding']
results = index.query(vector=query_emb, top_k=2, include_metadata=True)

# 4. Ergebnisse
for match in results['matches']:
    print(f"Score: {match['score']:.3f} | Text: {match['metadata']['text']}")
```

Output:
```
Score: 0.912 | Text: Wartungsanleitung für CNC-Fräsen
Score: 0.734 | Text: Sicherheitsvorschriften für Drehmaschinen
```

Die semantische Ähnlichkeit zwischen "Fräsmaschine warten" und "Wartungsanleitung für CNC-Fräsen" wird erkannt, obwohl die Wörter unterschiedlich sind.

#### Hybrid-Ansätze

Viele produktive Systeme kombinieren relationale Datenbanken mit Vector Databases:

**PostgreSQL + pgvector**: PostgreSQL-Extension für Vektor-Ähnlichkeitssuche. Gut für kleine bis mittlere Datenmengen (<1 Million Vektoren).

**Elasticsearch + Dense Vectors**: Elasticsearch bietet seit Version 7.x Vector-Suche. Kombiniert Volltext-Suche mit semantischer Suche.

**Weaviate**: Vector Database mit eingebautem Objekt-Schema (wie relationale Tabellen). Unterstützt Hybrid Search (Keyword + Vektor).

> [!WARNING]
> **Vector Databases sind teuer**: Speicherung und Indexierung hochdimensionaler Vektoren benötigt viel RAM. Eine Million 1536-dimensionale Vektoren (Float32) = ~6 GB reiner Daten + Index-Overhead. Cloud-Kosten können schnell steigen.

---

## 🐍 Python-Praxis: Datenbankverbindung & SQL – Teil 2

In Vorlesung 19 wurden die Grundlagen von SQLite und SQL eingeführt: Verbindung zu Datenbanken herstellen, Tabellen erstellen, Daten einfügen und einfache Abfragen durchführen. In dieser Vorlesung vertiefen wir diese Kenntnisse und behandeln Sicherheitsaspekte, Transaktionen, fortgeschrittene Query-Techniken und Best Practices für professionelle Datenbankprogrammierung.

### Prepared Statements gegen SQL-Injection

**SQL-Injection** ist eine der gefährlichsten Sicherheitslücken in Webanwendungen. Sie entsteht, wenn Benutzereingaben unsicher in SQL-Queries eingefügt werden. Ein Angreifer kann dadurch beliebige SQL-Befehle ausführen, Daten lesen, ändern oder löschen.

> [!WARNING]
> **SQL-Injection Beispiel** (NIEMALS SO PROGRAMMIEREN!):
> 
> ```python
> # UNSICHER – SQL-Injection möglich!
> maschinen_id = input("Maschinen-ID: ")
> cursor.execute(f"SELECT * FROM Maschinen WHERE Maschinen_ID = {maschinen_id}")
> ```
> 
> Eingabe: `1 OR 1=1` führt zu:
> ```sql
> SELECT * FROM Maschinen WHERE Maschinen_ID = 1 OR 1=1
> ```
> Dies gibt **alle** Maschinen zurück, nicht nur ID 1!
> 
> Schlimmerer Fall – Eingabe: `1; DROP TABLE Maschinen; --`
> ```sql
> SELECT * FROM Maschinen WHERE Maschinen_ID = 1; DROP TABLE Maschinen; --
> ```
> Dies löscht die gesamte Tabelle!

**Prepared Statements** (auch Parameterized Queries) sind die Lösung. Der SQL-Code wird vom DBMS vorkompiliert, Parameter werden separat übergeben und können nicht als Code interpretiert werden.

In Python mit `sqlite3` verwenden wir **`?` Platzhalter**:

```python
import sqlite3

conn = sqlite3.connect('produktionsdb.db')
cursor = conn.cursor()

# SICHER – Prepared Statement
maschinen_id = input("Maschinen-ID: ")
cursor.execute('SELECT * FROM Maschinen WHERE Maschinen_ID = ?', (maschinen_id,))
zeilen = cursor.fetchall()
```

Selbst wenn der Benutzer `1 OR 1=1` eingibt, wird dies als String `"1 OR 1=1"` interpretiert, nicht als SQL-Code. Die Abfrage findet keine Maschine mit dieser ID.

> [!NOTE]
> **Wichtig**: Der zweite Parameter von `.execute()` muss ein **Tupel** sein, auch bei nur einem Parameter: `(wert,)` mit Komma! `(wert)` ohne Komma ist kein Tupel, sondern nur eine geklammerte Expression.

**Beispiel mit mehreren Parametern**:

```python
# Maschine einfügen
cursor.execute('''
    INSERT INTO Maschinen (Name, Typ, Baujahr, Standort) 
    VALUES (?, ?, ?, ?)
''', ('CNC-Fräse DMU 50', 'Fräse', 2020, 'Halle A1'))
conn.commit()
```

**Named Placeholders** (Alternative Syntax mit Dictionaries):

```python
cursor.execute('''
    SELECT * FROM Maschinen 
    WHERE Typ = :typ AND Baujahr > :jahr
''', {'typ': 'Fräse', 'jahr': 2015})
```

Named Placeholders sind lesbarer bei vielen Parametern, aber `?` Platzhalter sind schneller und der Standard.

> [!TIP]
> **Best Practice**: Verwende **IMMER** Prepared Statements für Benutzereingaben. Niemals String-Formatierung (`f"..."`, `.format()`, `%`) für SQL verwenden!

### UPDATE und DELETE Operationen

Neben `INSERT` und `SELECT` (aus V19) sind `UPDATE` (Ändern) und `DELETE` (Löschen) essenzielle Operationen.

#### UPDATE: Daten ändern

**Syntax**:
```sql
UPDATE Tabelle SET Spalte1 = Wert1, Spalte2 = Wert2 WHERE Bedingung
```

**Beispiel**: Maschine auf "inaktiv" setzen:

```python
maschinen_id = 5
cursor.execute('UPDATE Maschinen SET Aktiv = 0 WHERE Maschinen_ID = ?', (maschinen_id,))
conn.commit()
print(f"{cursor.rowcount} Zeile(n) aktualisiert")
```

`cursor.rowcount` gibt die Anzahl betroffener Zeilen zurück.

**Beispiel**: Wartungsintervall für alle Fräsen verlängern:

```python
cursor.execute('''
    UPDATE Maschinen 
    SET Wartungsintervall_Tage = Wartungsintervall_Tage + 30 
    WHERE Typ = ?
''', ('Fräse',))
conn.commit()
print(f"{cursor.rowcount} Maschine(n) aktualisiert")
```

> [!WARNING]
> **Vorsicht ohne WHERE-Klausel**: `UPDATE Maschinen SET Aktiv = 0` (ohne WHERE) ändert **alle** Zeilen! Immer WHERE-Bedingung verwenden, außer du willst wirklich alle Zeilen ändern.

**Bedingte Updates basierend auf aktuellen Werten**:

```python
# Erhöhe Wartungskosten um 10% für Maschinen älter als 10 Jahre
cursor.execute('''
    UPDATE Wartungsprotokolle 
    SET Kosten_Euro = Kosten_Euro * 1.10 
    WHERE Maschinen_ID IN (
        SELECT Maschinen_ID FROM Maschinen 
        WHERE Baujahr < ?
    )
''', (2014,))  # 2024 - 10 = 2014
conn.commit()
```

#### DELETE: Daten löschen

**Syntax**:
```sql
DELETE FROM Tabelle WHERE Bedingung
```

**Beispiel**: Wartungsprotokoll löschen:

```python
protokoll_id = 10
cursor.execute('DELETE FROM Wartungsprotokolle WHERE Protokoll_ID = ?', (protokoll_id,))
conn.commit()
print(f"{cursor.rowcount} Zeile(n) gelöscht")
```

**Beispiel**: Alle inaktiven Maschinen löschen:

```python
cursor.execute('DELETE FROM Maschinen WHERE Aktiv = 0')
conn.commit()
print(f"{cursor.rowcount} Maschine(n) gelöscht")
```

> [!WARNING]
> **CASCADE DELETE**: Wenn Fremdschlüssel-Constraints existieren, kann das Löschen eines Datensatzes fehlschlagen, wenn abhängige Datensätze in anderen Tabellen existieren. Lösung: Entweder erst abhängige Datensätze löschen oder `ON DELETE CASCADE` im Schema definieren.

**Foreign Key Constraints in SQLite** (müssen explizit aktiviert werden):

```python
cursor.execute('PRAGMA foreign_keys = ON')
```

Ohne dies werden Fremdschlüssel-Constraints in SQLite ignoriert!

**Beispiel mit CASCADE**:

```sql
CREATE TABLE Wartungsprotokolle (
    Protokoll_ID INTEGER PRIMARY KEY,
    Maschinen_ID INTEGER,
    Wartungsdatum TEXT,
    FOREIGN KEY (Maschinen_ID) REFERENCES Maschinen(Maschinen_ID) 
        ON DELETE CASCADE
);
```

Jetzt werden beim Löschen einer Maschine automatisch alle zugehörigen Wartungsprotokolle gelöscht.

### Transaktionen: Commit und Rollback

Wie in der Theorie besprochen, sind **Transaktionen** fundamental für Datenintegrität. In Python mit `sqlite3` funktionieren Transaktionen folgendermaßen:

**Explizite Transaktionen**:

```python
conn = sqlite3.connect('produktionsdb.db')
cursor = conn.cursor()

try:
    # Transaktion beginnt implizit beim ersten modifizierenden Statement
    cursor.execute('UPDATE Lagerbestand SET Menge = Menge - 10 WHERE Artikel_ID = ?', (5,))
    cursor.execute('INSERT INTO Buchungen (Artikel_ID, Menge, Datum) VALUES (?, ?, ?)', 
                   (5, -10, '2024-12-15'))
    
    # Beide Operationen erfolgreich → Speichern
    conn.commit()
    print("Transaktion erfolgreich committed")

except sqlite3.Error as e:
    # Bei Fehler: Rückgängig machen
    conn.rollback()
    print(f"Fehler: {e}. Transaktion wurde zurückgerollt.")

finally:
    conn.close()
```

**Wichtig**: In SQLite beginnt eine Transaktion automatisch beim ersten `INSERT`, `UPDATE` oder `DELETE`. Sie wird mit `.commit()` gespeichert oder mit `.rollback()` rückgängig gemacht.

> [!NOTE]
> **Isolation Level** in SQLite: SQLite unterstützt nur `DEFERRED`, `IMMEDIATE` und `EXCLUSIVE` Transaktionen. Der Standard ist `DEFERRED` (Locks werden erst bei erstem Write gesetzt). Für meiste Anwendungen ist dies ausreichend.

**Beispiel: Banküberweisungs-Simulation**:

```python
def ueberweise(von_konto, nach_konto, betrag):
    try:
        cursor.execute('UPDATE Konten SET Saldo = Saldo - ? WHERE Konto_ID = ?', 
                       (betrag, von_konto))
        
        if cursor.rowcount == 0:
            raise ValueError("Quellkonto existiert nicht")
        
        cursor.execute('SELECT Saldo FROM Konten WHERE Konto_ID = ?', (von_konto,))
        neuer_saldo = cursor.fetchone()[0]
        
        if neuer_saldo < 0:
            raise ValueError("Unzureichende Deckung")
        
        cursor.execute('UPDATE Konten SET Saldo = Saldo + ? WHERE Konto_ID = ?', 
                       (betrag, nach_konto))
        
        if cursor.rowcount == 0:
            raise ValueError("Zielkonto existiert nicht")
        
        conn.commit()
        print(f"{betrag} Euro von Konto {von_konto} nach {nach_konto} überwiesen")
    
    except (sqlite3.Error, ValueError) as e:
        conn.rollback()
        print(f"Überweisung fehlgeschlagen: {e}")

# Verwendung
ueberweise(1, 2, 100.0)
```

Falls einer der Schritte fehlschlägt (z.B. Zielkonto existiert nicht), wird das Geld nicht abgebucht – Atomarität ist garantiert.

### Cursor-Objekte und fetchall() / fetchone()

Aus V19 wissen wir bereits, dass `.execute()` ein Cursor-Objekt zurückgibt und `.fetchall()` alle Ergebnisse als Liste liefert. Hier vertiefen wir die Cursor-Funktionalität.

**Cursor-Methoden im Detail**:

**`.fetchone()`**: Gibt die nächste Zeile als Tupel zurück oder `None` bei Ende:

```python
cursor.execute('SELECT * FROM Maschinen WHERE Aktiv = 1')

zeile = cursor.fetchone()
while zeile:
    print(zeile)
    zeile = cursor.fetchone()
```

**`.fetchall()`**: Gibt alle verbleibenden Zeilen als Liste zurück:

```python
cursor.execute('SELECT Name, Baujahr FROM Maschinen')
zeilen = cursor.fetchall()

for name, baujahr in zeilen:
    print(f"{name} ({baujahr})")
```

**`.fetchmany(size)`**: Gibt bis zu `size` Zeilen zurück (nützlich für große Ergebnisse):

```python
cursor.execute('SELECT * FROM Messdaten')

while True:
    zeilen = cursor.fetchmany(1000)  # Blockweise 1000 Zeilen
    if not zeilen:
        break
    
    for zeile in zeilen:
        verarbeite(zeile)
```

Dies ist speichereffizienter als `.fetchall()` bei Millionen Zeilen.

**Cursor als Iterator**:

```python
cursor.execute('SELECT * FROM Maschinen')

for zeile in cursor:
    print(zeile)
```

Dies ist äquivalent zu wiederholtem `.fetchone()`, aber pythonischer.

**`.rowcount`**: Anzahl betroffener Zeilen bei `UPDATE`/`DELETE` oder `-1` bei `SELECT` (in SQLite):

```python
cursor.execute('DELETE FROM Maschinen WHERE Aktiv = 0')
print(f"{cursor.rowcount} Zeilen gelöscht")
```

**`.description`**: Metadaten über Spalten (Name, Typ, etc.):

```python
cursor.execute('SELECT Name, Baujahr FROM Maschinen')
print(cursor.description)
# Ausgabe: (('Name', None, None, None, None, None, None), ('Baujahr', None, None, None, None, None, None))

spalten = [desc[0] for desc in cursor.description]
print(spalten)  # ['Name', 'Baujahr']
```

**Zugriff nach Spaltennamen mit `row_factory`** (aus V19 bekannt, hier vertieft):

```python
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute('SELECT Name, Baujahr FROM Maschinen WHERE Maschinen_ID = ?', (1,))
zeile = cursor.fetchone()

if zeile:
    print(zeile['Name'])    # Zugriff nach Name
    print(zeile[0])         # Zugriff nach Index (auch möglich)
    print(dict(zeile))      # Als Dictionary ausgeben
```

`sqlite3.Row` verhält sich wie ein Tupel, unterstützt aber auch Dictionary-ähnlichen Zugriff. Dies macht Code lesbarer bei vielen Spalten.

### Context Manager für sichere Verbindungen

**Context Manager** (`with`-Statement) garantieren, dass Ressourcen korrekt freigegeben werden, auch wenn Fehler auftreten. Dies ist Best Practice für Datenbankverbindungen.

**Ohne Context Manager** (fehleranfällig):

```python
conn = sqlite3.connect('daten.db')
cursor = conn.cursor()
cursor.execute('INSERT INTO Tabelle VALUES (?)', (wert,))
conn.commit()
conn.close()  # Wird bei Exception NICHT ausgeführt!
```

**Mit Context Manager** (sicher):

```python
with sqlite3.connect('daten.db') as conn:
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Tabelle VALUES (?)', (wert,))
    conn.commit()
# conn.close() wird automatisch aufgerufen
```

> [!WARNING]
> **Wichtig**: Der Context Manager für `sqlite3.connect()` ruft bei Verlassen des Blocks **nicht** `.close()` auf, sondern nur `.commit()` (bei Erfolg) oder `.rollback()` (bei Exception). Für vollständiges Cleanup manuell `.close()` in `finally` oder zweiten Context Manager verwenden.

**Empfohlenes Pattern**:

```python
try:
    with sqlite3.connect('daten.db') as conn:
        cursor = conn.cursor()
        
        # Datenbank-Operationen
        cursor.execute('INSERT INTO Maschinen (Name, Typ) VALUES (?, ?)', ('CNC-07', 'Fräse'))
        # Kein manuelles conn.commit() nötig – passiert automatisch
        
except sqlite3.IntegrityError as e:
    print(f"Constraint-Verletzung: {e}")
except sqlite3.Error as e:
    print(f"Datenbankfehler: {e}")
finally:
    if 'conn' in locals():
        conn.close()
```

**Noch besser: Eigene Context Manager-Klasse**:

```python
class DatenbankVerbindung:
    def __init__(self, db_pfad):
        self.db_pfad = db_pfad
        self.conn = None
    
    def __enter__(self):
        self.conn = sqlite3.connect(self.db_pfad)
        self.conn.row_factory = sqlite3.Row
        return self.conn
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.conn.close()

# Verwendung
with DatenbankVerbindung('daten.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Maschinen')
    for zeile in cursor:
        print(dict(zeile))
```

Dies garantiert immer Commit bei Erfolg, Rollback bei Exception und Close am Ende.

### Aggregationen und GROUP BY in Python

Aggregat-Funktionen (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) und `GROUP BY` wurden in V19 theoretisch eingeführt. Hier zeigen wir praktische Anwendung in Python.

**Beispiel: Statistiken über Wartungen**:

```python
# Anzahl Wartungen pro Maschine
cursor.execute('''
    SELECT m.Name, COUNT(w.Protokoll_ID) AS Anzahl_Wartungen
    FROM Maschinen m
    LEFT JOIN Wartungsprotokolle w ON m.Maschinen_ID = w.Maschinen_ID
    GROUP BY m.Maschinen_ID, m.Name
    ORDER BY Anzahl_Wartungen DESC
''')

for zeile in cursor.fetchall():
    print(f"{zeile[0]}: {zeile[1]} Wartungen")
```

**Beispiel: Durchschnittliche Kosten pro Maschinentyp**:

```python
cursor.execute('''
    SELECT m.Typ, 
           COUNT(w.Protokoll_ID) AS Anzahl,
           AVG(w.Kosten_Euro) AS Durchschnitt_Kosten,
           SUM(w.Kosten_Euro) AS Gesamt_Kosten
    FROM Maschinen m
    INNER JOIN Wartungsprotokolle w ON m.Maschinen_ID = w.Maschinen_ID
    GROUP BY m.Typ
    HAVING COUNT(w.Protokoll_ID) > 5
    ORDER BY Gesamt_Kosten DESC
''')

conn.row_factory = sqlite3.Row
for zeile in cursor.fetchall():
    print(f"{zeile['Typ']}: "
          f"{zeile['Anzahl']} Wartungen, "
          f"Ø {zeile['Durchschnitt_Kosten']:.2f} €, "
          f"Gesamt {zeile['Gesamt_Kosten']:.2f} €")
```

**HAVING-Klausel**: Filtert Gruppen nach Aggregation. `WHERE` filtert vor Gruppierung, `HAVING` danach.

```python
# Maschinen mit mehr als 3 Wartungen im letzten Jahr
cursor.execute('''
    SELECT m.Name, COUNT(w.Protokoll_ID) AS Anzahl
    FROM Maschinen m
    INNER JOIN Wartungsprotokolle w ON m.Maschinen_ID = w.Maschinen_ID
    WHERE w.Wartungsdatum >= date('now', '-1 year')
    GROUP BY m.Maschinen_ID, m.Name
    HAVING COUNT(w.Protokoll_ID) > 3
''')
```

> [!TIP]
> **Performance-Tipp**: Bei großen Tabellen können Aggregationen langsam sein. Erstelle Indizes auf Spalten in GROUP BY und JOIN-Bedingungen.

### JOINs: Daten aus mehreren Tabellen verknüpfen

**INNER JOIN**: Nur Zeilen mit Übereinstimmung in beiden Tabellen:

```python
cursor.execute('''
    SELECT m.Name AS Maschine, 
           w.Wartungsdatum, 
           w.Wartungstyp, 
           w.Kosten_Euro
    FROM Maschinen m
    INNER JOIN Wartungsprotokolle w ON m.Maschinen_ID = w.Maschinen_ID
    WHERE m.Typ = ?
    ORDER BY w.Wartungsdatum DESC
''', ('Fräse',))

for zeile in cursor.fetchall():
    print(f"{zeile[0]} | {zeile[1]} | {zeile[2]} | {zeile[3]} €")
```

**LEFT JOIN**: Alle Zeilen aus linker Tabelle + Übereinstimmungen aus rechter:

```python
# Alle Maschinen + ihre Wartungen (auch wenn keine Wartungen vorhanden)
cursor.execute('''
    SELECT m.Name, 
           COUNT(w.Protokoll_ID) AS Anzahl_Wartungen
    FROM Maschinen m
    LEFT JOIN Wartungsprotokolle w ON m.Maschinen_ID = w.Maschinen_ID
    GROUP BY m.Maschinen_ID, m.Name
''')

for zeile in cursor.fetchall():
    anzahl = zeile[1] if zeile[1] else 0
    print(f"{zeile[0]}: {anzahl} Wartungen")
```

Maschinen ohne Wartungen haben `COUNT = 0` (wegen LEFT JOIN). Bei INNER JOIN würden sie nicht auftauchen.

**Mehrere JOINs**:

```python
# Maschinen + Wartungen + zuständige Techniker
cursor.execute('''
    SELECT m.Name AS Maschine,
           w.Wartungsdatum,
           t.Name AS Techniker,
           w.Kosten_Euro
    FROM Maschinen m
    INNER JOIN Wartungsprotokolle w ON m.Maschinen_ID = w.Maschinen_ID
    INNER JOIN Techniker t ON w.Techniker_ID = t.Techniker_ID
    ORDER BY w.Wartungsdatum DESC
    LIMIT 10
''')
```

> [!WARNING]
> **JOIN-Performance**: Ohne Indizes auf Fremdschlüsseln können JOINs extrem langsam werden. Stelle sicher, dass Fremdschlüssel-Spalten indexiert sind:
> 
> ```python
> cursor.execute('CREATE INDEX idx_wartung_maschinen_id ON Wartungsprotokolle(Maschinen_ID)')
> ```

### Subqueries (Unterabfragen)

**Subquery in WHERE**:

```python
# Maschinen, deren Wartungskosten über dem Durchschnitt liegen
cursor.execute('''
    SELECT m.Name, SUM(w.Kosten_Euro) AS Gesamt_Kosten
    FROM Maschinen m
    INNER JOIN Wartungsprotokolle w ON m.Maschinen_ID = w.Maschinen_ID
    GROUP BY m.Maschinen_ID, m.Name
    HAVING SUM(w.Kosten_Euro) > (
        SELECT AVG(Gesamt) FROM (
            SELECT SUM(Kosten_Euro) AS Gesamt
            FROM Wartungsprotokolle
            GROUP BY Maschinen_ID
        )
    )
''')
```

**Subquery mit IN**:

```python
# Wartungen für Maschinen eines bestimmten Typs
cursor.execute('''
    SELECT Wartungsdatum, Wartungstyp, Kosten_Euro
    FROM Wartungsprotokolle
    WHERE Maschinen_ID IN (
        SELECT Maschinen_ID FROM Maschinen WHERE Typ = ?
    )
''', ('Fräse',))
```

Subqueries können JOINs ersetzen, sind aber meist langsamer. Verwende JOINs, wenn möglich.

### Best Practices und häufige Fehler

**1. Immer Prepared Statements verwenden**

```python
# FALSCH (SQL-Injection!):
name = input("Name: ")
cursor.execute(f"SELECT * FROM Maschinen WHERE Name = '{name}'")

# RICHTIG:
cursor.execute('SELECT * FROM Maschinen WHERE Name = ?', (name,))
```

**2. Transaktionen für zusammenhängende Operationen**

```python
# Mehrere Operationen in einer Transaktion
try:
    cursor.execute('INSERT INTO Maschinen (...) VALUES (...)', (...))
    cursor.execute('INSERT INTO Wartungsprotokolle (...) VALUES (...)', (...))
    conn.commit()  # Beide zusammen speichern
except sqlite3.Error:
    conn.rollback()  # Beide zurückrollen
```

**3. Ressourcen freigeben**

```python
# Immer schließen
conn.close()

# Oder Context Manager verwenden
with sqlite3.connect('daten.db') as conn:
    # ... Operationen ...
    pass  # Automatisches Cleanup
```

**4. Indizes für Performance**

```python
# Erstelle Indizes auf häufig gefilterte Spalten
cursor.execute('CREATE INDEX idx_typ ON Maschinen(Typ)')
cursor.execute('CREATE INDEX idx_wartung_datum ON Wartungsprotokolle(Wartungsdatum)')
```

**5. Error Handling**

```python
try:
    cursor.execute('INSERT INTO Maschinen (Maschinen_ID, Name) VALUES (?, ?)', (1, 'Test'))
    conn.commit()
except sqlite3.IntegrityError as e:
    print(f"Constraint-Verletzung: {e}")  # z.B. Duplikat-ID
except sqlite3.OperationalError as e:
    print(f"SQL-Fehler: {e}")  # z.B. Tabelle existiert nicht
except sqlite3.Error as e:
    print(f"Allgemeiner Datenbankfehler: {e}")
```

**6. Foreign Key Constraints aktivieren (SQLite-spezifisch)**

```python
conn = sqlite3.connect('daten.db')
cursor = conn.cursor()
cursor.execute('PRAGMA foreign_keys = ON')  # Standardmäßig OFF in SQLite!
```

Ohne dies werden Fremdschlüssel-Verletzungen nicht erkannt.

**7. Batch-Inserts mit executemany()**

```python
# LANGSAM (einzelne Transaktionen):
for daten in datenliste:
    cursor.execute('INSERT INTO Tabelle VALUES (?)', (daten,))
    conn.commit()

# SCHNELL (eine Transaktion):
cursor.executemany('INSERT INTO Tabelle VALUES (?)', [(d,) for d in datenliste])
conn.commit()
```

`executemany()` ist 10-100x schneller bei vielen Inserts.

**8. row_factory für Lesbarkeit**

```python
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute('SELECT Name, Baujahr FROM Maschinen')
for zeile in cursor:
    print(zeile['Name'], zeile['Baujahr'])  # Lesbar!
```

**9. LIMIT für große Ergebnisse**

```python
# Vermeide Speicher-Overflow bei Millionen Zeilen
cursor.execute('SELECT * FROM Messdaten LIMIT 1000')
```

Oder verwende `.fetchmany(size)` für Streaming.

**10. Backup vor kritischen Operationen**

```python
import shutil
shutil.copy('produktionsdb.db', 'produktionsdb_backup.db')

# Kritische Operation
cursor.execute('DELETE FROM ...')
conn.commit()
```

> [!TIP]
> **Debugging-Tipp**: Gib SQL-Queries mit Parametern aus, bevor du sie ausführst:
> 
> ```python
> query = 'SELECT * FROM Maschinen WHERE Typ = ?'
> params = ('Fräse',)
> print(f"Query: {query} | Params: {params}")
> cursor.execute(query, params)
> ```

### Praktische Übung: Datenbank für KI-Training-Logs

Wir erstellen eine Datenbank zur Verwaltung von Trainings-Logs für Machine-Learning-Modelle. Dies ist ein realistisches Anwendungsszenario in der Industrie.

**Schema**:

```python
import sqlite3
from datetime import datetime

conn = sqlite3.connect('ml_training_logs.db')
cursor = conn.cursor()

# Tabelle: Modelle
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Modelle (
        Modell_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Modellname TEXT NOT NULL UNIQUE,
        Architektur TEXT NOT NULL,
        Erstellt_Am TEXT DEFAULT CURRENT_TIMESTAMP
    )
''')

# Tabelle: Training-Runs
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Training_Runs (
        Run_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Modell_ID INTEGER NOT NULL,
        Hyperparameter TEXT,  -- JSON-String
        Start_Zeit TEXT NOT NULL,
        End_Zeit TEXT,
        Dauer_Sekunden REAL,
        Status TEXT CHECK(Status IN ('laufend', 'abgeschlossen', 'abgebrochen', 'fehler')),
        FOREIGN KEY (Modell_ID) REFERENCES Modelle(Modell_ID)
    )
''')

# Tabelle: Metriken pro Epoche
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Epochen_Metriken (
        Metrik_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Run_ID INTEGER NOT NULL,
        Epoche INTEGER NOT NULL,
        Train_Loss REAL,
        Val_Loss REAL,
        Train_Accuracy REAL,
        Val_Accuracy REAL,
        Learning_Rate REAL,
        FOREIGN KEY (Run_ID) REFERENCES Training_Runs(Run_ID) ON DELETE CASCADE,
        UNIQUE(Run_ID, Epoche)
    )
''')

# Indizes für Performance
cursor.execute('CREATE INDEX IF NOT EXISTS idx_runs_modell ON Training_Runs(Modell_ID)')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_metriken_run ON Epochen_Metriken(Run_ID)')

# Foreign Keys aktivieren
cursor.execute('PRAGMA foreign_keys = ON')

conn.commit()
print("Datenbank erstellt")
```

**Daten einfügen**:

```python
import json
import time

# Modell registrieren
cursor.execute('''
    INSERT INTO Modelle (Modellname, Architektur) 
    VALUES (?, ?)
''', ('Predictive_Maintenance_v1', 'LSTM'))
modell_id = cursor.lastrowid

# Training-Run starten
hyperparams = json.dumps({'batch_size': 32, 'learning_rate': 0.001, 'epochs': 50})
cursor.execute('''
    INSERT INTO Training_Runs (Modell_ID, Hyperparameter, Start_Zeit, Status)
    VALUES (?, ?, ?, ?)
''', (modell_id, hyperparams, datetime.now().isoformat(), 'laufend'))
run_id = cursor.lastrowid
conn.commit()

# Epochen-Metriken simulieren
for epoche in range(1, 51):
    train_loss = 0.5 * (0.95 ** epoche) + 0.01  # Simulierte Konvergenz
    val_loss = train_loss + 0.05
    
    cursor.execute('''
        INSERT INTO Epochen_Metriken (Run_ID, Epoche, Train_Loss, Val_Loss, Train_Accuracy, Val_Accuracy, Learning_Rate)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (run_id, epoche, train_loss, val_loss, 0.8 + epoche*0.004, 0.75 + epoche*0.003, 0.001))
    
    if epoche % 10 == 0:
        conn.commit()  # Batch-Commit alle 10 Epochen

# Training abschließen
end_zeit = datetime.now().isoformat()
dauer = 3600.5  # Simuliert 1 Stunde
cursor.execute('''
    UPDATE Training_Runs 
    SET End_Zeit = ?, Dauer_Sekunden = ?, Status = ?
    WHERE Run_ID = ?
''', (end_zeit, dauer, 'abgeschlossen', run_id))
conn.commit()

print(f"Training-Run {run_id} abgeschlossen")
```

**Abfragen**:

```python
# Bestes Modell basierend auf finaler Val-Accuracy
cursor.execute('''
    SELECT m.Modellname, 
           tr.Run_ID,
           MAX(em.Val_Accuracy) AS Beste_Accuracy
    FROM Modelle m
    INNER JOIN Training_Runs tr ON m.Modell_ID = tr.Modell_ID
    INNER JOIN Epochen_Metriken em ON tr.Run_ID = em.Run_ID
    WHERE tr.Status = 'abgeschlossen'
    GROUP BY m.Modell_ID, tr.Run_ID
    ORDER BY Beste_Accuracy DESC
    LIMIT 5
''')

print("Top 5 Runs:")
for zeile in cursor.fetchall():
    print(f"{zeile[0]} (Run {zeile[1]}): {zeile[2]:.4f} Val-Accuracy")

# Konvergenz-Analyse: Letzte 10 Epochen eines Runs
cursor.execute('''
    SELECT Epoche, Train_Loss, Val_Loss, Val_Accuracy
    FROM Epochen_Metriken
    WHERE Run_ID = ?
    ORDER BY Epoche DESC
    LIMIT 10
''', (run_id,))

print(f"\nLetzte 10 Epochen von Run {run_id}:")
for zeile in cursor.fetchall():
    print(f"Epoche {zeile[0]}: Train Loss {zeile[1]:.4f}, Val Loss {zeile[2]:.4f}, Val Acc {zeile[3]:.4f}")
```

Diese Datenbank ermöglicht Experiment-Tracking für ML-Projekte – ein kritischer Bestandteil moderner KI-Entwicklung.

---

## 🔚 Zusammenfassung

In dieser Vorlesung haben wir fortgeschrittene Datenbankkonzepte und SQL-Techniken behandelt:

**Theoretische Konzepte**:
- **Normalisierung** (1NF, 2NF, 3NF) zur Vermeidung von Redundanz und Anomalien
- **Indizes** zur Beschleunigung von Abfragen (B-Trees, Unique, Composite, Partial)
- **Transaktionen und ACID** (Atomicity, Consistency, Isolation, Durability)
- **NoSQL-Datenbanken** (Key-Value, Document, Column-Family, Graph) und CAP-Theorem
- **Vector Databases** für Embeddings und Similarity Search (RAG, semantische Suche)

**Python-Praxis**:
- **Prepared Statements** gegen SQL-Injection (IMMER `?` Platzhalter verwenden)
- **UPDATE und DELETE** Operationen mit WHERE-Klauseln
- **Transaktionen** explizit steuern (`.commit()`, `.rollback()`)
- **Cursor-Methoden** (`.fetchone()`, `.fetchall()`, `.fetchmany()`)
- **Context Manager** für sichere Ressourcenverwaltung
- **Aggregationen und JOINs** für komplexe Abfragen
- **Best Practices**: Indizes, Error Handling, `executemany()`, `row_factory`

Mit diesem Wissen können Sie professionelle, sichere und performante Datenbankanwendungen entwickeln – ob relationale Datenbanken für strukturierte Daten oder NoSQL-Lösungen für spezielle Anwendungsfälle wie KI-Embeddings.

