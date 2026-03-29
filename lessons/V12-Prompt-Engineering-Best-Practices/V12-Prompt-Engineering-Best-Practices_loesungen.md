# V12: Lösungen — KI richtig fragen

---

## Aufgabe 1: Prompt verbessern (Theorie)

**a)** Schlechter Prompt: "Erkläre Stahl."
```
Kontext: Ich bin Maschinenbau-Student im 1. Semester.
Aufgabe: Erkläre mir, was Stahl ist und welche Eigenschaften ihn für den Maschinenbau wichtig machen.
Format: Maximal 5 Sätze, einfache Sprache, mit einem Alltagsbeispiel.
```

**b)** Schlechter Prompt: "Schreib Python Code"
```
Kontext: Ich bin Python-Anfänger und lerne gerade if/else und Schleifen.
Aufgabe: Schreibe ein Python-Programm, das den Benutzer nach einer Temperatur fragt und "zu heiß" oder "OK" ausgibt.
Format: Einfacher Code, mit Kommentaren, nur print/input/if verwenden.
```

**c)** Schlechter Prompt: "Was ist Wartung?"
```
Kontext: Maschinenbau-Kontext, CNC-Maschinen.
Aufgabe: Erkläre den Unterschied zwischen vorbeugender Wartung und Instandsetzung.
Format: Stichpunkte, maximal 5 Punkte pro Kategorie.
```

---

## Aufgabe 2: Prompt-Generator (Python)

```python
print("=== Prompt-Generator ===")

kontext = input("Kontext (Wer bist du?): ")
aufgabe = input("Aufgabe (Was soll die KI tun?): ")
format_wunsch = input("Format (Wie soll die Antwort sein?): ")

print()
print("--- Dein Prompt ---")
print(f"Kontext: {kontext}")
print(f"Aufgabe: {aufgabe}")
print(f"Format: {format_wunsch}")
```

---

## Aufgabe 3: Maschinen-Begriffe übersetzen (Python)

```python
# Fachbegriff abfragen
begriff = input("Technischer Begriff: ")

# Begriffe "übersetzen"
if begriff == "Spindeldrehzahl":
    print("→ Wie schnell sich das Werkzeug dreht (in Umdrehungen pro Minute)")
elif begriff == "Vorschubgeschwindigkeit":
    print("→ Wie schnell sich das Werkstück bewegt (in mm pro Minute)")
elif begriff == "Kühlschmierstoff":
    print("→ Flüssigkeit die beim Fräsen kühlt und schmiert")
elif begriff == "Werkzeugwechsler":
    print("→ Vorrichtung die automatisch das Werkzeug in der Maschine tauscht")
elif begriff == "Spannfutter":
    print("→ Halterung die das Werkstück festhält")
else:
    print(f"→ '{begriff}' kenne ich noch nicht!")
```

**Bonus-Lösung mit `.lower()`:**
```python
begriff = input("Technischer Begriff: ")
begriff_klein = begriff.lower()

if begriff_klein == "spindeldrehzahl":
    print("→ Wie schnell sich das Werkzeug dreht (in Umdrehungen pro Minute)")
elif begriff_klein == "vorschubgeschwindigkeit":
    print("→ Wie schnell sich das Werkstück bewegt (in mm pro Minute)")
elif begriff_klein == "kühlschmierstoff":
    print("→ Flüssigkeit die beim Fräsen kühlt und schmiert")
else:
    print(f"→ '{begriff}' kenne ich noch nicht!")
```
