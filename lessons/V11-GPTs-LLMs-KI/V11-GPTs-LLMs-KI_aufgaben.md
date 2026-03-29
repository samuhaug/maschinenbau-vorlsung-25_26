# V11: Übungsaufgaben — Was ist Künstliche Intelligenz?

> Bearbeite die Aufgaben der Reihe nach.
> Du brauchst: VS Code im Codespace, Python, dieses Aufgabenblatt.

---

## Aufgabe 1: KI im Alltag erkennen (Theorie)

**Zeitaufwand**: ca. 10 Minuten

a) Nenne **drei Beispiele** aus deinem Alltag, wo du KI benutzt (bewusst oder unbewusst).

b) Erkläre in **einem Satz**, wie ein Large Language Model (LLM) wie ChatGPT funktioniert.

c) Warum kann ein LLM falsche Informationen ausgeben (Halluzinationen)? Erkläre es in eigenen Worten.

---

## Aufgabe 2: Maschinen-Steckbrief (Python)

**Zeitaufwand**: ca. 15 Minuten

Schreibe ein Python-Programm, das einen "Steckbrief" für eine CNC-Maschine ausgibt.

**So soll die Ausgabe aussehen:**
```
=== Maschinen-Steckbrief ===
Name: CNC-Fräse 01
Baujahr: 2020
Temperatur: 45.2 °C
Status: OK
```

**Starter-Code** (ergänze die fehlenden Stellen):
```python
# Variablen definieren
name = "CNC-Fräse 01"
baujahr = ___           # TODO: Setze das Baujahr auf 2020
temperatur = ___        # TODO: Setze die Temperatur auf 45.2
status = "OK"

# Ausgabe
print("=== Maschinen-Steckbrief ===")
print(f"Name: {name}")
print(f"Baujahr: {___}")         # TODO: Ergänze die Variable
print(f"Temperatur: {___} °C")   # TODO: Ergänze die Variable
print(f"Status: {status}")
```

---

## Aufgabe 3: Temperatur-Warnung (Python)

**Zeitaufwand**: ca. 20 Minuten

Schreibe ein Programm, das die Temperatur einer Maschine prüft und eine passende Meldung ausgibt.

**Regeln:**
- Über 80°C → `"ALARM: Maschine sofort abschalten!"`
- Über 60°C → `"WARNUNG: Temperatur erhöht!"`
- Sonst → `"OK: Temperatur normal."`

**Starter-Code:**
```python
# Temperatur abfragen
eingabe = input("Temperatur in °C eingeben: ")
temperatur = float(eingabe)    # Text in Kommazahl umwandeln

# TODO: Ergänze die if/elif/else-Abfrage
if ___:
    print("ALARM: Maschine sofort abschalten!")
elif ___:
    print("WARNUNG: Temperatur erhöht!")
else:
    print("OK: Temperatur normal.")
```

**Bonus:** Erweitere das Programm so, dass es den Benutzer auch nach dem Maschinennamen fragt und diesen in der Ausgabe anzeigt.
