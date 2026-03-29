# V18: Passwörter und Hashes — Warum man Passwörter nie im Klartext speichert

> **Lernziele dieser Vorlesung:**
> - Verstehen, was ein Hash ist ("digitaler Fingerabdruck")
> - Wissen, warum Passwörter nie im Klartext gespeichert werden
> - Einen einfachen Wörterbuch-Angriff verstehen
> - Python: `hashlib` zur Hash-Berechnung nutzen

---

## Teil 1: Theorie — Hashes und Passwörter

### Was ist ein Hash?

Ein **Hash** ist ein digitaler Fingerabdruck — eine Einweg-Funktion, die aus beliebigen Daten eine feste Zeichenkette erzeugt.

```
"Hallo"     → 59d9a6df06b9f610f7db8e036896ed03
"Hallo!"    → d84f11f09db5c1c45e18dae48ffe83d0
"hallo"     → 598d4c200461b81522a3328565c25f7c
```

**Drei wichtige Eigenschaften:**

| Eigenschaft | Bedeutung |
|-------------|-----------|
| **Einweg** | Aus dem Hash kann man den Originaltext NICHT zurückrechnen |
| **Deterministisch** | Gleicher Input → immer gleicher Hash |
| **Lawineneffekt** | Kleinste Änderung → komplett anderer Hash |

> **Analogie:** Ein Hash ist wie ein Fingerabdruck. Man kann ihn vergleichen, aber aus dem Abdruck nicht die Person rekonstruieren.

### Warum Passwörter nie im Klartext speichern?

**Schlecht** (so machen es leider manche):
```
Datenbank:
Benutzer: max     Passwort: geheim123
Benutzer: anna    Passwort: katze456
```

Wenn ein Hacker die Datenbank stiehlt, hat er alle Passwörter!

**Richtig** (so macht man es):
```
Datenbank:
Benutzer: max     Hash: 5f4dcc3b5aa765d61d8327deb882cf99
Benutzer: anna    Hash: a152e841783914146e4bcd4f39100686
```

**Beim Login:**
1. Benutzer gibt Passwort ein
2. System berechnet den Hash des eingegebenen Passworts
3. System vergleicht den berechneten Hash mit dem gespeicherten Hash
4. Stimmen sie überein → Login erfolgreich!

> Selbst der Server-Administrator kennt dein Passwort nicht!

### Wörterbuch-Angriff

Ein Angreifer probiert häufige Passwörter durch und vergleicht die Hashes:

```
hash("123456")    → e10adc...  ← stimmt nicht
hash("passwort")  → 5f4dcc...  ← stimmt nicht
hash("geheim123") → 5f4dcc...  ← TREFFER!
```

> **Darum sind sichere Passwörter wichtig!** Einfache Wörter werden in Sekunden geknackt.

### Zusammenfassung Theorie

- **Hash** = digitaler Fingerabdruck (Einweg, deterministisch, Lawineneffekt)
- **Passwörter** werden als Hash gespeichert, nie als Klartext
- **Login** = Hash des eingegebenen Passworts mit gespeichertem Hash vergleichen
- **Wörterbuch-Angriff** = häufige Passwörter durchprobieren

---

## Teil 2: Python-Praxis — hashlib

### Hash berechnen mit Python

```python
import hashlib

# Hash eines Textes berechnen
text = "Hallo Welt"
hash_wert = hashlib.md5(text.encode()).hexdigest()
print(hash_wert)  # fc5e038d38a57032085441e7fe7010b0
```

**Die 3 Schritte:**
1. `text.encode()` — Text in Bytes umwandeln
2. `hashlib.md5(...)` — Hash berechnen
3. `.hexdigest()` — Als lesbaren Hex-String ausgeben

### Gleicher Input → gleicher Hash

```python
import hashlib

wort1 = "Python"
wort2 = "Python"
wort3 = "python"  # Kleinbuchstabe!

print(hashlib.md5(wort1.encode()).hexdigest())
print(hashlib.md5(wort2.encode()).hexdigest())  # identisch mit wort1!
print(hashlib.md5(wort3.encode()).hexdigest())  # komplett anders!
```

### Einfacher Passwort-Check

```python
import hashlib

# Gespeicherter Hash (z.B. aus einer Datenbank)
gespeicherter_hash = hashlib.md5("geheim123".encode()).hexdigest()

# Benutzer-Login
eingabe = input("Passwort: ")
eingabe_hash = hashlib.md5(eingabe.encode()).hexdigest()

if eingabe_hash == gespeicherter_hash:
    print("Login erfolgreich!")
else:
    print("Falsches Passwort!")
```

> **Heute neu:** `hashlib.md5()`, `.encode()`, `.hexdigest()` — nur 3 Zeilen für einen Hash!
