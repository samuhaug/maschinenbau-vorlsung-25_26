# V15: Lösungen — Wie funktioniert das Internet?

---

## Aufgabe 1: Client-Server verstehen

**a)** Beispiel-Analogie: Wie ein Bibliotheksbesuch — du (Client) gehst zum Schalter und fragst nach einem Buch. Der Bibliothekar (Server) sucht es und gibt es dir. Du musst nicht wissen, wo es im Regal steht.

**b)** IP-Adresse = die Adresse eines Computers im Netzwerk (z.B. 192.168.1.1). Port = "Tür" zu einem bestimmten Dienst auf diesem Computer (z.B. Port 80 für Webseiten). Ein Computer hat eine IP, aber viele Ports.

**c)** DNS übersetzt Webseiten-Namen (wie google.de) in IP-Adressen (wie 173.194.70.113) — wie ein Telefonbuch für das Internet.

---

## Aufgabe 2: Erste Funktionen

```python
def ist_gueltige_ip(ip_text):
    anzahl_punkte = ip_text.count(".")
    if anzahl_punkte == 3:
        return True
    else:
        return False

def ist_localhost(ip):
    if ip == "127.0.0.1":
        return True
    else:
        return False

print(ist_gueltige_ip("192.168.1.1"))     # True
print(ist_gueltige_ip("192.168.1"))        # False
print(ist_localhost("127.0.0.1"))          # True
print(ist_localhost("192.168.1.1"))        # False
```

---

## Aufgabe 3: Maschinen-Status-Funktion

```python
def maschinen_status(name, temperatur):
    if temperatur > 80:
        return f"🔴 {name}: ALARM — sofort abschalten!"
    elif temperatur > 60:
        return f"🟡 {name}: WARNUNG"
    else:
        return f"🟢 {name}: OK"

print(maschinen_status("CNC-01", 45))
print(maschinen_status("CNC-02", 72))
print(maschinen_status("Drehbank", 95))
```

**Bonus:**
```python
def pruefe_alle(maschinen):
    for name, temp in maschinen:
        print(maschinen_status(name, temp))

maschinen = [("CNC-01", 45), ("CNC-02", 72), ("Drehbank", 95)]
pruefe_alle(maschinen)
```
