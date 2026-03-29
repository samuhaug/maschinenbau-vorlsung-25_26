# V16: Daten aus dem Internet holen — Lösungen

---

## Aufgabe 1: Theorie-Check

**a)** GET holt Daten vom Server ("Gib mir die Speisekarte!"), POST sendet Daten an den Server ("Hier ist meine Bestellung!").

**b)** JSON (JavaScript Object Notation)

**c)**

| JSON | Python |
|------|--------|
| `{ }` | `dict` (Dictionary) |
| `[ ]` | `list` (Liste) |
| `true` | `True` |

---

## Aufgabe 2: Wetter-Station

```python
import requests

# Beispiel: Stuttgart
latitude = 48.78
longitude = 9.18
stadt = "Stuttgart"

# API-Anfrage
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
antwort = requests.get(url)
daten = antwort.json()

# Daten auslesen
temperatur = daten["current_weather"]["temperature"]
windspeed = daten["current_weather"]["windspeed"]

# Ausgabe
print(f"=== Wetter in {stadt} ===")
print(f"Temperatur: {temperatur}°C")
print(f"Wind: {windspeed} km/h")

# Warnung bei Hitze
if temperatur > 30:
    print("⚠️  WARNUNG: Hitze! Viel trinken!")
```

---

## Aufgabe 3: Länder-Quiz

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

# Daten auslesen
name = info["name"]["official"]
einwohner = info["population"]
hauptstadt = info["capital"][0]
region = info["region"]

print(f"\n=== {name} ===")
print(f"Hauptstadt: {hauptstadt}")
print(f"Einwohner: {einwohner:,}")
print(f"Region: {region}")
```

### Bonus: 3 Länder vergleichen

```python
import requests

laender_daten = []

for i in range(3):
    land = input(f"Land {i + 1}: ")
    url = f"https://restcountries.com/v3.1/name/{land}"
    antwort = requests.get(url)
    daten = antwort.json()
    info = daten[0]

    name = info["name"]["official"]
    einwohner = info["population"]
    hauptstadt = info["capital"][0]

    print(f"  → {name}: {einwohner:,} Einwohner")

    laender_daten.append({"name": name, "einwohner": einwohner})

# Größtes Land finden
groesstes = laender_daten[0]
for land in laender_daten:
    if land["einwohner"] > groesstes["einwohner"]:
        groesstes = land

print(f"\n🏆 {groesstes['name']} hat die meisten Einwohner: {groesstes['einwohner']:,}")
```
