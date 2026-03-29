# V14: Lösungen — Was macht ein Betriebssystem?

---

## Aufgabe 1: Betriebssystem-Basics

**a)** 3 Hauptaufgaben: Programme verwalten, Dateien verwalten, Hardware ansprechen.

**b)** Linux (Ubuntu).

**c)** Der Dateiname ist nur der Name der Datei (z.B. `main.py`). Der Pfad ist der komplette Weg dorthin (z.B. `/home/student/projekt/main.py`).

---

## Aufgabe 2: Datei-Explorer

```python
import os

dateien = os.listdir(".")

print("Python-Dateien in diesem Ordner:")
for datei in dateien:
    if datei.endswith(".py"):
        print(f"  🐍 {datei}")
```

---

## Aufgabe 3: Datei-Sucher

```python
import os

endung = input("Welche Dateiendung suchst du? (z.B. .py): ")

dateien = os.listdir(".")
gefunden = 0

for datei in dateien:
    if datei.endswith(endung):
        print(f"  ✅ {datei}")
        gefunden = gefunden + 1

if gefunden == 0:
    print(f"Keine Dateien mit '{endung}' gefunden.")
else:
    print(f"\n{gefunden} Datei(en) gefunden.")
```

**Bonus:**
```python
import os

dateien = os.listdir(".")
anzahl_ordner = 0
anzahl_dateien = 0

for datei in dateien:
    if os.path.isdir(datei):
        anzahl_ordner = anzahl_ordner + 1
    else:
        anzahl_dateien = anzahl_dateien + 1

print(f"Ordner: {anzahl_ordner}")
print(f"Dateien: {anzahl_dateien}")
```
