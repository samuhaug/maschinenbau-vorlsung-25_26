# V14: Übungsaufgaben — Was macht ein Betriebssystem?

---

## Aufgabe 1: Betriebssystem-Basics (Theorie)

a) Nenne die **3 Hauptaufgaben** eines Betriebssystems.

b) Auf welchem Betriebssystem läuft euer GitHub Codespace?

c) Was ist der Unterschied zwischen einem **Pfad** und einem **Dateinamen**?

---

## Aufgabe 2: Datei-Explorer mit Python

**Starter-Code:**
```python
import os

# Alle Dateien im aktuellen Ordner auflisten
dateien = os.listdir(".")

print("Dateien in diesem Ordner:")
for datei in dateien:
    print(f"  📄 {datei}")

print(f"\nAnzahl: {len(dateien)} Dateien/Ordner")
```

Führe den Code aus und beantworte: Welche Dateien siehst du?

**Erweitere den Code:** Zeige nur die `.py`-Dateien an! (Tipp: `if datei.endswith(".py")`)

---

## Aufgabe 3: Datei-Sucher (Python)

Schreibe ein Programm, das den Benutzer nach einer Dateiendung fragt und alle passenden Dateien anzeigt.

**Starter-Code:**
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

**Bonus:** Zähle zusätzlich, wie viele Ordner und wie viele Dateien es im Verzeichnis gibt. (Tipp: `os.path.isdir(datei)`)
