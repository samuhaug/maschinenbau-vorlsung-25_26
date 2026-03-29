# V19 – Datenbanken – Teil 1: Aufgaben

---

## 📚 Theorie-Aufgaben

### T1: Entity-Relationship-Modellierung (Konzeptuelles Design)

Eine Maschinenfabrik produziert verschiedene **Werkstücke** auf **Maschinen**. Jede Maschine kann mehrere Werkstücktypen bearbeiten, und jedes Werkstück kann auf mehreren Maschinen gefertigt werden.

Zu jedem **Werkstück** sollen gespeichert werden: Werkstück-ID, Bezeichnung, Materialnummer, Gewicht (kg), Zielstückzahl pro Monat.

Zu jeder **Maschine** sollen gespeichert werden: Maschinen-ID, Maschinentyp, Baujahr, Standort, Max. Betriebsstunden pro Tag.

Zu jedem **Produktionsauftrag** (Verknüpfung zwischen Werkstück und Maschine) sollen gespeichert werden: Auftragsdatum, produzierte Stückzahl, tatsächliche Betriebsstunden, Ausschussrate (%).

**Teilaufgaben:**

a) **Kardinalität bestimmen**: Welche Beziehung (1:1, 1:n, m:n) besteht zwischen Werkstücken und Maschinen? Begründe deine Antwort anhand der Aufgabenbeschreibung.

b) **Tabellenschema entwerfen**: Erstelle ein Tabellenschema mit drei Tabellen (`Werkstuecke`, `Maschinen`, `Produktionsauftraege`). Gib für jede Tabelle die Spaltennamen, Datentypen (INTEGER, TEXT, REAL) und Constraints (PRIMARY KEY, FOREIGN KEY, NOT NULL, CHECK) an.

c) **Normalisierung prüfen**: Überprüfe dein Schema auf 3NF (Dritte Normalform). Gibt es Redundanzen oder transitive Abhängigkeiten? Falls ja, wie würdest du sie auflösen?

d) **Beispiel-INSERT-Statements**: Schreibe SQL-INSERT-Statements, um folgende Daten einzufügen:
   - Werkstück: "Zahnrad Z24" (Material M-1234, Gewicht 2.5 kg, Ziel: 500 Stk/Monat)
   - Maschine: "CNC-Drehmaschine Index G220" (Baujahr 2019, Standort Halle 3, Max. 20 h/Tag)
   - Produktionsauftrag: Zahnrad Z24 auf Index G220 am 15.03.2024, 120 Stück produziert, 8.5 Stunden, 2.5% Ausschuss

---

### T2: SQL-Abfragen formulieren (Szenario: Qualitätssicherung)

Gegeben sei folgende Tabellenstruktur für ein Qualitätssicherungs-System:

**Tabelle: Bauteile**
| Bauteil_ID | Bezeichnung          | Materialnummer | Sollmasse_mm | Toleranz_mm |
|------------|----------------------|----------------|--------------|-------------|
| 1          | Welle W-42           | ST-235         | 150.00       | 0.05        |
| 2          | Buchse B-18          | AL-601         | 25.00        | 0.02        |
| 3          | Flansch F-90         | ST-235         | 220.00       | 0.10        |

**Tabelle: Messungen**
| Mess_ID | Bauteil_ID | Messdatum  | Istmasse_mm | Pruefgeraet     |
|---------|------------|------------|-------------|-----------------|
| 1       | 1          | 2024-03-10 | 150.02      | Messschieber-A1 |
| 2       | 1          | 2024-03-10 | 150.07      | Messschieber-A1 |
| 3       | 2          | 2024-03-11 | 24.99       | Mikrometer-B3   |
| 4       | 3          | 2024-03-11 | 220.15      | Messschieber-A1 |
| 5       | 1          | 2024-03-12 | 149.98      | Messschieber-A2 |

**Teilaufgaben:**

a) **Abweichungsberechnung**: Schreibe eine SQL-Query, die für jede Messung die absolute Abweichung vom Sollmaß berechnet: `ABS(Istmasse_mm - Sollmasse_mm)`. Gib Mess_ID, Bauteil-Bezeichnung, Sollmasse, Istmasse und Abweichung aus. Sortiere nach Abweichung absteigend.

b) **Ausschuss-Identifikation**: Erweitere die Query aus (a), um nur Messungen auszugeben, bei denen die Abweichung größer als die Toleranz ist. Diese Bauteile sind Ausschuss.

c) **Aggregation nach Bauteil**: Schreibe eine Query, die pro Bauteil folgendes berechnet: Anzahl Messungen, durchschnittliche Istmasse, minimale Istmasse, maximale Istmasse, Anzahl Ausschuss-Teile (Abweichung > Toleranz).

d) **Prüfgeräte-Analyse**: Welches Prüfgerät wurde am häufigsten verwendet? Schreibe eine Query mit `GROUP BY Pruefgeraet` und `COUNT(*)`. Gib nur Geräte mit mehr als 1 Messung aus (HAVING).

---

### T3: Datenbankdesign-Entscheidungen (Multiple-Choice + Begründung)

**Frage 1**: Ein Unternehmen speichert Mitarbeiterdaten. Jeder Mitarbeiter hat genau eine E-Mail-Adresse, aber E-Mail-Adressen sind unique (keine zwei Mitarbeiter haben dieselbe E-Mail). Wie sollte die E-Mail-Spalte definiert werden?

a) `Email TEXT`  
b) `Email TEXT NOT NULL`  
c) `Email TEXT UNIQUE`  
d) `Email TEXT NOT NULL UNIQUE`  

**Begründe** deine Antwort und erkläre, welche Constraints notwendig sind.

---

**Frage 2**: Eine Datenbank speichert Sensormesswerte. Pro Sekunde werden 10.000 neue Zeilen eingefügt. Die Abfragen filtern häufig nach `Sensor_ID` und `Zeitstempel`. Was ist die beste Performance-Optimierung?

a) `CREATE INDEX` auf `Sensor_ID` und separaten Index auf `Zeitstempel`  
b) `CREATE INDEX` auf kombiniertem Paar `(Sensor_ID, Zeitstempel)`  
c) Keine Indizes (verlangsamen INSERTs)  
d) Datenbank-Normalisierung auf 5NF  

**Begründe** deine Wahl mit Bezug auf Abfrage- vs. INSERT-Performance.

---

**Frage 3**: Ein Produktionsauftrag kann mehrere Werkstücke enthalten, und jedes Werkstück kann in mehreren Aufträgen vorkommen. Welche Kardinalität liegt vor und wie wird sie implementiert?

a) 1:1 – Eine Zwischentabelle ist nicht nötig  
b) 1:n – Fremdschlüssel in Werkstück-Tabelle  
c) n:m – Junction Table mit zwei Fremdschlüsseln  
d) n:m – Verschachtelte JSON-Arrays in Auftragstabelle  

**Begründe** deine Antwort und nenne Vor-/Nachteile von JSON-Speicherung im Vergleich zu Junction Table.

---

## 🐍 Python-Aufgaben

### P1: Temperatur-Monitoring-System (CRUD-Operationen + SQLite)

Ein **Temperaturüberwachungssystem** für Kühlschränke in einer Lebensmittelproduktion soll Messwerte in einer SQLite-Datenbank speichern.

**Datenbankschema:**

**Tabelle: Kuehlschraenke**
- `Kuehlschrank_ID` INTEGER PRIMARY KEY AUTOINCREMENT
- `Bezeichnung` TEXT NOT NULL
- `Standort` TEXT NOT NULL
- `Soll_Temperatur_Celsius` REAL NOT NULL
- `Toleranz_Celsius` REAL DEFAULT 2.0
- `Aktiv` INTEGER DEFAULT 1  (1 = aktiv, 0 = inaktiv)

**Tabelle: Temperaturmessungen**
- `Mess_ID` INTEGER PRIMARY KEY AUTOINCREMENT
- `Kuehlschrank_ID` INTEGER NOT NULL
- `Zeitstempel` TEXT NOT NULL  (ISO-Format: "2024-03-10T14:25:30")
- `Temperatur_Celsius` REAL NOT NULL
- `Alarm` INTEGER DEFAULT 0  (1 = Temperatur außerhalb Toleranz)
- `FOREIGN KEY (Kuehlschrank_ID) REFERENCES Kuehlschraenke(Kuehlschrank_ID)`

**Aufgaben:**

a) **Datenbank erstellen**: Schreibe ein Python-Skript `aufgabe_p1.py`, das die Datenbankdatei `kuehlueberwachung.db` erstellt und beide Tabellen anlegt (falls nicht vorhanden).

b) **Kühlschränke initialisieren**: Füge folgende Kühlschränke ein:
   - "Kühlraum A1" @ "Produktionshalle 1", Soll: 4°C, Toleranz: 1.5°C
   - "Gefrierschrank B2" @ "Lager Gebäude 2", Soll: -18°C, Toleranz: 3.0°C
   - "Kühlzelle C3" @ "Versandhalle", Soll: 2°C, Toleranz: 1.0°C

c) **Messwerte importieren**: Lies Messwerte aus der Datei `testdaten/temperaturmessungen.csv` (siehe unten) und füge sie in die Datenbank ein. Berechne für jede Messung das `Alarm`-Flag: `1` wenn `ABS(Temperatur - Soll_Temperatur) > Toleranz`, sonst `0`.

d) **Alarm-Report**: Erstelle eine Funktion `alarm_report()`, die alle Messungen mit `Alarm = 1` ausgibt. Sortiere nach Zeitstempel absteigend (neueste zuerst). Ausgabe-Format:
   ```
   ALARM: Kühlraum A1 (Soll: 4°C ±1.5°C) – 2024-03-10 14:25:30 – IST: 7.2°C [ÜBERHITZT]
   ALARM: Gefrierschrank B2 (Soll: -18°C ±3.0°C) – 2024-03-10 10:15:00 – IST: -13.5°C [ZU WARM]
   ...
   ```

e) **Statistik pro Kühlschrank**: Erstelle eine Funktion `statistik_pro_kuehlschrank()`, die pro Kühlschrank ausgibt:
   - Anzahl Messungen
   - Durchschnittstemperatur
   - Min-/Max-Temperatur
   - Anzahl Alarme
   - Alarmrate (Prozent)

**Hinweis**: Alle SQL-Queries sollen Prepared Statements verwenden (keine String-Interpolation!).

---

### P2: Werkstoff-Prüfdatenbank mit JOINs (Analyse komplexer Beziehungen)

Ein Labor führt **Zugversuche** an verschiedenen Werkstoffen durch. Die Prüfdaten sollen in einer relationalen Datenbank gespeichert und analysiert werden.

**Datenbankschema:**

**Tabelle: Werkstoffe**
- `Werkstoff_ID` INTEGER PRIMARY KEY
- `Bezeichnung` TEXT NOT NULL
- `Werkstoffnummer` TEXT UNIQUE NOT NULL
- `Dichte_g_cm3` REAL
- `E_Modul_GPa` REAL

**Tabelle: Proben**
- `Proben_ID` INTEGER PRIMARY KEY
- `Werkstoff_ID` INTEGER NOT NULL
- `Probendurchmesser_mm` REAL NOT NULL
- `Probenlaenge_mm` REAL NOT NULL
- `Herstellungsdatum` TEXT
- `FOREIGN KEY (Werkstoff_ID) REFERENCES Werkstoffe(Werkstoff_ID)`

**Tabelle: Zugversuche**
- `Versuchs_ID` INTEGER PRIMARY KEY
- `Proben_ID` INTEGER NOT NULL
- `Versuchsdatum` TEXT NOT NULL
- `Streckgrenze_MPa` REAL
- `Zugfestigkeit_MPa` REAL
- `Bruchdehnung_Prozent` REAL
- `Pruefgeraet` TEXT NOT NULL
- `FOREIGN KEY (Proben_ID) REFERENCES Proben(Proben_ID)`

**Aufgaben:**

a) **Datenbank erstellen und befüllen**: Erstelle `werkstoffpruefung.db` mit allen drei Tabellen. Importiere Testdaten aus `testdaten/werkstoffe.csv`, `testdaten/proben.csv` und `testdaten/zugversuche.csv`.

b) **JOIN-Query (Vollständige Versuchsdaten)**: Schreibe eine SQL-Query, die **alle** Informationen zu jedem Zugversuch ausgibt: Versuchs-ID, Versuchsdatum, Werkstoffbezeichnung, Werkstoffnummer, Probendurchmesser, Streckgrenze, Zugfestigkeit, Bruchdehnung, Prüfgerät. Verwende INNER JOINs.

c) **Aggregation (Durchschnittswerte pro Werkstoff)**: Berechne pro Werkstoff: Anzahl Zugversuche, durchschnittliche Streckgrenze, durchschnittliche Zugfestigkeit, durchschnittliche Bruchdehnung. Sortiere nach Anzahl Versuche absteigend.

d) **Qualitätssicherung (Ausreißer-Detektion)**: Für jeden Werkstoff: Finde Zugversuche, bei denen die Zugfestigkeit mehr als 10% vom Durchschnitt dieses Werkstoffs abweicht. Verwende eine Subquery zur Berechnung des Durchschnitts.

e) **Prüfgeräte-Vergleich**: Analysiere, ob verschiedene Prüfgeräte systematische Unterschiede zeigen. Berechne pro Prüfgerät die durchschnittliche Zugfestigkeit. Gibt es Auffälligkeiten?

**Erwartete Ausgabe (Beispiel für c):**
```
Werkstoff: S235JR (Werkstoffnummer 1.0038)
  Anzahl Versuche: 5
  Ø Streckgrenze: 245.6 MPa
  Ø Zugfestigkeit: 382.3 MPa
  Ø Bruchdehnung: 24.5%
```

---

### P3: Fertigungsauftragsverwaltung (Transaktionen + Fehlerbehandlung)

Ein **Auftragsverwaltungssystem** für eine Fertigungshalle soll Aufträge, Materialverbrauch und Maschinenbelegung tracken. Bei Buchungen sollen Transaktionen verwendet werden, um Datenkonsistenz zu garantieren.

**Datenbankschema:**

**Tabelle: Auftraege**
- `Auftrags_ID` INTEGER PRIMARY KEY
- `Auftragsnummer` TEXT UNIQUE NOT NULL
- `Kundennummer` TEXT NOT NULL
- `Produkt` TEXT NOT NULL
- `Stueckzahl` INTEGER CHECK (Stueckzahl > 0)
- `Status` TEXT DEFAULT 'OFFEN'  -- OFFEN, IN_BEARBEITUNG, ABGESCHLOSSEN, STORNIERT

**Tabelle: Materialbestand**
- `Material_ID` INTEGER PRIMARY KEY
- `Bezeichnung` TEXT NOT NULL
- `Lagerbestand_kg` REAL CHECK (Lagerbestand_kg >= 0)
- `Mindestbestand_kg` REAL DEFAULT 100.0

**Tabelle: Materialbuchungen**
- `Buchungs_ID` INTEGER PRIMARY KEY
- `Auftrags_ID` INTEGER NOT NULL
- `Material_ID` INTEGER NOT NULL
- `Menge_kg` REAL CHECK (Menge_kg > 0)
- `Buchungsdatum` TEXT NOT NULL
- `FOREIGN KEY (Auftrags_ID) REFERENCES Auftraege(Auftrags_ID)`
- `FOREIGN KEY (Material_ID) REFERENCES Materialbestand(Material_ID)`

**Aufgaben:**

a) **Datenbank initialisieren**: Erstelle `fertigungsauftraege.db` mit allen Tabellen. Füge Testdaten aus `testdaten/materialbestand.json` ein (Material-ID, Bezeichnung, Lagerbestand, Mindestbestand).

b) **Auftrag anlegen (mit Validierung)**: Schreibe eine Funktion `auftrag_anlegen(auftragsnummer, kundennummer, produkt, stueckzahl)`, die einen neuen Auftrag anlegt. Prüfe vorher, ob die Auftragsnummer bereits existiert (verwende `sqlite3.IntegrityError`-Exception).

c) **Material buchen (Transaktion)**: Schreibe eine Funktion `material_buchen(auftrags_id, material_id, menge_kg)`, die:
   1. Prüft, ob genug Material im Lager ist (`Lagerbestand >= Menge`)
   2. Falls ja: Lagerbestand reduzieren **und** Buchung eintragen (beide Operationen in **einer Transaktion**)
   3. Falls nein: Exception werfen (`ValueError`) mit Meldung "Nicht genug Material im Lager"
   
   Verwende `try-except-finally` mit `conn.commit()` bei Erfolg und `conn.rollback()` bei Fehler.

d) **Mindestbestand-Warnung**: Schreibe eine Funktion `mindestbestand_pruefung()`, die alle Materialien ausgibt, deren Lagerbestand unter dem Mindestbestand liegt. Ausgabe-Format:
   ```
   WARNUNG: Stahlblech ST37 – Lagerbestand: 85.5 kg (Mindestbestand: 100.0 kg) [NACHBESTELLEN]
   ```

e) **Auftrags-Dashboard**: Erstelle eine Funktion `auftrags_dashboard()`, die für jeden Auftrag ausgibt:
   - Auftragsnummer, Produkt, Stückzahl, Status
   - Summe der gebuchten Materialmengen (JOIN mit `Materialbuchungen`)
   - Anzahl verschiedener Materialien

**Testfall für c)**: Versuche, 150 kg Stahlblech zu buchen, obwohl nur 100 kg im Lager sind. Die Transaktion soll fehlschlagen, und der Lagerbestand darf sich nicht ändern.

---

### P4: Sensor-Datenbank mit Zeitreihen-Analyse (pandas Integration)

Eine **IoT-Plattform** sammelt Sensordaten von Maschinen. Die Daten werden in SQLite gespeichert und mit pandas analysiert.

**Datenbankschema:**

**Tabelle: Sensoren**
- `Sensor_ID` INTEGER PRIMARY KEY
- `Sensorname` TEXT NOT NULL
- `Maschinen_ID` INTEGER NOT NULL
- `Sensor_Typ` TEXT NOT NULL  -- TEMPERATUR, DREHZAHL, VIBRATION, DRUCK
- `Einheit` TEXT NOT NULL

**Tabelle: Sensormesswerte**
- `Messwert_ID` INTEGER PRIMARY KEY
- `Sensor_ID` INTEGER NOT NULL
- `Zeitstempel` TEXT NOT NULL
- `Wert` REAL NOT NULL
- `FOREIGN KEY (Sensor_ID) REFERENCES Sensoren(Sensor_ID)`

**Aufgaben:**

a) **Datenbank befüllen**: Importiere Testdaten aus `testdaten/sensoren.csv` und `testdaten/sensormesswerte.csv` in `sensor_datenbank.db`.

b) **DataFrame-Export**: Schreibe eine Funktion `export_zu_pandas(sensor_id)`, die alle Messwerte eines Sensors als pandas DataFrame exportiert. Der DataFrame soll Spalten `Zeitstempel` (als datetime), `Wert` und `Einheit` haben. Sortiere nach Zeitstempel.

c) **Zeitreihen-Plot**: Verwende matplotlib, um für einen bestimmten Sensor (z.B. Temperatursensor "TEMP_01") einen Zeitreihen-Plot zu erstellen. X-Achse: Zeitstempel, Y-Achse: Temperatur in °C. Füge horizontale Linien für Min/Max/Durchschnitt hinzu.

d) **Gleitender Durchschnitt**: Berechne einen gleitenden 10-Punkte-Durchschnitt für einen Drehzahlsensor mit pandas (`df['Wert'].rolling(window=10).mean()`). Plotte Original-Daten und geglättete Kurve in einem Plot.

e) **Anomalie-Detektion**: Definiere Anomalien als Messwerte, die mehr als 2 Standardabweichungen vom Mittelwert abweichen. Markiere diese Punkte in einem Scatter-Plot rot, normale Punkte blau.

**Hinweise:**
- Verwende `pd.read_sql_query()` zum direkten Laden von SQL-Ergebnissen in pandas.
- Konvertiere Zeitstempel mit `pd.to_datetime(df['Zeitstempel'])`.
- Bei Plots: Aussagekräftige Titel, Achsenbeschriftungen, Legende.

**Beispiel-Ausgabe für e):**
```
Sensor: DREHZAHL_01 (Maschine 5)
  Mittelwert: 1485.2 U/min
  Standardabweichung: 45.8 U/min
  Anomalien erkannt: 3 (von 1000 Messungen)
  Zeitpunkte: 2024-03-10 08:23:15, 2024-03-10 14:51:42, 2024-03-11 09:12:05
```

---

### P5: Produktionsplanungs-Tool (Komplexes JOIN-Szenario + Export)

Ein **Produktionsplanungs-Tool** verwaltet Produktionsaufträge, Maschinenbelegungen und Materialien. Das System soll Excel-kompatible CSV-Reports generieren.

**Datenbankschema:**

**Tabelle: Produkte**
- `Produkt_ID` INTEGER PRIMARY KEY
- `Produktname` TEXT UNIQUE NOT NULL
- `Produktionszeit_Minuten` INTEGER NOT NULL
- `Material_pro_Stueck_kg` REAL NOT NULL

**Tabelle: Produktionsauftraege**
- `Auftrag_ID` INTEGER PRIMARY KEY
- `Produkt_ID` INTEGER NOT NULL
- `Stueckzahl` INTEGER NOT NULL
- `Prioritaet` INTEGER DEFAULT 5  -- 1 (höchste) bis 10 (niedrigste)
- `Status` TEXT DEFAULT 'GEPLANT'  -- GEPLANT, IN_ARBEIT, ABGESCHLOSSEN
- `Zieltermin` TEXT NOT NULL
- `FOREIGN KEY (Produkt_ID) REFERENCES Produkte(Produkt_ID)`

**Tabelle: Maschinenbelegung**
- `Belegungs_ID` INTEGER PRIMARY KEY
- `Auftrag_ID` INTEGER NOT NULL
- `Maschinen_ID` INTEGER NOT NULL
- `Startzeit` TEXT NOT NULL
- `Endzeit` TEXT NOT NULL
- `Tatsaechliche_Stueckzahl` INTEGER
- `FOREIGN KEY (Auftrag_ID) REFERENCES Produktionsauftraege(Auftrag_ID)`

**Aufgaben:**

a) **Datenbank befüllen**: Importiere Testdaten aus `testdaten/produkte.csv`, `testdaten/produktionsauftraege.json` und `testdaten/maschinenbelegung.xml`.

b) **Produktionsplan-Report (komplexer JOIN)**: Erstelle eine SQL-Query, die folgende Informationen ausgibt:
   - Auftragsnummer (Auftrag_ID)
   - Produktname
   - Geplante Stückzahl
   - Priorität
   - Zieltermin
   - Status
   - Anzahl zugewiesener Maschinenbelegungen
   - Summe tatsächlich produzierter Stückzahl
   - Produktionsfortschritt in % (`(Summe tatsächlich / geplant) * 100`)

   Sortiere nach Priorität (niedrigste zuerst = höchste Dringlichkeit) und dann nach Zieltermin.

c) **Materialbedarfsrechnung**: Berechne für alle Aufträge mit Status "GEPLANT" den gesamten Materialbedarf. Gruppiere nach Produktname und summiere `Stueckzahl * Material_pro_Stueck_kg`.

d) **Auslastungs-Analyse**: Für jede Maschine (Maschinen_ID): Berechne die Gesamtbetriebszeit in Stunden (Summe aller `JULIANDAY(Endzeit) - JULIANDAY(Startzeit)` * 24). Gib die drei meistausgelasteten Maschinen aus.

e) **CSV-Export**: Schreibe eine Funktion `export_produktionsplan(ausgabedatei)`, die den Produktionsplan-Report aus (b) als CSV-Datei exportiert. Verwende das `csv`-Modul mit Header-Zeile. Die CSV soll in Excel geöffnet werden können (Separator: `;`, Dezimaltrennzeichen: `,` für deutsche Lokalisierung).

**Beispiel-Ausgabe für b):**
```
Auftrag 101 | Zahnrad Z42 | 500 Stk | Prio 2 | Ziel: 2024-03-20 | IN_ARBEIT | 3 Maschinen | 320 Stk produziert | Fortschritt: 64.0%
Auftrag 102 | Welle W-18  | 200 Stk | Prio 3 | Ziel: 2024-03-25 | GEPLANT   | 0 Maschinen | 0 Stk produziert   | Fortschritt: 0.0%
...
```

---

## 📁 Testdaten

Alle Testdaten befinden sich im Unterordner **`testdaten/`**. Folgende Dateien werden bereitgestellt:

1. **P1 (Temperatur-Monitoring)**:
   - `temperaturmessungen.csv`: 50 Messwerte für 3 Kühlschränke über 7 Tage

2. **P2 (Werkstoff-Prüfdatenbank)**:
   - `werkstoffe.csv`: 5 verschiedene Werkstoffe (S235JR, C45, AlMg3, X5CrNi18-10, GGG-40)
   - `proben.csv`: 20 Proben verschiedener Werkstoffe
   - `zugversuche.csv`: 30 Zugversuche auf den Proben

3. **P3 (Fertigungsauftragsverwaltung)**:
   - `materialbestand.json`: 8 Materialien mit Lagerbeständen

4. **P4 (Sensor-Datenbank)**:
   - `sensoren.csv`: 10 Sensoren (Temperatur, Drehzahl, Vibration, Druck)
   - `sensormesswerte.csv`: 1000 Messwerte über 24 Stunden

5. **P5 (Produktionsplanungs-Tool)**:
   - `produkte.csv`: 6 Produkte mit Produktionszeiten und Materialbedarf
   - `produktionsauftraege.json`: 15 Aufträge in verschiedenen Status
   - `maschinenbelegung.xml`: 25 Maschinenbelegungen

Die Dateien werden im nächsten Schritt erstellt.