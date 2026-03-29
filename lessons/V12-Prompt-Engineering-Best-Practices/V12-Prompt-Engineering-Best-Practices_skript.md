# V12: KI richtig fragen — Prompt Engineering

> **Lernziele dieser Vorlesung:**
> - Verstehen, was ein "Prompt" ist und warum die Formulierung wichtig ist
> - Gute von schlechten Prompts unterscheiden können
> - Die 3 Bausteine eines guten Prompts kennen: Kontext, Aufgabe, Format
> - Python-Grundlagen vertiefen: f-Strings, String-Operationen

---

## Teil 1: Theorie — Prompt Engineering

### Was ist ein Prompt?

Ein **Prompt** ist die Anweisung, die du einer KI gibst. Es ist deine "Frage" oder dein "Auftrag" an ChatGPT, Copilot & Co.

> **Die Qualität der KI-Antwort hängt direkt von der Qualität deines Prompts ab.**

**Schlechter Prompt:**
```
Schreib was über CNC.
```

**Guter Prompt:**
```
Erkläre einem Maschinenbau-Studenten im 1. Semester in 5 Sätzen, 
was eine CNC-Fräsmaschine ist und wofür sie verwendet wird.
```

### Die 3 Bausteine eines guten Prompts

Jeder gute Prompt besteht aus drei Teilen:

| Baustein | Was ist das? | Beispiel |
|----------|-------------|---------|
| **Kontext** | Wer bist du / für wen? | "Du bist ein Maschinenbau-Dozent..." |
| **Aufgabe** | Was soll die KI tun? | "Erkläre den Begriff Vorschubgeschwindigkeit" |
| **Format** | Wie soll die Antwort aussehen? | "...in maximal 3 Sätzen, auf Deutsch" |

**Formel:**
```
Guter Prompt = Kontext + Aufgabe + Format
```

### Beispiel: Prompt verbessern

**Vorher (schlecht):**
```
Was ist Vorschubgeschwindigkeit?
```

**Nachher (gut):**
```
Kontext: Ich bin Maschinenbau-Student im 1. Semester.
Aufgabe: Erkläre mir den Begriff "Vorschubgeschwindigkeit" bei CNC-Maschinen.
Format:  Verwende einfache Sprache, maximal 3 Sätze, mit einem Beispiel.
```

### Few-Shot: Beispiele helfen

Wenn du der KI **Beispiele** gibst, versteht sie besser, was du willst:

```
Übersetze technische Begriffe ins Einfache:
- "Spindeldrehzahl" → "Wie schnell sich das Werkzeug dreht"
- "Vorschubgeschwindigkeit" → "Wie schnell sich das Werkstück bewegt"
- "Kühlschmierstoff" → ???
```

Die KI erkennt das Muster und ergänzt im gleichen Stil.

### Iterativ verbessern

Dein erster Prompt muss nicht perfekt sein! Verbessere Schritt für Schritt:

1. **Erster Versuch** → Antwort lesen
2. **Was fehlt?** → Prompt ergänzen ("Mach es kürzer", "Gib ein Beispiel")
3. **Wiederholen** bis das Ergebnis passt

> **Tipp:** Speichere gute Prompts — du wirst sie wiederverwenden!

### Zusammenfassung Theorie

- **Prompt** = Anweisung an die KI
- Guter Prompt = **Kontext** + **Aufgabe** + **Format**
- **Beispiele geben** (Few-Shot) verbessert die Ergebnisse
- **Iterativ verbessern** — der erste Versuch muss nicht perfekt sein
- Prompt Engineering ist eine **Schlüsselkompetenz** für die Arbeit mit KI

---

## Teil 2: Python-Praxis — f-Strings und String-Operationen

> Wir üben f-Strings und verwenden sie, um Prompt-Templates zu bauen.

### f-Strings: Variablen in Text einbauen

```python
# f-String: Text mit Variablen mischen
maschine = "CNC-Fräse"
temperatur = 42.5

print(f"Die {maschine} hat eine Temperatur von {temperatur}°C.")
```

### Strings zusammenbauen

```python
# Strings mit + verbinden
vorname = "Max"
nachname = "Müller"
name = vorname + " " + nachname
print(name)  # Max Müller
```

### Strings verändern

```python
text = "  Hallo Welt  "

print(text.strip())       # "Hallo Welt" (Leerzeichen entfernen)
print(text.upper())       # "  HALLO WELT  " (GROSSBUCHSTABEN)
print(text.lower())       # "  hallo welt  " (kleinbuchstaben)
print(text.replace("Welt", "Python"))  # "  Hallo Python  "
```

### Prompt-Template mit f-Strings

```python
# Einen Prompt aus Bausteinen zusammenbauen
kontext = "Maschinenbau-Student, 1. Semester"
aufgabe = "Erkläre den Begriff Vorschubgeschwindigkeit"
format_wunsch = "Maximal 3 Sätze, einfache Sprache"

prompt = f"""Kontext: {kontext}
Aufgabe: {aufgabe}
Format: {format_wunsch}"""

print(prompt)
```
