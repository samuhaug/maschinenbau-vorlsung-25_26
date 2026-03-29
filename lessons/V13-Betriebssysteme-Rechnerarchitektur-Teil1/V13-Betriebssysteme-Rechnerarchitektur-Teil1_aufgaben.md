# V13: Übungsaufgaben — Was ist drin im Computer?

---

## Aufgabe 1: Computer-Teile zuordnen (Theorie)

**Zeitaufwand**: ca. 10 Minuten

a) Ordne zu: Welcher Teil des Computers (CPU, RAM, Festplatte) passt zu welcher Beschreibung?

| Beschreibung | Teil |
|-------------|------|
| Speichert deine Python-Dateien dauerhaft | ___ |
| Führt `if temperatur > 80` aus | ___ |
| Hält die Variablen deines laufenden Programms | ___ |

b) Warum hat ein Computer verschiedene Speichertypen (RAM und Festplatte) statt nur einen?

c) CNC-Maschinen brauchen einen schnellen Prozessor. Warum?

---

## Aufgabe 2: Speichergrößen berechnen (Python)

**Zeitaufwand**: ca. 15 Minuten

Schreibe ein Programm, das Speichergrößen umrechnet.

**Starter-Code:**
```python
# Speichergrößen umrechnen
gb = float(input("Wie viele Gigabyte? "))

mb = gb * 1024
kb = mb * 1024

print(f"{gb} GB = {mb} MB")
print(f"{gb} GB = {___} KB")    # TODO: Ergänze
```

**Bonus:** Erweitere das Programm, so dass es auch in Terabyte (TB) umrechnet: `tb = gb / 1024`

---

## Aufgabe 3: Balkendiagramm erstellen (Python + matplotlib)

**Zeitaufwand**: ca. 20 Minuten

Erstelle ein Balkendiagramm, das die Speichergrößen verschiedener Geräte vergleicht.

**Starter-Code:**
```python
import matplotlib.pyplot as plt

# Daten
geraete = ["Smartphone", "Laptop", "CNC-Steuerung", "Server"]
speicher_gb = [128, 512, 32, 2048]

# Diagramm
plt.bar(geraete, speicher_gb)
plt.title("Speichervergleich")
plt.ylabel("Speicher (GB)")
plt.show()
```

Führe den Code aus. Dann **ändere die Werte** und erstelle ein eigenes Diagramm!
