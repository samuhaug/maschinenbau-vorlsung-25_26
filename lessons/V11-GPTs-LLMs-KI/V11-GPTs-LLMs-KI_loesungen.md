# V11: Lösungen — Was ist Künstliche Intelligenz?

---

## Aufgabe 1: KI im Alltag erkennen (Theorie)

**a) Drei Beispiele für KI im Alltag:**
- Handy-Autovervollständigung / Autokorrektur
- Google Maps Navigation (Routenberechnung, Stauvorhersage)
- Spotify/Netflix Empfehlungen ("Das könnte dir gefallen")
- Spam-Filter im E-Mail-Postfach
- Gesichtserkennung zum Handy-Entsperren

**b) Wie funktioniert ein LLM?**
Ein LLM liest den bisherigen Text und berechnet, welches Wort am wahrscheinlichsten als nächstes kommt — wie eine sehr gute Autovervollständigung, trainiert auf Milliarden von Texten.

**c) Warum Halluzinationen?**
Das LLM hat kein echtes Wissen — es kennt nur Muster. Wenn ein Muster plausibel klingt, gibt es die Information aus, auch wenn sie falsch ist. Es kann nicht zwischen wahr und falsch unterscheiden.

---

## Aufgabe 2: Maschinen-Steckbrief (Python)

```python
# Variablen definieren
name = "CNC-Fräse 01"
baujahr = 2020
temperatur = 45.2
status = "OK"

# Ausgabe
print("=== Maschinen-Steckbrief ===")
print(f"Name: {name}")
print(f"Baujahr: {baujahr}")
print(f"Temperatur: {temperatur} °C")
print(f"Status: {status}")
```

**Erwartete Ausgabe:**
```
=== Maschinen-Steckbrief ===
Name: CNC-Fräse 01
Baujahr: 2020
Temperatur: 45.2 °C
Status: OK
```

---

## Aufgabe 3: Temperatur-Warnung (Python)

```python
# Temperatur abfragen
eingabe = input("Temperatur in °C eingeben: ")
temperatur = float(eingabe)

# Temperatur prüfen
if temperatur > 80:
    print("ALARM: Maschine sofort abschalten!")
elif temperatur > 60:
    print("WARNUNG: Temperatur erhöht!")
else:
    print("OK: Temperatur normal.")
```

**Bonus-Lösung mit Maschinenname:**
```python
maschine = input("Maschinenname: ")
eingabe = input("Temperatur in °C eingeben: ")
temperatur = float(eingabe)

if temperatur > 80:
    print(f"ALARM: {maschine} sofort abschalten!")
elif temperatur > 60:
    print(f"WARNUNG: {maschine} - Temperatur erhöht!")
else:
    print(f"OK: {maschine} - Temperatur normal.")
```
