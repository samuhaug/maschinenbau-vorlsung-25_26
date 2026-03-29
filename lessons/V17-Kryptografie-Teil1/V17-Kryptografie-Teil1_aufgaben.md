# V17: Geheime Nachrichten — Aufgaben

> **Punkte-System:** Sammle Punkte für die Klausurvorbereitung!

---

## Aufgabe 1: Theorie-Check (2 Punkte)

**a)** Verschlüssle das Wort `PYTHON` mit der Caesar-Chiffre (Verschiebung +3). Mache es von Hand!

| P | Y | T | H | O | N |
|---|---|---|---|---|---|
| _ | _ | _ | _ | _ | _ |

**b)** Was ist der Unterschied zwischen symmetrischer und asymmetrischer Verschlüsselung? Nenne jeweils ein Beispiel.

**c)** Was geben diese Python-Befehle aus?

```python
print(ord("A"))
print(chr(72))
print(ord("B") - ord("A"))
```

---

## Aufgabe 2: Caesar-Verschlüsselung programmieren (4 Punkte)

Vervollständige die Funktion, die einen Text mit der Caesar-Chiffre verschlüsselt.

```python
def caesar(text, verschiebung):
    ergebnis = ""
    for buchstabe in text:
        if buchstabe.isalpha():
            # TODO: Berechne den neuen ASCII-Code
            # Tipp: ord(buchstabe) + verschiebung
            neuer_code = ___
            ergebnis = ergebnis + chr(neuer_code)
        else:
            # Leerzeichen und Sonderzeichen nicht verändern
            ergebnis = ergebnis + buchstabe
    return ergebnis

# Test: Verschlüsseln
geheim = caesar("HALLO WELT", 3)
print(f"Verschlüsselt: {geheim}")    # Erwartet: KDOOR ZHOW

# Test: Entschlüsseln (negative Verschiebung!)
klartext = caesar(geheim, -3)
print(f"Entschlüsselt: {klartext}")   # Erwartet: HALLO WELT
```

---

## Aufgabe 3: Nachrichten-Knacker (5 Punkte)

Jemand hat dir eine geheime Nachricht geschickt — aber du kennst die Verschiebung nicht!

```
Geheimtext: "LQIRUPDWLN LVW WROO"
```

Schreibe ein Programm, das **alle 26 möglichen Verschiebungen** durchprobiert, damit du den Klartext findest.

```python
geheimtext = "LQIRUPDWLN LVW WROO"

for verschiebung in range(26):
    # TODO: Entschlüssle den Text mit negativer Verschiebung
    # Tipp: Benutze deine caesar()-Funktion von Aufgabe 2
    klartext = caesar(geheimtext, ___)
    print(f"Verschiebung {verschiebung:2d}: {klartext}")

# Schau dir die Ausgabe an — welche Verschiebung ergibt einen sinnvollen Text?
```

**Bonus (+ 2 Punkte):** Erweitere das Programm: Der Benutzer gibt eine geheime Nachricht per `input()` ein. Das Programm probiert alle 26 Verschiebungen und der Benutzer wählt, welche richtig ist.

---

## Punkte-Übersicht

| Aufgabe | Thema | Punkte |
|---------|-------|--------|
| 1 | Theorie-Check | 2 |
| 2 | Caesar programmieren | 4 |
| 3 | Nachrichten-Knacker | 5 |
| Bonus | Interaktiver Knacker | +2 |
| **Gesamt** | | **max. 13** |
