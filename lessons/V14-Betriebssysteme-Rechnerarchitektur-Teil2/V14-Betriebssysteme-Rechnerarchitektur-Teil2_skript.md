# V14: Was macht ein Betriebssystem? — Dateien, Programme, Terminal

> **Lernziele dieser Vorlesung:**
> - Wissen, was ein Betriebssystem ist und welche 3 Hauptaufgaben es hat
> - Dateisysteme verstehen: Ordner, Dateien, Pfade
> - Das Terminal (Kommandozeile) grundlegend bedienen können
> - Python: Dateien im System erkunden mit dem `os`-Modul

---

## Teil 1: Theorie — Betriebssysteme

### Was ist ein Betriebssystem?

Das **Betriebssystem** (OS = Operating System) ist die Software zwischen dir und der Hardware. Es hat 3 Hauptaufgaben:

| Aufgabe | Was macht es? | Beispiel |
|---------|--------------|---------|
| **Programme verwalten** | Startet, stoppt, wechselt zwischen Programmen | Du öffnest VS Code und Chrome gleichzeitig |
| **Dateien verwalten** | Organisiert Dateien in Ordnern | Deine Python-Dateien liegen in `lessons/V14/` |
| **Hardware ansprechen** | Verbindet Software mit Tastatur, Bildschirm, Drucker | Du drückst eine Taste → Buchstabe erscheint |

**Bekannte Betriebssysteme:**
- **Windows** — Am weitverbreitetsten auf PCs
- **macOS** — Apple-Computer
- **Linux** — Server, Industriesteuerungen, GitHub Codespaces!

> **Euer Codespace läuft auf Linux!** Das ist der Grund, warum manche Befehle anders sind als auf eurem Windows-PC.

### Dateisystem: Ordner und Pfade

Dateien sind in einer **Baumstruktur** organisiert:

```
/ (Wurzel)
├── home/
│   └── student/
│       ├── projekt/
│       │   ├── main.py
│       │   └── daten.csv
│       └── notizen.txt
└── usr/
    └── bin/
```

**Wichtige Begriffe:**
- **Pfad**: Der "Weg" zu einer Datei, z.B. `/home/student/projekt/main.py`
- **Ordner** (Verzeichnis): Enthält Dateien und andere Ordner
- **Dateiendung**: `.py` = Python, `.md` = Markdown, `.csv` = Tabelle

### Das Terminal — Die Kommandozeile

Das **Terminal** ist eine textbasierte Steuerung des Computers. Statt mit der Maus zu klicken, tippst du Befehle ein.

| Befehl | Was macht er? | Beispiel |
|--------|--------------|---------|
| `ls` | Dateien auflisten | `ls` → zeigt alle Dateien |
| `cd` | Ordner wechseln | `cd lessons/V14` |
| `pwd` | Aktuellen Ordner anzeigen | `pwd` → `/home/student` |
| `cat` | Datei anzeigen | `cat main.py` |
| `mkdir` | Neuen Ordner erstellen | `mkdir mein_ordner` |

> **Tipp:** Im Codespace könnt ihr das Terminal öffnen mit `Strg + Ö` (oder über das Menü: Terminal → New Terminal).

### Zusammenfassung Theorie

- **Betriebssystem** = Software die Programme, Dateien und Hardware verwaltet
- **Dateisystem** = Baumstruktur aus Ordnern und Dateien
- **Pfad** = Weg zu einer Datei (z.B. `lessons/V14/main.py`)
- **Terminal** = Textbasierte Steuerung des Computers

---

## Teil 2: Python-Praxis — Dateien erkunden mit `os`

> Das `os`-Modul lässt uns mit Python das Dateisystem erkunden.

### Dateien auflisten

```python
import os

# Alle Dateien im aktuellen Ordner anzeigen
dateien = os.listdir(".")
print(dateien)
```

### Aktuellen Ordner anzeigen

```python
import os

aktueller_ordner = os.getcwd()
print(f"Ich bin hier: {aktueller_ordner}")
```

### Prüfen ob eine Datei existiert

```python
import os

if os.path.exists("main.py"):
    print("Die Datei existiert!")
else:
    print("Datei nicht gefunden.")
```

> **Nur 3 Befehle:** `os.listdir()`, `os.getcwd()`, `os.path.exists()` — mehr braucht ihr heute nicht!
