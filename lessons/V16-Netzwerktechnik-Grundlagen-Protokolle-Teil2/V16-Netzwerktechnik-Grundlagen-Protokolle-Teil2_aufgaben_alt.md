# V16: Netzwerktechnik Grundlagen & Protokolle – Teil 2 - Übungsaufgaben

---

## Theorieaufgaben

### Aufgabe T1: TCP vs. UDP - Protokollauswahl (⭐)

**Kontext**: Ein Unternehmen plant verschiedene Netzwerkanwendungen und muss entscheiden, welches Transportprotokoll (TCP oder UDP) jeweils am besten geeignet ist.

**Aufgabenstellung**:

Analysiere die folgenden Anwendungsfälle und entscheide begründet, ob TCP oder UDP die bessere Wahl ist. Erkläre jeweils in 2-3 Sätzen, warum.

a) **Online-Banking-Anwendung**: Kunden können Überweisungen tätigen und ihren Kontostand abfragen.

b) **Video-Streaming-Plattform**: Benutzer schauen Live-Sportübertragungen.

c) **Firmendatenbank-Backup**: Nächtliche Sicherung von 500 GB Unternehmensdaten auf einen Remote-Server.

d) **VoIP-Telefonie**: Mitarbeiter führen Sprachtelefonate über das Netzwerk.

e) **IoT-Sensoren**: 1000 Temperatursensoren in einer Produktionshalle senden alle 5 Sekunden Messwerte an einen zentralen Server.

**Lernziele**: Verständnis der Unterschiede zwischen TCP und UDP; Fähigkeit, das passende Protokoll für konkrete Anwendungsfälle auszuwählen.

---

### Aufgabe T2: REST-API Design (⭐⭐)

**Kontext**: Du entwickelst eine REST-API für ein Bibliothekssystem. Die API soll die Verwaltung von Büchern, Autoren und Ausleihen ermöglichen.

**Aufgabenstellung**:

Entwirf RESTful API-Endpunkte für die folgenden Operationen. Gib jeweils die **HTTP-Methode**, die **URI** und den erwarteten **HTTP-Statuscode bei Erfolg** an.

a) Alle Bücher abrufen

b) Details eines spezifischen Buches mit ID 42 abrufen

c) Ein neues Buch hinzufügen

d) Die Informationen eines Buches mit ID 42 vollständig aktualisieren

e) Ein Buch mit ID 42 löschen

f) Alle Bücher eines bestimmten Autors (Autor-ID 7) abrufen

g) Ein Buch (ID 42) an einen Benutzer (ID 123) ausleihen (Erstellen einer neuen Ausleihe)

**Zusatzfrage**: Welche REST-Prinzipien (von den 6 Hauptprinzipien) werden durch dein API-Design besonders gut erfüllt? Nenne mindestens zwei und erkläre kurz.

**Lernziele**: Verständnis der REST-Prinzipien; Fähigkeit, RESTful API-Endpunkte zu entwerfen; Korrekte Verwendung von HTTP-Methoden und Statuscodes.

---

### Aufgabe T3: DNS-Auflösung verstehen (⭐⭐⭐)

**Kontext**: Ein Benutzer gibt `https://shop.example.com/products` in seinen Browser ein. Der lokale DNS-Cache ist leer. Der DNS-Resolver des ISP hat ebenfalls keinen Eintrag für diese Domain.

**Aufgabenstellung**:

a) **DNS-Auflösung nachvollziehen**: Beschreibe Schritt für Schritt, wie die DNS-Auflösung für `shop.example.com` abläuft. Erkläre, welche DNS-Server (Root, TLD, Authoritative) nacheinander kontaktiert werden und welche Informationen jeweils zurückgegeben werden.

b) **DNS-Record-Typen**: Angenommen, die DNS-Zone für `example.com` enthält folgende Records:

```
example.com.          IN  A      93.184.216.34
www.example.com.      IN  CNAME  example.com.
shop.example.com.     IN  A      203.0.113.50
mail.example.com.     IN  A      203.0.113.100
example.com.          IN  MX     10 mail.example.com.
example.com.          IN  NS     ns1.example.com.
example.com.          IN  NS     ns2.example.com.
```

Beantworte folgende Fragen:
- Welche IP-Adresse erhält der Browser für `shop.example.com`?
- Wenn ein Benutzer `www.example.com` anfragt, welche Antwort erhält er vom DNS-Server? Erkläre, wie CNAME-Records funktionieren.
- An welchen Server werden E-Mails für `admin@example.com` zugestellt?
- Was ist die Funktion der NS-Records?

c) **Caching und TTL**: Die A-Records haben eine TTL (Time To Live) von 300 Sekunden. Erkläre, was das bedeutet und welche Auswirkungen eine zu kurze oder zu lange TTL haben kann.

**Lernziele**: Tiefes Verständnis der DNS-Auflösung; Kenntnis verschiedener DNS-Record-Typen; Verständnis von DNS-Caching und TTL.

---

## Python-Aufgaben

> [!NOTE]
> Für alle Python-Aufgaben gilt: Verwende **Pandas** für die Datenverarbeitung. Achte auf **Vektorisierung** statt Schleifen, wo möglich, um gute Performance zu erreichen.

---

### Aufgabe P1: Pandas-Grundlagen - Sensordaten einlesen und erkunden (⭐)

**Kontext**: Eine Produktionsanlage hat mehrere Sensoren installiert, die kontinuierlich Betriebsdaten aufzeichnen. Die Sensordaten wurden bereits in einer CSV-Datei gesammelt. Deine Aufgabe ist es, die Daten einzulesen und einen ersten Überblick zu gewinnen.

**Datensatz** (`sensoren_daten.csv` - 15 Zeilen verfügbar im Ordner):

Die CSV-Datei enthält folgende Spalten:
```
Sensor_ID,Sensor_Name,Typ,Position,Temperatur_C,Vibration_mm_s,Druck_bar,Letztwartung,Status
```

**Aufgabenstellung**:

a) Lies die CSV-Datei `sensoren_daten.csv` mit Pandas ein und speichere den DataFrame in der Variable `df`.

b) Zeige die **ersten 3 Zeilen** des DataFrames an.

c) Zeige **detaillierte Informationen** über den DataFrame an (Datentypen, fehlende Werte, Speicherverbrauch).

d) Berechne **deskriptive Statistiken** für numerische Spalten (Mittelwert, Standardabweichung, Min, Max, Quartile).

e) Wie viele **Zeilen und Spalten** hat der DataFrame?

f) Welche **Spaltennamen** existieren?

g) Konvertiere die Spalte `Letztwartung` in den Datentyp **datetime**.

**Lernziele**: CSV-Dateien einlesen; DataFrame inspizieren; Basis-Methoden anwenden; Zeitstempel-Konvertierung.

---

### Aufgabe P2: Qualitätskontrolle - Filtern und Sortieren (⭐⭐)

**Kontext**: Die Qualitätsabteilung möchte die Sensordaten filtern, um potenzielle Probleme zu identifizieren. Verwende den DataFrame aus Aufgabe P1.

**Aufgabenstellung**:

a) **Filter 1**: Zeige alle Sensoren der Maschine **"CNC-01"**.

b) **Filter 2**: Zeige alle Sensormessungen mit **Wert > 100** (unabhängig von der Einheit).

c) **Filter 3**: Zeige alle Temperatursensoren, die zwischen **70°C und 90°C** messen (inklusive).

d) **Kombinierter Filter**: Zeige alle Drucksensoren (Typ = "Druck"), die einen Wert **größer als 145 bar** haben.

e) **Filter mit `.isin()`**: Zeige alle Sensoren der Maschinen **"CNC-01"** oder **"CNC-02"**.

f) **Sortierung 1**: Sortiere den DataFrame nach **Wert** (absteigend) und zeige das Ergebnis an.

g) **Sortierung 2**: Sortiere den DataFrame nach **Maschine** (alphabetisch aufsteigend) und innerhalb jeder Maschine nach **Wert** (absteigend).

h) **Qualitätskontrolle**: Filtere alle Einträge mit Status **"Warnung"** und sortiere nach Wert (höchste zuerst).

**Lernziele**: Filtern mit Bedingungen; Kombinierte Bedingungen mit `&`, `|`; Sortieren nach einer oder mehreren Spalten; Praktische Qualitätskontrolle.

---

### Aufgabe P3: Wartungsplanung - Aggregation und Gruppierung (⭐⭐⭐)

**Kontext**: Die Wartungsabteilung möchte Statistiken pro Maschine erstellen. Verwende den DataFrame aus Aufgabe P1.

**Datensatz erweitern** - Füge weitere Zeilen hinzu für statistische Relevanz:
```csv
S009,CNC-01,Schwingung,0.8,mm/s,2024-01-15 08:00:00,Normal
S010,Presse-01,Schwingung,1.2,mm/s,2024-01-15 08:00:00,Warnung
S011,CNC-02,Schwingung,0.5,mm/s,2024-01-15 08:00:00,Normal
S012,Presse-02,Schwingung,0.9,mm/s,2024-01-15 08:00:00,Normal
```

**Aufgabenstellung**:

a) Berechne den **durchschnittlichen Wert** aller Sensoren.

b) Berechne den **durchschnittlichen Wert pro Maschine**.

c) Finde den **höchsten Wert pro Maschine**.

d) Zähle, wie viele **Sensoren pro Maschine** installiert sind.

e) Erstelle eine **Wartungsübersicht** pro Maschine, die folgende Informationen enthält:
   - Anzahl der Sensoren
   - Durchschnittlicher Wert
   - Minimaler Wert
   - Maximaler Wert
   - Anzahl Warnungen (Status = "Warnung")

f) Welche Maschine hat die **höchste Anzahl an Warnungen**?

g) **Bonus-Challenge**: Berechne die durchschnittliche Temperatur pro Maschine und zeige nur Maschinen, deren Durchschnittstemperatur **über 80°C** liegt.

**Lernziele**: Aggregatfunktionen anwenden; `.groupby()` verwenden; Mehrfache Aggregationen mit `.agg()`; Wartungsrelevante Statistiken erstellen.

---

### Aufgabe P4: Performance-Optimierung - Maschinenlaufzeit-Berechnung (⭐⭐⭐)

**Kontext**: Eine Produktionsanlage zeichnet Zyklusdaten auf. Du möchtest die Gesamtlaufzeit berechnen und Performance-Unterschiede zwischen Schleifen und Vektorisierung demonstrieren.

**Aufgabenstellung**:

a) Erstelle einen DataFrame mit **100.000 Zeilen** und folgenden Spalten:
   - `Maschine_ID`: Zufällige IDs von 1 bis 50 (verwende `numpy.random.randint()`)
   - `Zykluszeit_s`: Zufällige Zykluszeiten zwischen 10 und 120 Sekunden
   - `Ausschuss`: Zufällige Ausschusszahlen zwischen 0 und 5

b) **Methode 1 (LANGSAM)**: Berechne die **Netto-Zykluszeit** ((Zykluszeit_s × (100 - Ausschuss)) / 100) mit einer **for-Schleife** über alle Zeilen (`.iterrows()`). Messe die benötigte Zeit mit `time.time()`.

c) **Methode 2 (SCHNELL)**: Berechne die **Netto-Zykluszeit** mit **Vektorisierung** (direkte Spaltenoperation). Messe die benötigte Zeit.

d) Vergleiche die Laufzeiten und berechne, um welchen **Faktor** die Vektorisierung schneller ist.

e) **Zusatzfrage**: Erkläre in 2-3 Sätzen, warum Vektorisierung in Pandas/NumPy so viel schneller ist als Python-Schleifen.

f) **Bonus**: Berechne die durchschnittliche Netto-Zykluszeit pro Maschine mit vektorisierten Operationen und finde die effizienteste Maschine.

**Lernziele**: Verstehen, warum Schleifen in Pandas langsam sind; Vektorisierung anwenden; Performance messen und vergleichen; Praktische Produktionskennzahlen berechnen.

---

### Aufgabe P5: Produktionsplanung - Auftragsanalyse-Dashboard (⭐⭐⭐⭐)

**Kontext**: Ein Maschinenbau-Unternehmen fertigt verschiedene Bauteile. Die Produktionsdaten wurden bereits in einer CSV-Datei gesammelt. Du sollst ein Analyse-Dashboard mit Pandas erstellen, um Produktionseffizienz zu überwachen.

**Datensatz** (`produktion_auftrage.csv` - verfügbar im Ordner):

Die CSV-Datei enthält folgende Spalten:
```
Auftrag_ID,Maschine,Bauteil,Zielmenge,Produziert,Ausschuss,Zykluszeit_s,Datum,Status
```

Beispiel-Einträge:
```csv
A0001,CNC-01,Welle-A,100,98,2,12.5,2024-01-15,Abgeschlossen
A0002,CNC-02,Flansch-B,200,195,5,8.3,2024-01-15,Abgeschlossen
...
```

**Aufgabenstellung**:

a) Lies die CSV-Datei `produktion_auftrage.csv` mit Pandas ein. Konvertiere die Spalte `Datum` in datetime.

b) Füge folgende neue Spalten hinzu:
   - **`Ausschussrate`**: (Ausschuss / Zielmenge) × 100 in Prozent
   - **`Gutmenge`**: Produziert - Ausschuss
   - **`OEE_Availability`**: (Produziert / Zielmenge) × 100 (vereinfachte OEE-Kennzahl)

c) **Analyse 1 - Gesamtproduktion**: Berechne die **Gesamtgutmenge** aller abgeschlossenen Aufträge. Ignoriere verzögerte Aufträge.

d) **Analyse 2 - Top-Maschinen**: Welche 3 Maschinen haben die **höchste Gutmenge** produziert? Zeige Maschine und Gutmenge.

e) **Analyse 3 - Bauteile**: Welches **Bauteil** hat die höchste Gesamtproduktionsmenge? Zeige Bauteil, Gesamtproduktion und durchschnittliche Ausschussrate.

f) **Analyse 4 - Zeitreihe**: Berechne die **tägliche Gutmenge** (nur abgeschlossene Aufträge) und zeige das Ergebnis als Tabelle.

g) **Analyse 5 - Qualitätskontrolle**: Wie viele Aufträge haben eine Ausschussrate **> 5%**? Liste diese Aufträge auf.

h) **Analyse 6 - Effizienz**: Welche Maschine hat die **beste durchschnittliche OEE_Availability**? Zeige Top 3 Maschinen mit ihren OEE-Werten.

i) **Bonus - Visualisierung**: Falls du Matplotlib kennst (aus V13/V14), erstelle ein **Balkendiagramm**, das die Gutmenge pro Maschine zeigt.

**Lernziele**: Komplette Produktionsdatenanalyse durchführen; OEE-Kennzahlen berechnen; Daten filtern, gruppieren und aggregieren; Mehrere Analysen kombinieren; Praktisches Anwendungsbeispiel aus dem Maschinenbau.

---

**Ende der Übungsaufgaben V16**

Die Lösungen zu diesen Aufgaben findest du in der Datei [V16-Netzwerktechnik-Grundlagen-Protokolle-Teil2_loesungen.md](V16-Netzwerktechnik-Grundlagen-Protokolle-Teil2_loesungen.md).