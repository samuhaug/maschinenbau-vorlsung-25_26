# V16: Daten aus dem Internet holen — APIs und JSON

> **Lernziele dieser Vorlesung:**
> - HTTP-Anfragen verstehen (GET = Daten holen, POST = Daten senden)
> - JSON als Datenformat kennen
> - Wissen, was eine API ist
> - Python: Mit `requests` echte Daten aus dem Internet holen

---

## Teil 1: Theorie — HTTP, JSON und APIs

### HTTP: Anfrage → Antwort

Wenn dein Browser eine Webseite aufruft, passiert Folgendes:

1. **Dein Browser sendet eine Anfrage** (Request) an den Server
2. **Der Server sendet eine Antwort** (Response) zurück

Die zwei wichtigsten Anfrage-Typen:

| Methode | Was tut sie? | Analogie |
|---------|-------------|----------|
| **GET** | Daten holen | "Gib mir die Speisekarte!" |
| **POST** | Daten senden | "Hier ist meine Bestellung!" |

> **90% von allem was du im Browser machst sind GET-Anfragen:** Webseite öffnen, Bild laden, Suche starten.

### JSON: Das Universal-Datenformat

**JSON** (JavaScript Object Notation) ist das Standardformat, in dem Daten im Internet ausgetauscht werden. Es sieht aus wie ein Python-Dictionary!

```json
{
    "maschine": "CNC-01",
    "temperatur": 42.5,
    "status": "OK",
    "sensoren": ["Temperatur", "Vibration", "Druck"]
}
```

**JSON ↔ Python:**
| JSON | Python |
|------|--------|
| `{ }` (Object) | `dict` (Dictionary) |
| `[ ]` (Array) | `list` (Liste) |
| `"text"` | `str` (String) |
| `42` | `int` (Zahl) |
| `true` / `false` | `True` / `False` |

### Was ist eine API?

Eine **API** (Application Programming Interface) ist eine Schnittstelle, über die Programme Daten austauschen können — wie ein Bestellschalter:

> Du fragst die API: "Wie ist das Wetter in Stuttgart?"  
> Die API antwortet: `{"temperatur": 18.5, "regen": false}`

**Beispiele für kostenlose APIs:**
- **Open-Meteo**: Wetterdaten (kein API-Key nötig!)
- **REST Countries**: Länder-Informationen
- **JSONPlaceholder**: Test-Daten zum Üben

### Zusammenfassung Theorie

- **HTTP GET**: Daten vom Server holen
- **JSON**: Standard-Datenformat im Internet (sieht aus wie Python-Dictionary)
- **API**: Schnittstelle um Daten programmatisch abzufragen
- Mit Python können wir APIs aufrufen und die Daten weiterverarbeiten!

---

## Teil 2: Python-Praxis — Daten holen mit `requests`

> Die Bibliothek `requests` macht es einfach, Daten aus dem Internet zu holen.

### Erste API-Anfrage

```python
import requests

# Wetterdaten für Stuttgart holen (Open-Meteo API — kostenlos!)
url = "https://api.open-meteo.com/v1/forecast?latitude=48.78&longitude=9.18&current_weather=true"
antwort = requests.get(url)
daten = antwort.json()

# Aktuelle Temperatur anzeigen
temperatur = daten["current_weather"]["temperature"]
print(f"Aktuelle Temperatur in Stuttgart: {temperatur}°C")
```

### JSON-Daten verarbeiten

```python
# Die API gibt ein Dictionary zurück
wetter = daten["current_weather"]

print(f"Temperatur: {wetter['temperature']}°C")
print(f"Windgeschwindigkeit: {wetter['windspeed']} km/h")
print(f"Windrichtung: {wetter['winddirection']}°")
```

### Nur 3 Schritte

```python
import requests

# 1. URL zusammenbauen
url = "https://api.example.com/daten"

# 2. Anfrage senden
antwort = requests.get(url)

# 3. JSON auslesen
daten = antwort.json()
print(daten)
```

> **Das war's!** `requests.get()` + `.json()` — mehr braucht ihr heute nicht.
