# V15: Netzwerktechnik Grundlagen & Protokolle – Teil 1 – Lösungen

## Teil A: Theorie-Lösungen

### Lösung 1: OSI-Schichten zuordnen ⭐

**Zuordnung:**

| Protokoll/Technologie | OSI-Schicht | Nummer |
|----------------------|-------------|--------|
| HTTP | Anwendungsschicht (Application Layer) | 7 |
| Ethernet | Sicherungsschicht (Data Link Layer) | 2 |
| TCP | Transportschicht (Transport Layer) | 4 |
| IP | Vermittlungsschicht (Network Layer) | 3 |
| DNS | Anwendungsschicht (Application Layer) | 7 |
| WLAN (IEEE 802.11) | Sicherungsschicht (Data Link Layer) | 2 |
| TLS/SSL | Darstellungsschicht (Presentation Layer) | 6 |
| MAC-Adresse | Sicherungsschicht (Data Link Layer) | 2 |
| Glasfaserkabel | Bitübertragungsschicht (Physical Layer) | 1 |
| SMTP | Anwendungsschicht (Application Layer) | 7 |

**Beispiel-Erklärungen:**

**HTTP (Schicht 7 - Anwendungsschicht):**
HTTP ist ein Protokoll der Anwendungsschicht, weil es direkt von Anwendungen (Web-Browsern, Web-Servern) genutzt wird, um Ressourcen (HTML-Seiten, Bilder, APIs) über das Netzwerk anzufordern und zu übertragen. Es definiert die Kommunikation zwischen Client und Server auf einer für Menschen verständlichen Ebene (URLs, HTTP-Methoden wie GET/POST). HTTP kümmert sich nicht um die technischen Details der Datenübertragung – diese Aufgaben werden an die darunter liegenden Schichten delegiert.

**TCP (Schicht 4 - Transportschicht):**
TCP arbeitet auf der Transportschicht, weil es für die zuverlässige Ende-zu-Ende-Kommunikation zwischen Anwendungen auf verschiedenen Hosts verantwortlich ist. TCP segmentiert Datenströme, nummeriert Segmente, bestätigt den Empfang und fordert bei Verlust eine erneute Übertragung an. Zudem nutzt TCP Port-Nummern, um verschiedene Anwendungen auf demselben Host zu unterscheiden. TCP abstrahiert die darunterliegende Netzwerkstruktur und bietet der Anwendungsschicht eine zuverlässige Verbindung.

**IP (Schicht 3 - Vermittlungsschicht):**
IP ist das zentrale Protokoll der Vermittlungsschicht, weil es für die logische Adressierung (IP-Adressen) und das Routing von Paketen durch verschiedene Netzwerke hinweg zuständig ist. IP bestimmt den optimalen Pfad vom Sender zum Empfänger, auch wenn diese in unterschiedlichen physikalischen Netzwerken liegen. Es fragmentiert Pakete bei Bedarf und leitet sie an den nächsten Router (Hop) weiter.

**Ethernet (Schicht 2 - Sicherungsschicht):**
Ethernet arbeitet auf der Sicherungsschicht, weil es für die fehlerfreie Übertragung von Daten zwischen direkt verbundenen Geräten im lokalen Netzwerk sorgt. Ethernet definiert, wie Datenpakete (Frames) strukturiert werden, nutzt MAC-Adressen zur physikalischen Adressierung und implementiert Mechanismen zur Fehlererkennung (CRC). Zudem regelt Ethernet den Zugriff auf das gemeinsame Übertragungsmedium (CSMA/CD).

---

### Lösung 2: IP-Adressen klassifizieren und umrechnen ⭐⭐

**Teil 1: Klassifikation**

| IPv4-Adresse | Typ | Adressbereich (falls privat) | Erklärung |
|--------------|-----|------------------------------|-----------|
| `192.168.50.10` | **Privat** | `192.168.0.0/16` | Liegt im privaten Bereich für Heimnetzwerke |
| `8.8.8.8` | **Öffentlich** | – | Google DNS-Server, öffentlich routbar |
| `172.20.15.100` | **Privat** | `172.16.0.0/12` | Liegt zwischen 172.16.0.0 und 172.31.255.255 |
| `10.255.255.255` | **Privat** | `10.0.0.0/8` | Höchste Adresse im 10.0.0.0/8 Bereich |
| `172.32.0.1` | **Öffentlich** | – | Liegt **außerhalb** des privaten Bereichs (172.16–172.31) |
| `127.0.0.1` | **Loopback** (Spezial) | `127.0.0.0/8` | Adressiert das lokale Gerät selbst (localhost) |

**Erklärung zu 172.32.0.1:**
Der private Bereich für Class-B-Adressen ist **`172.16.0.0` bis `172.31.255.255`** (`172.16.0.0/12`). Die Adresse `172.32.0.1` liegt **außerhalb** dieses Bereichs (32 > 31) und ist daher eine öffentliche IP-Adresse.

---

**Teil 2: Binäre Umrechnung**

```
IP-Adresse: 192.168.1.100

Dezimal:  192      .  168      .  1        .  100
Binär:    11000000 .  10101000 .  00000001 .  01100100
```

**Rechnung:**
- **192**: 128 + 64 = `11000000`
- **168**: 128 + 32 + 8 = `10101000`
- **1**: `00000001`
- **100**: 64 + 32 + 4 = `01100100`

**Merkh

ilfe:** Potenzen von 2 für jedes Bit (von links nach rechts):
```
128  64  32  16  8  4  2  1
```

Beispiel für 168:
- 168 - 128 = 40 → Bit 128 ist **1**
- 40 - 64? Nein → Bit 64 ist **0**
- 40 - 32 = 8 → Bit 32 ist **1**
- 8 - 16? Nein → Bit 16 ist **0**
- 8 - 8 = 0 → Bit 8 ist **1**
- Rest: 0 → Bits 4, 2, 1 sind **0**
- Ergebnis: `10101000`

---

**Teil 3: IPv6-Notation**

```
Original: 2001:0db8:0000:0000:0000:ff00:0042:8329
Gekürzt:  2001:db8::ff00:42:8329
```

**Angewandte Regeln:**
1. **Führende Nullen weglassen**: `0db8` → `db8`, `0042` → `42`
2. **Längste Folge von Null-Gruppen mit `::` ersetzen**: `0000:0000:0000` → `::`

**Wichtig:** `::` darf nur **einmal** vorkommen! Hier ersetzt es die drei Null-Gruppen in der Mitte.

---

### Lösung 3: Subnetting-Szenario ⭐⭐⭐

**Gegeben:**
- Netzwerk: `172.16.100.0/24`
- Aufteilen in: **8 Subnetze** (gleich groß)

---

**a) Berechnung der neuen Präfixlänge**

**Zusätzliche Bits für Subnetz-ID:**
- 8 Subnetze benötigt
- Kleinste Zweierpotenz ≥ 8: **2³ = 8**
- **3 zusätzliche Bits** erforderlich

**Neue Präfixlänge:**
- Original: `/24` (24 Netzwerk-Bits)
- Zusätzlich: `+3` Bits für Subnetze
- **Neue Präfixlänge: `/27`**

**Neue Subnetzmaske:**
- `/27` bedeutet: 27 Netzwerk-Bits, 5 Host-Bits
- Binär: `11111111.11111111.11111111.11100000`
- Dezimal: **`255.255.255.224`**

**Rechnung für letztes Oktett:**
- 27 Bits gesamt → 27 - 24 = 3 Bits im letzten Oktett auf 1
- `11100000` = 128 + 64 + 32 = **224**

---

**b) Hosts pro Subnetz**

**Host-Bits:**
- Gesamt: 32 Bits
- Netzwerk + Subnetz: 27 Bits
- **Host-Bits: 32 - 27 = 5 Bits**

**Anzahl Adressen pro Subnetz:**
- **2⁵ = 32 Adressen** pro Subnetz

**Nutzbare Hosts:**
- Gesamt: 32 Adressen
- Abzüglich Netzwerkadresse (alle Host-Bits 0): -1
- Abzüglich Broadcast-Adresse (alle Host-Bits 1): -1
- **Nutzbare Hosts: 32 - 2 = 30**

---

**c) Subnetz-Bereiche**

**Block-Größe:** 256 - 224 = **32**

Die Netzwerkadressen erhöhen sich jeweils um 32:

| Subnetz | Netzwerkadresse | Erste nutzbare IP | Letzte nutzbare IP | Broadcast-Adresse |
|---------|-----------------|-------------------|--------------------|-------------------|
| **1** | `172.16.100.0/27` | `172.16.100.1` | `172.16.100.30` | `172.16.100.31` |
| **2** | `172.16.100.32/27` | `172.16.100.33` | `172.16.100.62` | `172.16.100.63` |
| **3** | `172.16.100.64/27` | `172.16.100.65` | `172.16.100.94` | `172.16.100.95` |

**Rechnung für Subnetz 1:**
- Netzwerkadresse: `172.16.100.0` (Basis)
- Erste nutzbare: Netzwerkadresse + 1 = `172.16.100.1`
- Letzte nutzbare: Netzwerkadresse + 30 = `172.16.100.30`
- Broadcast: Netzwerkadresse + 31 = `172.16.100.31`

**Rechnung für Subnetz 2:**
- Netzwerkadresse: `172.16.100.0` + 32 = `172.16.100.32`
- Erste nutzbare: `172.16.100.33`
- Letzte nutzbare: `172.16.100.62`
- Broadcast: `172.16.100.63`

**Vollständige Übersicht aller 8 Subnetze:**

| Subnetz | Netzwerkadresse | Erster Host | Letzter Host | Broadcast | Nutzbare Hosts |
|---------|-----------------|-------------|--------------|-----------|----------------|
| 1 | 172.16.100.0/27 | .1 | .30 | .31 | 30 |
| 2 | 172.16.100.32/27 | .33 | .62 | .63 | 30 |
| 3 | 172.16.100.64/27 | .65 | .94 | .95 | 30 |
| 4 | 172.16.100.96/27 | .97 | .126 | .127 | 30 |
| 5 | 172.16.100.128/27 | .129 | .158 | .159 | 30 |
| 6 | 172.16.100.160/27 | .161 | .190 | .191 | 30 |
| 7 | 172.16.100.192/27 | .193 | .222 | .223 | 30 |
| 8 | 172.16.100.224/27 | .225 | .254 | .255 | 30 |

---

**d) Praktische Anwendung**

**Frage:** Ist ein Subnetz mit `/27` ausreichend für **20 Hosts**?

**Antwort:** **Ja, ausreichend.**

**Begründung:**
Jedes Subnetz bietet **30 nutzbare IP-Adressen**. Die Personalabteilung benötigt mindestens 20 Hosts. Da 30 > 20, ist die Kapazität ausreichend. Es bleiben sogar 10 Adressen für zukünftiges Wachstum übrig.

---

**Bonus: IT-Abteilung mit 60 Hosts**

**Frage:** Können zwei benachbarte Subnetze zusammengefasst werden?

**Antwort:** **Ja, durch Supernetting.**

**Vorgehensweise:**
Zwei benachbarte `/27`-Subnetze ergeben zusammen ein `/26`-Subnetz.

**Beispiel: Subnetze 1 + 2 zusammenfassen**

**Original:**
- Subnetz 1: `172.16.100.0/27` (0–31)
- Subnetz 2: `172.16.100.32/27` (32–63)

**Zusammengefasst:**
- **Neues Subnetz: `172.16.100.0/26`**
- Bereich: `172.16.100.0` bis `172.16.100.63`
- Nutzbare Hosts: **2⁶ - 2 = 64 - 2 = 62 Hosts**

**Neue CIDR-Notation:** `172.16.100.0/26`

**Nutzbarer IP-Bereich:**
- Netzwerkadresse: `172.16.100.0`
- Erste nutzbare IP: `172.16.100.1`
- Letzte nutzbare IP: `172.16.100.62`
- Broadcast-Adresse: `172.16.100.63`

**Ergebnis:** 62 nutzbare Hosts sind ausreichend für die IT-Abteilung (60 Hosts benötigt).

**Wichtig:** Dies funktioniert nur bei **benachbarten** Subnetzen, deren Netzwerkadressen sich korrekt zur nächstgrößeren Präfixlänge alignen (hier: beide sind Vielfache von 64).

---

## Teil B: Python-Lösungen

### Lösung P1: Netzwerk-Paket-Analyse

**Lösung** (`netzwerk_analyse.py`):

```python
import csv

def analysiere_pakete(dateiname):
    # Dicts für Zählungen initialisieren
    protokoll_count = {}
    port_count = {}
    maschinen_count = {}
    scada_maschinen = []
    gesamt_bytes = 0
    pakete_gesamt = 0
    
    try:
        with open(dateiname, 'r') as f:
            reader = csv.DictReader(f)
            for zeile in reader:
                try:
                    protokoll = zeile['Protokoll']
                    port = int(zeile['Port'])
                    groesse = int(zeile['Paketgroesse_Bytes'])
                    maschine = zeile['Maschine_ID']
                    ziel_ip = zeile['Ziel_IP']
                    
                    # Protokoll zählen
                    if protokoll in protokoll_count:
                        protokoll_count[protokoll] += 1
                    else:
                        protokoll_count[protokoll] = 1
                    
                    # Port zählen
                    if port in port_count:
                        port_count[port] += 1
                    else:
                        port_count[port] = 1
                    
                    # Maschinen zählen
                    if maschine in maschinen_count:
                        maschinen_count[maschine] += 1
                    else:
                        maschinen_count[maschine] = 1
                    
                    gesamt_bytes += groesse
                    pakete_gesamt += 1
                    
                    # SCADA-Kommunikation
                    if ziel_ip == '192.168.10.200' and maschine not in scada_maschinen:
                        scada_maschinen.append(maschine)
                        
                except (KeyError, ValueError):
                    continue
        
        # Ausgabe
        print("=== Netzwerk-Paket-Analyse ===\n")
        print("Protokoll-Verteilung:")
        for prot in sorted(protokoll_count.keys()):
            count = protokoll_count[prot]
            prozent = (count / pakete_gesamt * 100) if pakete_gesamt > 0 else 0
            print(f"  {prot}: {count} Pakete ({prozent:.1f}%)")
        
        print("\nIndustrieprotokolle (nach Port):")
        port_namen = {502: "Modbus TCP", 1883: "MQTT", 44818: "OPC UA"}
        for port in sorted(port_count.keys()):
            if port in port_namen:
                print(f"  {port_namen[port]} ({port}): {port_count[port]} Pakete")
        
        print(f"\nNetzwerk-Last:")
        print(f"  Gesamt: {gesamt_bytes / 1024:.1f} KB")
        print(f"  Ø Paketgröße: {gesamt_bytes // pakete_gesamt if pakete_gesamt > 0 else 0} Bytes")
        
        # Top 3 Maschinen
        maschinen_liste = list(maschinen_count.items())
        maschinen_liste.sort(key=lambda x: x[1], reverse=True)
        print(f"\nTop 3 aktivste Maschinen:")
        for i in range(min(3, len(maschinen_liste))):
            maschine, count = maschinen_liste[i]
            print(f"  {i+1}. {maschine}: {count} Pakete")
        
        print(f"\nKommunikation mit SCADA (192.168.10.200):")
        print(f"  Maschinen: {', '.join(sorted(scada_maschinen))}")
            
    except FileNotFoundError:
        print(f"Fehler: Datei '{dateiname}' nicht gefunden")

if __name__ == "__main__":
    analysiere_pakete("netzwerk_pakete.csv")
```

**Erklärung**: Verwendet nur reguläre `dict` mit manueller Prüfung, ob Keys existieren. Keine `defaultdict` oder `Counter`.

---

### Lösung P2: Maschinenkommunikations-Analyse (28 lines)

```python
import json

def lies_maschinen(dateiname):
    try:
        with open(dateiname, 'r') as f:
            daten = json.load(f)
            for maschine in daten['maschinen']:
                yield maschine
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Fehler: {e}")

def analysiere_maschinenkommunikation(dateiname):
    try:
        with open(dateiname, 'r') as f:
            daten = json.load(f)
            
        print("=== Maschinenkommunikations-Analyse ===\n")
        print(f"Produktionshalle: {daten['produktionshalle']['name']} ({daten['produktionshalle']['standort']})\n")
        
        print("Maschinen-Übersicht:")
        for maschine in lies_maschinen(dateiname):
            latenz = maschine['kommunikation']['durchschnittliche_latenz_ms']
            pakete = maschine['kommunikation']['pakete_pro_sekunde']
            print(f"  {maschine['maschine_id']} ({maschine['typ']}): Latenz {latenz}ms, {pakete} Pakete/s")
        
        # Protokoll-Zählung
        protokoll_count = {}
        langsame = []
        fehleranfaellig = []
        
        for maschine in lies_maschinen(dateiname):
            for proto in maschine['protokolle']:
                if proto in protokoll_count:
                    protokoll_count[proto] += 1
                else:
                    protokoll_count[proto] = 1
            
            latenz = maschine['kommunikation']['durchschnittliche_latenz_ms']
            fehlerrate = maschine['kommunikation']['fehlerrate_prozent']
            
            if latenz > 15:
                langsame.append((maschine['maschine_id'], latenz))
            if fehlerrate > 0.15:
                fehleranfaellig.append((maschine['maschine_id'], fehlerrate))
        
        print("\nProtokoll-Unterstützung:")
        for proto in sorted(protokoll_count.keys()):
            print(f"  {proto}: {protokoll_count[proto]} Maschinen")
        
        if langsame or fehleranfaellig:
            print("\nPerformance-Probleme:")
            if langsame:
                print(f"  Langsame Maschinen (>15ms): {', '.join([f'{m} ({l}ms)' for m, l in langsame])}")
            if fehleranfaellig:
                print(f"  Fehleranfällige Maschinen (>0.15%): {', '.join([f'{m} ({f}%)' for m, f in fehleranfaellig])}")
    
    except (FileNotFoundError, KeyError) as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    analysiere_maschinenkommunikation("maschinenkommunikation.json")
```

**Erklärung**: Generator-Funktion `lies_maschinen` verwendet `yield`. Manuelle Zählung mit `dict` statt `Counter`.

---

### Lösung P3: OPC UA-Datenstruktur-Analyse (35 lines)

```python
import xml.etree.ElementTree as ET

def analysiere_opc_server(dateiname):
    try:
        tree = ET.parse(dateiname)
        root = tree.getroot()
        
        print("=== OPC UA-Server-Analyse ===\n")
        
        # Server-Info
        server_info = root.find('server_info')
        if server_info is not None:
            print("Server-Info:")
            name = server_info.find('name')
            vendor = server_info.find('vendor')
            endpoint = server_info.find('endpoint')
            if name is not None:
                print(f"  Name: {name.text}")
            if vendor is not None:
                print(f"  Vendor: {vendor.text}")
            if endpoint is not None:
                print(f"  Endpoint: {endpoint.text}")
        
        print("\nMaschinen und Variablen:")
        
        # Knoten durchgehen
        nodes = root.findall('.//node')
        anzahl_knoten = 0
        anzahl_variablen = 0
        temp_sensoren = 0
        
        for node in nodes:
            anzahl_knoten += 1
            browse_name = node.find('browse_name')
            if browse_name is not None:
                print(f"  {browse_name.text}:")
                
                variables = node.findall('.//variable')
                for var in variables:
                    anzahl_variablen += 1
                    var_name = var.find('browse_name')
                    var_value = var.find('value')
                    var_unit = var.find('unit')
                    
                    if var_name is not None and var_value is not None:
                        unit_text = var_unit.text if var_unit is not None else ""
                        print(f"    - {var_name.text}: {var_value.text} {unit_text}")
                        
                        if unit_text == "°C":
                            temp_sensoren += 1
                
                print()  # Leerzeile
        
        print("Statistik:")
        print(f"  Anzahl Knoten: {anzahl_knoten}")
        print(f"  Anzahl Variablen: {anzahl_variablen}")
        print(f"  Temperatursensoren (°C): {temp_sensoren}")
        
    except (FileNotFoundError, ET.ParseError) as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    analysiere_opc_server("opc_ua_daten.xml")
```

**Erklärung**: XML-Parsing mit `ElementTree`. Manuelle Zählung der Knoten und Variablen ohne externe Hilfsbibliotheken.

---

### Lösung P4: Netzwerk-Latenz-Visualisierung

**Lösung** (`latenz_visualisierung.py`):

```python
import random
import matplotlib.pyplot as plt

def generiere_latenz_messungen(anzahl, basis_latenz=15, varianz=10):
    protokolle = ["Modbus TCP", "MQTT", "OPC UA"]
    for i in range(anzahl):
        yield {
            'timestamp': i,
            'latenz_ms': random.uniform(basis_latenz - varianz, basis_latenz + varianz),
            'protokoll': random.choice(protokolle)
        }

# Daten sammeln
messungen = list(generiere_latenz_messungen(300))

# Nach Protokoll gruppieren
daten_pro_protokoll = {}
for protokoll in ["Modbus TCP", "MQTT", "OPC UA"]:
    daten_pro_protokoll[protokoll] = {
        'timestamps': [],
        'latenzen': []
    }

for messung in messungen:
    protokoll = messung['protokoll']
    daten_pro_protokoll[protokoll]['timestamps'].append(messung['timestamp'])
    daten_pro_protokoll[protokoll]['latenzen'].append(messung['latenz_ms'])

# Visualisierung
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Liniendiagramm
for protokoll, farbe in zip(["Modbus TCP", "MQTT", "OPC UA"], ['blue', 'green', 'red']):
    ax1.plot(daten_pro_protokoll[protokoll]['timestamps'], 
             daten_pro_protokoll[protokoll]['latenzen'], 
             label=protokoll, color=farbe, alpha=0.6, linewidth=0.8)
ax1.set_xlabel('Zeit (Sekunden)')
ax1.set_ylabel('Latenz (ms)')
ax1.set_title('Latenz-Verlauf über Zeit')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Boxplot
boxplot_daten = [daten_pro_protokoll[p]['latenzen'] for p in ["Modbus TCP", "MQTT", "OPC UA"]]
ax2.boxplot(boxplot_daten, labels=["Modbus TCP", "MQTT", "OPC UA"])
ax2.set_ylabel('Latenz (ms)')
ax2.set_title('Latenz-Verteilung nach Protokoll')
ax2.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('latenz_analyse.png', dpi=150)
print("✓ Diagramm gespeichert: latenz_analyse.png")

# Statistik
print("\n=== Netzwerk-Latenz-Analyse ===\n")
for protokoll in ["Modbus TCP", "MQTT", "OPC UA"]:
    latenzen = daten_pro_protokoll[protokoll]['latenzen']
    avg = sum(latenzen) / len(latenzen)
    kritisch = sum(1 for l in latenzen if l > 25)
    print(f"{protokoll}:")
    print(f"  Ø Latenz: {avg:.1f} ms")
    print(f"  Min: {min(latenzen):.1f} ms | Max: {max(latenzen):.1f} ms")
    print(f"  Kritische Messwerte (>25ms): {kritisch}\n")
```

**Erklärung**: Generator produziert Messwerte on-the-fly. Daten werden nach Protokoll gruppiert (manuell mit Listen). Matplotlib erstellt professionelle Multi-Plot-Visualisierung.

---

### Lösung P5: Produktionsdaten-Simulator

**Lösung** (`produktions_simulator.py`):

```python
import random
import matplotlib.pyplot as plt

def simuliere_produktion(maschinen, dauer_sekunden):
    for sekunde in range(dauer_sekunden):
        for maschine in maschinen:
            basis_temp = 75 + (sekunde * 0.2)
            temp = basis_temp + random.uniform(-5, 5)
            
            ausschuss = random.uniform(0, 2)
            if random.random() < 0.05:
                ausschuss = random.uniform(5, 8)
            
            yield {
                'maschine_id': maschine,
                'timestamp': sekunde,
                'stueckzahl': random.randint(8, 12),
                'temperatur_c': min(temp, 100),
                'ausschuss': ausschuss
            }

# Simulation
maschinen = ["CNC-01", "Presse-01", "Robot-01"]
daten = list(simuliere_produktion(maschinen, 60))

# Daten gruppieren
maschinen_daten = {m: {'timestamps': [], 'stueckzahl': [], 'temperatur': [], 'ausschuss': []} for m in maschinen}

for eintrag in daten:
    m = eintrag['maschine_id']
    maschinen_daten[m]['timestamps'].append(eintrag['timestamp'])
    maschinen_daten[m]['stueckzahl'].append(eintrag['stueckzahl'])
    maschinen_daten[m]['temperatur'].append(eintrag['temperatur_c'])
    maschinen_daten[m]['ausschuss'].append(eintrag['ausschuss'])

# Dashboard erstellen
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Stückzahl über Zeit
for maschine, farbe in zip(maschinen, ['blue', 'green', 'red']):
    ax1.plot(maschinen_daten[maschine]['timestamps'], 
             maschinen_daten[maschine]['stueckzahl'],
             label=maschine, color=farbe, linewidth=1.5)
ax1.set_xlabel('Zeit (Sekunden)')
ax1.set_ylabel('Stückzahl pro Sekunde')
ax1.set_title('Produktionsrate über Zeit')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Plot 2: Temperatur mit Warnschwelle
for maschine, farbe in zip(maschinen, ['blue', 'green', 'red']):
    ax2.plot(maschinen_daten[maschine]['timestamps'],
             maschinen_daten[maschine]['temperatur'],
             label=maschine, color=farbe, linewidth=1.5)
ax2.axhline(y=90, color='red', linestyle='--', label='Warnschwelle', linewidth=2)
ax2.set_xlabel('Zeit (Sekunden)')
ax2.set_ylabel('Temperatur (°C)')
ax2.set_title('Temperaturverlauf')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Plot 3: Gesamtproduktion
gesamt_produktion = {m: sum(maschinen_daten[m]['stueckzahl']) for m in maschinen}
ax3.bar(maschinen, [gesamt_produktion[m] for m in maschinen], color=['blue', 'green', 'red'])
ax3.set_ylabel('Gesamtproduktion (Stück)')
ax3.set_title('Gesamtproduktion pro Maschine')
ax3.grid(True, alpha=0.3, axis='y')

# Plot 4: Ausschussrate
for maschine, farbe in zip(maschinen, ['blue', 'green', 'red']):
    ax4.fill_between(maschinen_daten[maschine]['timestamps'],
                      maschinen_daten[maschine]['ausschuss'],
                      alpha=0.5, label=maschine, color=farbe)
ax4.set_xlabel('Zeit (Sekunden)')
ax4.set_ylabel('Ausschussrate (%)')
ax4.set_title('Ausschussrate über Zeit')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('produktion_dashboard.png', dpi=150)

# Kennzahlen
print("=== Produktions-Monitoring (60 Sekunden) ===\n")
print("Gesamtproduktion:")
for maschine in maschinen:
    gesamt = gesamt_produktion[maschine]
    avg_temp = sum(maschinen_daten[maschine]['temperatur']) / len(maschinen_daten[maschine]['temperatur'])
    avg_ausschuss = sum(maschinen_daten[maschine]['ausschuss']) / len(maschinen_daten[maschine]['ausschuss'])
    print(f"  {maschine}: {gesamt} Stück (Ø Temp: {avg_temp:.1f}°C, Ø Ausschuss: {avg_ausschuss:.1f}%)")

print("\n⚠️  Temperatur-Warnungen:")
for maschine in maschinen:
    ueberschreitungen = sum(1 for t in maschinen_daten[maschine]['temperatur'] if t > 90)
    if ueberschreitungen > 0:
        print(f"  {maschine}: {ueberschreitungen} Überschreitungen (>90°C)")

print("\n✓ Dashboard gespeichert: produktion_dashboard.png")
```

**Erklärung**: Komplexer Generator simuliert realistische Produktionsdaten mit Trends. Dashboard verwendet 2×2 Subplot-Grid mit verschiedenen Visualisierungstypen (Linien, Balken, Flächen). Praktisches SCADA-Monitoring-System.

---

## Zusammenfassung

Die refaktorierten V15-Lösungen demonstrieren:
- **P1-P3**: Datenverarbeitung (CSV/JSON/XML) ohne unauthorized features
- **P4**: Professionelle Visualisierung mit Matplotlib (Subplots, Boxplot)
- **P5**: Komplexe Echtzeit-Simulation mit Multi-Plot-Dashboard
- **Manuelle Gruppierung**: Verwendung von Listen/Dicts statt defaultdict
- **Praktische Anwendung**: SCADA-Monitoring, Performance-Analyse, Dashboards
    """
    Generator, der nur Zeilen zurückgibt, die mindestens
    'mindestlaenge' Zeichen haben (nach strip()).
    
    Args:
        dateiname (str): Pfad zur Textdatei
        mindestlaenge (int): Mindestlänge der Zeilen
    
    Yields:
        str: Zeilen, die das Längen-Kriterium erfüllen
    
    Raises:
        FileNotFoundError: Wenn Datei nicht existiert
    """
    try:
        with open(dateiname, "r", encoding="utf-8") as datei:
            for zeile in datei:
                zeile_clean = zeile.strip()
                
                # Leerzeilen ignorieren
                if not zeile_clean:
                    continue
                
                # Nur Zeilen mit ausreichender Länge
                if len(zeile_clean) >= mindestlaenge:
                    yield zeile_clean
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Datei '{dateiname}' wurde nicht gefunden.")


# Test-Programm
if __name__ == "__main__":
    # Testdatei erstellen
    test_inhalt = """Kurz
Diese Zeile ist lang genug
x

Mittlere Länge hier
Superlange Zeile mit vielen Wörtern und Zeichen
"""
    
    with open("test.txt", "w", encoding="utf-8") as f:
        f.write(test_inhalt)
    
    # Generator nutzen
    print("Zeilen mit mindestens 20 Zeichen:")
    print("-" * 50)
    
    for zeile in filtere_zeilen("test.txt", mindestlaenge=20):
        print(zeile)
    
    # Erwartete Ausgabe:
    # Diese Zeile ist lang genug
    # Superlange Zeile mit vielen Wörtern und Zeichen
```

**Erklärung:**

**Generator-Funktion:**
Die Funktion verwendet `yield` statt `return`, was sie zu einem Generator macht. Beim Aufruf wird **kein Code ausgeführt** – stattdessen wird ein Generator-Objekt zurückgegeben. Erst wenn über den Generator iteriert wird (z.B. in der `for`-Schleife), werden die Zeilen tatsächlich eingelesen und verarbeitet.

**Speicher-Effizienz:**
Durch die Verwendung von `yield` wird immer nur **eine Zeile zur Zeit** im Speicher gehalten. Bei großen Dateien (GB-Bereich) ist dies entscheidend, da `.readlines()` alle Zeilen als Liste laden würde.

**Fehlerbehandlung:**
Der `try-except`-Block fängt `FileNotFoundError` ab und gibt eine aussagekräftige Fehlermeldung mit dem Dateinamen aus. Dies erleichtert Debugging erheblich.

**Leere Zeilen ignorieren:**
Nach `.strip()` wird geprüft, ob die Zeile leer ist (`if not zeile_clean`). Leere Zeilen werden mit `continue` übersprungen, sodass sie nicht an den Aufrufer zurückgegeben werden.

**Längenprüfung:**
Nur Zeilen mit `len(zeile_clean) >= mindestlaenge` werden mit `yield` zurückgegeben. Die Bedingung wird **vor** dem yield geprüft, sodass nur valide Zeilen den Aufrufer erreichen.

---

### Lösung 5: CSV-Analyse – Studenten-Datenbank ⭐⭐

**Vollständiges Programm:**

```python
import csv
from collections import defaultdict


def lies_studenten(dateiname):
    """
    Liest Studenten-CSV und gibt Liste von Dictionaries zurück.
    Konvertiert 'Semester' und 'Note' zu Zahlen.
    
    Args:
        dateiname (str): Pfad zur CSV-Datei
    
    Returns:
        list[dict]: Liste aller Studenten mit konvertierten Typen
    
    Raises:
        FileNotFoundError: Wenn Datei nicht existiert
        ValueError: Bei ungültigem Datenformat
    """
    studenten = []
    
    try:
        with open(dateiname, "r", encoding="utf-8") as datei:
            reader = csv.DictReader(datei)
            
            for zeile in reader:
                try:
                    # Typen konvertieren
                    zeile['Semester'] = int(zeile['Semester'])
                    zeile['Note'] = float(zeile['Note'])
                    studenten.append(zeile)
                except (ValueError, KeyError) as e:
                    print(f"⚠️  Überspringe ungültige Zeile: {zeile} ({e})")
        
        return studenten
    
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV-Datei '{dateiname}' nicht gefunden.")


def durchschnittsnote_pro_studiengang(studenten):
    """
    Berechnet Durchschnittsnote pro Studiengang.
    
    Args:
        studenten (list[dict]): Liste aller Studenten
    
    Returns:
        dict: {Studiengang: Durchschnittsnote (float)}
    """
    # Summieren mit defaultdict
    noten_summen = defaultdict(float)
    noten_anzahl = defaultdict(int)
    
    for student in studenten:
        gang = student['Studiengang']
        noten_summen[gang] += student['Note']
        noten_anzahl[gang] += 1
    
    # Durchschnitt berechnen
    durchschnitte = {}
    for gang in noten_summen:
        durchschnitte[gang] = noten_summen[gang] / noten_anzahl[gang]
    
    return durchschnitte


def beste_studenten(studenten, grenzwert=1.8):
    """
    Findet Studenten mit Note besser als Grenzwert, sortiert nach Note.
    
    Args:
        studenten (list[dict]): Liste aller Studenten
        grenzwert (float): Maximale Note (besser = kleiner)
    
    Returns:
        list[dict]: Sortierte Liste der besten Studenten
    """
    gefiltert = [s for s in studenten if s['Note'] < grenzwert]
    sortiert = sorted(gefiltert, key=lambda s: s['Note'])
    return sortiert


def exportiere_informatik_mit_bewertung(studenten, ausgabedatei):
    """
    Exportiert Informatik-Studenten mit zusätzlicher Bewertungs-Spalte.
    
    Args:
        studenten (list[dict]): Liste aller Studenten
        ausgabedatei (str): Pfad zur Ausgabe-CSV
    """
    # Nur Informatik-Studenten filtern
    informatik = [s for s in studenten if s['Studiengang'] == 'Informatik']
    
    # Bewertung hinzufügen
    for student in informatik:
        note = student['Note']
        if note <= 1.5:
            student['Bewertung'] = 'Sehr gut'
        elif note <= 2.0:
            student['Bewertung'] = 'Gut'
        else:
            student['Bewertung'] = 'Befriedigend'
    
    # CSV schreiben
    feldnamen = ['Matrikelnummer', 'Name', 'Studiengang', 'Semester', 'Note', 'Bewertung']
    
    with open(ausgabedatei, "w", newline='', encoding="utf-8") as datei:
        writer = csv.DictWriter(datei, fieldnames=feldnamen)
        writer.writeheader()
        writer.writerows(informatik)
    
    print(f"✅ {len(informatik)} Informatik-Studenten exportiert nach '{ausgabedatei}'")


def main():
    """Hauptprogramm – Führt alle Analysen durch."""
    
    # CSV erstellen (für Test)
    csv_inhalt = """Matrikelnummer,Name,Studiengang,Semester,Note
12345,Alice,Informatik,3,1.3
23456,Bob,Maschinenbau,5,2.1
34567,Charlie,Informatik,2,1.7
45678,Diana,Elektrotechnik,4,1.9
56789,Eve,Informatik,6,2.3
67890,Frank,Maschinenbau,1,3.0
78901,Grace,Informatik,4,1.5"""
    
    with open("studenten.csv", "w", encoding="utf-8") as f:
        f.write(csv_inhalt)
    
    # Daten einlesen
    studenten = lies_studenten("studenten.csv")
    print(f"📊 {len(studenten)} Studenten eingelesen\n")
    
    # Aufgabe a) Durchschnittsnote pro Studiengang
    print("=" * 60)
    print("Durchschnittsnoten nach Studiengang:")
    print("=" * 60)
    
    durchschnitte = durchschnittsnote_pro_studiengang(studenten)
    for gang in sorted(durchschnitte.keys()):
        print(f"  {gang}: {durchschnitte[gang]:.2f}")
    
    # Aufgabe b) Beste Studenten
    print("\n" + "=" * 60)
    print("Studenten mit Note < 1.8:")
    print("=" * 60)
    
    beste = beste_studenten(studenten, grenzwert=1.8)
    for i, student in enumerate(beste, 1):
        print(f"  {i}. {student['Name']} ({student['Studiengang']}, "
              f"Semester {student['Semester']}): {student['Note']}")
    
    # Aufgabe c) Informatik-Studenten exportieren
    print("\n" + "=" * 60)
    exportiere_informatik_mit_bewertung(studenten, "informatik_studenten.csv")
    print("=" * 60)


if __name__ == "__main__":
    main()
```

**Erwartete Ausgabe:**

```
📊 7 Studenten eingelesen

============================================================
Durchschnittsnoten nach Studiengang:
============================================================
  Elektrotechnik: 1.90
  Informatik: 1.70
  Maschinenbau: 2.55

============================================================
Studenten mit Note < 1.8:
============================================================
  1. Alice (Informatik, Semester 3): 1.3
  2. Grace (Informatik, Semester 4): 1.5
  3. Charlie (Informatik, Semester 2): 1.7

============================================================
✅ 4 Informatik-Studenten exportiert nach 'informatik_studenten.csv'
============================================================
```

**Erstellte Datei `informatik_studenten.csv`:**

```csv
Matrikelnummer,Name,Studiengang,Semester,Note,Bewertung
12345,Alice,Informatik,3,1.3,Sehr gut
34567,Charlie,Informatik,2,1.7,Gut
56789,Eve,Informatik,6,2.3,Befriedigend
78901,Grace,Informatik,4,1.5,Sehr gut
```

**Erklärung:**

**Daten einlesen mit Typ-Konvertierung:**
Die Funktion `lies_studenten()` nutzt `csv.DictReader()` und konvertiert `Semester` zu `int` und `Note` zu `float`. Dies ist wichtig, da CSV-Daten standardmäßig als Strings eingelesen werden. Die Typ-Konvertierung wird in einem `try-except`-Block durchgeführt, sodass ungültige Zeilen übersprungen werden, ohne das gesamte Programm zu stoppen.

**defaultdict für Aggregation:**
`collections.defaultdict(float)` und `defaultdict(int)` werden verwendet, um Summen und Zähler automatisch zu initialisieren. Ohne `defaultdict` müsste man vor dem ersten Zugriff prüfen, ob der Key bereits existiert.

**List Comprehensions für Filterung:**
- `[s for s in studenten if s['Note'] < grenzwert]` filtert Studenten nach Note
- `[s for s in studenten if s['Studiengang'] == 'Informatik']` filtert nach Studiengang
Dies ist kompakter und pythonischer als explizite `for`-Schleifen mit `if` und `.append()`.

**sorted() mit lambda:**
`sorted(gefiltert, key=lambda s: s['Note'])` sortiert die Liste nach dem `'Note'`-Wert jedes Dictionaries. Die `lambda`-Funktion extrahiert den Sortierschlüssel.

**csv.DictWriter:**
`csv.DictWriter()` nimmt `fieldnames` als Parameter, um die Spaltenreihenfolge zu definieren. `.writeheader()` schreibt die Kopfzeile mit den Spaltennamen. `.writerows()` schreibt alle Dictionaries als Zeilen.

**newline='' bei CSV-Schreiben:**
Der `newline=''`-Parameter ist unter Windows **zwingend erforderlich**, um doppelte Zeilenumbrüche zu vermeiden. Ohne diesen Parameter würde jede Zeile mit `\r\r\n` statt `\r\n` enden.

---

### Lösung 6: Iterator vs. Iterable verstehen ⭐⭐

**Teil 1: Analyse**

**Frage 1: Ist `Fibonacci` ein Iterable, Iterator oder beides?**

**Antwort:** `Fibonacci` ist **beides** – sowohl Iterable als auch Iterator.

**Begründung:**
- **Iterable**: Die Klasse implementiert `__iter__()`, welche erforderlich ist, um über ein Objekt in einer `for`-Schleife iterieren zu können.
- **Iterator**: Die Klasse implementiert zusätzlich `__next__()`, was sie zu einem Iterator macht. Iteratoren verwalten ihren eigenen Zustand und können Element für Element abgerufen werden.
- **Besonderheit**: `__iter__()` gibt `self` zurück, was bedeutet, dass das Objekt sein eigener Iterator ist.

**Frage 2: Was gibt `list(fib)` zurück?**

**Antwort:**
```python
fib = Fibonacci(5)
print(list(fib))  # [0, 1, 1, 2, 3]
```

**Erklärung:**
`list(fib)` iteriert über den Generator und sammelt alle zurückgegebenen Werte in einer Liste. Die Fibonacci-Sequenz startet bei 0 und 1, und jede weitere Zahl ist die Summe der beiden vorherigen: 0, 1, 1 (0+1), 2 (1+1), 3 (1+2).

**Frage 3: Was passiert beim zweiten `list(fib)`-Aufruf?**

**Antwort:**
```python
fib = Fibonacci(5)
print(list(fib))  # [0, 1, 1, 2, 3]
print(list(fib))  # [] (leer!)
```

**Erklärung:**
Der Iterator ist nach dem ersten Durchlauf **erschöpft** (exhausted). Der Zustand (`self.count`) wurde auf 5 gesetzt, sodass die Bedingung `if self.count >= self.n` sofort `True` ist und `StopIteration` geworfen wird. Iteratoren können nur **einmal** durchlaufen werden – danach sind sie leer.

**Frage 4: Wie müsste die Klasse geändert werden für mehrfache Iteration?**

**Antwort:** Die Klasse muss **Iterable** bleiben, aber **nicht selbst Iterator** sein. Stattdessen sollte `__iter__()` einen **neuen** Iterator zurückgeben.

**Korrigierte Implementierung:**

```python
class Fibonacci:
    """Iterable Fibonacci-Klasse (mehrfach durchlaufbar)."""
    
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        # Gibt NEUEN Iterator zurück (nicht self)
        return FibonacciIterator(self.n)


class FibonacciIterator:
    """Iterator für Fibonacci-Sequenz."""
    
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.count += 1
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result


# Test:
fib = Fibonacci(5)
print(list(fib))  # [0, 1, 1, 2, 3]
print(list(fib))  # [0, 1, 1, 2, 3] (funktioniert!)
```

**Erklärung:**
Jetzt gibt `__iter__()` jedes Mal einen **neuen** `FibonacciIterator` zurück. Dadurch kann das Iterable beliebig oft durchlaufen werden, da jede Iteration mit einem frischen Iterator startet.

---

**Teil 2: Generator-Implementierung**

```python
def fibonacci_generator(n):
    """
    Generator für Fibonacci-Zahlen von 0 bis zur n-ten Zahl.
    
    Args:
        n (int): Anzahl der zu erzeugenden Fibonacci-Zahlen
    
    Yields:
        int: Nächste Fibonacci-Zahl
    
    Examples:
        >>> list(fibonacci_generator(5))
        [0, 1, 1, 2, 3]
        >>> list(fibonacci_generator(10))
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    a, b = 0, 1
    count = 0
    
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


# Test:
print(list(fibonacci_generator(10)))
# Ausgabe: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

**Erklärung:**

**Generator vs. Klasse:**
Der Generator ist **deutlich kürzer** und **lesbarer** als die Klassen-Implementierung. Mit nur 6 Zeilen Code erreichen wir dieselbe Funktionalität wie mit 20+ Zeilen in der Iterator-Klasse.

**yield-Mechanismus:**
Bei jedem Aufruf von `next()` (implizit in der `for`-Schleife) läuft die Funktion bis zum nächsten `yield`, gibt den Wert zurück und **pausiert**. Der Zustand (Variablen `a`, `b`, `count`) bleibt erhalten. Beim nächsten `next()` setzt die Ausführung nach dem `yield` fort.

**Mehrfache Iteration:**
Auch der Generator kann nur **einmal** durchlaufen werden:
```python
gen = fibonacci_generator(5)
print(list(gen))  # [0, 1, 1, 2, 3]
print(list(gen))  # [] (erschöpft)
```
Um mehrfach zu iterieren, muss der Generator **neu erstellt** werden:
```python
print(list(fibonacci_generator(5)))  # [0, 1, 1, 2, 3]
print(list(fibonacci_generator(5)))  # [0, 1, 1, 2, 3] (neu erstellt)
```

**Performance:**
Generatoren haben minimalen Overhead und sind sehr speicher-effizient, da Werte **on-the-fly** berechnet werden, nicht vorher alle gespeichert.

---

### Lösung 7: Log-Datei-Analyse mit Generator-Pipeline ⭐⭐⭐

**Vollständige Implementierung:**

```python
import re
from collections import Counter, defaultdict


def lies_log_zeilen(dateiname):
    """
    Generator: Liest Log-Datei Zeile für Zeile.
    
    Args:
        dateiname (str): Pfad zur Log-Datei
    
    Yields:
        str: Einzelne Log-Zeile
    """
    with open(dateiname, "r", encoding="utf-8") as datei:
        for zeile in datei:
            yield zeile.strip()


def parse_log_zeile(zeilen):
    """
    Generator: Parst Log-Zeilen im Apache Combined Format.
    
    Args:
        zeilen (generator): Generator von Log-Zeilen
    
    Yields:
        dict: Geparstes Log-Entry mit ip, timestamp, method, path, status, bytes
    """
    # Regex für Apache Combined Log Format
    pattern = r'^(\S+) \S+ \S+ \[(.*?)\] "(\S+) (\S+) \S+" (\d+) (\d+|-)'
    regex = re.compile(pattern)
    
    for zeile in zeilen:
        match = regex.match(zeile)
        if match:
            ip, timestamp, method, path, status, bytes_str = match.groups()
            
            # Bytes können "-" sein (keine Daten übertragen)
            bytes_val = 0 if bytes_str == "-" else int(bytes_str)
            
            yield {
                'ip': ip,
                'timestamp': timestamp,
                'method': method,
                'path': path,
                'status': int(status),
                'bytes': bytes_val
            }
        # Ungültige Zeilen werden übersprungen (kein yield)


def filtere_status(log_entries, status_code):
    """
    Generator: Filtert Log-Entries nach Statuscode.
    
    Args:
        log_entries (generator): Generator von Log-Dictionaries
        status_code (int): Gewünschter HTTP-Statuscode
    
    Yields:
        dict: Log-Entries mit passendem Statuscode
    """
    for entry in log_entries:
        if entry['status'] == status_code:
            yield entry


def zaehle_status_codes(dateiname):
    """
    Analysiert Log-Datei und zählt HTTP-Statuscodes.
    
    Args:
        dateiname (str): Pfad zur Log-Datei
    
    Returns:
        dict: {status_code: anzahl}
    """
    # Pipeline aufbauen
    zeilen = lies_log_zeilen(dateiname)
    entries = parse_log_zeile(zeilen)
    
    # Mit Counter zählen
    status_counter = Counter()
    for entry in entries:
        status_counter[entry['status']] += 1
    
    return dict(status_counter)


def finde_fehlerhafte_requests(dateiname):
    """
    Findet alle Requests mit Statuscode 4xx oder 5xx.
    
    Args:
        dateiname (str): Pfad zur Log-Datei
    
    Returns:
        list[dict]: Fehlerhafte Requests, sortiert nach Status (höchste zuerst)
    """
    # Pipeline aufbauen
    zeilen = lies_log_zeilen(dateiname)
    entries = parse_log_zeile(zeilen)
    
    # Fehlerhafte Requests sammeln (4xx, 5xx)
    fehler = []
    for entry in entries:
        if entry['status'] >= 400:
            fehler.append(entry)
    
    # Nach Statuscode sortieren (höchste zuerst)
    fehler_sortiert = sorted(fehler, key=lambda e: e['status'], reverse=True)
    
    return fehler_sortiert


def top_ips(dateiname, n=5):
    """
    Findet die Top-N IP-Adressen mit den meisten Requests.
    
    Args:
        dateiname (str): Pfad zur Log-Datei
        n (int): Anzahl Top-IPs
    
    Returns:
        list[tuple]: [(ip, anzahl), ...] sortiert nach Anzahl (höchste zuerst)
    """
    # Pipeline aufbauen
    zeilen = lies_log_zeilen(dateiname)
    entries = parse_log_zeile(zeilen)
    
    # IP-Adressen zählen
    ip_counter = Counter()
    for entry in entries:
        ip_counter[entry['ip']] += 1
    
    # Top N zurückgeben
    return ip_counter.most_common(n)


def main():
    """Hauptprogramm mit Test-Daten."""
    
    # Test-Log-Datei erstellen
    log_inhalt = """192.168.1.100 - - [10/Jan/2024:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326
192.168.1.101 - - [10/Jan/2024:13:55:37 +0000] "GET /about.html HTTP/1.1" 200 1523
192.168.1.102 - - [10/Jan/2024:13:55:38 +0000] "POST /api/login HTTP/1.1" 401 512
192.168.1.100 - - [10/Jan/2024:13:55:39 +0000] "GET /admin HTTP/1.1" 403 234
192.168.1.103 - - [10/Jan/2024:13:55:40 +0000] "GET /data.json HTTP/1.1" 500 1024
192.168.1.100 - - [10/Jan/2024:13:55:41 +0000] "GET /test.html HTTP/1.1" 200 567
192.168.1.104 - - [10/Jan/2024:13:55:42 +0000] "GET /missing.html HTTP/1.1" 404 0
192.168.1.100 - - [10/Jan/2024:13:55:43 +0000] "POST /api/data HTTP/1.1" 500 234"""
    
    with open("access.log", "w", encoding="utf-8") as f:
        f.write(log_inhalt)
    
    # Analyse 1: Status-Code-Verteilung
    print("=" * 60)
    print("Status-Code-Verteilung:")
    print("=" * 60)
    
    status_counts = zaehle_status_codes("access.log")
    for code in sorted(status_counts.keys()):
        print(f"  {code}: {status_counts[code]}")
    
    # Analyse 2: Fehlerhafte Requests
    print("\n" + "=" * 60)
    print("Fehlerhafte Requests (4xx, 5xx):")
    print("=" * 60)
    
    errors = finde_fehlerhafte_requests("access.log")
    print(f"{len(errors)} fehlerhafte Requests gefunden:\n")
    
    for entry in errors:
        print(f"  [{entry['status']}] {entry['ip']} → {entry['method']} {entry['path']}")
    
    # Analyse 3: Top-5 IPs
    print("\n" + "=" * 60)
    print("Top-5 aktivste IP-Adressen:")
    print("=" * 60)
    
    top = top_ips("access.log", n=5)
    for i, (ip, count) in enumerate(top, 1):
        print(f"  {i}. {ip}: {count} Requests")


if __name__ == "__main__":
    main()
```

**Erwartete Ausgabe:**

```
============================================================
Status-Code-Verteilung:
============================================================
  200: 3
  401: 1
  403: 1
  404: 1
  500: 2

============================================================
Fehlerhafte Requests (4xx, 5xx):
============================================================
5 fehlerhafte Requests gefunden:

  [500] 192.168.1.103 → GET /data.json
  [500] 192.168.1.100 → POST /api/data
  [404] 192.168.1.104 → GET /missing.html
  [403] 192.168.1.100 → GET /admin
  [401] 192.168.1.102 → POST /api/login

============================================================
Top-5 aktivste IP-Adressen:
============================================================
  1. 192.168.1.100: 4 Requests
  2. 192.168.1.101: 1 Requests
  3. 192.168.1.102: 1 Requests
  4. 192.168.1.103: 1 Requests
  5. 192.168.1.104: 1 Requests
```

**Erklärung:**

**Generator-Pipeline:**
Die drei Generator-Funktionen (`lies_log_zeilen`, `parse_log_zeile`, `filtere_status`) sind **verkettbar**. Jeder Generator nimmt den vorherigen als Input und transformiert/filtert die Daten. Dies ist speicher-effizient, da nur ein Element zur Zeit durch die Pipeline läuft.

**Regex für Log-Parsing:**
Das Apache Combined Log Format hat eine feste Struktur. Die Regex extrahiert:
- `(\S+)`: IP-Adresse (nicht-whitespace Zeichen)
- `\[(.*?)\]`: Timestamp in eckigen Klammern
- `"(\S+) (\S+) \S+"`: HTTP-Methode, Pfad, Protokoll
- `(\d+)`: Statuscode (Ziffern)
- `(\d+|-)`: Bytes (Ziffern oder `-`)

**Counter aus collections:**
`Counter` ist eine spezialisierte Dictionary-Klasse zum Zählen. `.most_common(n)` gibt die n häufigsten Elemente als Liste von Tupeln zurück.

**Fehlerbehandlung:**
Ungültige Zeilen werden stillschweigend übersprungen (kein `yield` bei nicht-matched Zeilen). In Production-Code sollte man fehlerhafte Zeilen loggen.

**Pipeline-Effizienz:**
Jede Analyse-Funktion baut die Pipeline **neu** auf und liest die Datei einmal. Für mehrere Analysen auf denselben Daten könnte man `itertools.tee()` nutzen, um den Generator zu "klonen" (siehe Bonus in Aufgabe 8).

**Bonus: Zeitfenster-Analyse (Beispiel-Implementierung):**

```python
from datetime import datetime

def zeitfenster_analyse(dateiname, start_stunde, end_stunde):
    """
    Analysiert nur Requests innerhalb eines Stunden-Fensters.
    
    Args:
        dateiname (str): Pfad zur Log-Datei
        start_stunde (int): Start-Stunde (0-23)
        end_stunde (int): End-Stunde (0-23, exklusiv)
    
    Returns:
        dict: Status-Code-Verteilung für Zeitfenster
    """
    zeilen = lies_log_zeilen(dateiname)
    entries = parse_log_zeile(zeilen)
    
    status_counter = Counter()
    
    for entry in entries:
        # Timestamp parsen: "10/Jan/2024:13:55:36 +0000"
        timestamp_str = entry['timestamp']
        # Nur Stunde extrahieren (Position 12-13)
        stunde = int(timestamp_str[12:14])
        
        if start_stunde <= stunde < end_stunde:
            status_counter[entry['status']] += 1
    
    return dict(status_counter)

# Test:
result = zeitfenster_analyse("access.log", start_stunde=13, end_stunde=14)
print(f"Requests zwischen 13:00-14:00: {result}")
```

---

### Lösung 8: CSV-Daten-Transformation mit Generatoren ⭐⭐⭐⭐

**Vollständige Implementierung:**

```python
import csv
from datetime import datetime
from decimal import Decimal, InvalidOperation
from collections import defaultdict, Counter
import itertools
import time


def validiere_bestellungen(dateiname):
    """
    Generator: Liest CSV und validiert Bestellungen.
    Schreibt fehlerhafte Zeilen in errors.log.
    
    Args:
        dateiname (str): Pfad zur CSV-Datei
    
    Yields:
        dict: Validierte Bestellung mit originalen String-Werten
    """
    fehler_log = open("errors.log", "w", encoding="utf-8")
    zeilen_nr = 0
    
    try:
        with open(dateiname, "r", encoding="utf-8") as datei:
            reader = csv.DictReader(datei)
            
            for zeile in reader:
                zeilen_nr += 1
                fehler = []
                
                # Pflichtfelder prüfen
                if not zeile.get('OrderID'):
                    fehler.append("OrderID fehlt")
                if not zeile.get('CustomerID'):
                    fehler.append("CustomerID fehlt")
                if not zeile.get('ProductID'):
                    fehler.append("ProductID fehlt")
                
                # Quantity validieren
                try:
                    qty = int(zeile.get('Quantity', ''))
                    if qty <= 0:
                        fehler.append("Quantity muss positiv sein")
                except ValueError:
                    fehler.append("Quantity ist keine gültige Ganzzahl")
                
                # Price validieren
                try:
                    price = Decimal(zeile.get('Price', ''))
                    if price <= 0:
                        fehler.append("Price muss positiv sein")
                except (ValueError, InvalidOperation):
                    fehler.append("Price ist keine gültige Dezimalzahl")
                
                # OrderDate validieren
                try:
                    date_str = zeile.get('OrderDate', '')
                    datetime.strptime(date_str, '%Y-%m-%d')
                except ValueError:
                    fehler.append("OrderDate hat ungültiges Format (erwartet: YYYY-MM-DD)")
                
                # Status validieren
                valid_statuses = {'completed', 'pending', 'cancelled'}
                if zeile.get('Status') not in valid_statuses:
                    fehler.append(f"Status ungültig (erwartet: {valid_statuses})")
                
                # Fehler loggen oder Zeile weitergeben
                if fehler:
                    fehler_log.write(f"Zeile {zeilen_nr}: {'; '.join(fehler)} → {zeile}\n")
                else:
                    yield zeile
    
    finally:
        fehler_log.close()


def transformiere_bestellungen(bestellungen):
    """
    Generator: Transformiert Bestellungen (Typen konvertieren, Felder hinzufügen).
    
    Args:
        bestellungen (generator): Generator von validierten Bestellungen
    
    Yields:
        dict: Transformierte Bestellung mit zusätzlichen Feldern
    """
    for bestellung in bestellungen:
        # OrderDate zu datetime konvertieren
        order_date = datetime.strptime(bestellung['OrderDate'], '%Y-%m-%d')
        
        # Typen konvertieren
        quantity = int(bestellung['Quantity'])
        price = Decimal(bestellung['Price'])
        
        # TotalPrice berechnen
        total_price = quantity * price
        
        # Neue Felder hinzufügen
        bestellung_neu = bestellung.copy()
        bestellung_neu.update({
            'OrderDate_obj': order_date,  # datetime-Objekt
            'Quantity_int': quantity,
            'Price_decimal': price,
            'TotalPrice': total_price,
            'Year': order_date.year,
            'Month': order_date.month,
            'Day': order_date.day,
            'IsHighValue': total_price > 50
        })
        
        yield bestellung_neu


def umsatz_pro_tag(bestellungen):
    """
    Berechnet Gesamtumsatz pro Tag (nur completed Orders).
    
    Args:
        bestellungen (generator): Generator von transformierten Bestellungen
    
    Returns:
        dict: {date: Decimal(umsatz)}
    """
    tagesumsatz = defaultdict(Decimal)
    
    for bestellung in bestellungen:
        if bestellung['Status'] == 'completed':
            tag = bestellung['OrderDate_obj'].date()
            tagesumsatz[tag] += bestellung['TotalPrice']
    
    return dict(tagesumsatz)


def top_produkte(bestellungen, n=5):
    """
    Findet die Top-N meist-bestellten Produkte.
    
    Args:
        bestellungen (generator): Generator von transformierten Bestellungen
        n (int): Anzahl Top-Produkte
    
    Returns:
        list[tuple]: [(ProductID, Anzahl_Bestellungen, Gesamtumsatz), ...]
    """
    produkt_stats = defaultdict(lambda: {'count': 0, 'revenue': Decimal(0)})
    
    for bestellung in bestellungen:
        pid = bestellung['ProductID']
        produkt_stats[pid]['count'] += 1
        produkt_stats[pid]['revenue'] += bestellung['TotalPrice']
    
    # Als Liste mit Tupeln
    produkte = [
        (pid, stats['count'], stats['revenue'])
        for pid, stats in produkt_stats.items()
    ]
    
    # Nach Anzahl sortieren (höchste zuerst)
    produkte_sortiert = sorted(produkte, key=lambda x: x[1], reverse=True)
    
    return produkte_sortiert[:n]


def kunden_statistik(bestellungen):
    """
    Berechnet Statistiken pro Kunde.
    
    Args:
        bestellungen (generator): Generator von transformierten Bestellungen
    
    Returns:
        dict: {CustomerID: {'orders': int, 'total': Decimal, 'avg': Decimal}}
    """
    kunden_stats = defaultdict(lambda: {'orders': 0, 'total': Decimal(0)})
    
    for bestellung in bestellungen:
        cid = bestellung['CustomerID']
        kunden_stats[cid]['orders'] += 1
        kunden_stats[cid]['total'] += bestellung['TotalPrice']
    
    # Durchschnitt berechnen
    for cid in kunden_stats:
        stats = kunden_stats[cid]
        stats['avg'] = stats['total'] / stats['orders']
    
    return dict(kunden_stats)


def exportiere_aggregierte_daten(input_datei, output_prefix):
    """
    Führt gesamte Pipeline durch und exportiert Ergebnisse.
    
    Args:
        input_datei (str): Pfad zur Input-CSV
        output_prefix (str): Präfix für Output-Dateien
    """
    start_time = time.time()
    
    print("Verarbeitung gestartet...")
    
    # Pipeline aufbauen
    validiert = validiere_bestellungen(input_datei)
    transformiert = transformiere_bestellungen(validiert)
    
    # Mit itertools.tee() für mehrere Analysen klonen
    trans1, trans2, trans3 = itertools.tee(transformiert, 3)
    
    # Analysen durchführen
    tagesumsatz = umsatz_pro_tag(trans1)
    top_prods = top_produkte(trans2, n=5)
    kunden_stats = kunden_statistik(trans3)
    
    # Export 1: Tagesumsätze
    with open(f"{output_prefix}_daily_revenue.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Revenue'])
        for date in sorted(tagesumsatz.keys()):
            writer.writerow([date, str(tagesumsatz[date])])
    
    # Export 2: Top-Produkte
    with open(f"{output_prefix}_top_products.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(['ProductID', 'OrderCount', 'TotalRevenue'])
        for pid, count, revenue in top_prods:
            writer.writerow([pid, count, str(revenue)])
    
    # Export 3: Kunden-Statistik
    with open(f"{output_prefix}_customer_stats.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(['CustomerID', 'OrderCount', 'TotalRevenue', 'AvgOrderValue'])
        for cid in sorted(kunden_stats.keys()):
            stats = kunden_stats[cid]
            writer.writerow([cid, stats['orders'], str(stats['total']), str(stats['avg'])])
    
    # Statistiken zählen
    with open("errors.log", "r", encoding="utf-8") as f:
        fehler_anzahl = len(f.readlines())
    
    gesamt = sum(stats['orders'] for stats in kunden_stats.values())
    
    end_time = time.time()
    laufzeit = end_time - start_time
    
    print(f"✓ {gesamt} Bestellungen validiert")
    print(f"✗ {fehler_anzahl} fehlerhafte Zeilen (siehe errors.log)")
    print("✓ Export abgeschlossen")
    print(f"Laufzeit: {laufzeit:.2f} Sekunden")


def main():
    """Hauptprogramm mit Test-Daten."""
    
    # Test-CSV erstellen
    csv_inhalt = """OrderID,CustomerID,ProductID,Quantity,Price,OrderDate,Status
1001,C001,P100,2,19.99,2024-01-10,completed
1002,C002,P101,1,49.99,2024-01-10,completed
1003,C001,P102,3,9.99,2024-01-10,pending
1004,C003,P100,1,19.99,2024-01-11,completed
1005,C002,P103,5,5.99,2024-01-11,cancelled
1006,C004,P100,2,19.99,2024-01-11,completed
1007,C001,INVALID,-1,10.00,2024-01-12,completed
1008,C005,P101,2,25.00,INVALID,completed"""
    
    with open("orders.csv", "w", encoding="utf-8") as f:
        f.write(csv_inhalt)
    
    # Pipeline ausführen
    exportiere_aggregierte_daten("orders.csv", "report_2024_01")
    
    # Ergebnisse anzeigen
    print("\n" + "=" * 60)
    print("Tagesumsätze:")
    with open("report_2024_01_daily_revenue.csv", "r", encoding="utf-8") as f:
        print(f.read())
    
    print("=" * 60)
    print("Top-Produkte:")
    with open("report_2024_01_top_products.csv", "r", encoding="utf-8") as f:
        print(f.read())


if __name__ == "__main__":
    main()
```

**Erwartete Ausgabe:**

```
Verarbeitung gestartet...
✓ 6 Bestellungen validiert
✗ 2 fehlerhafte Zeilen (siehe errors.log)
✓ Export abgeschlossen
Laufzeit: 0.03 Sekunden

============================================================
Tagesumsätze:
Date,Revenue
2024-01-10,69.98
2024-01-11,39.98

============================================================
Top-Produkte:
ProductID,OrderCount,TotalRevenue
P100,3,59.97
P101,1,49.99
P102,1,29.97
```

**Erklärung:**

**itertools.tee() für Generator-Klonen:**
`itertools.tee(generator, n)` erstellt `n` unabhängige Kopien eines Generators. Dadurch können wir denselben Datenstream für mehrere Analysen nutzen, ohne die Datei mehrmals einlesen zu müssen.

**Decimal für Geldbeträge:**
`Decimal` aus dem `decimal`-Modul verhindert Rundungsfehler bei Fließkomma-Arithmetik. `Decimal('19.99')` ist exakt, während `float(19.99)` intern als `19.989999...` gespeichert wird.

**defaultdict mit lambda:**
`defaultdict(lambda: {'count': 0, 'revenue': Decimal(0)})` erstellt automatisch ein Dictionary als Default-Wert. So müssen wir nicht vor jedem Zugriff prüfen, ob der Key existiert.

**Fehlertoleranz:**
Fehlerhafte Zeilen werden in `errors.log` geschrieben, stoppen aber nicht die Verarbeitung. Der Generator überspringt sie einfach (kein `yield`).

**Performance:**
Mit `itertools.tee()` wird die Datei nur **einmal** gelesen, aber die Daten dreimal verwendet. Dies ist effizienter als dreimal separat einzulesen, hat aber einen Speicher-Overhead (alle Werte müssen zwischengespeichert werden, bis alle Kopien sie konsumiert haben).

**Bonus: Inkrementeller Export (Konzept):**
```python
import json

def inkrementeller_export(input_datei, state_datei, output_prefix):
    # State laden (bereits verarbeitete OrderIDs)
    try:
        with open(state_datei, "r") as f:
            processed_ids = set(json.load(f))
    except FileNotFoundError:
        processed_ids = set()
    
    # Nur neue Bestellungen verarbeiten
    neue_ids = []
    for bestellung in validiere_bestellungen(input_datei):
        if bestellung['OrderID'] not in processed_ids:
            # Verarbeiten...
            neue_ids.append(bestellung['OrderID'])
    
    # State aktualisieren
    processed_ids.update(neue_ids)
    with open(state_datei, "w") as f:
        json.dump(list(processed_ids), f)
```

