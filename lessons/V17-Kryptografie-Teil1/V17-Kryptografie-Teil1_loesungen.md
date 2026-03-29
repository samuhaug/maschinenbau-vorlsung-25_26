# V17: Geheime Nachrichten — Lösungen

---

## Aufgabe 1: Theorie-Check

**a)** PYTHON mit Verschiebung +3:

| P | Y | T | H | O | N |
|---|---|---|---|---|---|
| S | B | W | K | R | Q |

**b)** 
- **Symmetrisch:** Gleicher Schlüssel zum Ver- und Entschlüsseln (z.B. Caesar-Chiffre, AES). Problem: Schlüsseltausch.
- **Asymmetrisch:** Zwei Schlüssel — öffentlich (zum Verschlüsseln) und privat (zum Entschlüsseln). Beispiel: RSA, HTTPS.

**c)**
```python
print(ord("A"))           # 65
print(chr(72))            # H
print(ord("B") - ord("A")) # 1
```

---

## Aufgabe 2: Caesar-Verschlüsselung

```python
def caesar(text, verschiebung):
    ergebnis = ""
    for buchstabe in text:
        if buchstabe.isalpha():
            neuer_code = ord(buchstabe) + verschiebung
            ergebnis = ergebnis + chr(neuer_code)
        else:
            ergebnis = ergebnis + buchstabe
    return ergebnis

# Test: Verschlüsseln
geheim = caesar("HALLO WELT", 3)
print(f"Verschlüsselt: {geheim}")    # KDOOR ZHOW

# Test: Entschlüsseln
klartext = caesar(geheim, -3)
print(f"Entschlüsselt: {klartext}")   # HALLO WELT
```

---

## Aufgabe 3: Nachrichten-Knacker

```python
geheimtext = "LQIRUPDWLN LVW WROO"

for verschiebung in range(26):
    klartext = caesar(geheimtext, -verschiebung)
    print(f"Verschiebung {verschiebung:2d}: {klartext}")
```

**Lösung:** Verschiebung 3 ergibt: `INFORMATIK IST TOLL`

### Bonus: Interaktiver Knacker

```python
geheimtext = input("Gib den Geheimtext ein: ").upper()

print("\nAlle möglichen Entschlüsselungen:")
print("-" * 40)

for verschiebung in range(26):
    klartext = caesar(geheimtext, -verschiebung)
    print(f"  [{verschiebung:2d}] {klartext}")

wahl = int(input("\nWelche Verschiebung ist richtig? "))
ergebnis = caesar(geheimtext, -wahl)
print(f"\nDie Nachricht lautet: {ergebnis}")
```
