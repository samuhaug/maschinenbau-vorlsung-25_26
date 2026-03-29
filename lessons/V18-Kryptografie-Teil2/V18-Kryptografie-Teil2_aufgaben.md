# V18: Passwörter und Hashes — Aufgaben

> **Punkte-System:** Sammle Punkte für die Klausurvorbereitung!

---

## Aufgabe 1: Theorie-Check (2 Punkte)

**a)** Nenne die drei wichtigen Eigenschaften eines Hashes.

**b)** Warum speichert man Passwörter als Hash und nicht als Klartext?

**c)** Was passiert beim Login, wenn Passwörter als Hash gespeichert sind? Beschreibe die Schritte.

---

## Aufgabe 2: Hash-Experimente (4 Punkte)

Berechne Hashes und beobachte den Lawineneffekt.

```python
import hashlib

# TODO: Berechne den MD5-Hash von "Maschinenbau"
# Tipp: hashlib.md5("Maschinenbau".encode()).hexdigest()
hash1 = ___
print(f"Maschinenbau:  {hash1}")

# TODO: Berechne den Hash von "maschinenbau" (Kleinbuchstaben!)
hash2 = ___
print(f"maschinenbau:  {hash2}")

# TODO: Berechne den Hash von "Maschinenbau1"
hash3 = ___
print(f"Maschinenbau1: {hash3}")

# Frage: Sind die Hashes ähnlich oder komplett verschieden?
# Antwort: ___

# === Passwort-Check ===
# Gespeicherter Hash für das Passwort "sicher2024"
gespeicherter_hash = hashlib.md5("sicher2024".encode()).hexdigest()

# TODO: Frage den Benutzer nach dem Passwort
passwort = input("Passwort eingeben: ")

# TODO: Berechne den Hash der Eingabe
eingabe_hash = ___

# TODO: Vergleiche die Hashes und gib "Login OK" oder "Falsch" aus
if ___:
    print("Login erfolgreich!")
else:
    print("Falsches Passwort!")
```

---

## Aufgabe 3: Passwort-Knacker (5 Punkte)

Du hast einen gestohlenen Hash gefunden. Knacke das Passwort mit einem Wörterbuch-Angriff!

```python
import hashlib

# Dieser Hash wurde aus einer "gestohlenen" Datenbank gelesen
gestohlener_hash = "5f4dcc3b5aa765d61d8327deb882cf99"

# Wörterbuch mit häufigen Passwörtern
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

# TODO: Probiere jedes Passwort aus dem Wörterbuch
for versuch in woerterbuch:
    # TODO: Berechne den Hash des Versuchs
    versuch_hash = ___

    # TODO: Vergleiche mit dem gestohlenen Hash
    if versuch_hash == gestohlener_hash:
        print(f"GEKNACKT! Das Passwort ist: {versuch}")
        break
else:
    print("Passwort nicht im Wörterbuch gefunden.")
```

**Bonus (+ 2 Punkte):** Erweitere den Knacker: Lies die Passwörter aus einer Datei statt aus einer Liste. Erstelle dazu eine Datei `woerterbuch.txt` mit einem Passwort pro Zeile.

---

## Punkte-Übersicht

| Aufgabe | Thema | Punkte |
|---------|-------|--------|
| 1 | Theorie-Check | 2 |
| 2 | Hash-Experimente | 4 |
| 3 | Passwort-Knacker | 5 |
| Bonus | Datei-basierter Knacker | +2 |
| **Gesamt** | | **max. 13** |
