# V15: Netzwerktechnik Grundlagen & Protokolle – Teil 1 – Aufgaben

## Teil A: Theorie-Aufgaben

### Aufgabe 1: OSI-Schichten zuordnen ⭐ (Leicht)

Ordne die folgenden Protokolle und Technologien der **korrekten OSI-Schicht** zu:

1. HTTP
2. Ethernet
3. TCP
4. IP
5. DNS
6. WLAN (IEEE 802.11)
7. TLS/SSL
8. MAC-Adresse
9. Glasfaserkabel
10. SMTP

**Schichten zur Auswahl:**
- Schicht 1: Bitübertragungsschicht (Physical Layer)
- Schicht 2: Sicherungsschicht (Data Link Layer)
- Schicht 3: Vermittlungsschicht (Network Layer)
- Schicht 4: Transportschicht (Transport Layer)
- Schicht 5: Sitzungsschicht (Session Layer)
- Schicht 6: Darstellungsschicht (Presentation Layer)
- Schicht 7: Anwendungsschicht (Application Layer)

**Zusatzfrage:** Erkläre für **zwei** der genannten Protokolle/Technologien, warum sie dieser Schicht zugeordnet sind (jeweils 2-3 Sätze).

---

### Aufgabe 2: IP-Adressen klassifizieren und umrechnen ⭐⭐ (Mittel)

**Teil 1: Klassifikation**

Bestimme für jede der folgenden IPv4-Adressen, ob sie **privat** oder **öffentlich** ist. Wenn privat: Gib den privaten Adressbereich an (z.B. `10.0.0.0/8`).

1. `192.168.50.10`
2. `8.8.8.8`
3. `172.20.15.100`
4. `10.255.255.255`
5. `172.32.0.1`
6. `127.0.0.1`

**Teil 2: Binäre Umrechnung**

Wandle die folgende IPv4-Adresse in ihre **binäre Darstellung** um:

```
IP-Adresse: 192.168.1.100
```

Notation:
```
Dezimal:  192      .  168      .  1        .  100
Binär:    ________ .  ________ .  ________ .  ________
```

**Teil 3: IPv6-Notation**

Kürze die folgende IPv6-Adresse **maximal** (nutze beide Vereinfachungsregeln):

```
Original: 2001:0db8:0000:0000:0000:ff00:0042:8329
Gekürzt:  _______________________________________
```

---

### Aufgabe 3: Subnetting für Produktionsanlagen ⭐⭐⭐ (Schwer)

Ein Maschinenbau-Unternehmen hat das Netzwerk **`172.16.100.0/24`** für seine Produktionshalle zugewiesen bekommen. Die IT-Abteilung soll dieses Netzwerk in **acht gleich große Subnetze** aufteilen, um verschiedene Produktionszellen zu isolieren:

- **Zelle 1**: CNC-Fräsmaschinen (15 Maschinen)
- **Zelle 2**: Drehmaschinen (12 Maschinen)
- **Zelle 3**: Roboterarme (20 Maschinen)
- **Zelle 4**: Qualitätsprüfung (8 Geräte)
- **Zelle 5**: Lagerverwaltung (10 Scanner)
- **Zelle 6**: Montage (18 Arbeitsplätze)
- **Zelle 7**: Wartung (5 Mobile Geräte)
- **Zelle 8**: Management/SCADA (10 Systeme)

**Aufgaben:**

**a) Berechnung der neuen Präfixlänge**
- Wie viele zusätzliche Bits werden für die Subnetz-ID benötigt?
- Wie lautet die neue Präfixlänge (CIDR-Notation)?
- Wie lautet die neue Subnetzmaske in Dezimalschreibweise?

**b) Hosts pro Subnetz**
- Wie viele Bits bleiben für die Host-ID?
- Wie viele **nutzbare** Adressen gibt es pro Subnetz (berücksichtige Netzwerk- und Broadcast-Adresse)?

**c) Subnetz-Bereiche**

Fülle die folgende Tabelle für die **ersten drei** Subnetze aus:

| Subnetz | Produktionszelle | Netzwerkadresse | Erste nutzbare IP | Letzte nutzbare IP | Broadcast-Adresse |
|---------|------------------|-----------------|-------------------|--------------------|-------------------|
| 1 | CNC-Fräsmaschinen | | | | |
| 2 | Drehmaschinen | | | | |
| 3 | Roboterarme | | | | |

**d) Praktische Anwendung**

- Zelle 3 (Roboterarme) benötigt **20 Hosts**. Ist eines der acht Subnetze ausreichend? Begründe deine Antwort.
- Welche Produktionszellen passen **nicht** in ein einzelnes Subnetz und benötigen spezielle Lösungen?

**Bonus (+⭐):** Die SCADA-Systeme benötigen **60 Adressen** für zukünftige Erweiterungen. Kannst du zwei benachbarte Subnetze zu einem größeren zusammenfassen? Wenn ja, wie lautet die neue CIDR-Notation und der nutzbare IP-Bereich?

---

## Teil B: Python-Aufgaben

### Aufgabe P1: Netzwerk-Paket-Analyse ⭐⭐ (Mittel)

**Datei:** `netzwerk_pakete.csv`

In einer Produktionshalle wurden über 5 Minuten industrielle Netzwerkpakete aufgezeichnet. Die CSV-Datei enthält folgende Spalten:

```
Zeitstempel,Quell_IP,Ziel_IP,Protokoll,Port,Paketgroesse_Bytes,Maschine_ID
```

**Aufgabe:**

Schreibe ein Python-Programm, das die CSV-Datei analysiert und folgende Informationen ausgibt:

**a) Protokoll-Verteilung**
- Anzahl der Pakete pro Protokoll (TCP, UDP)
- Prozentuale Verteilung

**b) Port-Analyse**
- Identifiziere die Industrieprotokolle anhand der Ports:
  - Port 502: Modbus TCP
  - Port 1883: MQTT
  - Port 44818: OPC UA
- Zeige Anzahl Pakete pro Industrieprotokoll

**c) Netzwerk-Last**
- Gesamtes übertragenes Datenvolumen in KB
- Durchschnittliche Paketgröße

**d) Maschinen-Kommunikation**
- Top 3 aktivste Maschinen (nach Maschine_ID mit den meisten gesendeten Paketen)
- Liste aller Maschinen-IDs, die mit dem SCADA-Server (192.168.10.200) kommunizieren

**Anforderungen:**
- Nutze `csv.DictReader` für das Einlesen
- Behandle fehlerhafte oder unvollständige Zeilen mit try-except
- Formatiere Ausgaben übersichtlich mit Einheiten

**Erwartete Ausgabe (Beispiel):**
```
=== Netzwerk-Paket-Analyse ===

Protokoll-Verteilung:
  TCP: 70 Pakete (70.0%)
  UDP: 30 Pakete (30.0%)

Industrieprotokolle (nach Port):
  Modbus TCP (502): 50 Pakete
  MQTT (1883): 30 Pakete
  OPC UA (44818): 20 Pakete

Netzwerk-Last:
  Gesamt: 15.5 KB
  Ø Paketgröße: 155 Bytes

Top 3 aktivste Maschinen:
  1. CNC-01: 18 Pakete
  2. CNC-02: 15 Pakete
  3. Robot-01: 12 Pakete

Kommunikation mit SCADA (192.168.10.200):
  Maschinen: CNC-01, CNC-02, Robot-01, Press-01, Sensor-01
```

---

### Aufgabe P2: Maschinenkommunikations-Analyse mit JSON ⭐⭐ (Mittel)

**Datei:** `maschinenkommunikation.json`

Die JSON-Datei enthält Konfigurationsdaten von Produktionsmaschinen in einer Fertigungshalle. Die Struktur umfasst:

```json
{
  "produktionshalle": { "name": "...", "standort": "..." },
  "maschinen": [
    {
      "maschine_id": "CNC-01",
      "typ": "CNC-Drehmaschine",
      "ip_adresse": "192.168.10.100",
      "protokolle": ["Modbus TCP", "OPC UA"],
      "kommunikation": {
        "durchschnittliche_latenz_ms": 12,
        "pakete_pro_sekunde": 45,
        "fehlerrate_prozent": 0.1
      }
    },
    ...
  ]
}
```

**Aufgabe:**

Schreibe ein Python-Programm, das die JSON-Datei mit einem **Generator** verarbeitet und folgende Analysen durchführt:

**a) Generator-Funktion implementieren**

Erstelle eine Generator-Funktion `lies_maschinen(dateiname)`, die:
- Die JSON-Datei einliest
- Über die Liste `maschinen` iteriert
- Jede Maschine als Dictionary zurückgibt (mit `yield`)
- Bei Fehler eine aussagekräftige Fehlermeldung ausgibt

**b) Kommunikationsstatistik**

Berechne für jede Maschine:
- Maschinen-ID und Typ
- Durchschnittliche Latenz
- Paketrate (Pakete pro Sekunde)

**c) Protokoll-Analyse**

- Zähle, wie viele Maschinen welches Protokoll unterstützen
- Zeige die Protokolle mit Anzahl der Maschinen

**d) Performance-Bewertung**

- Identifiziere Maschinen mit Latenz > 15ms (als "langsam")
- Identifiziere Maschinen mit Fehlerrate > 0.15% (als "fehleranfällig")

**Anforderungen:**
- Nutze `json.load()` zum Einlesen
- Verwende `yield` für die Generator-Funktion
- Behandle FileNotFoundError und json.JSONDecodeError
- Formatiere Ausgaben übersichtlich

**Erwartete Ausgabe (Beispiel):**
```
=== Maschinenkommunikations-Analyse ===

Produktionshalle: Fertigungshalle A (Werk Stuttgart)

Maschinen-Übersicht:
  CNC-01 (CNC-Drehmaschine): Latenz 12ms, 45 Pakete/s
  CNC-02 (CNC-Fräsmaschine): Latenz 15ms, 42 Pakete/s
  Robot-01 (Industrieroboter): Latenz 10ms, 58 Pakete/s
  ...

Protokoll-Unterstützung:
  Modbus TCP: 7 Maschinen
  OPC UA: 6 Maschinen
  MQTT: 3 Maschinen
  EtherNet/IP: 2 Maschinen

Performance-Probleme:
  Langsame Maschinen (>15ms): Grinder-01 (22ms), Lathe-01 (20ms)
  Fehleranfällige Maschinen (>0.15%): Grinder-01 (0.30%), Lathe-01 (0.25%)
```

---

### Aufgabe P3: OPC UA-Datenstruktur-Analyse mit XML ⭐⭐ (Mittel)

**Datei:** `opc_ua_daten.xml`

Die XML-Datei enthält die Konfiguration eines OPC-UA-Servers mit Maschinenvariablen aus einer Produktionsanlage. Die Struktur umfasst:

```xml
<opc_ua_server>
  <server_info>...</server_info>
  <nodes>
    <node id="ns=2;i=1001">
      <browse_name>CNC_Maschine_01</browse_name>
      <variables>
        <variable id="ns=2;i=1101">
          <browse_name>Drehzahl</browse_name>
          <value>2450.5</value>
          <unit>U/min</unit>
        </variable>
      </variables>
    </node>
  </nodes>
</opc_ua_server>
```

**Aufgabe:**

Schreibe ein Python-Programm mit Generatoren, das die XML-Datei analysiert:

**a) Server-Informationen**
- Lies und zeige die Server-Informationen (Name, Vendor, Version, Endpoint)

**b) Maschinen-Variablen extrahieren**
- Erstelle eine Generator-Funktion, die über alle Knoten (nodes) iteriert
- Für jeden Knoten: Zeige Maschinenname (browse_name) und alle Variablen
- Format: Variable (Wert Einheit)

**c) Variablen-Statistik**
- Zähle die Gesamtanzahl der Knoten
- Zähle die Gesamtanzahl der Variablen
- Identifiziere alle Variablen mit Einheit "°C" (Temperatursensoren)

**Anforderungen:**
- Nutze `xml.etree.ElementTree` zum Parsen
- Verwende `.find()` und `.findall()` für Navigation
- Behandle fehlende Elemente mit try-except oder Existenzprüfungen
- Formatiere Ausgaben übersichtlich

**Erwartete Ausgabe (Beispiel):**
```
=== OPC UA-Server-Analyse ===

Server-Info:
  Name: Produktions-OPC-UA-Server
  Vendor: Siemens AG
  Endpoint: opc.tcp://192.168.10.200:4840

Maschinen und Variablen:
  CNC_Maschine_01:
    - Drehzahl: 2450.5 U/min
    - Vorschub: 0.25 mm/Umdrehung
    - Spindelleistung: 18.7 kW
    - Werkzeugtemperatur: 85.2 °C
    
  Fraesmaschine_01:
    - Spindeldrehzahl: 8500.0 U/min
    - Vorschubgeschwindigkeit: 1200.0 mm/min
    ...

Statistik:
  Anzahl Knoten: 5
  Anzahl Variablen: 27
  Temperatursensoren (°C): 6
```

---

### Aufgabe P4: Netzwerk-Latenz-Visualisierung mit Matplotlib ⭐⭐⭐ (Schwer)

**Kontext**: Du möchtest die Netzwerk-Performance in einer Produktionsanlage visualisieren, um Latenzmuster zu erkennen und Optimierungspotenziale zu identifizieren.

**Aufgabe:**

Schreibe ein Python-Programm, das **simulierte Latenz-Messungen** generiert und visualisiert:

**a) Daten-Generator erstellen**

Implementiere eine Generator-Funktion `generiere_latenz_messungen(anzahl, basis_latenz=15, varianz=10)`, die:
- `anzahl` Messwerte erzeugt (mit `yield`)
- Jeder Messwert ist ein Dictionary mit:
  - `timestamp`: Fortlaufende Sekunde (0, 1, 2, ...)
  - `latenz_ms`: Zufällige Latenz zwischen `basis_latenz ± varianz` (nutze `random.uniform()`)
  - `protokoll`: Zufällig eines von ["Modbus TCP", "MQTT", "OPC UA"]

**b) Daten sammeln und gruppieren**

- Generiere 300 Messwerte
- Gruppiere die Latenzen nach Protokoll (erstelle 3 Listen)

**c) Visualisierung mit Matplotlib**

Erstelle **zwei Subplots** nebeneinander:

1. **Liniendiagramm** (links):
   - X-Achse: Zeitstempel (Sekunden)
   - Y-Achse: Latenz (ms)
   - Zeige alle drei Protokolle in verschiedenen Farben
   - Legende, Titel "Latenz-Verlauf über Zeit"

2. **Boxplot** (rechts):
   - Vergleiche die Latenz-Verteilungen der drei Protokolle
   - Titel "Latenz-Verteilung nach Protokoll"

**d) Statistik-Ausgabe**

Berechne und zeige für jedes Protokoll:
- Durchschnittliche Latenz
- Minimale/Maximale Latenz
- Anzahl Messwerte > 25ms (kritisch)

**Anforderungen:**
- Nutze `random` für Zufallszahlen
- Nutze `matplotlib.pyplot` für Visualisierung
- Verwende `plt.subplots(1, 2)` für zwei Plots nebeneinander
- Speichere das Diagramm als `latenz_analyse.png`

**Beispiel-Ausgabe:**
```
=== Netzwerk-Latenz-Analyse ===

Modbus TCP:
  Ø Latenz: 14.8 ms
  Min: 5.2 ms | Max: 24.9 ms
  Kritische Messwerte (>25ms): 3

MQTT:
  Ø Latenz: 15.3 ms
  Min: 5.5 ms | Max: 25.1 ms
  Kritische Messwerte (>25ms): 4

OPC UA:
  Ø Latenz: 15.1 ms
  Min: 5.0 ms | Max: 24.8 ms
  Kritische Messwerte (>25ms): 2

✓ Diagramm gespeichert: latenz_analyse.png
```

**Lernziele**: Generator für Datenproduktion; Matplotlib für professionelle Visualisierungen; Datenanalyse mit mehreren Plots; Praktische Performance-Überwachung.

---

### Aufgabe P5: Produktionsdaten-Simulator mit Live-Monitoring ⭐⭐⭐⭐ (Sehr Schwer)

**Kontext**: Erstelle einen Simulator, der Produktionsdaten in Echtzeit generiert und visualisiert - ähnlich einem SCADA-Dashboard.

**Aufgabe:**

Implementiere einen **Echtzeit-Produktions-Simulator** mit Generator-Pipeline und Matplotlib:

**a) Produktionslinie-Generator**

Erstelle eine Generator-Funktion `simuliere_produktion(maschinen, dauer_sekunden)`, die:
- Für mehrere Maschinen Produktionsdaten simuliert
- Jede Sekunde einen Messwert pro Maschine erzeugt (mit `yield`)
- Messwerte enthalten:
  - `maschine_id`: Maschinenname
  - `timestamp`: Aktuelle Sekunde
  - `stueckzahl`: Zufällig 8-12 Stück/Sekunde
  - `temperatur_c`: Zufällig 70-95°C (mit Trend: steigt leicht über Zeit)
  - `ausschuss`: Zufällig 0-2% (gelegentlich Spitzen bis 8%)

**b) Datensammlung und Verarbeitung**

- Definiere 3 Maschinen: `["CNC-01", "Presse-01", "Robot-01"]`
- Simuliere 60 Sekunden Produktion
- Sammle alle Daten in einer Liste

**c) Multi-Plot-Dashboard**

Erstelle ein **2×2 Dashboard** mit 4 Subplots:

1. **Oben links**: Stückzahl über Zeit (Linien für alle 3 Maschinen)
2. **Oben rechts**: Temperatur über Zeit (mit Warnschwelle bei 90°C als horizontale Linie)
3. **Unten links**: Gesamtproduktion pro Maschine (Balkendiagramm)
4. **Unten rechts**: Ausschussrate über Zeit (gestapeltes Flächendiagramm mit `plt.fill_between()`)

**d) Produktionskennzahlen**

Berechne und zeige:
- Gesamtproduktion pro Maschine
- Durchschnittliche Temperatur pro Maschine
- Maschinen mit Temperatur-Überschreitungen (>90°C)
- Durchschnittliche Ausschussrate pro Maschine

**e) Alarm-System (Optional Bonus)**

- Markiere Zeitpunkte mit rotem Punkt, wo Temperatur > 90°C
- Gib Warnung aus, wenn Ausschussrate > 5%

**Anforderungen:**
- Nutze `random` für realistische Simulation
- Nutze `matplotlib.pyplot` mit `plt.subplots(2, 2)`
- Verwende `plt.tight_layout()` für besseres Layout
- Speichere Dashboard als `produktion_dashboard.png`

**Beispiel-Code-Struktur:**
```python
import random
import matplotlib.pyplot as plt

def simuliere_produktion(maschinen, dauer_sekunden):
    for sekunde in range(dauer_sekunden):
        for maschine in maschinen:
            # Trend: Temperatur steigt leicht
            basis_temp = 75 + (sekunde * 0.2)
            temp = basis_temp + random.uniform(-5, 5)
            
            yield {
                'maschine_id': maschine,
                'timestamp': sekunde,
                'stueckzahl': random.randint(8, 12),
                'temperatur_c': min(temp, 100),  # Max 100°C
                'ausschuss': random.uniform(0, 2) if random.random() > 0.1 else random.uniform(5, 8)
            }

# Hauptprogramm
maschinen = ["CNC-01", "Presse-01", "Robot-01"]
daten = list(simuliere_produktion(maschinen, 60))

# ... Datenverarbeitung und Plots
```

**Erwartete Ausgabe:**
```
=== Produktions-Monitoring (60 Sekunden) ===

Gesamtproduktion:
  CNC-01: 598 Stück (Ø Temp: 85.2°C, Ø Ausschuss: 2.1%)
  Presse-01: 612 Stück (Ø Temp: 84.8°C, Ø Ausschuss: 2.3%)
  Robot-01: 605 Stück (Ø Temp: 85.5°C, Ø Ausschuss: 1.9%)

⚠️  Temperatur-Warnungen:
  CNC-01: 3 Überschreitungen (>90°C)
  Presse-01: 2 Überschreitungen (>90°C)

✓ Dashboard gespeichert: produktion_dashboard.png
```

**Lernziele**: Komplexe Generator-Pipelines; Multi-Plot-Dashboards; Echtzeit-Datenvisualisierung; Alarm-Systeme; Praktische SCADA-Konzepte.

---

**Ende der Übungsaufgaben V15**

Die 5 Python-Aufgaben decken ab:
- **P1-P3**: Datenverarbeitung (CSV/JSON/XML) mit Generatoren
- **P4**: Visualisierung mit Matplotlib (Subplots, Boxplot)
- **P5**: Komplexe Simulation und Dashboard-Erstellung

Lösungen findest du in der Datei [V15-Netzwerktechnik-Grundlagen-Protokolle-Teil1_loesungen.md](V15-Netzwerktechnik-Grundlagen-Protokolle-Teil1_loesungen.md).

**Bonus (+⭐):** Erweitere die Pipeline um eine Funktion `error_burst_detection(dateiname, zeitfenster_sekunden=60, min_errors=3)`, die Zeiträume mit gehäuften ERROR-Meldungen findet (z.B. 3+ Errors innerhalb von 60 Sekunden).

---

### Aufgabe P6: Produktionsdaten-ETL mit Generator-Pipeline ⭐⭐⭐⭐ (Sehr Schwer)

Du arbeitest für ein Maschinenbau-Unternehmen und erhältst täglich eine große CSV-Datei `produktion_maschinen.csv` mit Produktionsdaten:

```csv
Maschine_ID,Schicht,Produkt_ID,Menge,Ausschuss,Zykluszeit_s,Timestamp,Status
M001,Frueh,P100,250,5,12.5,2024-01-15T06:00:00,completed
M002,Frueh,P101,180,3,18.2,2024-01-15T06:00:00,completed
M001,Frueh,P100,245,8,12.8,2024-01-15T07:00:00,warning
M003,Frueh,P102,320,1,9.5,2024-01-15T07:00:00,completed
M002,Spaet,P101,0,0,0,2024-01-15T14:00:00,malfunction
M001,Spaet,P100,260,4,12.3,2024-01-15T14:00:00,completed
```

**Aufgabe: Erstelle eine speicher-effiziente ETL-Pipeline (Extract, Transform, Load)**

**Teil 1: Extrahieren und Validieren**

Implementiere einen Generator `validiere_produktionsdaten(dateiname)`, der:
- CSV-Datei mit `csv.DictReader` liest
- Jede Produktionszeile validiert:
  - `Maschine_ID`, `Produkt_ID`, `Schicht` müssen vorhanden sein
  - `Menge`, `Ausschuss` müssen nicht-negative Ganzzahlen sein
  - `Zykluszeit_s` muss positive Dezimalzahl sein
  - `Timestamp` muss gültiges Datum sein (Format: ISO 8601)
  - `Status` muss einer der Werte sein: `completed`, `warning`, `malfunction`
- Nur **valide** Produktionsdaten als Dictionary zurückgibt
- **Fehlerhafte** Zeilen in separate Datei `validation_errors.log` schreibt (mit Fehlerbeschreibung)

**Teil 2: Transformieren**

Implementiere einen Generator `transformiere_produktionsdaten(daten)`, der:
- `Timestamp` von String zu `datetime`-Objekt konvertiert
- Neues Feld `Ausschussrate` berechnet: `(Ausschuss / Menge) * 100` in Prozent
- Neues Feld `OEE_Faktor` berechnet: Simplified OEE = `((Menge - Ausschuss) / Menge) * 100`
- Neues Feld `Stunde`, `Datum` aus `Timestamp` extrahiert
- Neues Feld `IstProblematisch` hinzufügt: `True` wenn `Status != "completed"` oder `Ausschussrate > 3%`

**Teil 3: Aggregieren**

Implementiere folgende Analyse-Funktionen:

1. **`produktion_pro_schicht(daten)`**:
   - Berechnet Gesamtproduktion (gute Stücke = Menge - Ausschuss) pro Schicht
   - Gibt Dictionary zurück: `{"Frueh": int, "Spaet": int, "Nacht": int}`

2. **`top_maschinen(daten, n=5)`**:
   - Findet die Top-N produktivsten Maschinen (höchste Gutmenge)
   - Gibt Liste von Tupeln: `[(Maschine_ID, Gutmenge, Durchschnitt_OEE), ...]`

3. **`problem_analyse(daten)`**:
   - Berechnet pro Maschine: Anzahl problematischer Zyklen, durchschnittliche Ausschussrate
   - Gibt Dictionary: `{Maschine_ID: {'probleme': int, 'avg_ausschuss': float}}`

**Teil 4: Laden (Exportieren)**

Implementiere `exportiere_produktionsbericht(input_datei, output_prefix)`, das:
- Die gesamte Pipeline durchläuft
- Drei neue CSV-Dateien erstellt:
  - `{output_prefix}_schicht_uebersicht.csv`: Produktionen pro Schicht
  - `{output_prefix}_top_maschinen.csv`: Beste Maschinen
  - `{output_prefix}_problem_bericht.csv`: Problemanalyse
- Alle Dateien mit `csv.DictWriter` schreibt (mit `newline=''`)

**Anforderungen:**
- **Speicher-Effizienz**: Datei wird nur **einmal** durchgelesen für alle Analysen (nutze `itertools.tee()` falls nötig)
- **Fehlertoleranz**: Einzelne fehlerhafte Zeilen stoppen nicht die gesamte Verarbeitung
- **Genauigkeit**: Nutze `decimal.Decimal` für Prozentsätze und OEE-Berechnungen
- **Performance**: Bei 100.000 Zeilen < 30 Sekunden
- **Logging**: Schreibe Statistiken (Anzahl verarbeitete/fehlerhafte Zeilen, Laufzeit)

**Beispiel-Nutzung:**
```python
exportiere_produktionsbericht("produktion_maschinen.csv", "bericht_2024_01_15")

# Erstellt:
# - bericht_2024_01_15_schicht_uebersicht.csv
# - bericht_2024_01_15_top_maschinen.csv
# - bericht_2024_01_15_problem_bericht.csv
# - validation_errors.log

# Konsolen-Ausgabe:
# Verarbeitung gestartet...
# ✓ 1.543 Produktionszyklen validiert
# ✗ 12 fehlerhafte Zeilen (siehe validation_errors.log)
# ✓ Export abgeschlossen
# Laufzeit: 0.85 Sekunden
# Durchschnittliche OEE: 96.5%
```

**Bonus (+⭐):** Implementiere eine Funktion `echtzeit_monitoring(dateiname, update_intervall_s=5)`, die:
- Die Produktionsdatei kontinuierlich überwacht
- Bei neuen Zeilen automatisch Warnungen ausgibt, wenn:
  - Ausschussrate > 5%
  - Zykluszeit > 20% über Durchschnitt
  - Status = "malfunction"

**Tipp:** Nutze `collections.defaultdict`, `itertools.tee()` und `decimal.Decimal` aus der Standard-Library.

