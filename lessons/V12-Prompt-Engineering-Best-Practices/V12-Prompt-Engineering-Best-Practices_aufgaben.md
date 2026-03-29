# V12: Übungsaufgaben — KI richtig fragen

---

## Aufgabe 1: Prompt verbessern (Theorie)

**Zeitaufwand**: ca. 10 Minuten

Verbessere die folgenden schlechten Prompts. Verwende die 3 Bausteine: **Kontext + Aufgabe + Format**.

a) Schlechter Prompt: `"Erkläre Stahl."`
   → Schreibe einen guten Prompt.

b) Schlechter Prompt: `"Schreib Python Code"`
   → Schreibe einen guten Prompt.

c) Schlechter Prompt: `"Was ist Wartung?"`
   → Schreibe einen guten Prompt.

---

## Aufgabe 2: Prompt-Generator (Python)

**Zeitaufwand**: ca. 15 Minuten

Schreibe ein Programm, das den Benutzer nach den 3 Bausteinen fragt und daraus einen fertigen Prompt zusammenbaut.

**So soll es aussehen:**
```
=== Prompt-Generator ===
Kontext (Wer bist du?): Maschinenbau-Student
Aufgabe (Was soll die KI tun?): Erkläre Vorschubgeschwindigkeit
Format (Wie soll die Antwort sein?): 3 Sätze, einfache Sprache

--- Dein Prompt ---
Kontext: Maschinenbau-Student
Aufgabe: Erkläre Vorschubgeschwindigkeit
Format: 3 Sätze, einfache Sprache
```

**Starter-Code:**
```python
print("=== Prompt-Generator ===")

kontext = input("Kontext (Wer bist du?): ")
aufgabe = ___                                    # TODO: Frage nach der Aufgabe
format_wunsch = ___                              # TODO: Frage nach dem Format

print()
print("--- Dein Prompt ---")
print(f"Kontext: {kontext}")
print(f"Aufgabe: {___}")                         # TODO: Ergänze
print(f"Format: {___}")                          # TODO: Ergänze
```

---

## Aufgabe 3: Maschinen-Begriffe übersetzen (Python)

**Zeitaufwand**: ca. 20 Minuten

Schreibe ein Programm, das technische Fachbegriffe in einfache Sprache "übersetzt".

**Starter-Code:**
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
else:
    print(f"→ '{begriff}' kenne ich noch nicht!")

# TODO: Füge 2 weitere Begriffe hinzu, die du aus dem Studium kennst!
```

**Bonus:** Mache die Eingabe unempfindlich gegen Groß-/Kleinschreibung (Tipp: `.lower()`).
