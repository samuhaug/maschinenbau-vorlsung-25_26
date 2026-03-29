# V18: Passwörter und Hashes — Lösungen

---

## Aufgabe 1: Theorie-Check

**a)** Drei Eigenschaften eines Hashes:
1. **Einweg:** Aus dem Hash kann man den Originaltext nicht zurückrechnen
2. **Deterministisch:** Gleicher Input ergibt immer den gleichen Hash
3. **Lawineneffekt:** Kleinste Änderung am Input → komplett anderer Hash

**b)** Wenn ein Angreifer die Datenbank stiehlt, sieht er nur Hashes — nicht die echten Passwörter. Aus den Hashes kann er die Passwörter nicht direkt zurückrechnen.

**c)** Login-Schritte:
1. Benutzer gibt Passwort ein
2. System berechnet den Hash des eingegebenen Passworts
3. System vergleicht den berechneten Hash mit dem gespeicherten Hash
4. Stimmen sie überein → Login erfolgreich

---

## Aufgabe 2: Hash-Experimente

```python
import hashlib

# Hash-Berechnungen
hash1 = hashlib.md5("Maschinenbau".encode()).hexdigest()
print(f"Maschinenbau:  {hash1}")

hash2 = hashlib.md5("maschinenbau".encode()).hexdigest()
print(f"maschinenbau:  {hash2}")

hash3 = hashlib.md5("Maschinenbau1".encode()).hexdigest()
print(f"Maschinenbau1: {hash3}")

# Antwort: Die Hashes sind komplett verschieden (Lawineneffekt)!

# Passwort-Check
gespeicherter_hash = hashlib.md5("sicher2024".encode()).hexdigest()

passwort = input("Passwort eingeben: ")
eingabe_hash = hashlib.md5(passwort.encode()).hexdigest()

if eingabe_hash == gespeicherter_hash:
    print("Login erfolgreich!")
else:
    print("Falsches Passwort!")
```

---

## Aufgabe 3: Passwort-Knacker

```python
import hashlib

gestohlener_hash = "5f4dcc3b5aa765d61d8327deb882cf99"

woerterbuch = [
    "123456",
    "passwort",
    "hallo123",
    "qwerty",
    "password",
    "admin",
    "geheim",
    "letmein",
    "abc123",
    "monkey"
]

for versuch in woerterbuch:
    versuch_hash = hashlib.md5(versuch.encode()).hexdigest()
    if versuch_hash == gestohlener_hash:
        print(f"GEKNACKT! Das Passwort ist: {versuch}")
        break
else:
    print("Passwort nicht im Wörterbuch gefunden.")
```

**Ergebnis:** Das Passwort ist `password` (MD5-Hash: `5f4dcc3b5aa765d61d8327deb882cf99`)

### Bonus: Datei-basierter Knacker

```python
import hashlib

gestohlener_hash = "5f4dcc3b5aa765d61d8327deb882cf99"

# Passwörter aus Datei lesen
with open("woerterbuch.txt", "r") as datei:
    for zeile in datei:
        versuch = zeile.strip()  # Zeilenumbruch entfernen
        versuch_hash = hashlib.md5(versuch.encode()).hexdigest()
        if versuch_hash == gestohlener_hash:
            print(f"GEKNACKT! Das Passwort ist: {versuch}")
            break
    else:
        print("Passwort nicht im Wörterbuch gefunden.")
```
