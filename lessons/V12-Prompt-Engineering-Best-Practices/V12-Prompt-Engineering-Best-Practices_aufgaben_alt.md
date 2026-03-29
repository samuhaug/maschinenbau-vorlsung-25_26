# V12: Übungsaufgaben - Prompt Engineering & Imports

> [!NOTE]
> Diese Übungsaufgaben vertiefen das Verständnis der Vorlesung V12.
> Bearbeite die Aufgaben in der angegebenen Reihenfolge.

---

## Teil A: Theorie-Aufgaben

### Aufgabe T1: Prompt-Anatomie analysieren (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 5-10 Minuten

Analysiere den folgenden Prompt und identifiziere die vier Kernkomponenten (Kontext, Aufgabe, Format, Constraints):

```
Du bist ein erfahrener Python-Entwickler. Erstelle eine Funktion zur 
Berechnung der Fakultät einer Zahl. Die Funktion soll Type Hints haben, 
einen Docstring im Google Style enthalten und rekursiv implementiert 
sein. Maximale Länge: 15 Zeilen.
```

**Fragen**:
1. Was ist der Kontext in diesem Prompt?
2. Was ist die konkrete Aufgabe?
3. Welches Format wird verlangt?
4. Welche Constraints sind definiert?

**Hinweise**:
- Überlege, welche Informationen dem Modell Hintergrund liefern
- Identifiziere die Aktion, die ausgeführt werden soll
- Achte auf strukturelle Anforderungen
- Finde alle Einschränkungen und Regeln

---

### Aufgabe T2: Prompt-Verbesserung (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 10-15 Minuten

Verbessere den folgenden vagen Prompt systematisch, indem du alle vier Komponenten ergänzt:

**Ursprünglicher Prompt**:
```
Erkläre Sortieralgorithmen.
```

**Aufgaben**:
1. Füge einen klaren Kontext hinzu (z.B. Rolle, Zielgruppe)
2. Präzisiere die Aufgabe
3. Definiere ein konkretes Format
4. Setze sinnvolle Constraints

Schreibe den verbesserten Prompt und erkläre kurz, warum jede Änderung den Prompt verbessert.

**Hinweise**:
- Denke an die SMART-Kriterien: Spezifisch, Messbar, Erreichbar, Relevant, Terminiert
- Berücksichtige verschiedene Lerntypen (visuell, textuell)
- Überlege, welche Informationen ein LLM benötigt, um präzise zu antworten

---

### Aufgabe T3: Few-Shot Learning Design (Schwer)

**Schwierigkeit**: ⭐⭐⭐ Schwer  
**Zeitaufwand**: ca. 15-25 Minuten

Entwerfe einen Few-Shot-Prompt für folgende Aufgabe:

**Ziel**: Ein LLM soll aus Kunden-Reviews automatisch extrahieren:
- Sentiment (positiv/neutral/negativ)
- Hauptthema (Produkt/Lieferung/Service/Preis)
- Handlungsempfehlung (keine/Antworten/Eskalieren)

**Aufgaben**:
1. Erstelle 3 repräsentative Beispiele (Few-Shot)
2. Jedes Beispiel sollte ein anderes Sentiment haben
3. Jedes Beispiel sollte alle drei Informationen demonstrieren
4. Formuliere den vollständigen Prompt mit Kontext, Aufgabe, Format und Constraints
5. Begründe kurz, warum du diese Beispiele gewählt hast

**Hinweise**:
- Beispiele sollten realistisch sein
- Decke verschiedene Edge Cases ab (z.B. gemischtes Sentiment)
- Achte auf konsistente Formatierung der Beispiele
- Überlege, welche Beispiele dem Modell helfen, die Aufgabe zu verallgemeinern

---

## Teil B: Python-Aufgaben

### Aufgabe P1: CNC-Maschinenparameter-Modul (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten  
**Vorkenntnisse**: Module, Funktionen  
**Maschinenbau-Kontext**: Berechnung von Schnittparametern für CNC-Maschinen

Erstelle ein Modul `cnc_parameter.py` mit Funktionen zur Berechnung wichtiger Schnittparameter:

1. `berechne_schnittgeschwindigkeit(durchmesser_mm: float, drehzahl_min: float) -> float`: Berechnet Schnittgeschwindigkeit vc in m/min mit Formel: vc = (π × d × n) / 1000
2. `berechne_vorschubgeschwindigkeit(drehzahl_min: float, vorschub_pro_umdrehung_mm: float) -> float`: Berechnet vf in mm/min mit Formel: vf = n × fz
3. `berechne_zeitspanvolumen(schnitttiefe_mm: float, schnittbreite_mm: float, vorschub_mm_min: float) -> float`: Berechnet Q in cm³/min mit Formel: Q = ap × ae × vf / 1000

**Anforderungen**:
- Jede Funktion hat Type Hints
- Jede Funktion hat einen einzeiligen Docstring
- Das Modul hat einen Modul-Docstring
- Erstelle dann eine `main.py`, die das Modul importiert und alle Funktionen mit Beispielwerten testet

**Beispiel Ein-/Ausgabe**:
```python
# main.py
import cnc_parameter

vc = cnc_parameter.berechne_schnittgeschwindigkeit(20.0, 1500.0)  # ~94.25 m/min
vf = cnc_parameter.berechne_vorschubgeschwindigkeit(1500.0, 0.1)  # 150.0 mm/min
Q = cnc_parameter.berechne_zeitspanvolumen(2.0, 10.0, 150.0)  # 3.0 cm³/min
```

**Hinweise**:
- π (Pi) kannst du mit `import math` und `math.pi` verwenden
- Modul-Docstring steht an erster Stelle in der Datei
- Verwende f-Strings für formatierte Ausgabe

---

### Aufgabe P2: Werkstoff-Rechner mit `if __name__ == "__main__":` (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: Module, `if __name__`  
**Maschinenbau-Kontext**: Festigkeitsberechnungen für Maschinenbauteile

Erstelle ein Modul `werkstoff_rechner.py` mit Funktionen zur Festigkeitsberechnung:

**Funktionen**:
- `berechne_spannung(kraft_n: float, flaeche_mm2: float) -> float`: Berechnet Spannung σ = F/A in MPa
- `berechne_dehnung(laenge_mm: float, laengenaenderung_mm: float) -> float`: Berechnet Dehnung ε = ΔL/L₀ (dimensionslos)
- `berechne_e_modul(spannung_mpa: float, dehnung: float) -> float`: Berechnet E-Modul E = σ/ε in GPa
- `berechne_sicherheitsfaktor(zugfestigkeit_mpa: float, betriebsspannung_mpa: float) -> float`: Berechnet S = Rm/σ

**Anforderungen**:
1. Jede Funktion hat Type Hints und Docstrings
2. Im `if __name__ == "__main__":`-Block:
   - Implementiere ein interaktives Berechnungsprogramm
   - Lese Kraft und Fläche vom Benutzer ein
   - Berechne und zeige Spannung
   - Frage nach Zugfestigkeit des Materials
   - Berechne und zeige Sicherheitsfaktor
3. Das Modul soll sowohl als Skript als auch als Bibliothek nutzbar sein
4. Behandle ZeroDivisionError für Division durch Null

**Beispiel Ausführung als Skript**:
```bash
$ python werkstoff_rechner.py
Kraft (N): 5000
Querschnittsfläche (mm²): 100
Spannung: 50.0 MPa
Zugfestigkeit des Materials (MPa): 250
Sicherheitsfaktor: 5.0
```

**Beispiel Import als Modul**:
```python
from werkstoff_rechner import berechne_spannung, berechne_sicherheitsfaktor
sigma = berechne_spannung(5000, 100)  # 50.0 MPa
S = berechne_sicherheitsfaktor(250, sigma)  # 5.0
```

---

### Aufgabe P3: Fertigungs-Tools-Package (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 20-30 Minuten  
**Vorkenntnisse**: Packages, `__init__.py`  
**Maschinenbau-Kontext**: Werkzeuge zur Fertigungsplanung und Qualitätssicherung

Erstelle ein Package `fertigungs_tools` mit folgender Struktur:

```
fertigungs_tools/
├── __init__.py
├── toleranzen.py
└── kosten.py
```

**`toleranzen.py`**:
- `pruefe_toleranz(ist_wert: float, soll_wert: float, toleranz: float) -> bool`: Prüft ob |Ist - Soll| ≤ Toleranz
- `berechne_passungsart(bohrung_mm: float, welle_mm: float) -> str`: Gibt "Übermaß", "Spiel" oder "Übergangspassung" zurück

**`kosten.py`**:
- `berechne_fertigungskosten(stueckzahl: int, stueckkosten_eur: float, ruestkosten_eur: float) -> float`: K = n × k + Kr
- `berechne_stueckpreis(gesamtkosten_eur: float, stueckzahl: int) -> float`: p = K/n

**`__init__.py`**:
- Importiere alle Funktionen, sodass sie direkt aus `fertigungs_tools` importiert werden können

**Hauptprogramm `main.py`**:
- Teste alle Funktionen mit Beispielwerten

**Beispiel Ein-/Ausgabe**:
```python
from fertigungs_tools import pruefe_toleranz, berechne_fertigungskosten

ist_ok = pruefe_toleranz(50.2, 50.0, 0.5)  # True
kosten = berechne_fertigungskosten(100, 15.0, 500.0)  # 2000.0 EUR
```

**Hinweise**:
- Passungsart: Wenn Bohrung > Welle: "Spiel", Bohrung < Welle: "Übermaß", sonst "Übergangspassung"
- Relativer Import in `__init__.py`: `from .toleranzen import ...`

---

### Aufgabe P4: Produktionsdaten-Verarbeitung mit relativen/absoluten Imports (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 30-40 Minuten  
**Vorkenntnisse**: Packages, relative Imports  
**Maschinenbau-Kontext**: Analyse von Produktionsdaten und Qualitätsmetriken

Erstelle eine Package-Hierarchie für Produktionsdatenverarbeitung:

**Struktur**:
```
produktionsdaten/
├── __init__.py
├── io/
│   ├── __init__.py
│   ├── reader.py
│   └── writer.py
└── analyse/
    ├── __init__.py
    ├── qualitaet.py
    └── oee.py
```

**Implementierung**:

**`io/reader.py`**:
- `lese_produktionsdaten(dateiname: str) -> list[dict]`: Liest CSV-Format (Zeit,Stueckzahl,Ausschuss)

**`io/writer.py`**:
- `schreibe_bericht(dateiname: str, daten: str) -> None`: Schreibt Bericht in Datei

**`analyse/qualitaet.py`**:
- `berechne_ausschussquote(gesamt: int, ausschuss: int) -> float`: Quote = (Ausschuss/Gesamt) × 100

**`analyse/oee.py`**:
- Importiere `berechne_ausschussquote` aus `qualitaet.py` mit **relativem Import**
- `berechne_oee(verfuegbarkeit: float, leistung: float, qualitaet: float) -> float`: OEE = V × L × Q / 1000000
- `berechne_qualitaetsrate(gesamt: int, ausschuss: int) -> float`: Q = (1 - Ausschussquote/100) × 100

**Hauptprogramm `main.py`**:
- Nutze **absolute Imports** aus dem Package
- Erstelle Test-CSV mit Produktionsdaten
- Lese Daten ein
- Berechne Ausschussquote und OEE
- Schreibe Bericht

**Anforderungen**:
1. `oee.py` nutzt relative Imports für `qualitaet.py`
2. `main.py` nutzt absolute Imports
3. Alle Funktionen haben Type Hints und Docstrings
4. Implementiere Error Handling (FileNotFoundError)

**Hinweise**:
- Relativer Import in `oee.py`: `from .qualitaet import berechne_ausschussquote`
- Absoluter Import in `main.py`: `from produktionsdaten.io.reader import lese_produktionsdaten`
- CSV-Format: Einfaches Format mit `split(',')` verarbeiten

---

### Aufgabe P5: CNC-Überwachungs-CLI mit venv und Dependencies (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 45-60 Minuten  
**Vorkenntnisse**: venv, pip, Module, Error Handling  
**Maschinenbau-Kontext**: Echtzeit-Überwachung von CNC-Maschinenparametern

Erstelle ein CLI-Tool zur Überwachung von CNC-Maschinendaten.

**Projekt: CNC-Monitor-CLI**

**Ziel**: Ein Kommandozeilen-Tool, das Maschinendaten abruft, analysiert und formatiert ausgibt.

**Anforderungen**:

**1. Projekt-Struktur**:
```
cnc_monitor/
├── venv/  (gitignored)
├── cnc_monitor/
│   ├── __init__.py
│   ├── sensor.py
│   ├── analyzer.py
│   └── cli.py
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
```

**2. Implementierung**:

**`cnc_monitor/sensor.py`**:
- Funktion `lese_maschinendaten(maschinen_id: str) -> dict`: Gibt Mock-Daten zurück (Temperatur, Drehzahl, Vibration, Werkzeugverschleiß)
- Mock-Daten Format: `{"id": maschinen_id, "temperatur_c": 65, "drehzahl_rpm": 1200, "vibration_mm_s": 2.5, "werkzeugverschleiss_prozent": 35}`

**`cnc_monitor/analyzer.py`**:
- Funktion `analysiere_zustand(daten: dict) -> str`: Gibt Zustandsbewertung zurück ("OK", "Warnung", "Kritisch") basierend auf Grenzwerten
- Grenzwerte: Temp > 80°C = Warnung, Temp > 90°C = Kritisch; Vibration > 5 mm/s = Warnung; Verschleiß > 80% = Warnung

**`cnc_monitor/cli.py`**:
- Funktion `main()`: Hauptlogik für CLI
- Nutze `argparse` für Kommandozeilen-Argumente
- Argumente: `--maschine` (erforderlich), `--format` (text/json, optional, default: text)

**`main.py`**:
- Einstiegspunkt: Ruft `cli.main()` auf mit `if __name__ == "__main__":`

**`requirements.txt`**:
- Keine externen Dependencies nötig (nur Standard-Library)

**`.gitignore`**:
- `venv/`, `__pycache__/`, `*.pyc`

**`README.md`**:
- Setup-Anweisungen (venv erstellen, Nutzung)

**3. Schritte**:
1. Erstelle virtuelle Umgebung: `python -m venv venv`
2. Aktiviere venv
3. Implementiere alle Module
4. Teste: `python main.py --maschine CNC-001`

**Beispiel Ein-/Ausgabe**:
```bash
$ python main.py --maschine CNC-Fräse-001
╔════════════════════════════════════════╗
║  CNC-Maschinenüberwachung              ║
╠════════════════════════════════════════╣
║  Maschine: CNC-Fräse-001               ║
║  Temperatur: 65°C                      ║
║  Drehzahl: 1200 U/min                  ║
║  Vibration: 2.5 mm/s                   ║
║  Werkzeugverschleiß: 35%               ║
║  Status: ✅ OK                         ║
╚════════════════════════════════════════╝
```

**Hinweise**:
- Mock-Sensordaten: Einfach ein Dictionary zurückgeben, keine echte Hardware-Anbindung
- `argparse` ist Teil der Standard Library
- Formatierung mit Box-Drawing-Characters wie in V11
