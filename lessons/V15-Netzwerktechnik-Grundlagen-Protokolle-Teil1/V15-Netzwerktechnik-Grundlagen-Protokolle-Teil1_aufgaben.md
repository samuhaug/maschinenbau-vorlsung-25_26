# V15: Übungsaufgaben — Wie funktioniert das Internet?

---

## Aufgabe 1: Client-Server verstehen (Theorie)

a) Erkläre das Client-Server-Prinzip mit einer eigenen Analogie (nicht das Restaurant-Beispiel).

b) Was ist der Unterschied zwischen einer IP-Adresse und einem Port?

c) Was macht DNS? Erkläre es in einem Satz.

---

## Aufgabe 2: Erste Funktionen (Python)

Schreibe eine Funktion, die eine IP-Adresse prüft (vereinfacht).

**Starter-Code:**
```python
def ist_gueltige_ip(ip_text):
    # Eine gültige IP hat genau 3 Punkte
    anzahl_punkte = ip_text.count(".")
    if anzahl_punkte == 3:
        return True
    else:
        return False

# Teste die Funktion
print(ist_gueltige_ip("192.168.1.1"))     # True
print(ist_gueltige_ip("192.168.1"))        # False
print(ist_gueltige_ip("hallo"))            # False
```

**Erweitere:** Schreibe eine zweite Funktion `ist_localhost(ip)`, die prüft ob die IP `"127.0.0.1"` ist.

---

## Aufgabe 3: Maschinen-Status-Funktion (Python)

Schreibe eine Funktion, die den Status einer Maschine basierend auf der Temperatur zurückgibt.

**Starter-Code:**
```python
def maschinen_status(name, temperatur):
    if temperatur > 80:
        return f"🔴 {name}: ALARM — sofort abschalten!"
    elif ___:                              # TODO: Über 60°C
        return f"🟡 {name}: WARNUNG"
    else:
        return f"🟢 {name}: OK"

# Teste die Funktion mit verschiedenen Maschinen
print(maschinen_status("CNC-01", 45))
print(maschinen_status("CNC-02", 72))
print(maschinen_status("Drehbank", 95))
```

**Bonus:** Schreibe eine Funktion `pruefe_alle(maschinen)` die eine Liste von Maschinen durchgeht. Die Liste enthält Tupel wie `("CNC-01", 45)`.
