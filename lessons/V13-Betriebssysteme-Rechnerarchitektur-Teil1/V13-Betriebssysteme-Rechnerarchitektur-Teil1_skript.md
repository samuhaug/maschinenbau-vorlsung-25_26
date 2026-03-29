# V13: Was ist drin im Computer? — Rechnerarchitektur

> **Lernziele dieser Vorlesung:**
> - Die 3 Hauptteile eines Computers kennen: CPU, RAM, Speicher
> - Verstehen, warum RAM schneller ist als eine Festplatte
> - Bits und Bytes einordnen können (Wiederholung V01)
> - Erstes einfaches Diagramm mit `matplotlib` erstellen

---

## Teil 1: Theorie — Wie ist ein Computer aufgebaut?

### Die 3 Hauptteile

Jeder Computer (ob PC, Server oder CNC-Steuerung) besteht aus drei Hauptteilen:

| Teil | Aufgabe | Analogie |
|------|---------|----------|
| **CPU** (Prozessor) | Rechnet und steuert | Der **Koch** in der Küche |
| **RAM** (Arbeitsspeicher) | Speichert Daten kurzfristig | Die **Arbeitsfläche** |
| **Festplatte/SSD** | Speichert Daten dauerhaft | Der **Kühlschrank/Vorratsraum** |

> **Analogie Küche:** Der Koch (CPU) arbeitet auf der Arbeitsfläche (RAM). Die Zutaten holt er aus dem Kühlschrank (Festplatte). Je größer die Arbeitsfläche, desto mehr kann er gleichzeitig vorbereiten. Der Kühlschrank hat viel Platz, aber es dauert länger, etwas zu holen.

### CPU — Der Prozessor

Die **CPU** (Central Processing Unit) ist das "Gehirn" des Computers. Sie rechnet und führt Befehle aus.

**Was macht die CPU?**
- Berechnungen durchführen (z.B. 42 + 17)
- Entscheidungen treffen (z.B. if/else in Python)
- Daten hin- und herbewegen

**Geschwindigkeit:** Eine moderne CPU kann Milliarden Operationen pro Sekunde ausführen (gemessen in **GHz** = Milliarden Takte pro Sekunde).

### RAM — Der Arbeitsspeicher

Der **RAM** (Random Access Memory) ist der schnelle Zwischenspeicher:
- Speichert Daten, die gerade gebraucht werden
- **Sehr schnell**, aber **begrenzt** (typisch: 8-32 GB)
- **Flüchtig**: Daten gehen verloren, wenn der Strom weg ist

### Festplatte/SSD — Der Dauerspeicher

Die **Festplatte** (HDD) oder **SSD** speichert Daten dauerhaft:
- Programme, Dateien, Betriebssystem
- **Viel Platz** (typisch: 256 GB - 4 TB)
- **Langsamer** als RAM
- Daten bleiben erhalten, auch ohne Strom

### Geschwindigkeitsvergleich

| Speichertyp | Geschwindigkeit | Größe (typisch) |
|-------------|----------------|------------------|
| CPU-Register | Extrem schnell | Wenige Bytes |
| RAM | Sehr schnell | 8 - 32 GB |
| SSD | Schnell | 256 GB - 2 TB |
| Festplatte (HDD) | Langsam | 1 - 4 TB |

> **Merke:** Je schneller der Speicher, desto kleiner und teurer ist er. Deshalb gibt es verschiedene Stufen.

### Bits und Bytes — Wiederholung

Daten im Computer werden als **Bits** (0 oder 1) gespeichert:

| Einheit | Größe | Beispiel |
|---------|-------|---------|
| 1 Bit | 0 oder 1 | Ein Schalter: an/aus |
| 1 Byte | 8 Bits | Ein Buchstabe (z.B. "A") |
| 1 Kilobyte (KB) | 1.024 Bytes | Ein kurzer Text |
| 1 Megabyte (MB) | 1.024 KB | Ein Foto |
| 1 Gigabyte (GB) | 1.024 MB | Ein Film |
| 1 Terabyte (TB) | 1.024 GB | Viele Filme |

### Maschinenbau-Bezug

In der modernen Fertigung stecken überall Computer:
- **CNC-Steuerungen**: Berechnen Werkzeugbahnen in Echtzeit (brauchen schnelle CPU + viel RAM)
- **SPS** (Speicherprogrammierbare Steuerung): Steuert Maschinen und Anlagen
- **Industriecomputer**: Erfassen Sensordaten (Temperatur, Vibration, Druck)

### Zusammenfassung Theorie

- Computer = **CPU** (rechnet) + **RAM** (schneller Zwischenspeicher) + **Festplatte** (Dauerspeicher)
- RAM ist schnell aber klein, Festplatte ist langsam aber groß
- Daten werden in **Bits und Bytes** gespeichert
- In CNC-Maschinen und Industrieanlagen stecken dieselben Prinzipien

---

## Teil 2: Python-Praxis — Erstes Diagramm mit matplotlib

> Heute lernen wir, wie man mit Python einfache Diagramme erstellt.

### Ein Balkendiagramm erstellen

```python
import matplotlib.pyplot as plt

# Daten
speicher = ["RAM", "SSD", "HDD"]
geschwindigkeit = [50000, 3500, 150]    # MB/s (vereinfacht)

# Diagramm erstellen
plt.bar(speicher, geschwindigkeit)
plt.title("Geschwindigkeitsvergleich Speicher")
plt.ylabel("Geschwindigkeit (MB/s)")
plt.show()
```

### Das Wichtigste zu matplotlib

```python
import matplotlib.pyplot as plt    # Immer diese Zeile zuerst!

# Balkendiagramm
plt.bar(x_werte, y_werte)

# Liniendiagramm
plt.plot(x_werte, y_werte)

# Beschriftungen
plt.title("Titel")
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")

# Anzeigen
plt.show()
```

> **Nur 4 Befehle:** `plt.bar()`, `plt.title()`, `plt.ylabel()`, `plt.show()` — mehr braucht ihr heute nicht!
