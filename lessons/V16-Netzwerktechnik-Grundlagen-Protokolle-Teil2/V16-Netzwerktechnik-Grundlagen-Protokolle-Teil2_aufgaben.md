# V16: Daten aus dem Internet holen — Aufgaben

> **Punkte-System:** Sammle Punkte für die Klausurvorbereitung!

---

## Aufgabe 1: Theorie-Check (2 Punkte)

Beantworte folgende Fragen:

**a)** Was ist der Unterschied zwischen GET und POST?

**b)** In welchem Format liefern die meisten APIs ihre Daten zurück?

**c)** Ergänze die Python-Entsprechungen:

| JSON | Python |
|------|--------|
| `{ }` | __________ |
| `[ ]` | __________ |
| `true` | __________ |

---

## Aufgabe 2: Wetter-Station (4 Punkte)

Schreibe ein Programm, das das aktuelle Wetter für **deine Heimatstadt** abfragt.

**So findest du die Koordinaten:**
- Google Maps → Rechtsklick auf deine Stadt → Koordinaten kopieren

**Template:**

```python
import requests

# TODO: Trage deine Koordinaten ein
latitude = ___      # Breitengrad
longitude = ___     # Längengrad
stadt = "___"       # Name deiner Stadt

# API-Anfrage
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
antwort = requests.get(url)
daten = antwort.json()

# TODO: Hole die aktuelle Temperatur aus den Daten
# Tipp: Die Temperatur steckt in daten["current_weather"]["temperature"]
temperatur = ___

# TODO: Hole die Windgeschwindigkeit
windspeed = ___

# Ausgabe
print(f"=== Wetter in {stadt} ===")
print(f"Temperatur: {temperatur}°C")
print(f"Wind: {windspeed} km/h")

# TODO: Gib eine Warnung aus wenn die Temperatur über 30°C liegt
# Tipp: if temperatur > 30: ...
```

---

## Aufgabe 3: Länder-Quiz (5 Punkte)

Schreibe ein Programm, das Informationen über ein Land abfragt und anzeigt.

**API:** `https://restcountries.com/v3.1/name/{land}`

**Beispiel:** Für Deutschland: `https://restcountries.com/v3.1/name/germany`

**Template:**

```python
import requests

# Benutzer nach einem Land fragen
land = input("Welches Land möchtest du nachschlagen? ")

# API-Anfrage
url = f"https://restcountries.com/v3.1/name/{land}"
antwort = requests.get(url)

# Die API gibt eine Liste zurück — wir nehmen das erste Ergebnis
daten = antwort.json()
info = daten[0]

# TODO: Hole den offiziellen Namen
# Tipp: info["name"]["official"]
name = ___

# TODO: Hole die Einwohnerzahl
# Tipp: info["population"]
einwohner = ___

# TODO: Hole die Hauptstadt (ist eine Liste, nimm das erste Element)
# Tipp: info["capital"][0]
hauptstadt = ___

# TODO: Hole die Region (z.B. "Europe")
region = ___

print(f"\n=== {name} ===")
print(f"Hauptstadt: {hauptstadt}")
print(f"Einwohner: {einwohner:,}")  # :, fügt Tausender-Punkte ein
print(f"Region: {region}")
```

**Bonus (+ 2 Punkte):** Erweitere das Programm so, dass es 3 Länder nacheinander abfragt (mit einer `for`-Schleife) und am Ende anzeigt, welches Land die meisten Einwohner hat.

---

## Punkte-Übersicht

| Aufgabe | Thema | Punkte |
|---------|-------|--------|
| 1 | Theorie-Check | 2 |
| 2 | Wetter-Station | 4 |
| 3 | Länder-Quiz | 5 |
| Bonus | 3 Länder vergleichen | +2 |
| **Gesamt** | | **max. 13** |
