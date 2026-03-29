# V17: Übungsaufgaben - Kryptografie Teil 1

> [!NOTE]
> Diese Übungsaufgaben vertiefen das Verständnis der Vorlesung V17.
> Bearbeite die Aufgaben in der angegebenen Reihenfolge.

---

## Teil A: Theorie-Aufgaben

### Aufgabe T1: Symmetrische vs. Asymmetrische Verschlüsselung (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 5-10 Minuten

Vergleiche symmetrische und asymmetrische Verschlüsselungsverfahren anhand folgender Kriterien:

1. Welche Schlüssel werden verwendet?
2. Wie schnell sind die Verfahren im Vergleich?
3. Welches Verfahren eignet sich besser für die Verschlüsselung großer Datenmengen (z.B. 1 GB Videodatei)?
4. Welches Verfahren löst das Schlüsselaustausch-Problem?
5. Nenne je ein Beispiel für einen symmetrischen und asymmetrischen Algorithmus.

**Hinweise**:
- Denke an die Vor- und Nachteile beider Verfahren aus der Vorlesung.
- Überlege, welche praktischen Anwendungsfälle jeweils besser geeignet sind.

---

### Aufgabe T2: RSA-Schlüsselgenerierung verstehen (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 10-15 Minuten

Gegeben seien die beiden Primzahlen $p = 11$ und $q = 13$.

1. Berechne den Modulus $n = p \cdot q$.
2. Berechne die Euler'sche Phi-Funktion $\phi(n) = (p-1)(q-1)$.
3. Wähle einen öffentlichen Exponenten $e = 7$. Prüfe, ob $\gcd(e, \phi(n)) = 1$ gilt (Hinweis: 7 und 120 teilen keinen gemeinsamen Teiler außer 1).
4. Der private Exponent $d$ muss die Bedingung $d \cdot e \equiv 1 \mod \phi(n)$ erfüllen. Welcher Wert von $d$ erfüllt diese Bedingung? Teste die Werte $d = 103$ und prüfe: $(d \cdot e) \mod \phi(n) = 1$?
5. Gib den öffentlichen Schlüssel $(n, e)$ und den privaten Schlüssel $(n, d)$ an.

**Hinweise**:
- Verwende für Schritt 4 die Formel: $(d \cdot e) \mod \phi(n)$ sollte 1 ergeben.
- Du kannst Python als Taschenrechner verwenden: `(103 * 7) % 120`

---

### Aufgabe T3: Hybride Verschlüsselung analysieren (Schwer)

**Schwierigkeit**: ⭐⭐⭐ Schwer  
**Zeitaufwand**: ca. 15-25 Minuten

Alice möchte eine 500 MB große CAD-Datei sicher an Bob senden. Sie kennen sich nicht persönlich und haben noch nie kommuniziert. Bob hat ein RSA-Schlüsselpaar (2048 Bit) erstellt und seinen öffentlichen Schlüssel auf seiner Webseite veröffentlicht.

1. Erkläre Schritt für Schritt, wie Alice die Datei mit **hybrider Verschlüsselung** sicher an Bob senden kann.
2. Warum würde es **nicht funktionieren**, die gesamte 500 MB-Datei direkt mit RSA zu verschlüsseln? (Nenne mindestens zwei Gründe)
3. Welche Rolle spielt AES in diesem Szenario? Warum kann Alice nicht einfach die Datei mit AES verschlüsseln und den AES-Schlüssel per E-Mail an Bob senden?
4. Ein Angreifer (Eve) fängt die verschlüsselte Datei und den verschlüsselten AES-Schlüssel ab. Kann Eve die Datei entschlüsseln? Warum/warum nicht?
5. Bonus: Was passiert, wenn Alice versehentlich ihren **privaten** RSA-Schlüssel statt Bobs **öffentlichen** Schlüssel verwendet, um den AES-Schlüssel zu verschlüsseln?

**Hinweise**:
- Überlege dir die Schritte der hybriden Verschlüsselung aus der Vorlesung.
- Denke an die Geschwindigkeitsunterschiede zwischen RSA und AES.

---

## Teil B: Python-Aufgaben

### Aufgabe P1: Echo-Server und Client (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten  
**Vorkenntnisse**: `socket`-Modul, `socket.socket()`, `.bind()`, `.listen()`, `.accept()`, `.connect()`, `.send()`, `.recv()`, `.close()`  
**Maschinenbau-Kontext**: Grundlegende Client-Server-Kommunikation für CNC-Maschinen, die Statusmeldungen an einen zentralen Monitor senden.

Schreibe zwei Programme:

**1. Echo-Server** (`echo_server.py`):
- Erstelle einen TCP-Server auf `localhost` Port `9000`.
- Warte auf eine Client-Verbindung.
- Empfange eine Nachricht vom Client (bis zu 1024 Bytes).
- Gib die empfangene Nachricht auf der Konsole aus.
- Sende die Nachricht mit dem Präfix `"ECHO: "` zurück an den Client.
- Schließe die Verbindung.

**2. Echo-Client** (`echo_client.py`):
- Erstelle einen TCP-Client, der sich mit `localhost` Port `9000` verbindet.
- Sende die Nachricht `"CNC-Maschine #42: Bereit"` an den Server.
- Empfange die Antwort vom Server und gib sie auf der Konsole aus.
- Schließe die Verbindung.

**Beispiel Ein-/Ausgabe**:

```
# Server-Ausgabe:
Echo-Server läuft auf Port 9000...
Verbindung von ('127.0.0.1', 54321)
Empfangen: CNC-Maschine #42: Bereit
Gesendet: ECHO: CNC-Maschine #42: Bereit
Verbindung geschlossen

# Client-Ausgabe:
Verbunden mit Echo-Server
Gesendet: CNC-Maschine #42: Bereit
Antwort: ECHO: CNC-Maschine #42: Bereit
Verbindung geschlossen
```

**Hinweise**:
- Starte zuerst den Server, dann den Client.
- Vergiss nicht, Strings in Bytes zu konvertieren (`.encode()` und `.decode()`).
- **Testprogramm verfügbar**: Im Ordner `testprogramme/` findest du:
  - `P1_echo_server_VORLAGE.py` – Vorlage zum Vervollständigen
  - `P1_echo_client_TEST.py` – Test-Client für deinen Server

---

### Aufgabe P2: CNC-Temperatur-Monitor (Client/Server) (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: `socket`, `json`, String-Formatierung, Verzweigungen  
**Maschinenbau-Kontext**: Eine CNC-Maschine sendet Temperaturwerte an einen Monitoring-Server, der Warnungen ausgibt, wenn Grenzwerte überschritten werden.

Schreibe zwei Programme:

**1. Temperatur-Server** (`cnc_temp_server.py`):
- Erstelle einen TCP-Server auf `localhost` Port `5555`.
- Warte auf eine Verbindung von einer CNC-Maschine.
- Empfange JSON-Daten im Format: `{"maschine_id": "CNC-01", "temperatur": 75.5}`.
- Werte die Temperatur aus:
  - `temperatur < 60`: Antwort `{"status": "OK", "meldung": "Temperatur im Normbereich"}`
  - `60 <= temperatur < 80`: Antwort `{"status": "WARNUNG", "meldung": "Temperatur erhöht, Überwachung empfohlen"}`
  - `temperatur >= 80`: Antwort `{"status": "KRITISCH", "meldung": "Temperatur zu hoch! Kühlsystem prüfen!"}`
- Sende die Antwort als JSON zurück.
- Schließe die Verbindung.

**2. Temperatur-Client** (`cnc_temp_client.py`):
- Erstelle einen TCP-Client, der sich mit `localhost` Port `5555` verbindet.
- Sende Temperatur-Daten als JSON: `{"maschine_id": "CNC-01", "temperatur": 85.0}`.
- Empfange die Server-Antwort und gib sie formatiert aus.

**Beispiel Ein-/Ausgabe**:

```
# Server-Ausgabe:
Temperatur-Monitor läuft auf Port 5555...
Verbindung von ('127.0.0.1', 54322)
Empfangen: Maschine CNC-01, Temperatur: 85.0°C
Status: KRITISCH
Gesendet: {"status": "KRITISCH", "meldung": "Temperatur zu hoch! Kühlsystem prüfen!"}

# Client-Ausgabe:
Verbunden mit Temperatur-Server
Sende: {"maschine_id": "CNC-01", "temperatur": 85.0}
Antwort vom Server:
  Status: KRITISCH
  Meldung: Temperatur zu hoch! Kühlsystem prüfen!
```

**Hinweise**:
- Verwende `json.dumps()` zum Serialisieren und `json.loads()` zum Deserialisieren.
- Denke an `.encode("utf-8")` und `.decode("utf-8")`.
- **Testprogramm verfügbar**: `testprogramme/P2_cnc_temp_client_TEST.py` sendet automatisch 4 Tests mit verschiedenen Temperaturen (55°C, 72°C, 85°C, 60°C) und prüft die Antworten.

---

### Aufgabe P3: Multi-Client Sensordaten-Server (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 20-30 Minuten  
**Vorkenntnisse**: `socket`, `json`, Schleifen, Fehlerbehandlung (`try-except`)  
**Maschinenbau-Kontext**: Ein zentraler Server empfängt Sensordaten von mehreren Maschinen (sequenziell) und protokolliert kritische Ereignisse.

Schreibe ein Server-Programm **`sensor_server.py`**:

- Erstelle einen TCP-Server auf `localhost` Port `6000`.
- Implementiere eine Endlos-Schleife (`while True`), die kontinuierlich auf neue Verbindungen wartet.
- Empfange JSON-Daten im Format:
  ```json
  {
    "maschine_id": "Drehmaschine-03",
    "drehzahl": 8500,
    "vibration": 3.2,
    "temperatur": 68.5
  }
  ```
- Werte die Sensordaten aus und prüfe kritische Grenzwerte:
  - **Drehzahl** > 10000 RPM: Warnung
  - **Vibration** > 5.0 mm/s: Warnung
  - **Temperatur** > 80°C: Warnung
- Gib die empfangenen Daten und eventuelle Warnungen auf der Konsole aus.
- Sende eine Bestätigung zurück: `{"status": "OK", "warnungen": [...]}` (Liste der Warnungen oder leer).
- Schließe die Client-Verbindung nach jeder Übertragung.
- Der Server soll mit `Strg+C` beendet werden können (nutze `try-except KeyboardInterrupt`).

Schreibe zusätzlich ein Test-Client-Programm **`sensor_client_test.py`**:

- Verbinde dich mit `localhost` Port `6000`.
- Sende JSON-Testdaten (z.B. mit kritischen Werten: Drehzahl 12000, Vibration 6.5).
- Empfange und zeige die Server-Antwort an.

**Beispiel Ein-/Ausgabe**:

```
# Server-Ausgabe:
Sensor-Server läuft auf Port 6000...
Drücke Strg+C zum Beenden

[Neue Verbindung] ('127.0.0.1', 54323)
Maschine Drehmaschine-03:
  - Drehzahl: 12000 RPM ⚠️ WARNUNG: Drehzahl zu hoch!
  - Vibration: 6.5 mm/s ⚠️ WARNUNG: Vibration zu hoch!
  - Temperatur: 68.5°C
[Verbindung geschlossen]

# Client-Ausgabe:
Verbunden mit Sensor-Server
Gesendet: {"maschine_id": "Drehmaschine-03", ...}
Antwort: {"status": "OK", "warnungen": ["Drehzahl zu hoch", "Vibration zu hoch"]}
```

**Hinweise**:
- Verwende `while True` für die Endlos-Schleife.
- Nutze `try-except KeyboardInterrupt` zum sauberen Beenden.
- Schließe Client-Sockets mit `finally`, um Ressourcen-Lecks zu vermeiden.
- **Testprogramm verfügbar**: `testprogramme/P3_sensor_client_TEST.py` simuliert 5 verschiedene Maschinen mit normalen und kritischen Werten.

---

### Aufgabe P4: Roboter-Steuerungs-Protokoll (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 30-40 Minuten  
**Vorkenntnisse**: `socket`, `json`, Funktionen, Schleifen, Fehlerbehandlung  
**Maschinenbau-Kontext**: Ein Industrie-Roboter empfängt Steuerungsbefehle über ein Netzwerk und führt diese aus. Der Roboter-Server verarbeitet Befehle wie Bewegung, Greifen und Status-Abfragen.

Schreibe ein Server-Programm **`robot_server.py`**:

- Erstelle einen TCP-Server auf `localhost` Port `7000`.
- Definiere einen Roboter-Zustand (Dictionary oder Klasse):
  - `position`: Tupel `(x, y, z)` (initial: `(0, 0, 0)`)
  - `greifer_offen`: Boolean (initial: `True`)
  - `batterie`: Integer 0-100 (initial: `100`)
- Implementiere eine Endlos-Schleife, die Verbindungen akzeptiert.
- Empfange JSON-Befehle im Format:
  ```json
  {"befehl": "BEWEGE", "x": 10, "y": 20, "z": 5}
  {"befehl": "GREIFE"}
  {"befehl": "OEFFNE"}
  {"befehl": "STATUS"}
  ```
- Verarbeite die Befehle:
  - **"BEWEGE"**: Aktualisiere Position auf `(x, y, z)`. Reduziere Batterie um 5%. Antwort: `{"status": "OK", "position": [10, 20, 5], "batterie": 95}`
  - **"GREIFE"**: Schließe Greifer (`greifer_offen = False`). Reduziere Batterie um 2%. Antwort: `{"status": "OK", "greifer": "geschlossen", "batterie": 93}`
  - **"OEFFNE"**: Öffne Greifer (`greifer_offen = True`). Reduziere Batterie um 2%. Antwort: `{"status": "OK", "greifer": "offen", "batterie": 91}`
  - **"STATUS"**: Gib aktuellen Zustand zurück: `{"position": [10, 20, 5], "greifer": "offen", "batterie": 91}`
  - **Unbekannter Befehl**: Antwort: `{"status": "FEHLER", "meldung": "Unbekannter Befehl"}`
- Prüfe Batterie: Wenn `batterie <= 10`, sende zusätzlich Warnung in jeder Antwort: `{"warnung": "Batterie kritisch!"}`
- Schließe Verbindung nach jedem Befehl.

Schreibe zusätzlich ein Test-Client-Programm **`robot_client_test.py`**:

- Sende eine Sequenz von Befehlen:
  1. `{"befehl": "STATUS"}`
  2. `{"befehl": "BEWEGE", "x": 100, "y": 50, "z": 30}`
  3. `{"befehl": "GREIFE"}`
  4. `{"befehl": "STATUS"}`
- Gib jeweils die Antworten aus.

**Hinweise**:
- Verwende Funktionen für Befehlsverarbeitung, um den Code übersichtlich zu halten.
- Achte darauf, dass Batterie nicht unter 0 fällt.
- **Testprogramm verfügbar**: `testprogramme/P4_robot_client_TEST.py` führt 7 Tests durch: STATUS, BEWEGE, GREIFE, OEFFNE, Batterie-Warnung und unbekannte Befehle.

---

### Aufgabe P5: Verschlüsselte Maschinen-Kommunikation (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 45-60 Minuten  
**Vorkenntnisse**: `socket`, `json`, `hashlib` (für HMAC-Simulation), Funktionen, Error Handling  
**Maschinenbau-Kontext**: In sicherheitskritischen Produktionsumgebungen (z.B. Pharma, Aerospace) müssen Maschinenbefehle authentifiziert werden, um Sabotage oder unberechtigte Zugriffe zu verhindern. Diese Aufgabe simuliert eine einfache Authentifizierung mit einem gemeinsamen Geheimnis (Pre-Shared Key).

**Hintergrund**: Echte Verschlüsselung mit AES oder RSA würde externe Bibliotheken (z.B. `cryptography`) erfordern, die in dieser Vorlesung noch nicht behandelt wurden. Stattdessen simulieren wir Authentifizierung mit einem **HMAC-ähnlichen Verfahren**: Der Client sendet eine Nachricht zusammen mit einem Hash, der aus der Nachricht und einem gemeinsamen Geheimnis berechnet wird. Der Server prüft den Hash, um die Authentizität zu verifizieren.

Schreibe ein Server-Programm **`secure_machine_server.py`**:

- Erstelle einen TCP-Server auf `localhost` Port `8000`.
- Definiere ein gemeinsames Geheimnis (Pre-Shared Key): `SECRET_KEY = "GEHEIM_CNC_2024"` (beide Programme müssen diesen kennen).
- Empfange JSON-Daten im Format:
  ```json
  {
    "befehl": "START_PRODUKTION",
    "maschine_id": "CNC-05",
    "auftrag_id": "A12345",
    "hash": "..."
  }
  ```
- Berechne den erwarteten Hash:
  - Erstelle einen String: `f"{befehl}|{maschine_id}|{auftrag_id}|{SECRET_KEY}"`
  - Berechne SHA-256 Hash: `hashlib.sha256(string.encode()).hexdigest()`
- Vergleiche den empfangenen Hash mit dem berechneten Hash:
  - **Stimmen überein**: Authentisch, führe Befehl aus. Antwort: `{"status": "OK", "meldung": "Befehl authentifiziert und ausgeführt"}`
  - **Stimmen nicht überein**: Nicht authentisch, lehne ab. Antwort: `{"status": "FEHLER", "meldung": "Authentifizierung fehlgeschlagen!"}`
- Implementiere Befehle:
  - **"START_PRODUKTION"**: Gib aus "Produktion gestartet für Auftrag {auftrag_id}"
  - **"STOPP_PRODUKTION"**: Gib aus "Produktion gestoppt"
  - **"NOTAUS"**: Gib aus "⚠️ NOTAUS aktiviert!"
- Endlos-Schleife für mehrere Clients.

Schreibe zusätzlich ein Client-Programm **`secure_machine_client.py`**:

- Verbinde dich mit `localhost` Port `8000`.
- Definiere das gleiche Geheimnis: `SECRET_KEY = "GEHEIM_CNC_2024"`.
- Funktion `send_command(befehl, maschine_id, auftrag_id=None)`:
  - Erstelle String: `f"{befehl}|{maschine_id}|{auftrag_id or ''}|{SECRET_KEY}"`
  - Berechne Hash: `hashlib.sha256(string.encode()).hexdigest()`
  - Erstelle JSON: `{"befehl": befehl, "maschine_id": maschine_id, "auftrag_id": auftrag_id, "hash": hash_value}`
  - Sende JSON, empfange Antwort, gib sie aus.
- Sende mehrere Befehle:
  1. `"START_PRODUKTION"`, Maschine "CNC-05", Auftrag "A12345"
  2. `"STOPP_PRODUKTION"`, Maschine "CNC-05"

**Bonus**: Teste, was passiert, wenn ein Angreifer den Hash manipuliert (sende falsche Hash-Werte).

**Beispiel Ein-/Ausgabe**:

```
# Server-Ausgabe:
Secure Machine Server läuft auf Port 8000...

[Neue Verbindung] ('127.0.0.1', 54324)
Empfangen: START_PRODUKTION für CNC-05, Auftrag A12345
Hash-Verifizierung: ✅ Authentisch
Produktion gestartet für Auftrag A12345
Gesendet: {"status": "OK", "meldung": "Befehl authentifiziert und ausgeführt"}

[Neue Verbindung] ('127.0.0.1', 54325)
Empfangen: START_PRODUKTION für CNC-05, Auftrag A12345
Hash-Verifizierung: ❌ Fehlgeschlagen (manipulierter Hash)
Befehl abgelehnt!
Gesendet: {"status": "FEHLER", "meldung": "Authentifizierung fehlgeschlagen!"}

# Client-Ausgabe:
Verbunden mit Secure Machine Server
Sende: START_PRODUKTION für CNC-05, Auftrag A12345
Antwort: {"status": "OK", "meldung": "Befehl authentifiziert und ausgeführt"}
...
```

**Hinweise**:
- `import hashlib` für SHA-256-Hashing.
- Hash-Berechnung: `hashlib.sha256(string.encode()).hexdigest()`.
- Achte darauf, dass Client und Server denselben String für Hashing verwenden (gleiche Reihenfolge der Felder!).
- **Testprogramm verfügbar**: `testprogramme/P5_secure_client_TEST.py` führt 6 Tests durch, inkl. Authentifizierung und Angriffssimulation mit manipuliertem Hash.

---