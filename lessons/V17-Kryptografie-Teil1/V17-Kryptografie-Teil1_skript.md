# V17: Geheime Nachrichten — Kryptografie mit Python

> **Lernziele dieser Vorlesung:**
> - Verstehen, warum Verschlüsselung wichtig ist
> - Die Caesar-Chiffre kennen und anwenden können
> - Den Unterschied zwischen symmetrischer und asymmetrischer Verschlüsselung kennen
> - Python: `ord()` und `chr()` zur Buchstaben-Manipulation nutzen

---

## Teil 1: Theorie — Warum Verschlüsselung?

### Das Problem: Mitleser

Stell dir vor, du schickst eine Nachricht über das Internet:

```
"Maschine CNC-01 hat einen Defekt am Lagersensor"
```

Ohne Verschlüsselung kann **jeder** diese Nachricht lesen, der den Datenverkehr abfängt. Das ist ein Problem bei:
- Firmengeheimnissen
- Passwörtern
- Persönlichen Daten
- Finanzdaten

> **Lösung:** Die Nachricht wird verschlüsselt — nur wer den Schlüssel hat, kann sie lesen.

### Die Caesar-Chiffre: Die einfachste Verschlüsselung

Julius Caesar hat seine Nachrichten verschlüsselt, indem er **jeden Buchstaben um eine feste Anzahl verschoben** hat.

**Beispiel mit Verschiebung 3:**

```
A → D       Klartext:    HALLO
B → E       Verschlüsselt: KDOOR
C → F
...
H → K
```

**So funktioniert es:**
| Klartext  | H | A | L | L | O |
|-----------|---|---|---|---|---|
| +3        | K | D | O | O | R |
| Geheimtext| K | D | O | O | R |

**Zum Entschlüsseln:** Einfach in die andere Richtung verschieben (-3).

### Symmetrisch vs. Asymmetrisch

| | Symmetrisch | Asymmetrisch |
|--|-------------|-------------|
| **Schlüssel** | Gleicher Schlüssel zum Ver- und Entschlüsseln | Zwei Schlüssel: öffentlich + privat |
| **Analogie** | Ein Schlüssel für ein Vorhängeschloss | Briefkasten: jeder kann einwerfen, nur du kannst öffnen |
| **Beispiel** | Caesar-Chiffre, AES | RSA, HTTPS |
| **Problem** | Wie tauscht man den Schlüssel sicher aus? | Langsamer, aber sicherer Schlüsseltausch |

> **HTTPS** (das Schloss im Browser) nutzt **beide**: Asymmetrisch für den Schlüsseltausch, dann symmetrisch für die Daten.

---

## Teil 2: Python-Praxis — Buchstaben als Zahlen

### `ord()` und `chr()`: Buchstaben ↔ Zahlen

Jeder Buchstabe hat eine Nummer (ASCII-Code):

```python
print(ord("A"))   # 65
print(ord("B"))   # 66
print(ord("Z"))   # 90

print(chr(65))    # "A"
print(chr(66))    # "B"
print(chr(90))    # "Z"
```

**Das Prinzip:**
- `ord("A")` → 65 (Buchstabe → Zahl)
- `chr(65)` → "A" (Zahl → Buchstabe)

### Caesar-Verschlüsselung in Python

```python
def caesar_verschluesseln(text, verschiebung):
    ergebnis = ""
    for buchstabe in text:
        if buchstabe.isalpha():  # Nur Buchstaben verschieben
            code = ord(buchstabe) + verschiebung
            ergebnis = ergebnis + chr(code)
        else:
            ergebnis = ergebnis + buchstabe  # Leerzeichen etc. beibehalten
    return ergebnis

# Verschlüsseln
geheim = caesar_verschluesseln("HALLO", 3)
print(geheim)  # KDOOR

# Entschlüsseln: gleiche Funktion, negative Verschiebung
klartext = caesar_verschluesseln("KDOOR", -3)
print(klartext)  # HALLO
```

### Durch einen String iterieren

```python
text = "HALLO"
for buchstabe in text:
    print(buchstabe, "→", ord(buchstabe))

# Ausgabe:
# H → 72
# A → 65
# L → 76
# L → 76
# O → 79
```

> **Heute neu:** `ord()`, `chr()`, und String-Iteration mit `for buchstabe in text:`
