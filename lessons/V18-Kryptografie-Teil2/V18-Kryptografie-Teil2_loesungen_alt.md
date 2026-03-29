# V18: Lösungen - Kryptografie Teil 2 & HTTP-Requests

> [!WARNING]
> Versuche die Aufgaben zuerst selbstständig zu lösen, bevor du die Lösungen ansiehst!

---

## Teil A: Theorie-Aufgaben - Lösungen

### Lösung T1: Hash-Funktionen und ihre Eigenschaften

**Lösung**:

**a) Was ist eine kryptografische Hash-Funktion?**

Eine kryptografische Hash-Funktion ist eine mathematische Funktion, die eine Eingabe beliebiger Länge (z.B. eine Datei, ein Passwort, eine Nachricht) auf eine Ausgabe fester Länge abbildet, den sogenannten Hash-Wert oder Fingerprint. Die Funktion ist deterministisch (gleiche Eingabe → gleicher Hash) und eine Einwegfunktion (aus dem Hash kann die Eingabe nicht rekonstruiert werden).

**Drei Haupteigenschaften:**

1. **Einwegfunktion (Preimage Resistance)**: Aus einem gegebenen Hash-Wert $h$ ist es praktisch unmöglich, die ursprüngliche Eingabe $m$ zu finden, sodass $H(m) = h$. Dies gewährleistet, dass selbst wenn ein Angreifer den Hash-Wert sieht, er nicht auf die Originaldaten zurückschließen kann. Für Passwort-Hashing bedeutet das: Ein gestohlener Hash kann nicht zurück in das Passwort konvertiert werden.

2. **Kollisionsresistenz**: Es ist praktisch unmöglich, zwei unterschiedliche Eingaben $m_1 \neq m_2$ zu finden, die denselben Hash-Wert erzeugen: $H(m_1) = H(m_2)$. Dies ist die stärkste Eigenschaft und fundamental für digitale Signaturen. Wenn zwei Dateien unterschiedlich sind, müssen ihre Hashes unterschiedlich sein – sonst könnte ein Angreifer eine manipulierte Datei mit gleichem Hash unterschieben.

3. **Avalanche-Effekt (Lawineneffekt)**: Eine minimale Änderung der Eingabe (auch nur ein Bit) führt zu einer vollständig unterschiedlichen Ausgabe. Etwa 50% der Bits im Hash-Wert sollten sich ändern. Dies verhindert, dass aus ähnlichen Hashes auf ähnliche Eingaben geschlossen werden kann. Beispiel: "Hallo" und "Hallo!" haben komplett verschiedene SHA-256-Hashes, obwohl sie sich nur um ein Zeichen unterscheiden.

**b) Warum ist MD5 nicht geeignet?**

MD5 ist **kryptografisch gebrochen** und sollte nicht für sicherheitskritische Anwendungen wie NC-Programm-Integrität verwendet werden. Die Gründe:

1. **Praktische Kollisionsangriffe**: Seit 2004 sind Kollisionsangriffe gegen MD5 bekannt und praktisch durchführbar. Ein Angreifer kann zwei unterschiedliche NC-Programme erstellen, die denselben MD5-Hash haben. Das bedeutet: Ein manipuliertes Programm könnte den gleichen Hash haben wie das Original und würde von einem MD5-basierten Integritätssystem als "korrekt" akzeptiert werden. Ein solcher Angriff dauert auf modernen Computern nur wenige Stunden.

2. **Reale Angriffe in der Vergangenheit**: 2008 wurde demonstriert, dass man gefälschte SSL-Zertifikate mit identischem MD5-Hash erstellen kann. Dies führte zum kompletten Verbot von MD5 in TLS/SSL. Im Maschinenbau könnte ein Angreifer analog ein manipuliertes NC-Programm mit gleichem MD5-Hash einschleusen.

3. **128-Bit-Hash ist zu kurz**: MD5 erzeugt nur 128-Bit-Hashes (16 Byte). Mit modernen GPUs können Milliarden MD5-Hashes pro Sekunde berechnet werden, was Brute-Force-Angriffe vereinfacht.

**Empfehlung**: Verwende **SHA-256** oder besser. SHA-256 ist:
- Kollisionsresistent (keine praktischen Kollisionen bekannt)
- Weit verbreitet und standardisiert (NIST-Standard)
- Schnell genug für große Dateien
- 256-Bit-Ausgabe (32 Byte, 64 Hex-Zeichen)

SHA-3 ist eine Alternative, wenn Diversifikation gewünscht ist, aber SHA-256 ist der aktuelle Industriestandard.

**c) Zwei NC-Programme mit identischem SHA-256-Hash**

Wenn `Programm_A.nc` und `Programm_B.nc` denselben SHA-256-Hash haben, kannst du mit **an Sicherheit grenzender Wahrscheinlichkeit** aussagen, dass die beiden Programme **identisch** sind (Byte-für-Byte gleich).

**Begründung**: Die Eigenschaft der **Kollisionsresistenz** garantiert, dass es praktisch unmöglich ist, zwei unterschiedliche Dateien mit gleichem SHA-256-Hash zu finden. Die Wahrscheinlichkeit einer zufälligen Kollision ist astronomisch klein: $2^{-256} \approx 10^{-77}$. Zum Vergleich: Die Anzahl der Atome im sichtbaren Universum wird auf etwa $10^{80}$ geschätzt.

In der Praxis bedeutet gleicher SHA-256-Hash: **Die Dateien sind identisch**. Unterschiedliche Dateien haben immer unterschiedliche SHA-256-Hashes (mit praktischer Sicherheit).

**Hinweis**: Der Avalanche-Effekt verstärkt dies: Selbst wenn sich Programm A und Programm B nur um ein einziges Zeichen unterscheiden würden, wären ihre Hashes komplett verschieden.

**Erklärung**:

Die Aufgabe zeigt die praktische Anwendung von Hash-Funktionen zur Integritätsprüfung. Im Maschinenbau-Kontext:

- NC-Programme werden oft über Netzwerk übertragen (von Programmierer-PC zur CNC-Maschine)
- Während der Übertragung könnten Daten beschädigt werden (Netzwerkfehler, Bitfehler)
- Ein Angreifer könnte versuchen, das Programm zu manipulieren

Der SHA-256-Hash dient als digitaler Fingerabdruck. Vor der Übertragung berechnet der Programmierer den Hash, die CNC-Maschine berechnet nach Empfang ebenfalls den Hash und vergleicht. Stimmen sie überein → Datei ist identisch und unverändert.

**Häufige Fehler**:

- **Fehler**: "Gleicher Hash bedeutet, die Dateien sind wahrscheinlich gleich, aber nicht sicher."
  - **Warum falsch**: Bei SHA-256 ist die Wahrscheinlichkeit einer Kollision so gering, dass man von praktischer Sicherheit sprechen kann. Es ist keine "Wahrscheinlichkeit", sondern faktisch sicher.

- **Fehler**: "MD5 ist schneller, daher besser für große NC-Programme."
  - **Warum falsch**: Die Geschwindigkeitsdifferenz zwischen MD5 und SHA-256 ist für Dateien im Megabyte-Bereich vernachlässigbar (Millisekunden), aber die Sicherheitslücken von MD5 sind fatal. Sicherheit geht vor Geschwindigkeit.

- **Fehler**: "Ich nutze MD5, aber mit zusätzlichem Salt, dann ist es sicher."
  - **Warum falsch**: Salting hilft gegen Rainbow Tables bei Passwort-Hashing, aber nicht gegen Kollisionsangriffe. Ein Angreifer kann gezielt zwei Dateien erzeugen, die denselben MD5-Hash haben, unabhängig von Salt.

---

### Lösung T2: Digitale Signaturen verstehen

**Lösung**:

**a) Wie erstellt der Hersteller die digitale Signatur?**

**Schritt-für-Schritt-Prozess:**

1. **Hash berechnen**: Der Hersteller berechnet den SHA-256-Hash der Firmware-Datei `firmware_v2.3.bin` (200 MB):
   ```
   h = SHA-256(firmware_v2.3.bin)
   ```
   Ergebnis: Ein 256-Bit-Hash-Wert (32 Byte, 64 Hex-Zeichen), z.B. `3a5f8c9d7b2e...`

2. **Hash mit Private Key verschlüsseln**: Der Hash-Wert wird mit dem **privaten Schlüssel** des Herstellers verschlüsselt (RSA-Verschlüsselung):
   ```
   signature = RSA_Encrypt(h, Private_Key_Hersteller)
   ```
   Ergebnis: Die digitale Signatur (z.B. 256 Byte bei RSA-2048)

3. **Firmware und Signatur verteilen**: Der Hersteller sendet:
   - Die Firmware-Datei: `firmware_v2.3.bin` (200 MB)
   - Die digitale Signatur: `signature` (256 Byte)
   - Optional: Metadaten (Version, Datum, Zertifikat)

**Wichtig**: Nur der Hash wird verschlüsselt, nicht die gesamte Firmware! Dies ist effizienter.

**b) Wie verifiziert der Roboter die digitale Signatur?**

**Schritt-für-Schritt-Prozess:**

1. **Empfangene Firmware hashen**: Der Roboter berechnet den SHA-256-Hash der empfangenen Firmware-Datei:
   ```
   h_empfangen = SHA-256(firmware_v2.3.bin_empfangen)
   ```

2. **Signatur mit Public Key entschlüsseln**: Der Roboter entschlüsselt die Signatur mit dem **öffentlichen Schlüssel** des Herstellers (dieser ist im Roboter vorinstalliert):
   ```
   h_signatur = RSA_Decrypt(signature, Public_Key_Hersteller)
   ```

3. **Hashes vergleichen**: Der Roboter vergleicht die beiden Hashes:
   ```
   if h_empfangen == h_signatur:
       print("✓ Signatur gültig - Firmware authentisch")
       install_firmware()
   else:
       print("✗ Signatur ungültig - Firmware abgelehnt")
       abort_installation()
   ```

**Was passiert bei Fehlschlag?**
- Die Installation wird **sofort abgebrochen**
- Eine Fehlermeldung wird ins Log geschrieben
- Optional: Benachrichtigung an Administrator
- Der Roboter bleibt mit alter Firmware betriebsfähig

**Sicherheitsaspekt**: Selbst wenn ein Angreifer die Firmware manipuliert, ändert sich der Hash. Da der Angreifer nicht den Private Key des Herstellers besitzt, kann er keine gültige Signatur für die manipulierte Firmware erstellen.

**c) Warum nur Hash signieren statt gesamte Firmware?**

**Grund 1: Performance / Geschwindigkeit**
- RSA-Verschlüsselung ist sehr langsam (ca. 1000x langsamer als symmetrische Verschlüsselung)
- 200 MB Firmware direkt mit RSA verschlüsseln würde Stunden dauern
- Ein 256-Bit-Hash verschlüsseln dauert Millisekunden
- **Vorteil**: Signatur-Erstellung ist praktisch instant, auch für große Dateien

**Grund 2: Dateigröße / Speicher**
- RSA-verschlüsselte Daten sind größer als Original (bei RSA-2048: Ausgabe ist immer 256 Byte pro Block)
- 200 MB Firmware würde verschlüsselt zu ~250 MB
- Hash ist nur 32 Byte, Signatur ist 256 Byte → vernachlässigbar kleine Übertragung
- **Vorteil**: Signatur kann problemlos mit Firmware übertragen werden ohne Bandbreite zu verschwenden

**Grund 3: Mathematische Limitierung**
- RSA kann nur Datenblöcke bis zur Schlüssellänge verschlüsseln (RSA-2048 → max. 245 Byte pro Block)
- Große Dateien müssten in tausende Blöcke aufgeteilt werden
- **Vorteil**: Hash hat immer feste Länge (256 Bit), passt in einen RSA-Block

**d) Kann ein Angreifer mit Public Key gefälschte Firmware signieren?**

**Antwort: Nein!**

**Begründung**: 
Der **Public Key** kann nur zum **Entschlüsseln** (Verifizieren) von Signaturen verwendet werden, nicht zum **Erstellen** (Verschlüsseln) neuer Signaturen. 

**Asymmetrische Verschlüsselung funktioniert so:**
- **Private Key → Verschlüsseln** (Signatur erstellen): Nur der Hersteller kann das
- **Public Key → Entschlüsseln** (Signatur prüfen): Jeder kann das

Ein Angreifer mit Public Key kann:
- ✅ Bestehende Signaturen verifizieren
- ✅ Sehen, ob eine Firmware vom Hersteller stammt
- ❌ Keine neuen Signaturen erstellen (dafür bräuchte er den Private Key)

**Szenario**:
1. Angreifer manipuliert Firmware: `firmware_manipuliert.bin`
2. Angreifer berechnet Hash: `h_manipuliert = SHA-256(firmware_manipuliert.bin)`
3. Angreifer versucht Signatur zu erstellen: `signature = RSA_Encrypt(h_manipuliert, ???)`
   - **Problem**: Er hat keinen Private Key!
   - Selbst mit Public Key kann er keine gültige Signatur erzeugen
4. Roboter lehnt Firmware ab, da Signatur ungültig

**Hinweis**: Genau das ist der Sinn asymmetrischer Kryptografie: Der Public Key kann öffentlich sein, ohne die Sicherheit zu gefährden.

**Lösungsweg Schritt für Schritt**:

Die Aufgabe zeigt das Kernkonzept digitaler Signaturen:
1. **Authentizität**: Die Signatur beweist, dass die Firmware vom Hersteller stammt (nur er hat den Private Key)
2. **Integrität**: Jede Änderung an der Firmware macht die Signatur ungültig (Avalanche-Effekt des Hashes)
3. **Non-Repudiation**: Der Hersteller kann später nicht bestreiten, die Firmware signiert zu haben

Im Maschinenbau ist dies kritisch:
- Manipulierte Firmware könnte Maschinen beschädigen
- Malware könnte Produktionsdaten stehlen
- Fehlerhafte Firmware könnte Sicherheitssysteme deaktivieren

Digitale Signaturen sind daher in Industrie 4.0-Umgebungen unverzichtbar.

**Häufige Fehler**:

- **Fehler**: "Die gesamte Firmware wird mit dem Private Key verschlüsselt."
  - **Warum falsch**: Nur der Hash wird verschlüsselt, nicht die Firmware selbst. Grund: Performance und Praktikabilität.

- **Fehler**: "Mit dem Public Key kann man auch Signaturen erstellen."
  - **Warum falsch**: Public Key ist zum Entschlüsseln/Verifizieren, nicht zum Verschlüsseln/Signieren. Das ist der Kern asymmetrischer Kryptografie.

- **Fehler**: "Digitale Signatur und Verschlüsselung ist dasselbe."
  - **Warum falsch**: Signatur gewährleistet Authentizität + Integrität, Verschlüsselung gewährleistet Vertraulichkeit. Beides sind unterschiedliche Ziele.

---

## Teil B: Python-Aufgaben - Lösungen

### Lösung P1: NC-Programm Hash-Berechnung mit hashlib

```python
import hashlib
import os

def calculate_file_hash(filepath):
    """Berechnet SHA-256-Hash einer Datei (blockweise)."""
    try:
        hash_obj = hashlib.sha256()
        with open(filepath, 'rb') as f:
            while block := f.read(4096):
                hash_obj.update(block)
        return hash_obj.hexdigest()
    except FileNotFoundError:
        print(f"✗ Datei '{filepath}' nicht gefunden")
        return None
    except Exception as e:
        print(f"✗ Fehler: {e}")
        return None

def verify_nc_program(filepath, expected_hash):
    """Verifiziert NC-Programm gegen bekannten Hash."""
    calculated_hash = calculate_file_hash(filepath)
    if calculated_hash and calculated_hash.lower() == expected_hash.lower():
        print(f"✓ Integrität bestätigt: {calculated_hash[:16]}...")
        return True
    else:
        print(f"✗ Hash stimmt nicht überein!")
        return False
```

**Erklärung**: Blockweises Lesen mit `f.read(4096)` verhindert Speicherprobleme bei großen Dateien. Wichtig: `'rb'` für Binary-Modus (Hash-Funktionen arbeiten mit Bytes, nicht Strings). `.update()` fügt jeden Block zum Hash hinzu.

---

### Lösung P2: Material-Datenbank REST API

```python
import requests
from requests.exceptions import Timeout, ConnectionError, HTTPError
import json

def get_material_properties(material_name, api_key, base_url="https://api.materials-db.example.com/v1/materials"):
    """Ruft Materialeigenschaften von REST-API ab."""
    try:
        response = requests.get(
            base_url,
            params={"name": material_name},
            headers={
                "Authorization": f"Bearer {api_key}",
                "Accept": "application/json"
            },
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    
    except Timeout:
        print("✗ Timeout")
    except ConnectionError:
        print("✗ Verbindungsfehler")
    except HTTPError:
        print(f"✗ HTTP {response.status_code}")
    except json.JSONDecodeError:
        print("✗ Ungültiges JSON")
    return None

# Test mit Mock-Daten
if __name__ == "__main__":
    mock_file = "testdaten/material_api_mock.json"
    if os.path.exists(mock_file):
        with open(mock_file, 'r') as f:
            materials = json.load(f)
            material = next((m for m in materials if m['material'] == 'S355'), None)
            print(f"Material: {material['material']}, Zugfestigkeit: {material['properties']['tensile_strength_mpa']} MPa")
```

**Erklärung**: `params=` codiert Query-Parameter automatisch. `timeout=10` verhindert hängende Requests. `.raise_for_status()` wirft Exception bei 4xx/5xx. API-Keys gehören in Authorization-Header, nicht in URL (Security).

---

### Lösung P3: Passwort-Hashing mit bcrypt

```python
import bcrypt

users_db = {}

def register_user(username, password):
    """Registriert neuen Benutzer mit bcrypt-Hash."""
    if username in users_db:
        print(f"✗ Benutzer '{username}' existiert bereits")
        return False
    
    if len(password) < 8:
        print("✗ Passwort muss mindestens 8 Zeichen lang sein")
        return False
    
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    users_db[username] = hashed
    print(f"✓ Benutzer '{username}' registriert")
    return True

def authenticate_user(username, password):
    """Prüft Benutzeranmeldung."""
    if username not in users_db:
        return False
    return bcrypt.checkpw(password.encode('utf-8'), users_db[username])

# Test
if __name__ == "__main__":
    register_user("techniker01", "Sicher123!")
    register_user("operator02", "Maschine456")
    
    # Anmeldeversuche
    if authenticate_user("techniker01", "Sicher123!"):
        print("✓ Zugriff gewährt")
    
    if not authenticate_user("techniker01", "FalschesPasswort"):
        print("✗ Zugriff verweigert")
```

**Erklärung**: bcrypt ist für Passwörter geeignet (SHA-256 zu schnell → Brute-Force). `gensalt(rounds=12)` generiert Salt automatisch, bcrypt speichert ihn im Hash (`$2b$12$...`). Salt verhindert Rainbow Tables: Gleiches Passwort → unterschiedliche Hashes.

---

### Lösung P4: Cloud-API für Produktionsdaten mit Pagination

```python
import requests
import json
import os

def fetch_all_production_data(date, api_key, base_url="https://api.production-cloud.example.com/v1/machine-data"):
    """Ruft alle Produktionsdaten ab (alle Seiten)."""
    all_data = []
    page = 1
    
    try:
        while True:
            response = requests.get(
                base_url,
                params={"date": date, "page": page, "per_page": 100},
                headers={"Authorization": f"Bearer {api_key}"},
                timeout=10
            )
            response.raise_for_status()
            result = response.json()
            
            all_data.extend(result['data'])
            pagination = result['pagination']
            
            if page >= pagination['total_pages']:
                break
            page += 1
        
        return all_data
    except Exception as e:
        print(f"✗ Fehler: {e}")
        return None

def analyze_production_data(data):
    """Analysiert Produktionsdaten."""
    if not data:
        return None
    
    total_runtime = sum(m.get('runtime_hours', 0) for m in data)
    total_parts = sum(m.get('parts_produced', 0) for m in data)
    status_count = {}
    
    for machine in data:
        status = machine.get('status', 'unknown')
        status_count[status] = status_count.get(status, 0) + 1
    
    return {
        'total_machines': len(data),
        'total_runtime_hours': round(total_runtime, 2),
        'total_parts_produced': total_parts,
        'status_distribution': status_count
    }

# Test mit Mock-Daten
if __name__ == "__main__":
    # Mock-Daten laden
    all_data = []
    for i in range(1, 4):
        path = f"testdaten/production_api_page{i}.json"
        if os.path.exists(path):
            with open(path, 'r') as f:
                all_data.extend(json.load(f)['data'])
    
    results = analyze_production_data(all_data)
    print(f"Maschinen: {results['total_machines']}")
    print(f"Laufzeit: {results['total_runtime_hours']} h")
    print(f"Teile: {results['total_parts_produced']:,}")
    print(f"Status: {results['status_distribution']}")
```

**Erklärung**: Pagination-Loop läuft bis `page >= total_pages`. `.extend()` fügt Elemente hinzu (nicht `.append()`, das würde Liste-in-Liste erzeugen). Wichtig: `timeout=` setzen, sonst kann Loop bei Netzwerkfehler ewig laufen.

---

### Lösung P5: Firmware-Update-System mit Signatur-Verifizierung

```python
import hashlib
import requests
import json
import os
from datetime import datetime, timedelta

def download_firmware(version, api_key, save_path):
    """Lädt Firmware-Datei herunter."""
    url = f"https://api.robot-updates.example.com/v1/firmware/{version}/download"
    try:
        response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"}, timeout=30, stream=True)
        response.raise_for_status()
        
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return True, save_path, os.path.getsize(save_path)
    except Exception as e:
        print(f"✗ Download-Fehler: {e}")
        return False, None, 0

def download_signature(version, api_key):
    """Lädt digitale Signatur-Metadaten herunter."""
    url = f"https://api.robot-updates.example.com/v1/firmware/{version}/signature"
    try:
        response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"}, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"✗ Signatur-Fehler: {e}")
        return None

def verify_firmware_integrity(filepath, expected_hash):
    """Prüft Firmware-Hash."""
    try:
        hash_obj = hashlib.sha256()
        with open(filepath, 'rb') as f:
            while block := f.read(4096):
                hash_obj.update(block)
        
        calculated = hash_obj.hexdigest()
        if calculated.lower() == expected_hash.lower():
            print(f"✓ Hash stimmt überein: {calculated[:16]}...")
            return True
        else:
            print(f"✗ Hash-Mismatch! Firmware manipuliert?")
            return False
    except Exception as e:
        print(f"✗ Hash-Fehler: {e}")
        return False

def verify_signature_simple(signature_data):
    """Vereinfachte Signaturprüfung."""
    signed_by = signature_data.get('signed_by', '')
    if signed_by not in ['RobotCorp CA', 'RobotCorp Root CA']:
        print(f"✗ Unbekannte CA: {signed_by}")
        return False
    
    signing_date_str = signature_data.get('signing_date', '')
    try:
        signing_date = datetime.fromisoformat(signing_date_str.replace('Z', '+00:00'))
        age_days = (datetime.now() - signing_date.replace(tzinfo=None)).days
        if age_days > 30:
            print(f"✗ Signatur zu alt: {age_days} Tage")
            return False
    except:
        print("✗ Ungültiges Signatur-Datum")
        return False
    
    print(f"✓ Signatur gültig (CA: {signed_by})")
    return True

def update_robot_firmware(version, api_key, use_mock_data=False):
    """Hauptfunktion für Firmware-Update."""
    print(f"\n{'='*70}")
    print(f"FIRMWARE-UPDATE {version}")
    print(f"{'='*70}\n")
    
    # Schritt 1: Firmware herunterladen
    if use_mock_data:
        firmware_path = os.path.join("testdaten", f"firmware_{version}.bin")
        if not os.path.exists(firmware_path):
            print("✗ Mock-Datei nicht gefunden")
            return False
        print(f"[1/5] Firmware geladen (Mock): {os.path.getsize(firmware_path):,} Bytes")
    else:
        firmware_path = f"firmware_{version}.bin"
        success, firmware_path, size = download_firmware(version, api_key, firmware_path)
        if not success:
            return False
    
    # Schritt 2: Signatur herunterladen
    if use_mock_data:
        sig_path = os.path.join("testdaten", f"firmware_{version}_signature.json")
        with open(sig_path, 'r') as f:
            signature_data = json.load(f)
        print(f"[2/5] Signatur geladen (Mock)")
    else:
        signature_data = download_signature(version, api_key)
        if not signature_data:
            return False
    
    # Schritt 3: Integrität prüfen
    print("[3/5] Integrität prüfen...")
    if not verify_firmware_integrity(firmware_path, signature_data.get('sha256_hash', '')):
        print("\n✗ Update abgebrochen: Integritätsprüfung fehlgeschlagen")
        return False
    
    # Schritt 4: Signatur verifizieren
    print("[4/5] Signatur verifizieren...")
    if not verify_signature_simple(signature_data):
        print("\n✗ Update abgebrochen: Signatur ungültig")
        return False
    
    # Schritt 5: Installation
    print("[5/5] Installation simuliert... ✓")
    print(f"\n✓ Update erfolgreich: {version}")
    return True

# Test
if __name__ == "__main__":
    update_robot_firmware("v2.3.0", "demo_key", use_mock_data=True)
```

**Erklärung**: Kombiniert alle bisherigen Konzepte: Datei-Download mit `stream=True` für große Dateien, Hash-Berechnung (wie P1), API-Requests (wie P2), Signatur-Prüfung (CA-Trust + Datum). Wichtig: Bei Fehler in Schritt 3/4 → Installation abbrechen! In Produktion: Echte RSA-Signatur mit `cryptography`-Library.

---