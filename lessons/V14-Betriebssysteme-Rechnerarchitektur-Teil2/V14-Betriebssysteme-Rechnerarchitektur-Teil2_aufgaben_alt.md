# V14 - Betriebssysteme & Rechnerarchitektur – Teil 2 / Plots & Grafiken (Matplotlib) – Teil 2: Aufgaben

---

## Teil 1: Theorie-Aufgaben

### T1: Prozessverwaltung und Scheduling (⭐⭐)

Ein Betriebssystem muss folgende **vier Prozesse** schedulen. Gegeben sind die Ankunftszeit und die Burst-Time (benötigte CPU-Zeit):

| Prozess | Ankunft (ms) | Burst (ms) |
|---------|--------------|------------|
| P1      | 0            | 8          |
| P2      | 1            | 4          |
| P3      | 2            | 9          |
| P4      | 3            | 5          |

**Aufgaben:**

a) Erstellen Sie einen **Gantt-Chart** für **First-Come First-Served (FCFS)** Scheduling. Berechnen Sie die durchschnittliche **Wartezeit** und **Turnaround-Zeit**.

b) Erstellen Sie einen **Gantt-Chart** für **Shortest Job First (SJF)** (nicht-preemptiv). Berechnen Sie die durchschnittliche **Wartezeit** und **Turnaround-Zeit**.

c) Vergleichen Sie die Ergebnisse aus (a) und (b). Welcher Algorithmus ist effizienter und warum?

d) Nennen Sie **einen Nachteil** von SJF, der in der Praxis problematisch ist.

---

### T2: Virtueller Speicher und Paging (⭐⭐⭐)

Ein System verwendet **Paging** mit folgenden Eigenschaften:
- **Virtuelle Adressbreite**: 16 Bit
- **Page-Größe**: 1 KB (= 1024 Bytes)
- **Physischer Speicher**: 8 KB

**Page Table** für Prozess A:

| Virtuelle Page | Frame | Valid Bit |
|----------------|-------|-----------|
| 0              | 3     | 1         |
| 1              | 1     | 1         |
| 2              | -     | 0         |
| 3              | 5     | 1         |
| 4              | 2     | 1         |

**Aufgaben:**

a) Berechnen Sie die **Anzahl der virtuellen Pages** und die **Anzahl der physischen Frames** in diesem System.

b) Der Prozess greift auf die **virtuelle Adresse 0x0A50** (hexadezimal) zu. 
   - Berechnen Sie **Page Number** und **Offset**.
   - Bestimmen Sie die **physische Adresse** (hexadezimal).
   - Zeigen Sie die Umrechnung Schritt für Schritt.

c) Der Prozess greift auf die **virtuelle Adresse 0x0820** zu. Was passiert und warum? Welche Rolle spielt das Valid Bit?

d) Erklären Sie, warum **Paging** das **externe Fragmentierungsproblem** löst, aber **interne Fragmentierung** verursachen kann.

---

### T3: Dateisysteme und Journaling (⭐⭐)

**Situation**: Ein Linux-Server stürzt während eines Schreibvorgangs ab. Das Dateisystem ist **ext4** (mit Journaling).

**Aufgaben:**

a) Erklären Sie in **3-5 Sätzen**, wie **Journaling** funktioniert und welche Schritte das Dateisystem durchläuft, um Konsistenz zu gewährleisten.

b) **Vergleichen Sie** die drei Journaling-Modi von ext4:
   - **Journal**: Was wird geloggt?
   - **Ordered**: Was wird geloggt?
   - **Writeback**: Was wird geloggt?
   
   Ordnen Sie die Modi nach **Sicherheit** (höchste zuerst) und **Performance** (schnellste zuerst).

c) Nennen Sie **zwei moderne Dateisysteme** (außer ext4) und jeweils **eine Besonderheit**:
   - Beispiel: NTFS – verwendet Master File Table (MFT)

---

## Teil 2: Python-Aufgaben

### P1: Bar Chart - CNC-Maschinenpräzision visualisieren (⭐⭐)

Eine Qualitätskontrolle hat die **Positioniergenauigkeit** verschiedener CNC-Maschinen über einen Produktionstag gemessen. Die Daten liegen in der Datei **`cnc_praezision.csv`** vor.

**Aufgabe:**

a) Laden Sie die Daten aus `cnc_praezision.csv`:
```python
import pandas as pd
import matplotlib.pyplot as plt

daten = pd.read_csv('cnc_praezision.csv')
```

b) Berechnen Sie für jede Maschine die **durchschnittliche Gesamt-Abweichung**:
   - Formel: `gesamt_abweichung = sqrt(X² + Y² + Z²)` mit den drei Abweichungskomponenten
   - Verwenden Sie NumPy für die Berechnung

c) Erstellen Sie einen **Bar Chart**, der:
- Die ersten 10 Maschinen auf der X-Achse zeigt
- Die berechnete Gesamt-Abweichung (μm) auf der Y-Achse zeigt
- Balken **farbcodiert nach Toleranz**:
  - Grün: Abweichung ≤ 5 μm (innerhalb Toleranz)
  - Orange: 5 μm < Abweichung ≤ 10 μm (Warnung)
  - Rot: Abweichung > 10 μm (außerhalb Toleranz)
- Einen passenden **Titel** und **Achsenbeschriftungen** hat
- Ein **Gitter** auf der Y-Achse zeigt (`alpha=0.3`)

d) Fügen Sie eine **horizontale Linie** bei 5 μm (Toleranzgrenze) hinzu.

---

### P2: Histogramm - Hydraulikdruck-Schwankungen analysieren (⭐⭐)

Eine Hydraulikanlage hat **1000 Druckmessungen** während eines Produktionszyklus aufgezeichnet. Die Drücke (in bar) sind normalverteilt mit Mittelwert 180 bar und Standardabweichung 12 bar.

**Aufgabe:**

a) Generieren Sie die Daten mit NumPy:
```python
import numpy as np
np.random.seed(42)
druecke_bar = np.random.normal(180, 12, 1000)
```

b) Erstellen Sie ein **Histogramm** mit:
- 30 Bins
- Hellblauer Füllfarbe (`'lightblue'`)
- Schwarzen Rändern (`edgecolor='black'`)
- Titel: "Verteilung der Hydraulikdruck-Schwankungen"
- X-Achse: "Druck (bar)"
- Y-Achse: "Häufigkeit"
- Gitter auf der Y-Achse

c) Fügen Sie zwei **vertikale Linien** hinzu:
- Eine grüne gestrichelte Linie bei **Solldruck** (180 bar) mit Label "Solldruck"
- Eine rote gestrichelte Linie bei **Maximal zulässiger Druck** (204 bar = Mittelwert + 2×Standardabweichung) mit Label "Kritische Grenze"

d) Zeigen Sie eine **Legende** an.

---

### P3: Box Plots - Material-Festigkeits-Vergleich (⭐⭐⭐)

Vergleichen Sie die **Zugfestigkeit** verschiedener Stahl-Werkstoffe basierend auf Materialprüfungs-Daten aus der Datei **`werkstoff_pruefung.json`**.

**Aufgabe:**

a) Laden Sie die Daten aus `werkstoff_pruefung.json`:
```python
import json
import matplotlib.pyplot as plt

with open('werkstoff_pruefung.json', 'r', encoding='utf-8') as file:
    pruef_daten = json.load(file)
```

b) Gruppieren Sie die Zugfestigkeitswerte nach **Werkstoff-Typ**:
   - Extrahieren Sie alle Proben aus `pruef_daten['proben']`
   - Erstellen Sie ein Dictionary, das Werkstoff-Namen (z.B. "S235JR", "C45E") auf Listen von Zugfestigkeitswerten abbildet
   - Beispiel: `{'S235JR': [412, 425], 'C45E': [682, 695], ...}`

c) Erstellen Sie **Box Plots** zum Vergleich:
   - X-Achse: Werkstoff-Namen
   - Y-Achse: Zugfestigkeit (MPa)
   - Färben Sie die Boxen unterschiedlich (z.B. 'lightblue', 'lightgreen', 'lightyellow', etc.)
   - Zeigen Sie Ausreißer als rote Punkte
   - Titel: "Zugfestigkeit: Vergleich verschiedener Stahl-Werkstoffe"
   - X-Achse Beschriftung: "Werkstoff"
   - Y-Achse Beschriftung: "Zugfestigkeit (MPa)"
   - Gitter auf der Y-Achse

d) Fügen Sie eine **horizontale Linie** bei 500 MPa hinzu (Referenzwert für mittlere Festigkeit) mit Label "Referenz: 500 MPa"

e) Ergänzen Sie die Visualisierung mit:
   - Medianwert-Annotation über jeder Box
   - Legende für die Referenzlinie
   - Rotation der X-Achsen-Labels um 45° für bessere Lesbarkeit

---

### P4: Logarithmische Achsen - Werkzeugstandzeit-Analyse (⭐⭐⭐)

Eine Verschleißanalyse misst die **Werkzeugstandzeit** für verschiedene **Schnittgeschwindigkeiten** bei unterschiedlichen Werkzeugen:

```python
import numpy as np
import matplotlib.pyplot as plt

schnittgeschw_m_min = np.array([50, 100, 200, 400, 800])  # m/min
standzeit_min = np.array([720, 180, 45, 11, 3])  # Minuten (Taylor-Gleichung)
labels = ['HSS niedrig', 'HSS hoch', 'HM niedrig', 'HM hoch', 'Keramik']
```

**Aufgabe:**

a) Erstellen Sie einen **Plot mit logarithmischen Achsen** (log-log):
   - X-Achse: Schnittgeschwindigkeit (m/min) – logarithmisch
   - Y-Achse: Werkzeugstandzeit (min) – logarithmisch
   - Verwenden Sie rote Kreise als Marker (`'ro'`) mit `markersize=10`
   - Verbinden Sie Punkte mit gestrichelter Linie (`linestyle='--'`)

b) Beschriften Sie jeden Punkt mit dem entsprechenden Label aus der `labels`-Liste:
   - Verwenden Sie `plt.text()` oder `plt.annotate()`
   - Position: rechts neben jedem Punkt
   - Schriftgröße: 10

c) Fügen Sie hinzu:
   - Titel: "Werkzeugverschleiß: Schnittgeschwindigkeit vs. Standzeit (Taylor-Gleichung)"
   - X-Achse: "Schnittgeschwindigkeit (m/min, log)"
   - Y-Achse: "Werkzeugstandzeit (min, log)"
   - Gitter mit `alpha=0.3`

d) Erklären Sie in einem **Kommentar**, warum logarithmische Achsen hier sinnvoll sind (Hinweis: Taylor-Gleichung vc × T^n = konstant).

---

###P5: Radar/Polar Chart - Produktionslinien-Vergleich (⭐⭐⭐⭐)

Erstellen Sie eine **Radar-Chart-Visualisierung** zum Vergleich von 5 Produktionslinien basierend auf Daten aus der Datei **`produktionslinien_vergleich.xml`**.

**Aufgabe:**

a) Laden Sie die Daten aus `produktionslinien_vergleich.xml`:
```python
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np

tree = ET.parse('produktionslinien_vergleich.xml')
root = tree.getroot()
```

b) Extrahieren Sie für jede Produktionslinie folgende **6 Kennzahlen** (normalisiert auf 0-100):
   - **Auslastung**: `(tatsaechliche_output / kapazitaet) × 100`
   - **Qualität**: `(100 - ausschussquote)`
   - **Effizienz**: `(100 / ruestzeit) × 10` (skaliert)
   - **Personaleffizienz**: `(tatsaechliche_output / anzahl_mitarbeiter) × 10` (skaliert)
   - **Energieeffizienz**: `(tatsaechliche_output / energieverbrauch) × 100` (skaliert)
   - **Kosteneffizienz**: `(100000 / wartungskosten) × 10` (skaliert)

c) Erstellen Sie **ein Radar/Polar-Diagramm** mit allen 5 Linien:
   - Jede Linie in unterschiedlicher Farbe
   - Transparenz `alpha=0.25` für die Füllung
   - Linienstärke `linewidth=2`
   - 6 Achsen für die Kennzahlen (0-100 Skala)
   - Titel: "Produktionslinien-Vergleich: Multidimensionale Analyse"
   - Legende außerhalb des Plots (rechts oben)

d) Beschriften Sie die 6 Achsen mit:
   - "Auslastung (%)"
   - "Qualität (100-Ausschuss)"
   - "Rüst-Effizienz"
   - "Personal-Effizienz"
   - "Energie-Effizienz"
   - "Kosten-Effizienz"

e) Zusatz:
   - Markieren Sie auf jeder Achse die Idealwerte (z.B. 80, 95, 70, etc.) als gestrichelte Kreise
   - Fügen Sie Annotationen für die beste Linie in jeder Kategorie hinzu

**Hinweis**: Für Radar Charts verwenden Sie `subplot_kw=dict(projection='polar')` und Winkel-Berechnung mit `np.linspace(0, 2*np.pi, 6, endpoint=False)`.

---

## Hinweise

### Allgemeine Hinweise

- Verwenden Sie `import matplotlib.pyplot as plt` für alle Matplotlib-Aufgaben
- Verwenden Sie `import numpy as np` für numerische Operationen
- Testen Sie Ihren Code in einer Python-Umgebung (IDLE, Jupyter, VS Code)
- Achten Sie auf **konsistente Formatierung**: Titel, Labels, Legenden wo sinnvoll

### Matplotlib Best Practices

- Verwenden Sie **aussagekräftige Titel** und **Achsenbeschriftungen**
- Setzen Sie **Gitter** mit `alpha=0.3` für bessere Lesbarkeit
- Nutzen Sie `tight_layout()` bei Subplots
- Verwenden Sie `figsize` für angemessene Plot-Größen
- Speichern Sie Plots mit **mind. 300 DPI** für Publikationen

### Debugging-Tipps

- **Plot wird nicht angezeigt**: Fehlt `plt.show()` am Ende?
- **Subplots überlappen**: Haben Sie `tight_layout()` vergessen?
- **Logarithmische Achse leer**: Enthält Ihr Datensatz Null oder negative Werte?
- **Gruppierte Bar Charts falsch positioniert**: Prüfen Sie die `x`-Positionen mit `np.arange()` und die `width`-Anpassung

---

**Viel Erfolg bei den Aufgaben!** 🚀
