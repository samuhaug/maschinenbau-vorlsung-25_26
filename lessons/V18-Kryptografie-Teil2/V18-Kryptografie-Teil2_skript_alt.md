# V18: Kryptografie – Teil 2

> [!NOTE]
> **Lernziele dieser Vorlesung**:
> - Hash-Funktionen verstehen und deren Eigenschaften kennen (Kollisionsresistenz, Einwegfunktion, Avalanche-Effekt)
> - Unterschiede zwischen kryptografischen Hash-Funktionen (SHA-256, SHA-3) und nicht-kryptografischen (MD5) verstehen
> - Public-Key-Infrastruktur (PKI) und Zertifikate als Vertrauensanker kennenlernen
> - Digitale Signaturen zur Authentifizierung und Integrität anwenden können
> - TLS/SSL-Protokoll für sichere Webkommunikation verstehen
> - Passwort-Hashing mit Salting für sichere Passwortspeicherung implementieren
> - HTTP-Requests mit der `requests`-Bibliothek durchführen
> - GET- und POST-Requests für API-Kommunikation einsetzen
> - JSON-Daten von REST-APIs abrufen und verarbeiten
> - HTTP-Status-Codes interpretieren und Error Handling implementieren

---

## Teil 1: Theorie - Kryptografie Teil 2

### Überblick

In der vorherigen Vorlesung (V17) haben wir die Grundlagen der Kryptografie kennengelernt: symmetrische Verschlüsselung (AES), asymmetrische Verschlüsselung (RSA) und die Hybrid-Verschlüsselung als Kombination beider Verfahren. Diese Konzepte ermöglichen es uns, Daten vertraulich zu übertragen, sodass nur der beabsichtigte Empfänger sie lesen kann.

Heute erweitern wir unser Wissen um weitere essenzielle kryptografische Bausteine, die in modernen Sicherheitssystemen unverzichtbar sind. Während Verschlüsselung die **Vertraulichkeit** (Confidentiality) gewährleistet, konzentrieren wir uns heute auf **Integrität** (Integrity) und **Authentizität** (Authenticity). Diese beiden Eigenschaften sind genauso wichtig wie Vertraulichkeit, um ein vollständiges Sicherheitssystem aufzubauen.

**Hash-Funktionen** dienen als fundamentales Werkzeug zur Integritätsprüfung und bilden die Basis für viele weitere kryptografische Mechanismen. **Digitale Signaturen** kombinieren Hash-Funktionen mit asymmetrischer Kryptografie, um Authentizität und Integrität gleichzeitig zu garantieren. Die **Public-Key-Infrastruktur (PKI)** schafft ein Vertrauensnetzwerk, das die Echtheit von öffentlichen Schlüsseln bestätigt. Schließlich sehen wir mit **TLS/SSL**, wie all diese Komponenten in der Praxis zusammenwirken, um sichere Webkommunikation zu ermöglichen.

Im Maschinenbau sind diese Konzepte hochrelevant: Digitale Signaturen schützen Firmware-Updates von Industrierobotern vor Manipulation, Hash-Funktionen gewährleisten die Integrität von CAD-Dateien und Fertigungsdaten, und TLS/SSL sichert die Kommunikation zwischen Maschinen und Steuerungssystemen in vernetzten Produktionsanlagen (Industrie 4.0).

### Hash-Funktionen und deren Eigenschaften

Eine **Hash-Funktion** ist eine mathematische Funktion, die eine Eingabe beliebiger Länge (z.B. eine Datei, ein Passwort, eine Nachricht) auf eine Ausgabe fester Länge abbildet. Diese Ausgabe wird **Hash-Wert**, **Digest** oder **Fingerprint** genannt. Hash-Funktionen sind deterministische Einwegfunktionen: Die gleiche Eingabe erzeugt immer denselben Hash-Wert, aber aus dem Hash-Wert kann die ursprüngliche Eingabe nicht rekonstruiert werden.

> [!NOTE]
> **Hash-Funktion**: Eine mathematische Funktion $H: \{0,1\}^* \to \{0,1\}^n$, die eine beliebig lange Eingabe auf eine feste Ausgabelänge $n$ abbildet. Die Ausgabe wird Hash-Wert, Digest oder Fingerprint genannt.

**Zentrale Eigenschaften kryptografischer Hash-Funktionen:**

1. **Deterministisch**: Die gleiche Eingabe erzeugt immer denselben Hash-Wert. Dies ist fundamental für Integritätsprüfungen – wenn sich eine Datei auch nur minimal ändert, muss der Hash-Wert unterschiedlich sein.

2. **Schnelle Berechnung**: Der Hash-Wert kann effizient berechnet werden, auch für große Datenmengen (Gigabyte-Dateien in wenigen Sekunden).

3. **Einwegfunktion (Preimage Resistance)**: Aus einem gegebenen Hash-Wert $h$ ist es praktisch unmöglich, die ursprüngliche Eingabe $m$ zu finden, sodass $H(m) = h$. Mit "praktisch unmöglich" meinen wir, dass es mit heutigen Computern und in absehbarer Zeit nicht machbar ist (z.B. würde es Milliarden Jahre dauern).

4. **Kollisionsresistenz (Collision Resistance)**: Es ist praktisch unmöglich, zwei unterschiedliche Eingaben $m_1 \neq m_2$ zu finden, die denselben Hash-Wert erzeugen: $H(m_1) = H(m_2)$. Dies ist die stärkste Eigenschaft und kritisch für digitale Signaturen. Selbst wenn ein Angreifer gezielt nach Kollisionen sucht, sollte er keine finden können.

5. **Second-Preimage Resistance (Weak Collision Resistance)**: Für eine gegebene Eingabe $m_1$ ist es praktisch unmöglich, eine andere Eingabe $m_2 \neq m_1$ zu finden, sodass $H(m_1) = H(m_2)$. Diese Eigenschaft ist schwächer als Kollisionsresistenz, aber dennoch wichtig.

6. **Avalanche-Effekt (Lawineneffekt)**: Eine minimale Änderung der Eingabe (z.B. ein einzelnes Bit) führt zu einer vollständig unterschiedlichen Ausgabe. Etwa 50% der Bits im Hash-Wert sollten sich ändern. Dies macht es unmöglich, aus ähnlichen Hash-Werten auf ähnliche Eingaben zu schließen.

> [!TIP]
> **Avalanche-Effekt Beispiel** (vereinfacht):
> ```
> Eingabe:  "Hallo"     → Hash: 3a42f8... (256 Bit)
> Eingabe:  "Hallo!"    → Hash: 9f7c1e... (256 Bit)
> 
> Nur ein Zeichen Unterschied, aber komplett verschiedener Hash!
> ```

**Anwendungen von Hash-Funktionen:**

- **Integritätsprüfung**: Prüfen, ob Daten während der Übertragung oder Speicherung verändert wurden. CAD-Dateien, Firmware-Updates, NC-Programme – der Hash-Wert dient als digitaler Fingerabdruck.
- **Digitale Signaturen**: Statt die gesamte Nachricht zu signieren, wird nur der Hash-Wert signiert (viel effizienter bei großen Dateien).
- **Passwort-Speicherung**: Passwörter werden nicht im Klartext gespeichert, sondern als Hash-Wert (mit Salting, siehe unten).
- **Proof-of-Work** (Blockchain): Mining-Algorithmen suchen gezielt nach Eingaben, die einen Hash-Wert mit bestimmten Eigenschaften erzeugen (z.B. mit vielen führenden Nullen).
- **Datendeduplication**: Identische Dateien haben identische Hash-Werte und können erkannt werden, um Speicherplatz zu sparen.

### SHA-256, SHA-3 und die MD5-Problematik

Es gibt zahlreiche Hash-Funktionen, die sich in ihrer Sicherheit, Geschwindigkeit und Ausgabelänge unterscheiden. In der Praxis sind vor allem die **SHA-Familie** (Secure Hash Algorithm) und **MD5** (Message Digest 5) relevant, wobei MD5 heute als unsicher gilt.

**SHA-256 (Secure Hash Algorithm 256-Bit)**

SHA-256 ist Teil der **SHA-2-Familie**, die vom US-amerikanischen National Institute of Standards and Technology (NIST) im Jahr 2001 veröffentlicht wurde. SHA-2 umfasst mehrere Varianten mit unterschiedlichen Ausgabelängen: SHA-224, SHA-256, SHA-384 und SHA-512. SHA-256 ist heute der de-facto Standard für kryptografische Hash-Funktionen und wird in TLS/SSL, Bitcoin, digitalen Signaturen und unzähligen Sicherheitsprotokollen eingesetzt.

> [!NOTE]
> **SHA-256**: Kryptografische Hash-Funktion mit 256-Bit Ausgabelänge (32 Byte oder 64 Hexadezimal-Zeichen). Gilt als sicher gegen Kollisionsangriffe mit heutiger Technologie. Berechnung dauert etwa $2^{128}$ Operationen für eine Kollision (praktisch unmöglich).

**Eigenschaften von SHA-256:**
- **Ausgabelänge**: 256 Bit (32 Byte, 64 Hexadezimal-Zeichen)
- **Blockgröße**: 512 Bit (Eingabe wird in 512-Bit-Blöcke zerlegt)
- **Rundenzahl**: 64 Runden (mehrfache Transformation der Daten)
- **Sicherheit**: Gilt als sicher, keine praktischen Kollisionen bekannt
- **Performance**: Relativ schnell, optimiert für moderne CPUs

**SHA-3 (Keccak)**

SHA-3 wurde 2015 vom NIST als Alternative zu SHA-2 standardisiert, nachdem ein offener Wettbewerb stattgefunden hatte. Die Gewinner-Funktion **Keccak** basiert auf einer völlig anderen mathematischen Struktur als SHA-2 (Sponge-Konstruktion statt Merkle-Damgård). SHA-3 wurde nicht entwickelt, weil SHA-2 unsicher ist, sondern als Backup-Option für den Fall, dass in Zukunft Schwachstellen in SHA-2 entdeckt werden.

**Eigenschaften von SHA-3:**
- **Ausgabelänge**: Variabel (SHA3-224, SHA3-256, SHA3-384, SHA3-512)
- **Struktur**: Sponge-Konstruktion (fundamental anders als SHA-2)
- **Sicherheit**: Ebenfalls als sicher eingestuft
- **Performance**: Etwas langsamer als SHA-2 in Software, aber effizienter in Hardware

**Wann SHA-2, wann SHA-3?**
- **SHA-256 (SHA-2)**: Standard-Wahl für die meisten Anwendungen, breite Unterstützung, gut erforscht.
- **SHA-3**: Alternative bei speziellen Anforderungen, z.B. wenn Hardware-Implementierung wichtig ist oder als Diversifikation (nicht alle Eier in einen Korb).

**MD5 (Message Digest 5) – Eine Warnung**

MD5 wurde 1992 von Ronald Rivest entwickelt und war lange Zeit weit verbreitet. MD5 erzeugt einen 128-Bit Hash-Wert (16 Byte, 32 Hexadezimal-Zeichen). Allerdings wurden ab 2004 schwerwiegende Kollisionsangriffe demonstriert: Angreifer können zwei unterschiedliche Dateien erzeugen, die denselben MD5-Hash haben. Diese Kollisionen sind **praktisch durchführbar** – es dauert nur wenige Stunden auf einem modernen Computer.

> [!WARNING]
> **MD5 ist kryptografisch gebrochen!** Verwende MD5 niemals für sicherheitskritische Anwendungen wie digitale Signaturen, Zertifikate oder Passwort-Hashing. Kollisionsangriffe sind seit 2004 bekannt und praktisch durchführbar. Angreifer können zwei Dateien mit identischem MD5-Hash erstellen, was z.B. für Malware-Signaturen oder manipulierte Firmware fatal ist.

**Beispiel eines MD5-Kollisionsangriffs:**
Im Jahr 2008 wurde demonstriert, dass man zwei unterschiedliche SSL-Zertifikate mit identischem MD5-Hash erstellen kann. Ein Angreifer konnte so ein gefälschtes Zertifikat erzeugen, das von Webbrowsern als vertrauenswürdig akzeptiert wurde. Dies führte dazu, dass MD5 komplett aus TLS/SSL entfernt wurde.

**Wann kann MD5 noch verwendet werden?**
- **Nicht-kryptografische Zwecke**: Checksummen für Dateiintegrität ohne Sicherheitsanforderungen (z.B. Prüfen, ob eine Datei korrekt heruntergeladen wurde, wenn man dem Server vertraut).
- **Hash-Tabellen**: In Datenstrukturen, wo keine Sicherheit erforderlich ist (z.B. als schnelle Hash-Funktion für Dictionaries).

**Faustregel**: Wenn es um Sicherheit geht, verwende **SHA-256 oder besser**. MD5 ist nur für nicht-sicherheitsrelevante Anwendungen akzeptabel.

### Zusammenfassung Theorie (Zwischenstand)

Bisher haben wir die fundamentalen Konzepte kryptografischer Hash-Funktionen kennengelernt:

- **Hash-Funktionen** bilden beliebige Eingaben auf feste Ausgabelängen ab und sind **Einwegfunktionen** mit **Kollisionsresistenz**.
- **SHA-256** ist der aktuelle Standard für kryptografische Hash-Funktionen und gilt als sicher.
- **SHA-3** ist eine moderne Alternative mit anderer mathematischer Struktur.
- **MD5** ist kryptografisch gebrochen und sollte nur für nicht-sicherheitsrelevante Zwecke verwendet werden.

Im nächsten Abschnitt sehen wir, wie Hash-Funktionen als Bausteine für Public-Key-Infrastrukturen, digitale Signaturen und sichere Webkommunikation dienen.

### Public-Key-Infrastruktur (PKI) und Zertifikate

In der vorherigen Vorlesung haben wir asymmetrische Verschlüsselung (RSA) kennengelernt: Jeder Teilnehmer besitzt ein Schlüsselpaar aus öffentlichem Schlüssel (Public Key) und privatem Schlüssel (Private Key). Der öffentliche Schlüssel wird verteilt, damit andere Personen verschlüsselte Nachrichten senden können. Doch wie kann Bob sicher sein, dass der öffentliche Schlüssel, den er für Alice verwendet, wirklich zu Alice gehört und nicht von einem Angreifer manipuliert wurde?

Dieses Problem wird als **Public-Key-Distribution-Problem** oder **Key-Distribution-Problem** bezeichnet. Ohne eine vertrauenswürdige Instanz könnte ein Angreifer einen gefälschten öffentlichen Schlüssel verbreiten und sich als Alice ausgeben (Man-in-the-Middle-Angriff).

**Die Lösung: Public-Key-Infrastruktur (PKI)**

Eine **Public-Key-Infrastruktur (PKI)** ist ein System aus Richtlinien, Verfahren und Technologien, das die Erstellung, Verwaltung, Verteilung, Nutzung, Speicherung und Widerruf von digitalen Zertifikaten ermöglicht. PKI schafft ein **Vertrauensnetzwerk** (Web of Trust), in dem Zertifizierungsstellen (Certificate Authorities, CAs) die Echtheit von öffentlichen Schlüsseln bestätigen.

> [!NOTE]
> **Public-Key-Infrastruktur (PKI)**: Ein System aus Zertifizierungsstellen (CAs), Registrierungsstellen (RAs), Zertifikaten und Richtlinien, das die sichere Verteilung und Verwaltung öffentlicher Schlüssel ermöglicht. PKI bildet die Vertrauensbasis für TLS/SSL, Code-Signing und digitale Signaturen.

**Zentrale Komponenten einer PKI:**

1. **Certificate Authority (CA)**: Eine vertrauenswürdige Organisation, die digitale Zertifikate ausstellt. Die CA überprüft die Identität des Antragstellers (z.B. eines Webseitenbetreibers) und signiert dessen öffentlichen Schlüssel mit ihrem eigenen privaten Schlüssel. Bekannte CAs sind z.B. DigiCert, Let's Encrypt, Sectigo.

2. **Registration Authority (RA)**: Eine optionale Zwischeninstanz, die Identitätsprüfungen durchführt und Zertifikatsanträge validiert, bevor sie an die CA weitergeleitet werden. Dies entlastet die CA.

3. **Digitales Zertifikat (X.509)**: Ein elektronisches Dokument, das einen öffentlichen Schlüssel mit einer Identität (z.B. Domain-Name, Organisation, Person) verknüpft und von einer CA digital signiert ist. Das Zertifikat enthält u.a.:
   - **Subject** (Zertifikatsinhaber): Domain-Name (z.B. `www.example.com`), Organisation
   - **Public Key**: Der öffentliche Schlüssel des Inhabers
   - **Issuer** (Aussteller): Die CA, die das Zertifikat signiert hat
   - **Validity Period** (Gültigkeitsdauer): Von-Bis-Datum (z.B. 1 Jahr)
   - **Serial Number** (Seriennummer): Eindeutige Kennung des Zertifikats
   - **Signature**: Digitale Signatur der CA über alle oben genannten Daten

4. **Certificate Revocation List (CRL)**: Eine Liste von widerrufenen Zertifikaten, die nicht mehr als vertrauenswürdig gelten (z.B. weil der private Schlüssel kompromittiert wurde). Browser und Anwendungen prüfen CRLs, bevor sie ein Zertifikat akzeptieren.

5. **Online Certificate Status Protocol (OCSP)**: Ein Protokoll zur Echtzeitprüfung des Widerrufstatus eines Zertifikats (Alternative zu CRLs, schneller und effizienter).

**Wie funktioniert die Zertifikatskette (Certificate Chain)?**

Zertifikate sind hierarchisch organisiert. Eine CA signiert nicht nur End-Zertifikate (z.B. für Webseiten), sondern auch Zertifikate für Intermediate CAs, die wiederum weitere Zertifikate signieren können. An der Spitze stehen **Root-CAs**, deren Zertifikate in Betriebssystemen und Webbrowsern fest eingebaut sind (z.B. im Windows Certificate Store oder im Firefox Certificate Store).

```
Root CA (selbstsigniert, im Browser vorinstalliert)
  ├── Intermediate CA 1
  │     └── End-Entity Zertifikat (www.example.com)
  └── Intermediate CA 2
        └── End-Entity Zertifikat (www.another.com)
```

Wenn du eine HTTPS-Webseite besuchst, sendet der Server sein Zertifikat und die gesamte Zertifikatskette bis zur Root-CA. Der Browser prüft:
1. Ist die Signatur jedes Zertifikats gültig?
2. Vertraut der Browser der Root-CA (ist sie im Browser-Store)?
3. Ist das Zertifikat noch gültig (nicht abgelaufen)?
4. Ist das Zertifikat nicht widerrufen (CRL/OCSP-Prüfung)?
5. Stimmt der Domain-Name im Zertifikat mit der aufgerufenen URL überein?

Nur wenn alle Prüfungen erfolgreich sind, wird die HTTPS-Verbindung als vertrauenswürdig akzeptiert.

> [!TIP]
> **Zertifikatsanzeige im Browser**: In modernen Webbrowsern kannst du das Zertifikat einer HTTPS-Webseite anzeigen, indem du auf das Schloss-Symbol in der Adressleiste klickst und dann auf "Zertifikat" oder "Verbindung sicher". Hier siehst du die gesamte Zertifikatskette, Gültigkeitsdauer, Aussteller und weitere Details.

**PKI im Maschinenbau:**
- **Firmware-Updates**: Industrieroboter und CNC-Maschinen erhalten signierte Firmware-Updates. Das Zertifikat des Herstellers garantiert, dass die Firmware authentisch und unverändert ist.
- **Sichere Maschinen-Kommunikation**: In Industrie 4.0-Umgebungen kommunizieren Maschinen über OPC UA (OPC Unified Architecture), das auf PKI basiert. Jede Maschine hat ein Zertifikat, das ihre Identität beweist.
- **Code-Signing**: Software für Produktionssteuerung und SPS-Programme werden digital signiert, um Manipulation zu verhindern.

### Digitale Signaturen zur Authentifizierung

Eine **digitale Signatur** ist das digitale Äquivalent einer handschriftlichen Unterschrift. Sie dient dazu, die **Authentizität** (Wer hat das Dokument erstellt?) und **Integrität** (Wurde das Dokument verändert?) eines digitalen Dokuments oder einer Nachricht zu gewährleisten. Digitale Signaturen basieren auf asymmetrischer Kryptografie und Hash-Funktionen.

> [!NOTE]
> **Digitale Signatur**: Ein kryptografisches Verfahren, das die Authentizität und Integrität einer Nachricht gewährleistet. Der Sender hasht die Nachricht und verschlüsselt den Hash-Wert mit seinem privaten Schlüssel. Der Empfänger kann die Signatur mit dem öffentlichen Schlüssel des Senders verifizieren.

**Wie funktioniert eine digitale Signatur?**

**1. Signatur erstellen (durch Sender Alice):**

1. Alice berechnet den **Hash-Wert** der Nachricht $m$: $h = H(m)$ (z.B. SHA-256).
2. Alice verschlüsselt den Hash-Wert mit ihrem **privaten Schlüssel**: $s = \text{Encrypt}_{\text{PrivateKey}_{\text{Alice}}}(h)$. Dies ist die digitale Signatur.
3. Alice sendet die Nachricht $m$ und die Signatur $s$ an Bob.

**2. Signatur verifizieren (durch Empfänger Bob):**

1. Bob empfängt die Nachricht $m$ und die Signatur $s$.
2. Bob berechnet den Hash-Wert der empfangenen Nachricht: $h' = H(m)$.
3. Bob entschlüsselt die Signatur mit dem **öffentlichen Schlüssel von Alice**: $h'' = \text{Decrypt}_{\text{PublicKey}_{\text{Alice}}}(s)$.
4. Bob vergleicht $h'$ mit $h''$:
   - **Wenn $h' = h''$**: Die Signatur ist gültig → Die Nachricht wurde von Alice signiert und ist unverändert.
   - **Wenn $h' \neq h''$**: Die Signatur ist ungültig → Die Nachricht wurde entweder nicht von Alice signiert oder wurde manipuliert.

> [!TIP]
> **Warum wird nicht die gesamte Nachricht signiert?** Aus Performance-Gründen. RSA-Verschlüsselung ist sehr langsam für große Datenmengen. Ein Hash-Wert ist immer nur 256 Bit (32 Byte) groß, egal ob die Originalnachricht 1 KB oder 1 GB groß ist. Die Signatur des Hash-Werts ist daher viel effizienter.

**Eigenschaften digitaler Signaturen:**

1. **Authentizität**: Die Signatur beweist, dass die Nachricht vom angegebenen Sender stammt. Nur der Sender besitzt den privaten Schlüssel, der zum Signieren verwendet wurde.

2. **Integrität**: Jede Änderung an der Nachricht (auch nur ein Bit) führt zu einem anderen Hash-Wert. Die Signatur wird dann ungültig.

3. **Non-Repudiation (Nicht-Abstreitbarkeit)**: Der Sender kann später nicht bestreiten, die Nachricht signiert zu haben, da nur er den privaten Schlüssel besitzt. Dies ist wichtig für rechtliche Verbindlichkeit (z.B. bei elektronischen Verträgen).

4. **Öffentliche Verifizierbarkeit**: Jeder, der den öffentlichen Schlüssel des Senders kennt, kann die Signatur überprüfen. Es ist kein geteiltes Geheimnis notwendig (im Gegensatz zu MACs, siehe V17).

**Digitale Signaturen vs. MACs (Message Authentication Codes):**

In V17 haben wir MACs kennengelernt (z.B. HMAC), die ebenfalls Authentizität und Integrität bieten. Der Unterschied:

| Eigenschaft | Digitale Signatur (RSA, ECDSA) | MAC (HMAC) |
|-------------|-------------------------------|------------|
| Schlüssel | Asymmetrisch (Public/Private Key) | Symmetrisch (Shared Secret) |
| Non-Repudiation | ✅ Ja (Sender kann nicht abstreiten) | ❌ Nein (beide Parteien haben denselben Schlüssel) |
| Öffentliche Verifizierung | ✅ Ja (jeder mit Public Key kann prüfen) | ❌ Nein (nur Parteien mit Shared Secret) |
| Performance | 🐌 Langsam (RSA-Operationen) | ⚡ Schnell (nur Hashing) |
| Anwendung | Zertifikate, Code-Signing, E-Mails | Netzwerkprotokolle (z.B. TLS, IPsec) |

**Praktische Anwendungen digitaler Signaturen:**

- **Software-Verteilung**: Software-Hersteller signieren ihre Programme. Betriebssysteme prüfen die Signatur vor der Installation (z.B. Windows SmartScreen, macOS Gatekeeper).
- **PDF-Signaturen**: Elektronische Dokumente und Verträge werden digital signiert (z.B. mit Adobe Sign, DocuSign).
- **E-Mail-Signaturen**: S/MIME und PGP/GPG ermöglichen signierte E-Mails.
- **Firmware-Updates**: Industriesteuerungen und IoT-Geräte akzeptieren nur signierte Firmware-Updates vom Hersteller.
- **Blockchain**: Transaktionen in Bitcoin und anderen Kryptowährungen werden digital signiert (mit ECDSA statt RSA, da effizienter).

**Digitale Signaturen im Maschinenbau:**
- **CAD-Dateien**: Konstruktionszeichnungen werden signiert, um Manipulation zu verhindern und Urheberschaft zu beweisen.
- **NC-Programme**: CNC-Programme werden vom Programmierer signiert, bevor sie an die Maschine übertragen werden.
- **Wartungsprotokolle**: Techniker signieren digitale Wartungsprotokolle, um Nachvollziehbarkeit zu gewährleisten.
- **Fertigungsfreigaben**: Qualitätsbeauftragte signieren Fertigungsfreigaben digital, um Compliance nachzuweisen.

### TLS/SSL: Sichere Webkommunikation in der Praxis

**Transport Layer Security (TLS)** ist das wichtigste Sicherheitsprotokoll im Internet und der Nachfolger von **Secure Sockets Layer (SSL)**. TLS sichert die Kommunikation zwischen Client (z.B. Webbrowser) und Server (z.B. Webserver) und gewährleistet **Vertraulichkeit**, **Integrität** und **Authentizität**. Jedes Mal, wenn du eine HTTPS-Webseite besuchst, nutzt du TLS.

> [!NOTE]
> **TLS (Transport Layer Security)**: Ein kryptografisches Protokoll, das sichere Kommunikation über Netzwerke ermöglicht. TLS kombiniert asymmetrische Verschlüsselung (für Schlüsselaustausch), symmetrische Verschlüsselung (für Datenübertragung), digitale Signaturen (für Authentifizierung) und Hash-Funktionen (für Integrität).

**Geschichte und Versionen:**
- **SSL 1.0**: Nie veröffentlicht (zu viele Sicherheitslücken)
- **SSL 2.0** (1995): Erste öffentliche Version, heute als unsicher eingestuft
- **SSL 3.0** (1996): Verbesserte Version, aber ebenfalls unsicher (POODLE-Angriff 2014)
- **TLS 1.0** (1999): Nachfolger von SSL 3.0, leichte Verbesserungen
- **TLS 1.1** (2006): Schutz gegen CBC-Angriffe
- **TLS 1.2** (2008): Wichtige Sicherheitsverbesserungen, heute noch weit verbreitet
- **TLS 1.3** (2018): Aktueller Standard, deutlich schneller und sicherer als TLS 1.2

Heute sind **nur TLS 1.2 und TLS 1.3** als sicher anerkannt. Ältere Versionen (SSL 2.0, SSL 3.0, TLS 1.0, TLS 1.1) sollten deaktiviert werden.

**Der TLS-Handshake: Wie funktioniert der Verbindungsaufbau?**

Der TLS-Handshake ist der Prozess, bei dem Client und Server einen sicheren Kanal aufbauen. Er besteht aus mehreren Schritten:

**1. Client Hello:**
Der Client sendet eine Nachricht an den Server mit:
- **TLS-Version**: Welche TLS-Versionen der Client unterstützt (z.B. TLS 1.2, TLS 1.3)
- **Cipher Suites**: Welche Verschlüsselungsalgorithmen der Client unterstützt (z.B. AES-256-GCM, ChaCha20-Poly1305)
- **Zufallszahl (Client Random)**: Eine zufällig generierte Zahl für den Schlüsselaustausch
- **Server Name Indication (SNI)**: Domain-Name, den der Client aufrufen möchte (wichtig für Server, die mehrere Domains hosten)

**2. Server Hello:**
Der Server antwortet mit:
- **TLS-Version**: Die höchste TLS-Version, die sowohl Client als auch Server unterstützen
- **Cipher Suite**: Die ausgewählte Verschlüsselungskombination aus der Client-Liste
- **Zufallszahl (Server Random)**: Eine weitere Zufallszahl für den Schlüsselaustausch
- **Server-Zertifikat**: Das X.509-Zertifikat des Servers (mit öffentlichem Schlüssel und CA-Signatur)
- **Optional: Zertifikatsanforderung**: Der Server kann ein Client-Zertifikat anfordern (für gegenseitige Authentifizierung, z.B. in Industrie 4.0)

**3. Zertifikatsprüfung (Client):**
Der Client prüft das Server-Zertifikat:
- Ist die CA-Signatur gültig?
- Ist die CA vertrauenswürdig (im Browser-Store)?
- Ist das Zertifikat noch gültig (nicht abgelaufen)?
- Stimmt der Domain-Name im Zertifikat mit der URL überein?
- Ist das Zertifikat nicht widerrufen (CRL/OCSP)?

Wenn alle Prüfungen erfolgreich sind, fährt der Client fort.

**4. Schlüsselaustausch:**
Client und Server einigen sich auf einen gemeinsamen **Session Key** (symmetrischer Schlüssel für die Datenübertragung). Dies geschieht entweder mit:
- **RSA Key Exchange** (TLS 1.2 und älter): Client generiert Pre-Master-Secret, verschlüsselt es mit Public Key des Servers, sendet es. Beide berechnen daraus den Session Key.
- **Diffie-Hellman (DH/ECDH)** (TLS 1.2 und TLS 1.3): Client und Server tauschen öffentliche DH-Parameter aus und berechnen gemeinsam den Session Key, ohne ihn zu übertragen. Dies bietet **Forward Secrecy** (siehe unten).

**5. Finished Messages:**
Beide Seiten senden eine verschlüsselte "Finished"-Nachricht mit einem HMAC über alle bisherigen Handshake-Nachrichten. Dies beweist, dass der Handshake vollständig und unverändert empfangen wurde.

**6. Verschlüsselte Datenübertragung:**
Ab jetzt werden alle Daten mit dem Session Key symmetrisch verschlüsselt (z.B. mit AES-256-GCM). Der Session Key wird nur für diese Verbindung verwendet und nach Verbindungsende verworfen.

```mermaid
sequenceDiagram
    participant Client
    participant Server
    
    Client->>Server: 1. Client Hello (TLS-Version, Cipher Suites, Random)
    Server->>Client: 2. Server Hello (TLS-Version, Cipher Suite, Random, Zertifikat)
    Client->>Client: 3. Zertifikatsprüfung (CA-Signatur, Gültigkeit, Domain)
    Client->>Server: 4. Key Exchange (z.B. ECDH Public Key)
    Server->>Client: Key Exchange (ECDH Public Key)
    Note over Client,Server: Beide berechnen Session Key aus ECDH
    Client->>Server: 5. Finished (verschlüsselt mit Session Key)
    Server->>Client: Finished (verschlüsselt mit Session Key)
    Note over Client,Server: 6. Verschlüsselte Datenübertragung (AES-GCM)
```

**Forward Secrecy (Perfect Forward Secrecy, PFS):**

Ein wichtiges Konzept in TLS 1.2+ ist **Forward Secrecy**. Dies bedeutet, dass auch wenn der private Schlüssel des Servers in Zukunft kompromittiert wird, vergangene Verbindungen nicht nachträglich entschlüsselt werden können. Forward Secrecy wird durch **Ephemeral Diffie-Hellman (DHE/ECDHE)** erreicht: Für jede Verbindung wird ein neues, temporäres Schlüsselpaar generiert, das nach der Verbindung verworfen wird.

**Ohne Forward Secrecy (RSA Key Exchange):**
- Ein Angreifer zeichnet verschlüsselte Verbindungen auf.
- Jahre später wird der private Schlüssel des Servers gestohlen.
- Der Angreifer kann alle aufgezeichneten Verbindungen entschlüsseln (da der Session Key mit dem Server-Public-Key verschlüsselt wurde).

**Mit Forward Secrecy (ECDHE):**
- Jede Verbindung nutzt temporäre Schlüssel, die nach der Verbindung gelöscht werden.
- Selbst mit dem Server-Private-Key kann ein Angreifer alte Verbindungen nicht entschlüsseln.

> [!WARNING]
> **TLS 1.0, TLS 1.1 und SSL sind unsicher!** Diese Versionen sind anfällig für Angriffe wie POODLE, BEAST und andere. Moderne Webserver und Browser sollten nur TLS 1.2 und TLS 1.3 unterstützen. TLS 1.3 ist deutlich schneller (weniger Roundtrips beim Handshake) und sicherer (keine unsicheren Cipher Suites mehr).

**TLS im Maschinenbau:**
- **HTTPS für Maschinen-Dashboards**: Web-Interfaces von CNC-Maschinen, Robotern und Industriesteuerungen sollten über HTTPS erreichbar sein.
- **OPC UA über TLS**: Der Industriestandard OPC UA nutzt TLS für sichere Maschinen-zu-Maschinen-Kommunikation.
- **REST-APIs**: Wenn Maschinen Daten über REST-APIs austauschen, sollte dies über HTTPS erfolgen.
- **MQTT over TLS**: IoT-Protokolle wie MQTT können über TLS gesichert werden (MQTTS).

### Passwort-Hashing und Salting

Die sichere Speicherung von Passwörtern ist eine der wichtigsten Sicherheitsaufgaben in der Softwareentwicklung. Passwörter dürfen **niemals im Klartext** gespeichert werden, da ein Datenbankdiebstahl sofort alle Benutzerkonten kompromittieren würde. Stattdessen werden Passwörter als **Hash-Werte** gespeichert. Allerdings reicht einfaches Hashing nicht aus – es muss mit **Salting** und speziellen **Password Hashing Functions** kombiniert werden.

> [!NOTE]
> **Passwort-Hashing**: Der Prozess, ein Passwort mit einer Hash-Funktion in einen nicht umkehrbaren Hash-Wert zu transformieren. Bei der Anmeldung wird das eingegebene Passwort erneut gehasht und mit dem gespeicherten Hash-Wert verglichen. Ein Match bedeutet korrektes Passwort.

**Warum reicht SHA-256 nicht aus?**

Man könnte meinen, dass SHA-256 ausreicht, um Passwörter zu hashen. Allerdings gibt es mehrere Probleme:

1. **Rainbow Tables**: Angreifer können riesige Datenbanken (Rainbow Tables) mit vorberechneten Hash-Werten häufiger Passwörter erstellen. Beispiel: SHA-256("password123") ist immer derselbe Wert. Wenn ein Angreifer eine Datenbank mit Millionen vorberechneter Hashes hat, kann er sofort sehen, welches Passwort zu einem Hash gehört.

2. **Geschwindigkeit**: SHA-256 ist bewusst schnell designt. Ein moderner Computer kann Milliarden SHA-256-Hashes pro Sekunde berechnen. Bei einem Brute-Force-Angriff (alle möglichen Passwörter durchprobieren) ist dies ein Vorteil für den Angreifer.

3. **Gleiche Passwörter = gleiche Hashes**: Wenn zwei Benutzer dasselbe Passwort haben, haben sie auch denselben Hash-Wert. Ein Angreifer kann sofort sehen, welche Benutzer identische Passwörter haben.

**Die Lösung: Salting**

**Salting** löst das Problem der Rainbow Tables und identischer Hashes. Ein **Salt** ist eine zufällige Zeichenkette, die vor dem Hashing an das Passwort angehängt wird. Jeder Benutzer erhält einen individuellen Salt.

**Prozess mit Salt:**

**1. Registrierung (Passwort speichern):**
- Benutzer gibt Passwort ein: `"MeinPasswort123"`
- System generiert zufälligen Salt: `"x8Kd92pQ"` (z.B. 16 Byte zufällige Daten)
- System kombiniert Passwort und Salt: `"MeinPasswort123x8Kd92pQ"`
- System hasht die Kombination: `hash = SHA-256("MeinPasswort123x8Kd92pQ")`
- System speichert **Salt und Hash** in der Datenbank: `("x8Kd92pQ", "a5f3c2...")`

**2. Anmeldung (Passwort prüfen):**
- Benutzer gibt Passwort ein: `"MeinPasswort123"`
- System liest Salt aus Datenbank: `"x8Kd92pQ"`
- System kombiniert eingegebenes Passwort mit Salt: `"MeinPasswort123x8Kd92pQ"`
- System hasht die Kombination: `hash' = SHA-256("MeinPasswort123x8Kd92pQ")`
- System vergleicht `hash'` mit gespeichertem Hash: Wenn gleich → Anmeldung erfolgreich

**Vorteile von Salting:**

1. **Rainbow Tables nutzlos**: Da jeder Benutzer einen individuellen Salt hat, müsste ein Angreifer für jeden Salt eine eigene Rainbow Table erstellen – praktisch unmöglich.

2. **Gleiche Passwörter ≠ gleiche Hashes**: Zwei Benutzer mit Passwort `"password123"` haben unterschiedliche Salts und damit unterschiedliche Hashes. Ein Angreifer kann nicht erkennen, dass sie dasselbe Passwort haben.

3. **Kein zusätzlicher Aufwand**: Der Salt muss nicht geheim gehalten werden und kann zusammen mit dem Hash in der Datenbank gespeichert werden.

> [!TIP]
> **Salt-Länge**: Salts sollten mindestens 128 Bit (16 Byte) lang sein. Für jeden Benutzer sollte ein neuer, zufälliger Salt generiert werden (z.B. mit `os.urandom(16)` in Python).

**Password Hashing Functions: Langsam ist gut!**

Während SHA-256 zu schnell ist, gibt es spezielle **Password Hashing Functions**, die bewusst langsam designt sind. Die bekanntesten sind:

1. **bcrypt**: Basiert auf Blowfish-Verschlüsselung, konfigurierbare Rechenzeit (Work Factor), weit verbreitet.
2. **scrypt**: Benötigt nicht nur viel Rechenzeit, sondern auch viel Speicher (Memory-Hard Function), erschwert Hardware-Angriffe.
3. **Argon2**: Gewinner des Password Hashing Competition 2015, gilt als aktueller Standard. Kombiniert Rechenzeit und Speicher-Anforderungen.

Diese Funktionen sind so designt, dass sie **viel Zeit** benötigen (z.B. 100 Millisekunden pro Hash). Das ist für einen legitimen Login-Vorgang vernachlässigbar, aber für einen Angreifer, der Milliarden Passwörter testen will, fatal: Statt 10 Milliarden Hashes pro Sekunde können nur noch 10 Hashes pro Sekunde berechnet werden.

> [!WARNING]
> **Niemals eigene Passwort-Hashing-Algorithmen entwickeln!** Nutze immer etablierte Bibliotheken wie bcrypt, scrypt oder Argon2. Selbst kleine Fehler können die Sicherheit komplett zunichtemachen. In Python: Verwende `bcrypt` oder `argon2-cffi` Bibliotheken.

**Beispiel-Vergleich:**

| Methode | Geschwindigkeit | Sicherheit | Empfohlen? |
|---------|----------------|------------|------------|
| SHA-256 (ohne Salt) | ⚡⚡⚡ Sehr schnell | ❌ Unsicher (Rainbow Tables) | ❌ Nein |
| SHA-256 (mit Salt) | ⚡⚡⚡ Sehr schnell | ⚠️ Besser, aber zu schnell | ⚠️ Nur wenn keine Alternative |
| bcrypt | 🐌 Langsam | ✅ Sicher | ✅ Ja |
| scrypt | 🐌🐌 Sehr langsam | ✅✅ Sehr sicher | ✅ Ja |
| Argon2 | 🐌🐌 Sehr langsam | ✅✅✅ Aktueller Standard | ✅✅ Ja (bevorzugt) |

**Passwort-Hashing im Maschinenbau:**
- **Zugriffskontrolle für Maschinen**: Bediener-Passwörter für CNC-Maschinen und Roboter sollten gehasht gespeichert werden.
- **Web-Interfaces**: Maschinen-Dashboards mit Login sollten Passwörter mit bcrypt/Argon2 speichern.
- **Wartungszugang**: Techniker-Accounts für Fernwartung sollten mit starkem Passwort-Hashing geschützt sein.

### Zusammenfassung Theorie

Wir haben die wichtigsten kryptografischen Konzepte für Integrität und Authentizität kennengelernt:

- **Hash-Funktionen** (SHA-256, SHA-3) sind Einwegfunktionen mit Kollisionsresistenz und Avalanche-Effekt. Sie dienen zur Integritätsprüfung und als Bausteine für digitale Signaturen.
- **MD5 ist kryptografisch gebrochen** und sollte nur für nicht-sicherheitsrelevante Zwecke verwendet werden. Verwende stattdessen SHA-256 oder besser.
- **Public-Key-Infrastruktur (PKI)** schafft ein Vertrauensnetzwerk mit Certificate Authorities (CAs), die digitale Zertifikate ausstellen. Zertifikatsketten verbinden End-Zertifikate mit Root-CAs.
- **Digitale Signaturen** kombinieren Hash-Funktionen mit asymmetrischer Verschlüsselung, um Authentizität, Integrität und Non-Repudiation zu gewährleisten. Sie sind essenziell für Code-Signing, E-Mails und Firmware-Updates.
- **TLS/SSL** sichert die Webkommunikation durch eine Kombination aus asymmetrischer Verschlüsselung (Handshake), symmetrischer Verschlüsselung (Datenübertragung), digitalen Signaturen (Zertifikate) und Hash-Funktionen (Integrität). TLS 1.2+ bietet Forward Secrecy.
- **Passwort-Hashing mit Salting** schützt Passwörter gegen Rainbow Tables. Verwende spezielle Password Hashing Functions wie **bcrypt**, **scrypt** oder **Argon2** statt schneller Hash-Funktionen wie SHA-256.

Diese Konzepte bilden die Grundlage für sichere Systeme in Webentwicklung, Netzwerkkommunikation und industriellen Anwendungen.

---

## Teil 2: Python-Praxis - Netzwerk-Programmierung (HTTP-Requests) – Teil 2

> [!WARNING]
> **Python-Konsistenz beachten**: Prüfe [../../python_topics.md](../../python_topics.md) für bereits eingeführte Konzepte! In V17 haben wir Socket-Programmierung mit TCP/IP kennengelernt. Heute bauen wir darauf auf und arbeiten auf höherer Abstraktionsebene mit HTTP und REST-APIs.

### Überblick

In der vorherigen Vorlesung (V17) haben wir Low-Level-Netzwerkprogrammierung mit Sockets kennengelernt. Wir haben TCP-Server und -Clients implementiert, Daten über Sockets gesendet und empfangen, und sogar einfache Authentifizierung mit HMAC-ähnlichen Mechanismen umgesetzt. Diese Socket-Programmierung ist fundamental für das Verständnis von Netzwerkkommunikation, aber in der Praxis arbeiten wir häufig auf einer höheren Abstraktionsebene.

Heute konzentrieren wir uns auf **HTTP (Hypertext Transfer Protocol)** – das Protokoll, das das World Wide Web antreibt. HTTP ist ein Anwendungsprotokoll auf Layer 7 des OSI-Modells (siehe V15) und läuft über TCP. Während Socket-Programmierung uns volle Kontrolle gibt, ermöglicht HTTP eine standardisierte Kommunikation zwischen Clients und Servern mit festgelegten Methoden, Status-Codes und Datenformaten.

Die Python-Bibliothek **`requests`** abstrahiert die Komplexität von HTTP und macht es einfach, Daten von Webservern und REST-APIs abzurufen. REST-APIs (Representational State Transfer APIs) sind der Standard für moderne Web-Services und werden in industriellen Anwendungen häufig eingesetzt – von Cloud-Diensten über Maschinen-Dashboards bis hin zu IoT-Plattformen.

**Warum ist HTTP im Maschinenbau relevant?**

- **REST-APIs für Maschinen-Daten**: Moderne CNC-Maschinen, Roboter und Industriesteuerungen bieten oft REST-APIs, um Statusdaten abzurufen, Parameter zu setzen oder Befehle zu senden.
- **Cloud-Integration**: Sensordaten werden an Cloud-Plattformen (z.B. AWS IoT, Azure IoT Hub, Siemens MindSphere) über HTTP-APIs gesendet.
- **Datenbanken und Dashboards**: Produktionsdaten werden über HTTP-APIs aus Datenbanken abgerufen und in Dashboards visualisiert.
- **Externe Dienste**: Wetterdaten, Material-Datenbanken, CAD-Bibliotheken – viele externe Dienste bieten HTTP-APIs.

### HTTP-Protokoll verstehen

**HTTP (Hypertext Transfer Protocol)** ist ein zustandsloses (stateless) Request-Response-Protokoll. Der Client (z.B. Webbrowser, Python-Skript) sendet eine **HTTP-Request**, der Server antwortet mit einer **HTTP-Response**. HTTP ist textbasiert, was bedeutet, dass Requests und Responses als menschenlesbare Textnachrichten formatiert sind (im Gegensatz zu binären Protokollen).

> [!NOTE]
> **HTTP (Hypertext Transfer Protocol)**: Ein Anwendungsprotokoll für verteilte Informationssysteme. HTTP ist zustandslos (jede Request ist unabhängig) und basiert auf dem Request-Response-Modell. HTTP läuft standardmäßig über TCP Port 80, HTTPS über Port 443 (HTTP über TLS).

**Struktur einer HTTP-Request:**

Eine HTTP-Request besteht aus drei Teilen:

1. **Request-Line**: Methode, URI (Uniform Resource Identifier) und HTTP-Version
   ```
   GET /api/sensors/temperature HTTP/1.1
   ```
   - `GET`: HTTP-Methode (siehe unten)
   - `/api/sensors/temperature`: Pfad zur Ressource
   - `HTTP/1.1`: HTTP-Version

2. **Header**: Metadaten über die Request (Key-Value-Paare)
   ```
   Host: api.example.com
   User-Agent: Python-requests/2.31.0
   Accept: application/json
   Authorization: Bearer abc123token
   ```
   - `Host`: Server-Domain (erforderlich in HTTP/1.1)
   - `User-Agent`: Identifiziert den Client
   - `Accept`: Gewünschtes Antwortformat
   - `Authorization`: Authentifizierungs-Token

3. **Body** (optional): Daten, die an den Server gesendet werden (z.B. bei POST)
   ```json
   {
     "sensor_id": "temp_01",
     "value": 75.3,
     "unit": "celsius"
   }
   ```

**Struktur einer HTTP-Response:**

1. **Status-Line**: HTTP-Version, Status-Code und Reason-Phrase
   ```
   HTTP/1.1 200 OK
   ```
   - `HTTP/1.1`: HTTP-Version
   - `200`: Status-Code (siehe unten)
   - `OK`: Reason-Phrase (menschenlesbare Beschreibung)

2. **Header**: Metadaten über die Response
   ```
   Content-Type: application/json
   Content-Length: 142
   Date: Sun, 05 Jan 2026 10:30:00 GMT
   ```

3. **Body**: Die eigentlichen Daten (z.B. JSON, HTML, Bild)
   ```json
   {
     "sensor_id": "temp_01",
     "temperature": 75.3,
     "timestamp": "2026-01-05T10:30:00Z"
   }
   ```

**HTTP-Methoden (Verben):**

HTTP definiert verschiedene Methoden, die angeben, welche Aktion auf einer Ressource ausgeführt werden soll:

| Methode | Bedeutung | Verwendung | Idempotent? | Sicher? |
|---------|-----------|------------|-------------|---------|
| **GET** | Daten abrufen | Lesen von Ressourcen (z.B. Sensordaten abrufen) | ✅ Ja | ✅ Ja |
| **POST** | Daten senden/erstellen | Neue Ressourcen erstellen, Formulare absenden | ❌ Nein | ❌ Nein |
| **PUT** | Ressource aktualisieren/ersetzen | Bestehende Ressource komplett ersetzen | ✅ Ja | ❌ Nein |
| **PATCH** | Ressource teilweise aktualisieren | Nur bestimmte Felder ändern | ❌ Nein | ❌ Nein |
| **DELETE** | Ressource löschen | Ressource entfernen | ✅ Ja | ❌ Nein |
| **HEAD** | Wie GET, aber ohne Body | Header abrufen (z.B. Dateigröße prüfen) | ✅ Ja | ✅ Ja |
| **OPTIONS** | Unterstützte Methoden abfragen | Server-Fähigkeiten prüfen | ✅ Ja | ✅ Ja |

> [!NOTE]
> **Idempotent**: Eine Operation ist idempotent, wenn mehrfaches Ausführen dasselbe Ergebnis liefert wie einmaliges Ausführen. Beispiel: `GET /api/sensor/temp_01` liefert immer denselben Wert (zum Zeitpunkt der Anfrage). `POST /api/sensors` erstellt bei jedem Aufruf eine neue Ressource.

> [!NOTE]
> **Sicher (Safe)**: Eine Methode ist sicher, wenn sie den Server-Zustand nicht verändert. `GET` und `HEAD` sind sicher (nur lesend), `POST`, `PUT`, `DELETE` sind nicht sicher (ändern Daten).

**HTTP-Status-Codes:**

Status-Codes geben das Ergebnis einer Request an. Sie sind in fünf Kategorien unterteilt:

**1xx - Informational (Informativ):**
- `100 Continue`: Server hat Request-Header empfangen, Client kann Body senden
- `101 Switching Protocols`: Server wechselt Protokoll (z.B. von HTTP zu WebSocket)

**2xx - Success (Erfolg):**
- `200 OK`: Request erfolgreich, Antwort enthält Daten
- `201 Created`: Ressource erfolgreich erstellt (z.B. nach POST)
- `202 Accepted`: Request akzeptiert, aber noch nicht verarbeitet
- `204 No Content`: Request erfolgreich, aber keine Antwortdaten (z.B. nach DELETE)

**3xx - Redirection (Umleitung):**
- `301 Moved Permanently`: Ressource permanent verschoben, neue URL in `Location`-Header
- `302 Found`: Ressource temporär unter anderer URL
- `304 Not Modified`: Ressource seit letztem Abruf nicht geändert (Caching)

**4xx - Client Error (Client-Fehler):**
- `400 Bad Request`: Ungültige Syntax oder Parameter
- `401 Unauthorized`: Authentifizierung erforderlich (trotz Name: nicht autorisiert)
- `403 Forbidden`: Zugriff verweigert (auch mit Authentifizierung)
- `404 Not Found`: Ressource existiert nicht
- `405 Method Not Allowed`: HTTP-Methode nicht unterstützt (z.B. DELETE auf read-only-Ressource)
- `429 Too Many Requests`: Rate-Limit überschritten

**5xx - Server Error (Server-Fehler):**
- `500 Internal Server Error`: Allgemeiner Server-Fehler
- `502 Bad Gateway`: Gateway/Proxy erhielt ungültige Antwort von Upstream-Server
- `503 Service Unavailable`: Server temporär nicht verfügbar (Wartung, Überlastung)
- `504 Gateway Timeout`: Gateway/Proxy erhielt keine rechtzeitige Antwort

> [!TIP]
> **Eselsbrücke für Status-Codes:**
> - **2xx = Good** (alles gut)
> - **3xx = Go elsewhere** (woanders hingehen)
> - **4xx = You screwed up** (Client-Fehler)
> - **5xx = Server screwed up** (Server-Fehler)

### HTTP-Requests mit der `requests`-Bibliothek

Die `requests`-Bibliothek ist der de-facto Standard für HTTP-Requests in Python. Sie ist nicht Teil der Standardbibliothek, aber weit verbreitet und einfach zu verwenden. Die Bibliothek abstrahiert die Komplexität von HTTP und macht es einfach, GET- und POST-Requests zu senden, JSON zu verarbeiten und Fehler zu behandeln.

**Installation:**
```bash
pip install requests
```

**Import:**
```python
import requests
```

> [!NOTE]
> **`requests`-Bibliothek** (Drittanbieter-Bibliothek): Eine benutzerfreundliche HTTP-Bibliothek für Python. Entwickelt von Kenneth Reitz, erste Version 2011. Die Bibliothek bietet eine einfache API für GET, POST, PUT, DELETE und andere HTTP-Methoden. Sie kümmert sich automatisch um Cookies, Sessions, Timeouts und viele andere Details.

**Einfaches GET-Request-Beispiel:**

```python
import requests

# GET-Request an eine API senden
response = requests.get("https://api.example.com/sensors/temperature")

# Status-Code prüfen
print(f"Status-Code: {response.status_code}")  # z.B. 200

# Antwort als Text
print(f"Antwort (Text): {response.text}")

# Antwort als JSON (wenn Server JSON sendet)
data = response.json()
print(f"Temperatur: {data['temperature']}°C")
```

**Wichtige `Response`-Attribute:**

- **`response.status_code`**: HTTP-Status-Code als Integer (z.B. `200`, `404`)
- **`response.text`**: Antwort-Body als String
- **`response.content`**: Antwort-Body als Bytes (für binäre Daten wie Bilder)
- **`response.json()`**: Antwort als Python-Dictionary (wenn JSON, sonst `JSONDecodeError`)
- **`response.headers`**: Response-Header als Dictionary-ähnliches Objekt
- **`response.url`**: Finale URL (nach Redirects)
- **`response.ok`**: Boolean, `True` wenn Status-Code < 400 (200-399)
- **`response.raise_for_status()`**: Wirft Exception bei 4xx/5xx Status-Codes

> [!TIP]
> **GET-Request mit Query-Parametern**:
> ```python
> # Parameter als Dictionary übergeben
> params = {"sensor_id": "temp_01", "unit": "celsius"}
> response = requests.get("https://api.example.com/sensors", params=params)
> # Erzeugt URL: https://api.example.com/sensors?sensor_id=temp_01&unit=celsius
> ```

### GET-Requests: Daten von APIs abrufen

GET-Requests sind die häufigste HTTP-Methode und dienen zum Abrufen von Daten. Sie sollten niemals Server-Zustand verändern (idempotent und sicher). Parameter werden in der URL als Query-String übergeben (z.B. `?key1=value1&key2=value2`).

**Vollständiges GET-Request-Beispiel mit Error Handling:**

```python
import requests

def get_sensor_data(sensor_id):
    """
    Ruft Sensordaten von einer REST-API ab.
    
    Args:
        sensor_id: ID des Sensors (z.B. "temp_01")
    
    Returns:
        Dictionary mit Sensordaten oder None bei Fehler
    """
    base_url = "https://api.example.com/api/v1/sensors"
    
    # Query-Parameter
    params = {
        "id": sensor_id,
        "format": "json"
    }
    
    # Header (optional, aber empfohlen)
    headers = {
        "User-Agent": "MaschinenbauApp/1.0",
        "Accept": "application/json"
    }
    
    try:
        # GET-Request mit Timeout
        response = requests.get(base_url, params=params, headers=headers, timeout=5)
        
        # Status-Code prüfen (wirft Exception bei 4xx/5xx)
        response.raise_for_status()
        
        # JSON parsen und zurückgeben
        data = response.json()
        return data
        
    except requests.exceptions.Timeout:
        print(f"Timeout: Server antwortet nicht innerhalb von 5 Sekunden")
        return None
    except requests.exceptions.ConnectionError:
        print(f"Verbindungsfehler: Keine Netzwerkverbindung")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP-Fehler: {e.response.status_code} - {e.response.text}")
        return None
    except requests.exceptions.JSONDecodeError:
        print(f"JSON-Fehler: Antwort ist kein gültiges JSON")
        return None
    except Exception as e:
        print(f"Unerwarteter Fehler: {e}")
        return None

# Verwendung
sensor_data = get_sensor_data("temp_01")
if sensor_data:
    print(f"Temperatur: {sensor_data['temperature']}°C")
    print(f"Zeitstempel: {sensor_data['timestamp']}")
```

**Header in GET-Requests:**

Header liefern zusätzliche Informationen über die Request. Häufige Header:

- **`User-Agent`**: Identifiziert die Anwendung (manche APIs blockieren Requests ohne User-Agent)
- **`Accept`**: Gewünschtes Response-Format (z.B. `application/json`, `text/html`)
- **`Authorization`**: Authentifizierungs-Token (z.B. `Bearer abc123token`, `Basic dXNlcjpwYXNz`)
- **`Accept-Language`**: Bevorzugte Sprache (z.B. `de-DE`, `en-US`)

```python
headers = {
    "User-Agent": "CNC-Monitor/2.0",
    "Accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
response = requests.get(url, headers=headers)
```

**Timeout-Parameter:**

Immer einen Timeout setzen! Ohne Timeout kann eine Request unendlich lange warten, wenn der Server nicht antwortet. Dies führt zu hängenden Programmen.

```python
# Timeout in Sekunden (Connection Timeout + Read Timeout)
response = requests.get(url, timeout=5)

# Separate Timeouts für Connection und Read
response = requests.get(url, timeout=(3, 10))  # 3s Connect, 10s Read
```

> [!WARNING]
> **Immer Timeout setzen!** Ohne Timeout kann dein Programm unendlich lange warten, wenn ein Server nicht antwortet oder die Netzwerkverbindung unterbrochen ist. Dies ist besonders kritisch in produktiven Systemen (z.B. Maschinen-Monitoring).

### POST-Requests: Daten an Server senden

POST-Requests senden Daten an den Server, typischerweise um neue Ressourcen zu erstellen oder Formulare abzusenden. Daten werden im Request-Body übertragen, nicht in der URL. POST-Requests sind weder idempotent noch sicher.

**POST-Request mit JSON-Daten:**

```python
import requests

def send_measurement(sensor_id, value, unit):
    """
    Sendet Messwerte an eine REST-API.
    
    Args:
        sensor_id: ID des Sensors
        value: Messwert (float)
        unit: Einheit (z.B. "celsius", "bar")
    
    Returns:
        True bei Erfolg, False bei Fehler
    """
    url = "https://api.example.com/api/v1/measurements"
    
    # Daten als Dictionary (wird automatisch zu JSON konvertiert)
    data = {
        "sensor_id": sensor_id,
        "value": value,
        "unit": unit,
        "timestamp": "2026-01-05T10:30:00Z"
    }
    
    # Header für JSON-Content
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer your_api_token_here"
    }
    
    try:
        # POST-Request mit json-Parameter (automatische Serialisierung)
        response = requests.post(url, json=data, headers=headers, timeout=5)
        
        # Status-Code prüfen
        response.raise_for_status()
        
        # Erfolg
        print(f"Messwert erfolgreich gesendet: {response.status_code}")
        print(f"Server-Antwort: {response.json()}")
        return True
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 400:
            print(f"Ungültige Daten: {e.response.json()}")
        elif e.response.status_code == 401:
            print(f"Nicht autorisiert: Prüfe API-Token")
        elif e.response.status_code == 429:
            print(f"Rate-Limit überschritten: Zu viele Requests")
        else:
            print(f"HTTP-Fehler: {e.response.status_code}")
        return False
    except Exception as e:
        print(f"Fehler beim Senden: {e}")
        return False

# Verwendung
success = send_measurement("temp_01", 75.3, "celsius")
```

**POST vs. json-Parameter vs. data-Parameter:**

Die `requests`-Bibliothek bietet mehrere Möglichkeiten, Daten zu senden:

1. **`json=` Parameter**: Konvertiert Python-Dictionary automatisch zu JSON und setzt `Content-Type: application/json`
   ```python
   data = {"key": "value"}
   response = requests.post(url, json=data)  # Automatisch JSON
   ```

2. **`data=` Parameter**: Sendet Daten als Form-Daten (`application/x-www-form-urlencoded`)
   ```python
   data = {"key": "value"}
   response = requests.post(url, data=data)  # Form-Daten
   # Sendet: key=value
   ```

3. **`data=` mit JSON-String**: Manuelle JSON-Serialisierung
   ```python
   import json
   data = {"key": "value"}
   response = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
   ```

**Faustregel**: Für moderne REST-APIs verwende **`json=`**. Für HTML-Formulare verwende **`data=`**.

> [!TIP]
> **POST-Request mit Datei-Upload**:
> ```python
> # Datei hochladen
> files = {"file": open("messdaten.csv", "rb")}
> response = requests.post(url, files=files)
> ```

### JSON-Daten von REST-APIs abrufen und verarbeiten

REST-APIs geben Daten typischerweise im JSON-Format zurück. JSON (JavaScript Object Notation) ist ein leichtgewichtiges Datenformat, das von Python direkt als Dictionary/Liste interpretiert werden kann.

**Typische JSON-Response-Strukturen:**

**1. Einzelnes Objekt:**
```json
{
  "sensor_id": "temp_01",
  "temperature": 75.3,
  "unit": "celsius",
  "timestamp": "2026-01-05T10:30:00Z",
  "status": "ok"
}
```

**Python-Verarbeitung:**
```python
response = requests.get(url)
data = response.json()  # Dictionary
print(f"Temperatur: {data['temperature']}°C")
print(f"Status: {data['status']}")
```

**2. Liste von Objekten:**
```json
{
  "sensors": [
    {"id": "temp_01", "value": 75.3, "unit": "celsius"},
    {"id": "press_01", "value": 5.2, "unit": "bar"},
    {"id": "rpm_01", "value": 1500, "unit": "rpm"}
  ],
  "total": 3,
  "timestamp": "2026-01-05T10:30:00Z"
}
```

**Python-Verarbeitung:**
```python
response = requests.get(url)
data = response.json()

# Über Liste iterieren
for sensor in data['sensors']:
    print(f"{sensor['id']}: {sensor['value']} {sensor['unit']}")

# Filtern mit List Comprehension
high_temp = [s for s in data['sensors'] if s['unit'] == 'celsius' and s['value'] > 70]
```

**3. Paginierte Daten (große Datensätze):**

Viele APIs liefern große Datensätze in Seiten (Pagination):

```json
{
  "data": [...],
  "page": 1,
  "per_page": 100,
  "total_pages": 5,
  "total_items": 487,
  "next": "https://api.example.com/data?page=2"
}
```

**Python-Verarbeitung mit Loop:**
```python
def fetch_all_pages(base_url):
    """Ruft alle Seiten einer paginierten API ab."""
    all_data = []
    page = 1
    
    while True:
        response = requests.get(base_url, params={"page": page}, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        all_data.extend(data['data'])
        
        # Letzte Seite erreicht?
        if page >= data['total_pages']:
            break
        
        page += 1
    
    return all_data

# Alle Messdaten abrufen
measurements = fetch_all_pages("https://api.example.com/measurements")
print(f"Insgesamt {len(measurements)} Messwerte abgerufen")
```

**Fehlerbehandlung bei JSON-Parsing:**

Nicht jede Response ist gültiges JSON. Server-Fehler liefern manchmal HTML-Fehlerseiten statt JSON.

```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()  # Kann JSONDecodeError werfen
except requests.exceptions.JSONDecodeError:
    print(f"Antwort ist kein gültiges JSON: {response.text[:200]}")
except requests.exceptions.HTTPError as e:
    print(f"HTTP-Fehler {e.response.status_code}")
    # Bei 4xx/5xx könnte Body trotzdem JSON mit Fehlermeldung sein
    try:
        error_data = e.response.json()
        print(f"API-Fehlermeldung: {error_data.get('message', 'Unbekannt')}")
    except:
        print(f"Server-Antwort: {e.response.text[:200]}")
```

> [!TIP]
> **Nested JSON-Strukturen navigieren**:
> ```python
> # Verschachtelte Daten sicher abrufen
> data = response.json()
> temperature = data.get('sensors', {}).get('temperature', {}).get('value', None)
> 
> # Oder mit Exception Handling
> try:
>     temperature = data['sensors']['temperature']['value']
> except (KeyError, TypeError):
>     temperature = None
> ```

### Häufige Fehler und Lösungen

> [!WARNING]
> **Fehler 1: Kein Timeout gesetzt**
> 
> **Problem**: `response = requests.get(url)` ohne Timeout kann unendlich lange warten.
> 
> **Lösung**: Immer Timeout setzen:
> ```python
> response = requests.get(url, timeout=5)  # 5 Sekunden
> ```

> [!WARNING]
> **Fehler 2: Status-Code nicht geprüft**
> 
> **Problem**: Auch bei 404 oder 500 wirft `requests.get()` keine Exception. Die Response existiert, aber die Daten sind ungültig.
> 
> **Lösung**: Status-Code prüfen mit `.raise_for_status()`:
> ```python
> response = requests.get(url)
> response.raise_for_status()  # Wirft HTTPError bei 4xx/5xx
> ```

> [!WARNING]
> **Fehler 3: JSONDecodeError nicht abgefangen**
> 
> **Problem**: `.json()` wirft Exception, wenn Response kein gültiges JSON ist (z.B. HTML-Fehlerseite).
> 
> **Lösung**: Exception Handling:
> ```python
> try:
>     data = response.json()
> except requests.exceptions.JSONDecodeError:
>     print(f"Keine JSON-Antwort: {response.text[:200]}")
> ```

> [!WARNING]
> **Fehler 4: API-Keys im Code hardcoden**
> 
> **Problem**: `Authorization: "Bearer abc123secret"` direkt im Code ist ein Sicherheitsrisiko (landet in Git-Repository).
> 
> **Lösung**: Umgebungsvariablen verwenden:
> ```python
> import os
> api_key = os.environ.get("API_KEY")
> if not api_key:
>     raise ValueError("API_KEY Umgebungsvariable nicht gesetzt")
> headers = {"Authorization": f"Bearer {api_key}"}
> ```

> [!WARNING]
> **Fehler 5: Sensible Daten in URL-Parametern**
> 
> **Problem**: `requests.get(url, params={"password": "secret"})` → Passwort landet in Logs und Browser-History.
> 
> **Lösung**: Sensible Daten immer im Body (POST) oder Header (Authorization) senden, nicht in URL.

> [!WARNING]
> **Fehler 6: Zertifikatsprüfung deaktiviert**
> 
> **Problem**: `requests.get(url, verify=False)` deaktiviert TLS-Zertifikatsprüfung → Man-in-the-Middle-Angriffe möglich.
> 
> **Lösung**: Nur in Entwicklungsumgebung mit Self-Signed Certificates. In Produktion immer `verify=True` (Standard).

### Zusammenfassung Python

Wir haben die wichtigsten Konzepte der HTTP-Programmierung mit Python kennengelernt:

- **HTTP** ist ein zustandsloses Request-Response-Protokoll mit Methoden (GET, POST, PUT, DELETE) und Status-Codes (2xx Erfolg, 4xx Client-Fehler, 5xx Server-Fehler).
- **Die `requests`-Bibliothek** abstrahiert HTTP-Komplexität und bietet einfache Funktionen für GET- und POST-Requests.
- **GET-Requests** rufen Daten ab und sollten idempotent und sicher sein. Parameter werden als Query-String übergeben.
- **POST-Requests** senden Daten an den Server (typischerweise JSON) und sind weder idempotent noch sicher.
- **JSON-Verarbeitung** mit `.json()` konvertiert Response-Body automatisch zu Python-Dictionary/Liste.
- **Status-Codes** müssen immer geprüft werden mit `.raise_for_status()` oder manueller Prüfung von `.status_code`.
- **Error Handling** ist essenziell: `Timeout`, `ConnectionError`, `HTTPError`, `JSONDecodeError` abfangen.
- **Timeouts** sollten immer gesetzt werden, um hängende Requests zu vermeiden.
- **Header** liefern Metadaten wie `User-Agent`, `Accept`, `Authorization` und `Content-Type`.
- **Sicherheit**: API-Keys nie im Code hardcoden, sondern aus Umgebungsvariablen lesen. TLS-Zertifikate immer verifizieren.

Diese Konzepte ermöglichen die Integration von REST-APIs in Python-Programme – von Wetterdaten über Materialdatenbanken bis hin zu Cloud-Plattformen für Maschinen-Monitoring.

### Neue Python-Funktionen/Methoden in dieser Vorlesung

**`requests`-Bibliothek** (Drittanbieter-Bibliothek, Installation: `pip install requests`):

- **`requests.get(url, params=None, headers=None, timeout=None, verify=True)`**  
  Sendet HTTP-GET-Request. Gibt `Response`-Objekt zurück.  
  Signatur: `requests.get(url, **kwargs)` → `Response`

- **`requests.post(url, data=None, json=None, headers=None, timeout=None, verify=True)`**  
  Sendet HTTP-POST-Request mit Daten im Body. Gibt `Response`-Objekt zurück.  
  Signatur: `requests.post(url, **kwargs)` → `Response`

- **`requests.put(url, data=None, json=None, headers=None, timeout=None)`**  
  Sendet HTTP-PUT-Request (Ressource ersetzen).  
  Signatur: `requests.put(url, **kwargs)` → `Response`

- **`requests.patch(url, data=None, json=None, headers=None, timeout=None)`**  
  Sendet HTTP-PATCH-Request (Ressource teilweise aktualisieren).  
  Signatur: `requests.patch(url, **kwargs)` → `Response`

- **`requests.delete(url, headers=None, timeout=None)`**  
  Sendet HTTP-DELETE-Request (Ressource löschen).  
  Signatur: `requests.delete(url, **kwargs)` → `Response`

- **`requests.head(url, headers=None, timeout=None)`**  
  Sendet HTTP-HEAD-Request (nur Header abrufen, kein Body).  
  Signatur: `requests.head(url, **kwargs)` → `Response`

**`Response`-Objekt-Attribute und -Methoden**:

- **`response.status_code`** (Attribut)  
  HTTP-Status-Code als Integer (z.B. 200, 404, 500).  
  Typ: `int`

- **`response.text`** (Attribut)  
  Response-Body als String (automatische Dekodierung mit erkanntem Encoding).  
  Typ: `str`

- **`response.content`** (Attribut)  
  Response-Body als Bytes (für binäre Daten wie Bilder, PDFs).  
  Typ: `bytes`

- **`response.json()`** (Methode)  
  Parst Response-Body als JSON und gibt Python-Dictionary/Liste zurück. Wirft `JSONDecodeError` bei ungültigem JSON.  
  Signatur: `response.json()` → `dict | list`

- **`response.headers`** (Attribut)  
  Response-Header als Dictionary-ähnliches Objekt (case-insensitive).  
  Typ: `CaseInsensitiveDict`

- **`response.url`** (Attribut)  
  Finale URL nach Redirects.  
  Typ: `str`

- **`response.ok`** (Attribut)  
  Boolean, `True` wenn Status-Code 200-399, sonst `False`.  
  Typ: `bool`

- **`response.raise_for_status()`** (Methode)  
  Wirft `HTTPError`-Exception bei Status-Codes 4xx oder 5xx. Keine Aktion bei 2xx/3xx.  
  Signatur: `response.raise_for_status()` → `None`

- **`response.elapsed`** (Attribut)  
  Dauer der Request als `timedelta`-Objekt.  
  Typ: `datetime.timedelta`

- **`response.encoding`** (Attribut)  
  Zeichenkodierung der Response (z.B. `"utf-8"`). Kann gesetzt werden, um Dekodierung zu beeinflussen.  
  Typ: `str`

**`requests.exceptions`-Modul** (Exception-Typen):

- **`requests.exceptions.Timeout`**  
  Exception bei Timeout (Connection- oder Read-Timeout überschritten).

- **`requests.exceptions.ConnectionError`**  
  Exception bei Verbindungsfehlern (z.B. keine Netzwerkverbindung, DNS-Fehler).

- **`requests.exceptions.HTTPError`**  
  Exception bei 4xx/5xx Status-Codes (nur wenn `.raise_for_status()` aufgerufen wurde).

- **`requests.exceptions.TooManyRedirects`**  
  Exception bei zu vielen Redirects (Standard-Limit: 30).

- **`requests.exceptions.RequestException`**  
  Basis-Exception für alle `requests`-Fehler (kann als Catch-All verwendet werden).

- **`requests.exceptions.JSONDecodeError`**  
  Exception bei ungültigem JSON in `.json()` (erbt von `json.JSONDecodeError`).

**Weitere nützliche Funktionen**:

- **`os.environ.get(key, default=None)`** (Standard Library, `os`-Modul)  
  Liest Umgebungsvariable. Gibt `default` zurück, wenn Variable nicht existiert.  
  Signatur: `os.environ.get(key, default=None)` → `str | None`

---

## Weiterführende Ressourcen

### Theorie
- **RFC 2818 (HTTPS)**: [https://datatracker.ietf.org/doc/html/rfc2818](https://datatracker.ietf.org/doc/html/rfc2818) – HTTPS-Spezifikation
- **RFC 5280 (X.509 Certificates)**: [https://datatracker.ietf.org/doc/html/rfc5280](https://datatracker.ietf.org/doc/html/rfc5280) – Zertifikatsformat
- **RFC 8446 (TLS 1.3)**: [https://datatracker.ietf.org/doc/html/rfc8446](https://datatracker.ietf.org/doc/html/rfc8446) – Aktueller TLS-Standard
- **OWASP Top 10**: [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/) – Häufigste Sicherheitslücken
- **Hash Function Security Summary (NIST)**: [https://csrc.nist.gov/projects/hash-functions](https://csrc.nist.gov/projects/hash-functions)

### Python
- **`requests` Dokumentation**: [https://requests.readthedocs.io/](https://requests.readthedocs.io/)
- **`bcrypt` Python Library**: [https://github.com/pyca/bcrypt/](https://github.com/pyca/bcrypt/) – Passwort-Hashing
- **`argon2-cffi`**: [https://argon2-cffi.readthedocs.io/](https://argon2-cffi.readthedocs.io/) – Moderner Passwort-Hashing-Standard
- **RESTful API Design Best Practices**: [https://restfulapi.net/](https://restfulapi.net/)
- **HTTP Status Codes**: [https://httpstatuses.com/](https://httpstatuses.com/) – Interaktive Übersicht
