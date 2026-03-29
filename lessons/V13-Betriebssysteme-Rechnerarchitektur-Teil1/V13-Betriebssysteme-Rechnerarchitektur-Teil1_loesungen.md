# V13: Lösungen — Was ist drin im Computer?

---

## Aufgabe 1: Computer-Teile zuordnen

**a)**
| Beschreibung | Teil |
|-------------|------|
| Speichert deine Python-Dateien dauerhaft | **Festplatte/SSD** |
| Führt `if temperatur > 80` aus | **CPU** |
| Hält die Variablen deines laufenden Programms | **RAM** |

**b)** RAM ist sehr schnell, aber teuer und klein. Festplatten sind langsam, aber günstig und groß. Darum nutzt man beide: RAM für aktuelle Daten (schnell), Festplatte zum dauerhaften Speichern (viel Platz).

**c)** CNC-Maschinen müssen Werkzeugbahnen in Echtzeit berechnen — das Werkzeug bewegt sich mit hoher Geschwindigkeit, und die Steuerung muss ständig neue Positionen berechnen. Ein langsamer Prozessor würde das Werkzeug "stottern" lassen.

---

## Aufgabe 2: Speichergrößen berechnen

```python
gb = float(input("Wie viele Gigabyte? "))

mb = gb * 1024
kb = mb * 1024

print(f"{gb} GB = {mb} MB")
print(f"{gb} GB = {kb} KB")
```

**Bonus:**
```python
gb = float(input("Wie viele Gigabyte? "))

tb = gb / 1024
mb = gb * 1024
kb = mb * 1024

print(f"{gb} GB = {tb} TB")
print(f"{gb} GB = {mb} MB")
print(f"{gb} GB = {kb} KB")
```

---

## Aufgabe 3: Balkendiagramm erstellen

```python
import matplotlib.pyplot as plt

geraete = ["Smartphone", "Laptop", "CNC-Steuerung", "Server"]
speicher_gb = [128, 512, 32, 2048]

plt.bar(geraete, speicher_gb)
plt.title("Speichervergleich")
plt.ylabel("Speicher (GB)")
plt.show()
```

Das Diagramm zeigt 4 Balken mit den Gerätenamen auf der X-Achse und den Speichergrößen auf der Y-Achse. Der Server-Balken ist am höchsten (2048 GB).
