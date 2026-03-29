# V18: Übungsaufgaben - Kryptografie Teil 2 & HTTP-Requests

> [!NOTE]
> Diese Übungsaufgaben vertiefen das Verständnis der Vorlesung V18.
> Bearbeite die Aufgaben in der angegebenen Reihenfolge.

---

## Teil A: Theorie-Aufgaben

### Aufgabe T1: Hash-Funktionen und ihre Eigenschaften (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 5-10 Minuten

Du bist Ingenieur in einem Maschinenbau-Unternehmen und sollst ein System zur Integritätsprüfung von NC-Programmen implementieren. NC-Programme (CNC-Programme) werden von Programmierern erstellt und an die Maschinen übertragen. Um Manipulation zu verhindern, soll jedes Programm mit einem Hash-Wert versehen werden.

**Aufgaben:**

a) Erkläre in eigenen Worten, was eine **kryptografische Hash-Funktion** ist und welche drei Haupteigenschaften sie haben muss (Einwegfunktion, Kollisionsresistenz, Avalanche-Effekt).

b) Ein Kollege schlägt vor, MD5 zu verwenden, da es schnell ist. Erkläre, warum MD5 **nicht geeignet** ist für sicherheitskritische Anwendungen wie NC-Programm-Integrität. Welche Hash-Funktion würdest du stattdessen empfehlen?

c) Zwei NC-Programme haben folgende SHA-256-Hashes:
   - `Programm_A.nc`: `3a5f8c...` (64 Hex-Zeichen)
   - `Programm_B.nc`: `3a5f8c...` (identischer Hash)
   
   Was kannst du mit Sicherheit über die beiden Programme aussagen? Welche Eigenschaft der Hash-Funktion garantiert dies?

**Hinweise**:
- Denke an die theoretischen Eigenschaften aus dem Skript: Deterministisch, Einwegfunktion, Kollisionsresistenz
- MD5 ist seit 2004 gebrochen (praktische Kollisionsangriffe)

---

### Aufgabe T2: Digitale Signaturen verstehen (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 15-20 Minuten

Eine Maschinenbaufirma entwickelt Industrieroboter, die Firmware-Updates per Netzwerk erhalten. Um sicherzustellen, dass nur authentische Firmware vom Hersteller installiert wird, werden Updates digital signiert.

**Szenario:**
- Der Hersteller hat ein RSA-Schlüsselpaar: **Private Key** (geheim) und **Public Key** (öffentlich, im Roboter gespeichert)
- Firmware-Update: `firmware_v2.3.bin` (200 MB groß)
- Hersteller erstellt digitale Signatur

**Aufgaben:**

a) Beschreibe Schritt für Schritt, wie der Hersteller die digitale Signatur für `firmware_v2.3.bin` erstellt. Welche kryptografischen Operationen werden durchgeführt? (Tipp: Hash-Funktion + asymmetrische Verschlüsselung)

b) Beschreibe Schritt für Schritt, wie der Roboter die digitale Signatur verifiziert. Welche Schlüssel werden verwendet? Was passiert, wenn die Verifizierung fehlschlägt?

c) Warum wird die Firmware nicht direkt mit dem privaten Schlüssel verschlüsselt, sondern nur der Hash-Wert? Nenne mindestens zwei Gründe (Tipp: Denke an Performance und Dateigröße).

d) Ein Angreifer hat Zugriff auf den **Public Key** des Herstellers. Kann er damit eine gefälschte Firmware signieren, die der Roboter akzeptiert? Begründe deine Antwort.

**Hinweise**:
- Digitale Signatur = Hash der Nachricht verschlüsselt mit Private Key
- Verifizierung = Signatur entschlüsseln mit Public Key, mit eigenem Hash vergleichen
- RSA ist langsam für große Datenmengen

---

### Aufgabe T3: TLS/SSL und PKI-Vertrauenskette (Schwer)

**Schwierigkeit**: ⭐⭐⭐ Schwer  
**Zeitaufwand**: ca. 20-30 Minuten

Du implementierst ein Cloud-basiertes Monitoring-System für CNC-Maschinen. Die Maschinen senden Produktionsdaten über HTTPS an einen Cloud-Server (`https://api.cnc-monitor.com`).

**Szenario:**
- CNC-Maschine (Client) verbindet sich mit API-Server (HTTPS)
- Server hat ein TLS-Zertifikat von einer Certificate Authority (CA)
- TLS-Version: TLS 1.3

**Aufgaben:**

a) **TLS-Handshake**: Beschreibe die wichtigsten Schritte des TLS-Handshakes (vereinfacht):
   1. Was sendet der Client im "Client Hello"?
   2. Was sendet der Server im "Server Hello"?
   3. Wie wird der Session Key ausgehandelt (Stichwort: Diffie-Hellman)?
   4. Wann beginnt die verschlüsselte Datenübertragung?

b) **Zertifikatsprüfung**: Der Server sendet sein X.509-Zertifikat. Welche Prüfungen muss die CNC-Maschine durchführen, bevor sie dem Zertifikat vertraut? Nenne mindestens 5 Prüfungen.

c) **Zertifikatskette**: Das Server-Zertifikat wurde von einer Intermediate CA signiert, die wiederum von einer Root CA signiert wurde. Zeichne die Vertrauenskette auf (Root CA → Intermediate CA → Server-Zertifikat) und erkläre, warum die Root CA im CNC-Maschinen-System vorinstalliert sein muss.

d) **Forward Secrecy**: Erkläre das Konzept "Forward Secrecy" (Perfect Forward Secrecy) mit folgendem Szenario:
   - Ein Angreifer zeichnet alle verschlüsselten HTTPS-Verbindungen zwischen Maschine und Server auf (1 Jahr lang).
   - Nach einem Jahr wird der private Schlüssel des Servers gestohlen.
   - **Mit Forward Secrecy**: Kann der Angreifer die aufgezeichneten Verbindungen entschlüsseln? Warum/Warum nicht?
   - **Ohne Forward Secrecy (RSA Key Exchange)**: Kann der Angreifer die Verbindungen entschlüsseln?

e) **Vergleich TLS-Versionen**: Warum sollten TLS 1.0, TLS 1.1 und SSL 3.0 deaktiviert werden? Nenne mindestens zwei konkrete Angriffe oder Schwachstellen.

**Hinweise**:
- TLS-Handshake: Client Hello, Server Hello, Zertifikat, Key Exchange, Finished
- Zertifikatsprüfung: CA-Signatur, Gültigkeit, Domain, Widerruf (CRL/OCSP), Vertrauenskette
- Forward Secrecy: Ephemeral Diffie-Hellman (ECDHE) generiert temporäre Schlüssel
- Bekannte Angriffe: POODLE, BEAST, Heartbleed

---

## Teil B: Python-Aufgaben

### Aufgabe P1: Hash-Funktion für Dateiintegrität (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: `hashlib`-Modul (Python Standard Library), File I/O, Funktionen  
**Maschinenbau-Kontext**: Integritätsprüfung von NC-Programmen und CAD-Dateien

Ein Maschinenbau-Unternehmen überträgt NC-Programme (CNC-Programme) über das Netzwerk an die Maschinen. Um sicherzustellen, dass die Dateien während der Übertragung nicht beschädigt oder manipuliert wurden, wird für jede Datei ein SHA-256-Hash berechnet und mitgesendet.

**Aufgabenstellung:**

Implementiere eine Funktion `calculate_file_hash(filepath)`, die den SHA-256-Hash einer Datei berechnet und als Hexadezimal-String zurückgibt.

**Anforderungen:**

1. Die Funktion soll Dateien beliebiger Größe verarbeiten können (auch große Dateien > 100 MB).
2. Verwende das `hashlib`-Modul aus der Python Standard Library.
3. Lese die Datei blockweise (z.B. in 4096-Byte-Blöcken), um Speicher zu sparen.
4. Implementiere Error Handling für den Fall, dass die Datei nicht existiert.

**Benötigte Testdaten**: 
- Für diese Aufgabe keine externen Dateien erforderlich – du kannst eine temporäre Textdatei im Skript erstellen und hashen.

**Beispiel Ein-/Ausgabe**:
```python
# Beispiel-Datei erstellen
with open("test_nc_programm.nc", "w") as f:
    f.write("G00 X10 Y20\nG01 Z-5 F100\n")

# Hash berechnen
hash_value = calculate_file_hash("test_nc_programm.nc")
print(f"SHA-256: {hash_value}")
# Ausgabe (Beispiel): SHA-256: 3a5f8c9d...
```

**Starter-Code**:
```python
import hashlib

def calculate_file_hash(filepath):
    """
    Berechnet SHA-256 Hash einer Datei.
    
    Args:
        filepath: Pfad zur Datei
    
    Returns:
        Hash als Hexadezimal-String oder None bei Fehler
    """
    # Dein Code hier
    pass

# Test
if __name__ == "__main__":
    # Erstelle Testdatei
    with open("test_nc_programm.nc", "w") as f:
        f.write("G00 X10 Y20\nG01 Z-5 F100\nM30\n")
    
    # Hash berechnen
    hash_val = calculate_file_hash("test_nc_programm.nc")
    if hash_val:
        print(f"SHA-256: {hash_val}")
```

> [!TIP]
> `hashlib.sha256()` erstellt ein Hash-Objekt. Verwende `.update(data)` für jeden Block und `.hexdigest()` für das finale Ergebnis.

---

### Aufgabe P2: REST-API für Materialdatenbank abfragen (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 20-30 Minuten  
**Vorkenntnisse**: `requests`-Bibliothek, JSON-Verarbeitung, Exception Handling  
**Maschinenbau-Kontext**: Werkstoffeigenschaften aus Cloud-Datenbank abrufen

Ein Konstruktionsbüro nutzt eine Cloud-basierte Materialdatenbank, die über eine REST-API Werkstoffeigenschaften bereitstellt (z.B. Zugfestigkeit, E-Modul, Dichte). Konstrukteure müssen diese Daten abfragen, um Bauteilfestigkeiten zu berechnen.

**Aufgabenstellung:**

Implementiere eine Funktion `get_material_properties(material_name, api_key)`, die Materialigenschaften von einer REST-API abruft.

**API-Details:**
- **Base-URL**: `https://api.materials-db.example.com/v1/materials`
- **Methode**: GET
- **Query-Parameter**: `name` (Materialname, z.B. "S355", "AlMg3", "42CrMo4")
- **Header**: `Authorization: Bearer <api_key>`
- **Response-Format**: JSON

**Beispiel-Response:**
```json
{
  "material": "S355",
  "type": "Baustahl",
  "properties": {
    "yield_strength_mpa": 355,
    "tensile_strength_mpa": 510,
    "youngs_modulus_gpa": 210,
    "density_kg_m3": 7850,
    "poissons_ratio": 0.30
  },
  "standards": ["DIN EN 10025-2", "ISO 630"]
}
```

**Anforderungen:**

1. Die Funktion soll GET-Request mit Query-Parameter `name` und Authorization-Header senden.
2. Timeout von 10 Sekunden setzen.
3. Status-Code prüfen mit `.raise_for_status()`.
4. JSON-Response parsen und Dictionary zurückgeben.
5. Exception Handling für `Timeout`, `ConnectionError`, `HTTPError`, `JSONDecodeError`.
6. Bei Fehler: Fehlermeldung ausgeben und `None` zurückgeben.

**Benötigte Testdaten**: 
- **Mock-API-Datei**: `testdaten/material_api_mock.json` (siehe `testdaten/`-Ordner)
- Für Tests kannst du eine lokale JSON-Datei erstellen oder eine Mock-API verwenden

**Beispiel Ein-/Ausgabe**:
```python
api_key = "demo_key_12345"
material = get_material_properties("S355", api_key)

if material:
    props = material['properties']
    print(f"Material: {material['material']}")
    print(f"Zugfestigkeit: {props['tensile_strength_mpa']} MPa")
    print(f"E-Modul: {props['youngs_modulus_gpa']} GPa")
# Ausgabe:
# Material: S355
# Zugfestigkeit: 510 MPa
# E-Modul: 210 GPa
```

**Starter-Code**:
```python
import requests

def get_material_properties(material_name, api_key):
    """
    Ruft Materialeigenschaften von REST-API ab.
    
    Args:
        material_name: Name des Materials (z.B. "S355")
        api_key: API-Schlüssel für Authentifizierung
    
    Returns:
        Dictionary mit Materialdaten oder None bei Fehler
    """
    # Dein Code hier
    pass

# Test
if __name__ == "__main__":
    API_KEY = "demo_key_12345"  # In Produktion: aus Umgebungsvariable
    
    material = get_material_properties("S355", API_KEY)
    if material:
        print(f"✓ Material gefunden: {material['material']}")
```

> [!TIP]
> Da die API `https://api.materials-db.example.com` nicht real existiert, kannst du für Tests eine lokale JSON-Datei verwenden oder einen Mock-Server erstellen. Alternativ: Verwende eine echte Public API (z.B. OpenWeatherMap als Ersatz für Übungszwecke).

---

### Aufgabe P3: Passwort-Hashing mit bcrypt (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 25-35 Minuten  
**Vorkenntnisse**: Dictionaries, File I/O, JSON, bcrypt-Bibliothek  
**Maschinenbau-Kontext**: Zugangskontrolle für CNC-Maschinen und Roboter

Eine Produktionshalle hat mehrere CNC-Maschinen, die über ein lokales Zugangskontrollsystem geschützt sind. Bediener müssen sich mit Benutzername und Passwort anmelden. Die Passwörter werden mit bcrypt gehasht gespeichert (mit Salt).

**Aufgabenstellung:**

Implementiere ein einfaches Zugangskontrollsystem mit zwei Funktionen:
1. `register_user(username, password)`: Registriert neuen Benutzer, hasht Passwort mit bcrypt
2. `authenticate_user(username, password)`: Prüft, ob Passwort korrekt ist

**Anforderungen:**

1. Verwende die `bcrypt`-Bibliothek (Installation: `pip install bcrypt`).
2. Speichere Benutzerdaten in einem Dictionary: `users_db = {"username": "bcrypt_hash"}`.
3. Bei Registrierung: Passwort mit bcrypt hashen (bcrypt fügt automatisch Salt hinzu).
4. Bei Authentifizierung: Eingegebenes Passwort mit gespeichertem Hash vergleichen.
5. Implementiere Error Handling für fehlende Benutzer, falsche Passwörter, etc.

**Benötigte Testdaten**: 
- Keine externen Dateien erforderlich – Benutzerdatenbank wird im Programm verwaltet

**Beispiel Ein-/Ausgabe**:
```python
# Registrierung
register_user("techniker01", "Sicher123!")
register_user("operator02", "Maschine456")

# Anmeldung (erfolgreich)
if authenticate_user("techniker01", "Sicher123!"):
    print("✓ Anmeldung erfolgreich - Zugriff gewährt")
else:
    print("✗ Anmeldung fehlgeschlagen - Zugriff verweigert")

# Anmeldung (fehlgeschlagen - falsches Passwort)
if authenticate_user("techniker01", "FalschesPasswort"):
    print("✓ Anmeldung erfolgreich")
else:
    print("✗ Falsches Passwort")

# Ausgabe:
# ✓ Anmeldung erfolgreich - Zugriff gewährt
# ✗ Falsches Passwort
```

**Starter-Code**:
```python
import bcrypt

# Benutzerdatenbank (in Produktion: echte Datenbank verwenden)
users_db = {}

def register_user(username, password):
    """
    Registriert neuen Benutzer mit bcrypt-Hash.
    
    Args:
        username: Benutzername
        password: Passwort (Klartext)
    
    Returns:
        True bei Erfolg, False wenn Benutzer bereits existiert
    """
    # Dein Code hier
    pass

def authenticate_user(username, password):
    """
    Prüft Benutzeranmeldung.
    
    Args:
        username: Benutzername
        password: Passwort (Klartext)
    
    Returns:
        True wenn korrekt, False sonst
    """
    # Dein Code hier
    pass

# Test
if __name__ == "__main__":
    print("=== Registrierung ===")
    register_user("techniker01", "Sicher123!")
    register_user("operator02", "Maschine456")
    
    print("\n=== Anmeldeversuche ===")
    # Korrekt
    result = authenticate_user("techniker01", "Sicher123!")
    print(f"Anmeldung techniker01: {'✓ Erfolg' if result else '✗ Fehlgeschlagen'}")
    
    # Falsch
    result = authenticate_user("techniker01", "FalschesPasswort")
    print(f"Anmeldung (falsches PW): {'✓ Erfolg' if result else '✗ Fehlgeschlagen'}")
```

> [!TIP]
> bcrypt-Funktionen:
> - `bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())` → Hash erzeugen
> - `bcrypt.checkpw(password.encode('utf-8'), hashed)` → Passwort prüfen

---

### Aufgabe P4: Cloud-API für Produktionsdaten (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 40-50 Minuten  
**Vorkenntnisse**: `requests`, JSON, Error Handling, Pagination, Datenanalyse  
**Maschinenbau-Kontext**: Abruf von Produktionsdaten aus Cloud-Plattform (z.B. Azure IoT, AWS IoT)

Ein Produktionsleiter möchte täglich einen Report über die Maschinenauslastung erstellen. Die Daten werden von einer Cloud-Plattform bereitgestellt, die eine REST-API mit Pagination (Seiten) anbietet.

**Aufgabenstellung:**

Implementiere ein Programm, das Produktionsdaten von einer paginierten API abruft, aggregiert und einen Report ausgibt.

**API-Details:**
- **Base-URL**: `https://api.production-cloud.example.com/v1/machine-data`
- **Methode**: GET
- **Query-Parameter**: 
  - `date` (Format: "YYYY-MM-DD")
  - `page` (Seitennummer, Start: 1)
  - `per_page` (Datensätze pro Seite, max. 100)
- **Header**: `Authorization: Bearer <api_key>`
- **Response-Format**: JSON

**Beispiel-Response (Seite 1):**
```json
{
  "data": [
    {"machine_id": "CNC_01", "runtime_hours": 8.5, "parts_produced": 142, "status": "active"},
    {"machine_id": "CNC_02", "runtime_hours": 7.2, "parts_produced": 98, "status": "active"},
    {"machine_id": "ROBOT_01", "runtime_hours": 9.1, "parts_produced": 205, "status": "maintenance"}
  ],
  "pagination": {
    "page": 1,
    "per_page": 100,
    "total_pages": 3,
    "total_items": 287
  }
}
```

**Anforderungen:**

**Teilaufgabe 1**: Implementiere `fetch_all_production_data(date, api_key)`:
- Ruft alle Seiten der API ab (Pagination-Loop)
- Kombiniert alle Datensätze in einer Liste
- Gibt komplette Liste zurück

**Teilaufgabe 2**: Implementiere `analyze_production_data(data)`:
- Berechnet Gesamt-Laufzeit (Summe `runtime_hours`)
- Berechnet Gesamt-Stückzahl (Summe `parts_produced`)
- Zählt Maschinen nach Status (`active`, `maintenance`, `error`)
- Gibt Dictionary mit Ergebnissen zurück

**Teilaufgabe 3**: Implementiere `generate_report(date, api_key)`:
- Ruft Daten ab mit `fetch_all_production_data()`
- Analysiert Daten mit `analyze_production_data()`
- Gibt formatierten Report aus

**Benötigte Testdaten**: 
- **Mock-API-Datei**: `testdaten/production_api_pages.json` (mehrere Seiten simulieren)
- Für echte Tests: Verwende Mock-Server oder lokale JSON-Dateien

**Beispiel Ein-/Ausgabe**:
```python
API_KEY = "prod_key_xyz789"
generate_report("2026-01-05", API_KEY)

# Ausgabe:
# === Produktionsreport 2026-01-05 ===
# Gesamte Laufzeit: 245.8 Stunden
# Produzierte Teile: 5432 Stück
# Maschinenstatusverteilung:
#   - Aktiv: 18 Maschinen
#   - Wartung: 3 Maschinen
#   - Fehler: 1 Maschine
# Durchschnittliche Teile/Stunde: 22.1
```

**Starter-Code**:
```python
import requests

def fetch_all_production_data(date, api_key):
    """
    Ruft alle Produktionsdaten für ein Datum ab (alle Seiten).
    
    Args:
        date: Datum im Format "YYYY-MM-DD"
        api_key: API-Schlüssel
    
    Returns:
        Liste mit allen Datensätzen oder None bei Fehler
    """
    # Dein Code hier
    pass

def analyze_production_data(data):
    """
    Analysiert Produktionsdaten.
    
    Args:
        data: Liste von Maschinen-Datensätzen
    
    Returns:
        Dictionary mit Analyse-Ergebnissen
    """
    # Dein Code hier
    pass

def generate_report(date, api_key):
    """
    Erstellt und zeigt Produktionsreport an.
    
    Args:
        date: Datum im Format "YYYY-MM-DD"
        api_key: API-Schlüssel
    """
    # Dein Code hier
    pass

# Test
if __name__ == "__main__":
    API_KEY = "demo_key_xyz789"
    generate_report("2026-01-05", API_KEY)
```

> [!TIP]
> Pagination-Loop-Muster:
> ```python
> page = 1
> while True:
>     response = requests.get(url, params={"page": page})
>     data = response.json()
>     all_items.extend(data['data'])
>     if page >= data['pagination']['total_pages']:
>         break
>     page += 1
> ```

---

### Aufgabe P5: Firmware-Update-System mit Signatur-Verifizierung (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 60-75 Minuten  
**Vorkenntnisse**: `hashlib`, `requests`, File I/O, JSON, RSA (vereinfacht), Exception Handling  
**Maschinenbau-Kontext**: Sichere Firmware-Updates für Industrieroboter

Ein Roboterhersteller stellt Firmware-Updates über eine Cloud-API bereit. Jedes Update ist digital signiert, um Manipulation zu verhindern. Der Roboter prüft vor der Installation die digitale Signatur.

**Aufgabenstellung:**

Implementiere ein Firmware-Update-System mit folgenden Komponenten:

**Teilaufgabe 1**: `download_firmware(version, api_key, save_path)`:
- Lädt Firmware-Datei von API herunter
- Speichert Datei lokal
- Gibt Pfad und Metadaten zurück

**API-Details für Firmware-Download**:
- **URL**: `https://api.robot-updates.example.com/v1/firmware/{version}`
- **Methode**: GET
- **Response**: Binary-Datei (`.bin`)
- **Header**: `Authorization: Bearer <api_key>`

**Teilaufgabe 2**: `download_signature(version, api_key)`:
- Lädt digitale Signatur (Hash + Metadaten) von API
- Response-Format: JSON

**Beispiel-Response:**
```json
{
  "version": "v2.3.0",
  "sha256_hash": "3a5f8c9d7b2e...",
  "signature": "d8f2a1c4b3e...",
  "signed_by": "RobotCorp CA",
  "signing_date": "2026-01-05T09:00:00Z"
}
```

**Teilaufgabe 3**: `verify_firmware_integrity(filepath, expected_hash)`:
- Berechnet SHA-256-Hash der heruntergeladenen Firmware
- Vergleicht mit erwartetem Hash aus Signatur
- Gibt `True/False` zurück

**Teilaufgabe 4**: `verify_signature_simple(signature_data)`:
- Vereinfachte Signaturprüfung (ohne echtes RSA, da komplex)
- Prüft, ob `signed_by == "RobotCorp CA"` (vertrauenswürdige CA)
- Prüft, ob Signatur-Datum nicht älter als 30 Tage
- Gibt `True/False` zurück

**Teilaufgabe 5**: `install_firmware(filepath)`:
- Simuliert Firmware-Installation (nur Ausgabe, keine echte Installation)
- Zeigt Fortschritt und Erfolg an

**Teilaufgabe 6**: `update_robot_firmware(version, api_key)`:
- Hauptfunktion, die alle Schritte kombiniert:
  1. Firmware herunterladen
  2. Signatur herunterladen
  3. Integrität prüfen (Hash)
  4. Signatur verifizieren
  5. Bei Erfolg: Firmware installieren
  6. Bei Fehler: Update abbrechen

**Benötigte Testdaten**: 
- **Firmware-Datei**: `testdaten/firmware_v2.3.0.bin` (z.B. 500 KB Dummy-Datei)
- **Signatur-JSON**: `testdaten/firmware_v2.3.0_signature.json`
- Siehe `testdaten/README.md` für Details

**Beispiel Ein-/Ausgabe**:
```python
API_KEY = "robot_api_key_abc123"
update_robot_firmware("v2.3.0", API_KEY)

# Ausgabe:
# [1/5] Firmware v2.3.0 herunterladen...
# ✓ Firmware heruntergeladen: 524288 Bytes
# [2/5] Signatur herunterladen...
# ✓ Signatur abgerufen
# [3/5] Integrität prüfen (SHA-256)...
# ✓ Hash stimmt überein: 3a5f8c9d7b2e...
# [4/5] Digitale Signatur verifizieren...
# ✓ Signatur gültig (CA: RobotCorp CA)
# [5/5] Firmware installieren...
# ✓ Installation erfolgreich abgeschlossen
# 
# === Update-Report ===
# Version: v2.3.0
# Installiert am: 2026-01-05 10:45:23
# Status: ✓ Erfolgreich
```

**Starter-Code**:
```python
import hashlib
import requests
from datetime import datetime, timedelta

def download_firmware(version, api_key, save_path):
    """Lädt Firmware-Datei herunter."""
    # Dein Code hier
    pass

def download_signature(version, api_key):
    """Lädt Signatur-Metadaten herunter."""
    # Dein Code hier
    pass

def verify_firmware_integrity(filepath, expected_hash):
    """Prüft Firmware-Hash."""
    # Dein Code hier (wie P1)
    pass

def verify_signature_simple(signature_data):
    """Vereinfachte Signaturprüfung."""
    # Dein Code hier
    pass

def install_firmware(filepath):
    """Simuliert Firmware-Installation."""
    print("[5/5] Firmware installieren...")
    # Simulation (keine echte Installation)
    print("✓ Installation erfolgreich abgeschlossen")

def update_robot_firmware(version, api_key):
    """Hauptfunktion für Firmware-Update."""
    print(f"=== Firmware-Update {version} ===\n")
    # Dein Code hier: Kombiniere alle Schritte
    pass

# Test
if __name__ == "__main__":
    API_KEY = "demo_robot_key_abc123"
    update_robot_firmware("v2.3.0", API_KEY)
```

**Bonus-Challenge** (optional):
- Implementiere echte RSA-Signaturprüfung mit `cryptography`-Bibliothek (statt vereinfachter Prüfung)
- Speichere Update-History in JSON-Datei (Datum, Version, Status)
- Implementiere Rollback-Funktion (vorherige Firmware wiederherstellen)

> [!TIP]
> Für Tests kannst du Mock-Daten verwenden:
> - Erstelle kleine Dummy-Firmware-Datei mit `open("firmware.bin", "wb").write(b"FIRMWARE_DATA" * 1000)`
> - Berechne SHA-256-Hash dieser Datei
> - Erstelle JSON-Signatur mit diesem Hash