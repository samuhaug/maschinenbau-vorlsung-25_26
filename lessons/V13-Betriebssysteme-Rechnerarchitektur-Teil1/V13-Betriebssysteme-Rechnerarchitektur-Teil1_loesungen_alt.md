# V13: Betriebssysteme & Rechnerarchitektur – Teil 1 | Lösungen

**Vorlesung**: Informatik Grundlagen  
**Studiengang**: Bachelor Maschinenbau  
**Semester**: 1. Semester  
**Dozent**: [Name]  
**Datum**: [Datum einfügen]

---

## Teil A: Theorie-Lösungen

### Lösung T1: Von-Neumann-Architektur (Leicht)

#### Teilaufgabe a) Zentrale Komponenten

Die **Von-Neumann-Architektur** besteht aus folgenden vier zentralen Komponenten:

**1. Rechenwerk (ALU – Arithmetic Logic Unit)**
Das Rechenwerk führt alle arithmetischen Operationen (Addition, Subtraktion, Multiplikation, Division) und logischen Operationen (AND, OR, NOT, XOR, Vergleiche) durch. Es ist das eigentliche "Rechenzentrum" der CPU und verarbeitet Daten nach den Anweisungen des Steuerwerks. Die ALU arbeitet mit Registern zusammen, um Operanden zu laden und Ergebnisse zu speichern.

**2. Steuerwerk (Control Unit)**
Das Steuerwerk ist die "Kontrollzentrale" der CPU und koordiniert alle Abläufe. Es interpretiert Maschinenbefehle, die aus dem Speicher geladen wurden, und steuert die anderen Komponenten entsprechend. Das Steuerwerk enthält wichtige Register wie den **Instruction Pointer (IP)** bzw. **Program Counter (PC)**, der die Adresse des nächsten auszuführenden Befehls enthält, und das **Instruction Register (IR)**, das den aktuell zu verarbeitenden Befehl speichert.

**3. Speicherwerk (Memory)**
Das Speicherwerk umfasst den gesamten Arbeitsspeicher (RAM) und speichert sowohl Programminstruktionen als auch Daten. In der Von-Neumann-Architektur gibt es keine Trennung zwischen Programm- und Datenspeicher – beide teilen sich denselben physischen Speicher. Dies ermöglicht Flexibilität (Programme können sich selbst modifizieren), birgt aber auch Sicherheitsrisiken und führt zum Von-Neumann-Flaschenhals.

**4. Ein-/Ausgabewerk (I/O-System)**
Das Ein-/Ausgabewerk verbindet den Computer mit der Außenwelt. Es umfasst alle Schnittstellen zu Peripheriegeräten wie Tastatur, Maus, Bildschirm, Festplatten, Netzwerkkarten und USB-Geräten. Die Kommunikation erfolgt über Busse, und moderne Systeme nutzen DMA (Direct Memory Access), damit I/O-Operationen den Prozessor nicht blockieren.

**Gemeinsamer Bus**: Alle vier Komponenten sind über einen **gemeinsamen Bus** miteinander verbunden, der aus drei Teilen besteht:
- **Adressbus**: Überträgt Speicheradressen (von CPU zu Speicher)
- **Datenbus**: Überträgt Daten bidirektional (CPU ↔ Speicher ↔ I/O)
- **Steuerbus**: Überträgt Steuersignale (z.B. Lesen/Schreiben, Takt)

---

#### Teilaufgabe b) Von-Neumann-Flaschenhals

Der **Von-Neumann-Flaschenhals** (engl. *Von-Neumann Bottleneck*) bezeichnet eine fundamentale Leistungsbegrenzung in der klassischen Rechnerarchitektur. Er entsteht durch die folgenden strukturellen Eigenschaften:

**Ursachen**:

1. **Gemeinsamer Speicher für Code und Daten**
   Programme und Daten teilen sich denselben physischen Speicher. Dies bedeutet, dass die CPU nicht gleichzeitig eine Instruktion laden und Daten lesen/schreiben kann – beide Operationen müssen sequenziell über denselben Bus erfolgen.

2. **Sequenzielle Bus-Nutzung**
   Es gibt nur einen Bus zwischen CPU und Speicher. Zu jedem Zeitpunkt kann entweder eine Instruktion geladen ODER ein Datum gelesen/geschrieben werden, aber nicht beides gleichzeitig. Bei jedem Befehl muss die CPU:
   - Schritt 1: Instruktion aus Speicher laden (Bus-Zugriff)
   - Schritt 2: Evtl. Operanden aus Speicher laden (Bus-Zugriff)
   - Schritt 3: Berechnung durchführen (intern, kein Bus)
   - Schritt 4: Evtl. Ergebnis in Speicher schreiben (Bus-Zugriff)
   
   Die Schritte 1, 2 und 4 konkurrieren um dieselbe Bus-Bandbreite.

3. **CPU schneller als Speicher**
   Moderne CPUs sind extrem schnell (mehrere GHz Taktfrequenz), während der Hauptspeicher (RAM) deutlich langsamer ist. Die CPU muss oft viele Taktzyklen warten, bis Daten aus dem Speicher ankommen. Ohne Optimierungen würde die CPU die meiste Zeit im Leerlauf verbringen.

**Auswirkungen**:

- **Geringe Speicherbandbreiten-Ausnutzung**: Selbst wenn die CPU schneller werden könnte, wird sie durch die begrenzte Speicherbandbreite ausgebremst.
- **Wartezyklen (Wait States)**: Die CPU muss auf langsame Speicherzugriffe warten.
- **Skalierungsprobleme**: Eine Verdopplung der CPU-Geschwindigkeit führt nicht zu einer Verdopplung der Gesamtperformance, wenn der Speicherzugriff zum Engpass wird.

**Moderne Lösungsansätze**:

1. **Cache-Hierarchien (L1, L2, L3)**
   Kleine, extrem schnelle Zwischenspeicher zwischen CPU und RAM. Häufig genutzte Daten und Instruktionen werden im Cache gehalten, sodass viele Zugriffe ohne RAM-Zugriff erfolgen können. L1-Caches haben oft getrennte Bereiche für Instruktionen (I-Cache) und Daten (D-Cache), was simultane Zugriffe ermöglicht.

2. **Harvard-Architektur (in Mikrocontrollern)**
   Trennung von Instruktions- und Datenspeicher mit separaten Bussen. Dadurch können gleichzeitig eine Instruktion geladen und Daten verarbeitet werden. Wird oft in Embedded Systems (z.B. ARM Cortex-M) eingesetzt.

3. **Pipelining**
   Während eine Instruktion ausgeführt wird, kann die nächste bereits geladen und dekodiert werden. Dies parallelisiert die Befehlsverarbeitung und verringert die effektive Zeit pro Befehl.

4. **Prefetching**
   Die CPU versucht, Daten und Instruktionen vorherzusagen und diese bereits im Voraus zu laden, bevor sie tatsächlich benötigt werden.

5. **Multiple Cores**
   Mehrere CPU-Kerne können unabhängig arbeiten und den Speicherbus effizienter nutzen, da sie verschiedene Aufgaben parallel bearbeiten.

6. **Breitere Busse**
   Moderne Systeme verwenden 64-Bit- oder 128-Bit-Busse, um mehr Daten pro Taktzyklus zu übertragen.

**Fazit**: Der Von-Neumann-Flaschenhals ist ein fundamentales Problem der klassischen Architektur. Obwohl er nicht vollständig gelöst werden kann, haben moderne Technologien wie Caches und Pipelining seine Auswirkungen erheblich reduziert. Dennoch bleibt die Speicherbandbreite oft der limitierende Faktor bei rechenintensiven Anwendungen.

---

### Lösung T2: CPU & Fetch-Decode-Execute (Mittel)

#### Teilaufgabe a) Komponenten und Funktionen

**1. ALU (Arithmetic Logic Unit) – Rechenwerk**

Die **ALU** ist die zentrale Recheneinheit der CPU und führt alle arithmetischen und logischen Operationen durch.

**Funktionen**:
- **Arithmetische Operationen**: Addition, Subtraktion, Multiplikation, Division, Modulo
- **Logische Operationen**: AND, OR, NOT, XOR, NAND, NOR
- **Vergleichsoperationen**: Gleichheit (==), Ungleichheit (!=), Größer/Kleiner (<, >, ≤, ≥)
- **Bitoperationen**: Bit-Shift (links/rechts), Bit-Rotation, Bit-Maskierung
- **Flags setzen**: Nach jeder Operation setzt die ALU Status-Flags (Zero Flag, Carry Flag, Overflow Flag, Sign Flag), die für Verzweigungen und Fehlererkennung wichtig sind

**Arbeitsweise**: Die ALU erhält zwei Operanden (aus Registern) und einen Opcode (welche Operation durchgeführt werden soll) vom Steuerwerk. Sie führt die Operation durch und schreibt das Ergebnis in ein Zielregister. Die ALU hat keinen eigenen Speicher und arbeitet ausschließlich mit Registern.

**Beispiel**: Bei der Instruktion `ADD R1, R2, R3` (R1 = R2 + R3):
- Steuerwerk lädt Werte aus R2 und R3
- Sendet sie an die ALU mit Opcode "Addition"
- ALU addiert beide Werte
- Ergebnis wird in R1 geschrieben
- Flags werden gesetzt (z.B. Carry-Flag bei Überlauf)

---

**2. Control Unit (Steuerwerk)**

Das **Steuerwerk** ist die "Dirigentin" der CPU und koordiniert alle Abläufe. Es interpretiert Maschinenbefehle und generiert die notwendigen Steuersignale für alle anderen Komponenten.

**Funktionen**:
- **Befehlsdekodierung**: Liest den Opcode aus dem Instruction Register und ermittelt, welche Operation durchzuführen ist
- **Steuersignal-Generierung**: Sendet Signale an ALU, Register, Speicher und Bus, um die Operation auszuführen
- **Ablaufsteuerung**: Koordiniert die zeitliche Abfolge aller Operationen im Takt
- **Verzweigungssteuerung**: Verarbeitet Sprünge (Jumps) und bedingte Verzweigungen basierend auf Flags
- **Interrupt-Handling**: Reagiert auf externe Unterbrechungen (z.B. Timer, I/O)

**Wichtige Register im Steuerwerk**:
- **Program Counter (PC) / Instruction Pointer (IP)**: Enthält die Speicheradresse des nächsten auszuführenden Befehls. Wird nach jedem Fetch-Zyklus automatisch inkrementiert oder bei Sprüngen auf eine neue Adresse gesetzt.
- **Instruction Register (IR)**: Speichert den aktuell geladenen Befehl während der Dekodierung und Ausführung.

**Arbeitsweise**: Das Steuerwerk durchläuft kontinuierlich den Fetch-Decode-Execute-Zyklus:
1. Liest Adresse aus PC
2. Lädt Instruktion von dieser Adresse ins IR
3. Dekodiert die Instruktion
4. Generiert Steuersignale für ALU, Register, Speicher
5. Inkrementiert PC (oder setzt ihn bei Sprüngen)

---

**3. Register**

**Register** sind die schnellsten Speicherelemente in der CPU und dienen als temporäre Datenspeicher für laufende Operationen.

**Funktionen**:
- **Operanden-Speicher**: Halten Eingabewerte für ALU-Operationen
- **Ergebnis-Speicher**: Speichern Zwischenergebnisse von Berechnungen
- **Adress-Speicher**: Speichern Speicheradressen für Load/Store-Operationen
- **Status-Speicher**: Flags-Register speichert CPU-Status (Carry, Zero, Overflow, etc.)

**Typen von Registern**:

| Register-Typ | Funktion | Beispiel |
|--------------|----------|----------|
| **General Purpose Registers (GPR)** | Allgemeine Datenspeicherung | RAX, RBX, RCX, RDX (x86-64) |
| **Special Purpose Registers** | Spezifische Funktionen | SP (Stack Pointer), BP (Base Pointer) |
| **Program Counter (PC)** | Nächste Instruktionsadresse | RIP (x86-64), PC (ARM) |
| **Instruction Register (IR)** | Aktueller Befehl | (intern, nicht direkt zugreifbar) |
| **Flags Register** | Status-Bits | RFLAGS (x86-64) |
| **Segment Registers** | Speichersegmentierung | CS, DS, SS, ES (x86) |

**Eigenschaften**:
- **Zugriffszeit**: 1 Taktzyklus (schnellstes Speicherelement)
- **Größe**: 32-Bit oder 64-Bit pro Register (abhängig von CPU-Architektur)
- **Anzahl**: x86-64 hat 16 General Purpose Registers, ARM kann bis zu 31 haben

**Warum sind Register so wichtig?**
- **Performance**: 100x schneller als L1-Cache, 1000x schneller als RAM
- **Minimale Latenz**: Operationen zwischen Registern erfolgen in einem Taktzyklus
- **Compiler-Optimierung**: Moderne Compiler versuchen, häufig genutzte Variablen in Registern zu halten (Register Allocation)

---

#### Teilaufgabe b) Fetch-Decode-Execute-Zyklus

Der **Fetch-Decode-Execute-Zyklus** (auch **Instruction Cycle** genannt) ist der fundamentale Ablauf, den eine CPU kontinuierlich durchläuft, um Programme auszuführen.

**Gegeben**:
- Speicheradresse `0x1000`: `ADD R1, R2, R3` (Befehl: R1 = R2 + R3)
- Aktueller Zustand: R2 = 10, R3 = 25, PC = `0x1000`

**Schritt-für-Schritt-Ablauf**:

---

**Phase 1: FETCH (Befehl holen)**

1. **PC lesen**: Das Steuerwerk liest den aktuellen Wert des Program Counters (PC = `0x1000`).

2. **Speicherzugriff initiieren**: Das Steuerwerk sendet die Adresse `0x1000` über den Adressbus zum Hauptspeicher.

3. **Steuersignal senden**: Das Steuerwerk sendet ein "READ"-Signal über den Steuerbus, um anzuzeigen, dass Daten aus dem Speicher geladen werden sollen.

4. **Instruktion laden**: Der Speicher antwortet und sendet den Befehl `ADD R1, R2, R3` (in binärer Maschinencode-Form, z.B. `0b00000001 0001 0010 0011`) über den Datenbus zur CPU.

5. **Instruktion ins IR laden**: Der Befehl wird im **Instruction Register (IR)** gespeichert. Dies ist notwendig, damit der Befehl während der Dekodierung und Ausführung verfügbar bleibt, auch wenn der PC bereits auf die nächste Instruktion zeigt.

6. **PC inkrementieren**: Das Steuerwerk erhöht den Program Counter auf die nächste Instruktion: PC = `0x1004` (Annahme: 4 Bytes pro Instruktion).

**Zeitaufwand**: 
- Ohne Cache: ~100 Taktzyklen (RAM-Zugriff)
- Mit L1-Cache-Hit: ~4 Taktzyklen
- Mit L2-Cache-Hit: ~12 Taktzyklen

---

**Phase 2: DECODE (Befehl dekodieren)**

7. **Opcode extrahieren**: Das Steuerwerk analysiert die im IR gespeicherte Instruktion und extrahiert den **Opcode** (Operation Code). In diesem Fall: `ADD` (binär z.B. `0b00000001`).

8. **Operanden identifizieren**: Das Steuerwerk identifiziert die beteiligten Register:
   - Zielregister: R1 (Destination)
   - Quellregister 1: R2 (Source 1)
   - Quellregister 2: R3 (Source 2)

9. **Operation bestimmen**: Das Steuerwerk erkennt, dass eine Addition durchgeführt werden soll.

10. **Steuersignale vorbereiten**: Das Steuerwerk bereitet die notwendigen Steuersignale vor:
    - Signal an Register-File: "Lese R2 und R3"
    - Signal an ALU: "Führe Addition durch"
    - Signal an Register-File: "Schreibe Ergebnis in R1"

**Zeitaufwand**: 1-2 Taktzyklen (interne CPU-Operation)

---

**Phase 3: EXECUTE (Befehl ausführen)**

11. **Operanden laden**: Das Register-File (Register-Speicher) lädt die Werte aus R2 und R3:
    - Wert aus R2: 10
    - Wert aus R3: 25

12. **Werte an ALU senden**: Das Steuerwerk sendet beide Operanden (10 und 25) an die ALU zusammen mit dem Opcode "ADD".

13. **ALU-Berechnung**: Die ALU führt die Addition durch:
    - 10 + 25 = 35

14. **Flags setzen**: Die ALU aktualisiert die Status-Flags im Flags-Register:
    - **Zero Flag (ZF)**: 0 (Ergebnis ist nicht null)
    - **Carry Flag (CF)**: 0 (kein Übertrag)
    - **Overflow Flag (OF)**: 0 (kein Überlauf bei vorzeichenbehafteter Addition)
    - **Sign Flag (SF)**: 0 (Ergebnis ist positiv)

15. **Ergebnis zurückschreiben**: Das Ergebnis (35) wird über den internen Datenweg zurück ins Register-File geleitet und in R1 gespeichert.

**Zeitaufwand**: 1 Taktzyklus (Register-zu-Register-Operation)

---

**Zustand nach Ausführung**:
- R1 = 35 (neu berechnet)
- R2 = 10 (unverändert)
- R3 = 25 (unverändert)
- PC = `0x1004` (zeigt auf nächste Instruktion)
- IR = `ADD R1, R2, R3` (noch gespeichert, wird beim nächsten Fetch überschrieben)

---

**Gesamtzeit**: 
- **Best Case** (L1-Cache-Hit): ~6 Taktzyklen
- **Worst Case** (RAM-Zugriff): ~103 Taktzyklen

**Wichtige Beobachtungen**:

1. **Pipelining-Potenzial**: Während der Execute-Phase der aktuellen Instruktion könnte bereits die nächste Instruktion gefetcht werden (Befehlspipelining). Moderne CPUs führen mehrere Instruktionen parallel in verschiedenen Phasen aus.

2. **Cache-Bedeutung**: Der Fetch-Schritt ist der langsamste Teil (100 Taktzyklen bei RAM-Zugriff vs. 4 bei L1-Cache). Dies zeigt, warum Cache-Optimierung so wichtig ist.

3. **Sequenzielle Abarbeitung**: In der klassischen Von-Neumann-Architektur wird jede Instruktion vollständig durchlaufen, bevor die nächste beginnt. Moderne CPUs nutzen Pipelining, Out-of-Order-Execution und Superscalar-Architekturen, um mehrere Instruktionen parallel zu verarbeiten.

---

### Lösung T3: Cache-Hierarchie und Performance (Schwer)

#### Teilaufgabe a) Cache-Ebenen

Moderne Prozessoren verwenden eine **mehrstufige Cache-Hierarchie**, um den Von-Neumann-Flaschenhals zu minimieren. Jede Cache-Ebene hat unterschiedliche Eigenschaften bezüglich Größe, Geschwindigkeit und Architektur.

**L1-Cache (Level 1 Cache)**

**Größe**: 32-64 KB pro Core (typisch 32 KB für Instruktionen, 32 KB für Daten)

**Zugriffszeit**: 4-5 Taktzyklen (~1-2 ns bei 3 GHz CPU)

**Architektur**: 
- **Split-Cache**: L1 ist fast immer in zwei getrennte Bereiche aufgeteilt:
  - **L1-I (Instruction Cache)**: Speichert nur Programmbefehle
  - **L1-D (Data Cache)**: Speichert nur Daten
- Diese Trennung ermöglicht simultane Zugriffe (eine Instruktion fetchen und gleichzeitig Daten laden), was den Von-Neumann-Flaschenhals teilweise umgeht.

**Eigenschaften**:
- **Assoziativität**: Meist 8-way set associative
- **Cache Line Size**: 64 Bytes
- **Write-Policy**: Write-through oder Write-back (abhängig von Architektur)
- **Dediziert pro Core**: Jeder CPU-Core hat seinen eigenen L1-Cache

**Warum so klein?**
- Physische Nähe zur ALU erforderlich für minimale Latenz
- Schneller SRAM (Static RAM) ist teuer und benötigt viel Chipfläche
- Größere Caches würden längere Zugriffszeiten bedeuten

**Anwendungsfall**: Speichert die am häufigsten genutzten Daten und Instruktionen, die im aktuellen Moment benötigt werden (z.B. Schleifenvariablen, hot loops).

---

**L2-Cache (Level 2 Cache)**

**Größe**: 256 KB - 1 MB pro Core

**Zugriffszeit**: 12-15 Taktzyklen (~4-5 ns bei 3 GHz CPU)

**Architektur**: 
- **Unified Cache**: L2 ist typischerweise ein vereinheitlichter Cache, der sowohl Instruktionen als auch Daten speichert
- Liegt physisch weiter von der ALU entfernt als L1, aber noch auf demselben CPU-Die

**Eigenschaften**:
- **Assoziativität**: Meist 8-way oder 16-way set associative
- **Cache Line Size**: 64 Bytes
- **Inclusive/Exclusive**: Kann entweder alle Daten aus L1 enthalten (inclusive) oder nur zusätzliche Daten (exclusive) – abhängig von Architektur
- **Dediziert pro Core**: Jeder Core hat seinen eigenen L2-Cache

**Funktion**: 
L2 fungiert als "Puffer" zwischen dem sehr schnellen aber kleinen L1 und dem größeren aber langsameren L3. Bei einem L1-Cache-Miss wird zunächst L2 abgefragt, bevor auf L3 oder RAM zugegriffen wird.

**Anwendungsfall**: Speichert Daten, die nicht mehr in L1 passen, aber noch mit hoher Wahrscheinlichkeit bald wieder benötigt werden (z.B. Funktionskontext, größere Arrays, die nicht komplett in L1 passen).

---

**L3-Cache (Level 3 Cache)**

**Größe**: 8-64 MB (geteilt zwischen allen Cores)

**Zugriffszeit**: 40-50 Taktzyklen (~12-20 ns bei 3 GHz CPU)

**Architektur**: 
- **Shared Cache**: L3 ist zwischen allen CPU-Cores geteilt
- Dies ermöglicht effiziente Kommunikation zwischen Cores (Daten müssen nicht über RAM ausgetauscht werden)
- Liegt am Rand des CPU-Dies

**Eigenschaften**:
- **Assoziativität**: 12-way bis 20-way set associative
- **Cache Line Size**: 64 Bytes
- **Inclusive**: Enthält oft alle Daten aus L1 und L2 aller Cores
- **Victim Cache**: Fungiert als "Auffangbecken" für aus L1/L2 verdrängte Daten

**Funktion**: 
L3 reduziert die Anzahl der langsamen RAM-Zugriffe erheblich. Da er zwischen Cores geteilt wird, können Threads, die auf verschiedenen Cores laufen, effizient Daten austauschen.

**Anwendungsfall**: 
- **Multithreading**: Gemeinsam genutzte Datenstrukturen (z.B. Synchronisationsvariablen)
- **Context Switching**: Wenn ein Thread von einem Core zu einem anderen wechselt, sind seine Daten oft noch in L3 verfügbar
- **Large Working Sets**: Programme, die mehr Daten benötigen, als in L1/L2 passen

---

**Vergleichstabelle**:

| Eigenschaft | L1-Cache | L2-Cache | L3-Cache | RAM |
|-------------|----------|----------|----------|-----|
| **Größe** | 32-64 KB | 256 KB - 1 MB | 8-64 MB | 8-64 GB |
| **Zugriffszeit (Zyklen)** | 4-5 | 12-15 | 40-50 | 100-300 |
| **Zugriffszeit (ns @ 3 GHz)** | 1-2 ns | 4-5 ns | 12-20 ns | 50-100 ns |
| **Bandbreite** | ~1 TB/s | ~500 GB/s | ~200 GB/s | ~20-50 GB/s |
| **Pro Core / Shared** | Pro Core | Pro Core | Shared | Shared |
| **Split / Unified** | Split (I/D) | Unified | Unified | Unified |
| **Hit Rate** | ~95% | ~90% | ~80% | - |

---

**Warum diese Hierarchie?**

Die Cache-Hierarchie ist ein **Kompromiss zwischen Geschwindigkeit, Größe und Kosten**:

1. **Physikalische Grenzen**: Schneller SRAM benötigt viele Transistoren und kann nicht beliebig vergrößert werden, ohne die Zugriffszeit zu erhöhen.

2. **Wirtschaftlichkeit**: L1-SRAM kostet ~$1000 pro MB, RAM nur ~$5 pro GB. Eine CPU mit 64 MB L1-Cache wäre unbezahlbar.

3. **Temporal Locality**: Die meisten Programme greifen wiederholt auf dieselben Daten zu (Schleifen, Funktionsaufrufe). Ein kleiner, schneller Cache reicht oft aus.

4. **Spatial Locality**: Programme greifen oft auf räumlich benachbarte Daten zu (Arrays, Structs). Cache Lines von 64 Bytes nutzen dies aus.

5. **Pareto-Prinzip**: 90% der Zugriffe betreffen 10% der Daten. Die Cache-Hierarchie stellt sicher, dass diese 10% in schnellem Speicher liegen.

---

#### Teilaufgabe b) Zeitersparnis-Berechnung

**Gegeben**:
- CPU-Taktfrequenz: 3 GHz (1 Taktzyklus = 1/3 ns ≈ 0,33 ns)
- 1 Million Speicherzugriffe
- L1-Cache-Hit-Rate: 95%
- L2-Cache-Hit-Rate (bei L1-Miss): 90%
- Alle anderen Zugriffe gehen zum RAM
- Zugriffszeiten: L1 = 4 Zyklen, L2 = 12 Zyklen, RAM = 100 Zyklen

**Schritt 1: Zugriffsverteilung berechnen**

Von 1.000.000 Zugriffen:

- **L1-Hits**: 95% von 1.000.000 = 950.000 Zugriffe
- **L1-Misses**: 5% von 1.000.000 = 50.000 Zugriffe

Von den 50.000 L1-Misses:
- **L2-Hits**: 90% von 50.000 = 45.000 Zugriffe
- **L2-Misses** (gehen zu RAM): 10% von 50.000 = 5.000 Zugriffe

**Zusammenfassung**:
- L1: 950.000 Zugriffe
- L2: 45.000 Zugriffe
- RAM: 5.000 Zugriffe

---

**Schritt 2: Gesamtzeit MIT Cache berechnen**

Die Gesamtzeit ist die Summe aller Zugriffszeiten gewichtet nach Häufigkeit:

$$
\text{Zeit}_{\text{mit Cache}} = (\text{L1-Hits} \times t_{\text{L1}}) + (\text{L2-Hits} \times t_{\text{L2}}) + (\text{RAM-Hits} \times t_{\text{RAM}})
$$

$$
\text{Zeit}_{\text{mit Cache}} = (950{,}000 \times 4) + (45{,}000 \times 12) + (5{,}000 \times 100)
$$

$$
\text{Zeit}_{\text{mit Cache}} = 3{,}800{,}000 + 540{,}000 + 500{,}000 = 4{,}840{,}000 \text{ Zyklen}
$$

Umrechnung in Zeit bei 3 GHz:

$$
\text{Zeit}_{\text{mit Cache}} = \frac{4{,}840{,}000 \text{ Zyklen}}{3 \times 10^9 \text{ Zyklen/s}} = 1{,}613 \text{ ms} \approx 1{,}61 \text{ ms}
$$

---

**Schritt 3: Gesamtzeit OHNE Cache berechnen**

Ohne Cache müssten alle 1.000.000 Zugriffe direkt zum RAM gehen:

$$
\text{Zeit}_{\text{ohne Cache}} = 1{,}000{,}000 \times 100 = 100{,}000{,}000 \text{ Zyklen}
$$

Umrechnung in Zeit:

$$
\text{Zeit}_{\text{ohne Cache}} = \frac{100{,}000{,}000 \text{ Zyklen}}{3 \times 10^9 \text{ Zyklen/s}} = 33{,}33 \text{ ms}
$$

---

**Schritt 4: Zeitersparnis berechnen**

$$
\text{Zeitersparnis} = \text{Zeit}_{\text{ohne Cache}} - \text{Zeit}_{\text{mit Cache}}
$$

$$
\text{Zeitersparnis} = 33{,}33 \text{ ms} - 1{,}61 \text{ ms} = 31{,}72 \text{ ms}
$$

---

**Schritt 5: Speedup-Faktor berechnen**

$$
\text{Speedup} = \frac{\text{Zeit}_{\text{ohne Cache}}}{\text{Zeit}_{\text{mit Cache}}} = \frac{33{,}33 \text{ ms}}{1{,}61 \text{ ms}} \approx 20{,}7
$$

---

**Antwort**:

Die Cache-Hierarchie spart **31,72 ms** (etwa **95,2%** der ursprünglichen Zeit) und beschleunigt die Ausführung um den **Faktor 20,7**.

**Interpretation**:

1. **Dramatischer Effekt**: Ohne Cache würde das Programm mehr als **20-mal langsamer** laufen!

2. **L1 ist entscheidend**: 950.000 von 1.000.000 Zugriffen werden von L1 bedient. Dies zeigt, warum L1-Optimierung so wichtig ist.

3. **Effektive Zugriffszeit**: Die durchschnittliche Zugriffszeit beträgt:
   $$
   \text{Durchschnitt} = \frac{4{,}840{,}000 \text{ Zyklen}}{1{,}000{,}000 \text{ Zugriffe}} = 4{,}84 \text{ Zyklen pro Zugriff}
   $$
   Dies ist nur geringfügig höher als die reine L1-Zeit (4 Zyklen), was die Effizienz der Hierarchie zeigt.

4. **Cache-Größe vs. Hit-Rate Trade-off**: Selbst mit 95% L1-Hit-Rate haben wir noch 50.000 Misses. Programme mit schlechter Locality (z.B. zufällige Speicherzugriffe) hätten dramatisch schlechtere Performance.

---

#### Teilaufgabe c) Locality-Prinzipien

**Locality** (Lokalität) beschreibt die Tendenz von Programmen, bevorzugt auf bestimmte Speicherbereiche zuzugreifen. Cache-Systeme sind darauf optimiert, diese Muster auszunutzen. Es gibt zwei grundlegende Arten:

---

**1. Temporal Locality (Zeitliche Lokalität)**

**Definition**: Wenn auf eine Speicheradresse zugegriffen wurde, ist die Wahrscheinlichkeit hoch, dass **in naher Zukunft erneut** auf dieselbe Adresse zugegriffen wird.

**Kernidee**: "Was kürzlich benutzt wurde, wird wahrscheinlich bald wieder benutzt."

**Beispiele**:

**a) Schleifenvariablen:**
```python
summe = 0
for i in range(1000000):
    summe += i  # "summe" wird 1 Mio. Mal gelesen und geschrieben
```
Die Variable `summe` wird millionenfach innerhalb kurzer Zeit zugegriffen. Nach dem ersten Zugriff liegt sie im L1-Cache und alle weiteren Zugriffe erfolgen extrem schnell.

**b) Funktionsaufrufe:**
```python
def berechne_quadrat(x):
    return x * x

for i in range(1000):
    resultat = berechne_quadrat(i)
```
Der Code der Funktion `berechne_quadrat` wird 1000-mal hintereinander ausgeführt. Nach dem ersten Aufruf liegt der Instruktions-Code im L1-I-Cache, sodass alle weiteren Aufrufe keine RAM-Zugriffe mehr benötigen.

**c) Stack-Frames:**
```python
def recursive_factorial(n):
    if n <= 1:
        return 1
    return n * recursive_factorial(n-1)

factorial(100)
```
Bei Rekursion werden lokale Variablen auf dem Stack gespeichert. Der Stack-Pointer bewegt sich auf und ab, greift aber wiederholt auf denselben Speicherbereich zu. Diese Daten bleiben im Cache.

**Cache-Strategie**: 
- Cache speichert kürzlich genutzte Daten
- LRU (Least Recently Used) Replacement Policy: Die am längsten nicht genutzten Daten werden verdrängt
- Temporal Locality ist der **Hauptgrund**, warum selbst kleine Caches (32 KB L1) sehr hohe Hit-Raten erreichen

---

**2. Spatial Locality (Räumliche Lokalität)**

**Definition**: Wenn auf eine Speicheradresse zugegriffen wurde, ist die Wahrscheinlichkeit hoch, dass **bald auf benachbarte Adressen** zugegriffen wird.

**Kernidee**: "Wenn Adresse X gelesen wurde, werden wahrscheinlich auch X+1, X+2, X+3, ... benötigt."

**Beispiele**:

**a) Array-Durchlauf (sequenziell):**
```python
zahlen = [1, 2, 3, 4, 5, ..., 1000]
summe = 0
for zahl in zahlen:
    summe += zahl
```
Arrays werden sequenziell durchlaufen. Wenn `zahlen[0]` gelesen wird, werden `zahlen[1]`, `zahlen[2]`, etc. bald folgen. Der Cache lädt eine ganze **Cache Line** (64 Bytes = 8 Integers), sodass die nächsten 7 Zugriffe aus dem Cache bedient werden.

**b) String-Verarbeitung:**
```python
text = "Dies ist ein langer Text..."
for char in text:
    if char == ' ':
        print("Leerzeichen gefunden")
```
Strings sind im Speicher als zusammenhängende Byte-Arrays gespeichert. Jeder Zeichen-Zugriff profitiert davon, dass das nächste Zeichen bereits im Cache liegt.

**c) Structs / Objekte:**
```python
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

punkte = [Punkt(i, i*2) for i in range(1000)]
for punkt in punkte:
    distanz = (punkt.x**2 + punkt.y**2)**0.5
```
Die Attribute `x` und `y` eines Objekts liegen räumlich nah beieinander im Speicher. Wenn `punkt.x` geladen wird, ist `punkt.y` oft in derselben Cache Line enthalten.

**Cache-Strategie**: 
- Cache lädt nicht einzelne Bytes, sondern ganze **Cache Lines** (typisch 64 Bytes)
- Prefetching: Moderne CPUs erkennen sequenzielle Zugriffsmuster und laden vorausschauend weitere Cache Lines
- Spatial Locality ist der Grund, warum Array-Operationen **viel schneller** sind als Pointer-Chasing (zufällige Speicherzugriffe)

---

**Anti-Patterns: Schlechte Locality**

**a) Zufällige Zugriffe (Random Access):**
```python
import random
indices = list(range(1000000))
random.shuffle(indices)
for i in indices:
    daten[i] += 1  # Chaotisches Zugriffsmuster
```
Jeder Zugriff trifft eine zufällige Speicheradresse. Cache Lines werden geladen, aber nur ein einziges Element wird genutzt, bevor die Line verdrängt wird. **Cache-Hit-Rate sinkt dramatisch** (oft <10%).

**b) Pointer-Chasing (Linked Lists):**
```python
class Node:
    def __init__(self, wert):
        self.wert = wert
        self.next = None

# Linked List durchlaufen
current = head
while current:
    verarbeite(current.wert)
    current = current.next  # Pointer-Sprung zu beliebiger Adresse
```
Jeder Node kann irgendwo im Speicher liegen. Der nächste Node ist nicht vorhersagbar, sodass jeder Zugriff einen Cache-Miss verursachen kann. **Arrays sind 10-100x schneller** für sequenzielles Durchlaufen!

**c) Matrix-Transponierung (schlechte Reihenfolge):**
```python
# Schlecht: Spaltenweiser Zugriff in Row-Major-Layout
for col in range(N):
    for row in range(N):
        matrix[row][col] += 1  # Springt durch den Speicher
```
Matrizen werden zeilenweise gespeichert. Spaltenweiser Zugriff führt zu großen Sprüngen (jeder Zugriff ist eine ganze Zeile entfernt), was Spatial Locality zerstört.

**Bessere Variante (Cache-freundlich):**
```python
# Gut: Zeilenweiser Zugriff in Row-Major-Layout
for row in range(N):
    for col in range(N):
        matrix[row][col] += 1  # Sequenzieller Speicherzugriff
```

---

**Zusammenfassung der Locality-Prinzipien**:

| Prinzip | Beschreibung | Cache-Vorteil | Beispiele |
|---------|--------------|---------------|-----------|
| **Temporal Locality** | Gleiche Adresse wiederholt nutzen | Daten bleiben im Cache | Schleifen, Funktionen, Stack |
| **Spatial Locality** | Benachbarte Adressen nutzen | Cache Lines ausnutzen | Arrays, Strings, sequenzielle Daten |

**Cache-Hierarchie und Locality**:
- **L1-Cache**: Optimiert für hohe Temporal Locality (kleine Größe, sehr schnell)
- **Cache Lines**: Optimiert für Spatial Locality (64 Bytes pro Line)
- **Prefetcher**: Erkennt sequenzielle Muster und lädt vorausschauend (Spatial Locality)
- **LRU-Strategie**: Hält häufig genutzte Daten (Temporal Locality)

**Performance-Implikationen**:
- **Gute Locality**: 95%+ Cache-Hit-Rate, Programme laufen 20-50x schneller
- **Schlechte Locality**: 20-50% Cache-Hit-Rate, Programm wird durch RAM-Bandbreite limitiert
- **Cache-Optimierung** ist oft wichtiger als Algorithmus-Komplexität: Ein O(n²)-Algorithmus mit guter Locality kann schneller sein als O(n log n) mit schlechter Locality!

---

**Praktische Tipps für Cache-freundlichen Code**:

1. **Daten sequenziell verarbeiten** (Arrays bevorzugen, Linked Lists vermeiden)
2. **Kleine Working Sets** (Datenstrukturen klein halten, damit sie in Cache passen)
3. **Loop Blocking / Tiling** (Große Schleifen in kleinere Blöcke aufteilen)
4. **Struktur-Optimierung** (Häufig zusammen genutzte Daten räumlich nah speichern)
5. **Cache-Aware-Algorithmen** (Matrix-Multiplikation mit Blocking, Cache-Oblivious Algorithms)

---

## Teil B: Python-Lösungen

### Lösung P1: CNC-Werkzeugverschleiß Visualisierung (Leicht)

```python
import matplotlib.pyplot as plt

# Betriebszeit-Werte
betriebszeit = [i * 5 for i in range(21)]  # 0 bis 100 Minuten

# Verschleiß-Werte berechnen
hartmetall = [0.002 * t + 0.05 for t in betriebszeit]
hss = [0.008 * t + 0.10 for t in betriebszeit]
schnellstahl = [0.015 * t + 0.15 for t in betriebszeit]

# Plot erstellen
plt.plot(betriebszeit, hartmetall, 'b-', label='Hartmetall-Fräser', linewidth=2)
plt.plot(betriebszeit, hss, 'g-', label='HSS-Fräser', linewidth=2)
plt.plot(betriebszeit, schnellstahl, 'r-', label='Schnellstahl', linewidth=2)

# Kritische Verschleißgrenze
plt.axhline(y=1.0, color='red', linestyle='--', linewidth=2, label='Kritische Grenze (1.0 mm)')

plt.xlabel('Betriebszeit (Minuten)')
plt.ylabel('Verschleiß (mm)')
plt.title('Werkzeugverschleiß bei Fräsoperationen')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

---

### Lösung P2: Hydrauliksystem-Überwachung (Leicht-Mittel)

```python
import matplotlib.pyplot as plt

# Daten
stunden = list(range(24))
druck_bar = [145, 148, 152, 158, 165, 170, 178, 185, 192, 198, 
             205, 210, 215, 218, 215, 210, 205, 198, 190, 182, 
             170, 160, 152, 148]

# Plot mit Markern
plt.plot(stunden, druck_bar, 'o-', color='darkblue', linewidth=2, 
         markersize=6, label='Hydraulikdruck')

# Betriebsgrenzen
plt.axhline(y=150, color='green', linestyle='--', linewidth=2, label='Min. Betriebsdruck (150 bar)')
plt.axhline(y=200, color='red', linestyle='--', linewidth=2, label='Max. Betriebsdruck (200 bar)')

# Kritische Druckwerte finden
kritisch_stunden = [s for s, d in zip(stunden, druck_bar) if d < 150 or d > 200]
kritisch_druck = [d for d in druck_bar if d < 150 or d > 200]

# Kritische Punkte markieren
plt.scatter(kritisch_stunden, kritisch_druck, color='orange', s=120, 
            zorder=5, label='Kritischer Druck', edgecolors='darkorange', linewidth=2)

plt.xlabel('Uhrzeit (Stunde)')
plt.ylabel('Hydraulikdruck (bar)')
plt.title('Hydraulikdruck-Überwachung über 24 Stunden')
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
plt.show()
```

---

### Lösung P3: Produktionsqualität im Vergleich (Mittel)

```python
import matplotlib.pyplot as plt

# Daten
quartale = [1, 2, 3, 4, 5, 6, 7, 8, 9]
linie_a_ausschuss_prozent = [8.5, 7.2, 6.1, 5.5, 4.8, 4.2, 3.5, 2.9, 2.1]
linie_b_ausschuss_prozent = [9.2, 8.5, 7.8, 7.0, 6.5, 6.0, 5.2, 4.5, 3.8]
produktionsvolumen_tsd = [10, 12, 15, 18, 22, 25, 30, 35, 42]

# Scatter-Plots mit Volumen-Skalierung
plt.scatter(quartale, linie_a_ausschuss_prozent, s=produktionsvolumen_tsd, 
            color='blue', marker='o', alpha=0.6, label='Linie A', edgecolors='darkblue', linewidth=1.5)
plt.scatter(quartale, linie_b_ausschuss_prozent, s=produktionsvolumen_tsd, 
            color='red', marker='s', alpha=0.6, label='Linie B', edgecolors='darkred', linewidth=1.5)

# Verbindungslinien
plt.plot(quartale, linie_a_ausschuss_prozent, 'b--', linewidth=1.5, alpha=0.5)
plt.plot(quartale, linie_b_ausschuss_prozent, 'r:', linewidth=1.5, alpha=0.5)

# Ziel-Ausschussquote
plt.axhline(y=3, color='green', linestyle='-.', linewidth=2, label='Ziel-Ausschussquote (3%)')

# Annotation
plt.text(7, 8, "Größe ∝ Produktionsvolumen", fontsize=10, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.xlabel('Quartal')
plt.ylabel('Ausschussquote (%)')
plt.title('Qualitätsentwicklung: Linie A vs. Linie B')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.show()
```

---

### Lösung P4: FEM-Spannungsanalyse mit Fehlerbalken (Mittel-Schwer)

```python
import matplotlib.pyplot as plt
import numpy as np

# Daten
lasten_kn = [5, 10, 15, 20, 25, 30, 35, 40]
spannung_mittel_mpa = [48, 95, 142, 189, 235, 282, 328, 375]
spannung_std_mpa = [3, 5, 7, 9, 12, 15, 18, 22]

# Fehlerbalken-Plot
plt.errorbar(lasten_kn, spannung_mittel_mpa, yerr=spannung_std_mpa, 
             fmt='o-', color='darkblue', ecolor='blue', capsize=5, capthick=2,
             linewidth=2, markersize=8, label='Simulation ± σ', zorder=3)

# Unsicherheitsbereich
obere_grenze = [m + s for m, s in zip(spannung_mittel_mpa, spannung_std_mpa)]
untere_grenze = [m - s for m, s in zip(spannung_mittel_mpa, spannung_std_mpa)]
plt.fill_between(lasten_kn, untere_grenze, obere_grenze, 
                 alpha=0.2, color='blue', label='±1σ Bereich', zorder=1)

# Streckgrenze markieren
plt.axhline(y=300, color='red', linestyle='--', linewidth=2, label='Streckgrenze (300 MPa)')

# Plastischer Bereich
kritisch_start = 25  # Approximation: bei 25 kN wird Streckgrenze erreicht
plt.axvspan(kritisch_start, 40, color='red', alpha=0.1, label='Plastische Verformung', zorder=0)

# Trendlinie
koeffizienten = np.polyfit(lasten_kn, spannung_mittel_mpa, deg=1)
trendlinie = np.polyval(koeffizienten, lasten_kn)
plt.plot(lasten_kn, trendlinie, 'k--', linewidth=2, 
         label=f'Trendlinie (y = {koeffizienten[0]:.1f}x + {koeffizienten[1]:.1f})', zorder=2)

plt.xlabel('Last (kN)', fontsize=12)
plt.ylabel('Spannung (MPa)', fontsize=12)
plt.title('FEM-Spannungsanalyse mit Messunsicherheit', fontsize=14, fontweight='bold')
plt.legend(loc='upper left', fontsize=9)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

### Lösung P5: Lager-Vibrations-Performance-Analyse (Schwer)

```python
import matplotlib.pyplot as plt

# Konstanten
BASISVIBRATION = 0.5
REFERENZ_DREHZAHL = 1000
ZUSTANDSFAKTOREN = {
    'Neu': 1.0,
    'Leicht verschlissen': 1.8,
    'Stark verschlissen': 3.5,
    'Beschädigt': 8.0
}

def berechne_vibrationsamplitude(drehzahl_upm, zustandsfaktor):
    """Berechnet Vibrationsamplitude basierend auf Drehzahl und Lagerzustand."""
    return BASISVIBRATION * (drehzahl_upm / REFERENZ_DREHZAHL)**0.7 * zustandsfaktor

# Drehzahlen
drehzahlen = [100, 200, 500, 1000, 2000, 3000, 5000, 7000, 10000]

# Simuliere Lagerzustände
amplituden = {zustand: [berechne_vibrationsamplitude(d, faktor) for d in drehzahlen]
              for zustand, faktor in ZUSTANDSFAKTOREN.items()}

# Schadensfaktoren (relativ zu Neu)
neu_amplituden = amplituden['Neu']
schadensfaktoren = {zustand: [a / n for a, n in zip(ampl, neu_amplituden)]
                   for zustand, ampl in amplituden.items() if zustand != 'Neu'}

# Erstelle Figure mit 2 Subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot 1: Vibrationsamplituden
farben = ['green', 'orange', 'red', 'darkred']
linienstile = ['-', '--', '-.', ':']
for (zustand, ampl), farbe, stil in zip(amplituden.items(), farben, linienstile):
    ax1.plot(drehzahlen, ampl, color=farbe, linestyle=stil, 
             linewidth=2, marker='o', markersize=6, label=zustand)

ax1.set_xscale('log')
ax1.set_xlabel('Drehzahl (U/min)', fontsize=12)
ax1.set_ylabel('Vibrationsamplitude (mm/s)', fontsize=12)
ax1.set_title('Lager-Vibrations-Analyse: Einfluss von Drehzahl und Lagerzustand', 
              fontsize=14, fontweight='bold')
ax1.legend(loc='upper left')
ax1.grid(True, which='both', alpha=0.3)

# Plot 2: Schadensfaktoren
for (zustand, faktoren), farbe, stil in zip(schadensfaktoren.items(), farben[1:], linienstile[1:]):
    ax2.plot(drehzahlen, faktoren, color=farbe, linestyle=stil, 
             linewidth=2, marker='s', markersize=6, label=zustand)

# Kritische Schwelle
ax2.axhline(y=5, color='red', linestyle='--', linewidth=2, label='Kritische Schwelle')

ax2.set_xscale('log')
ax2.set_xlabel('Drehzahl (U/min)', fontsize=12)
ax2.set_ylabel('Schadensfaktor (relativ zu Neu-Lager)', fontsize=12)
ax2.set_title('Schadensfaktor vs. Drehzahl', fontsize=14, fontweight='bold')
ax2.legend(loc='upper left')
ax2.grid(True, which='both', alpha=0.3)

plt.tight_layout()
plt.show()
```

---

marker_groessen = [k * 20 for k in kerne]

plt.scatter(jahre, intel_mhz, s=marker_groessen, color='blue', 
            marker='o', alpha=0.6, label='Intel', 
            edgecolors='darkblue', linewidth=1.5)
```

**Marker-Größen-Skalierung**:
- `s` erwartet eine Größe in **Punkten²** (nicht Radius!)
- Ein Kern → 20 Punkte², zwei Kerne → 40 Punkte², etc.
- Die Fläche des Markers wächst also proportional zur Anzahl der Kerne

**Warum Faktor 20?**
- Faktor 1 wäre zu klein (kaum sichtbar)
- Faktor 100 wäre zu groß (Marker überlappen stark)
- Faktor 20 ist ein guter Kompromiss für Sichtbarkeit

**Parameter-Erklärung**:
- `marker='o'`: Kreise für Intel, `marker='s'`: Quadrate (squares) für AMD
- `alpha=0.6`: Leichte Transparenz (60% opak), damit überlappende Marker sichtbar bleiben
- `edgecolors='darkblue'`: Dunkler Rand um die Marker herum (verbessert Kontrast)
- `linewidth=1.5`: Dicke des Marker-Rands

**Verfügbare Marker-Stile**:
```python
'o'  # Kreis
's'  # Quadrat (square)
'^'  # Dreieck nach oben
'v'  # Dreieck nach unten
'D'  # Diamant
'*'  # Stern
'+'  # Plus
'x'  # Kreuz
```

---

**Teil b) Größen-Annotation**

```python
plt.text(2018, 1000, "Größe ∝ Kerne", fontsize=10, 
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
```

- `plt.text(x, y, text)`: Platziert Text an Position (x=2018, y=1000)
- `fontsize=10`: Schriftgröße in Punkten
- `bbox=dict(...)`: Zeichnet eine Box um den Text herum
  - `boxstyle='round'`: Abgerundete Ecken
  - `facecolor='wheat'`: Hintergrundfarbe (weizenfarbig)
  - `alpha=0.5`: Transparenz der Box

**Alternative Boxstyles**:
```python
boxstyle='round'      # Abgerundete Ecken
boxstyle='square'     # Rechte Ecken
boxstyle='circle'     # Kreisform
boxstyle='rarrow'     # Pfeil nach rechts
```

**Warum Position (2018, 1000)?**
- X=2018: Am rechten Rand des Plots, wo Platz ist
- Y=1000: Im mittleren Bereich der logarithmischen Skala (zwischen 100 und 10.000)

---

**Teil c) Verbindungslinien**

```python
plt.plot(jahre, intel_mhz, color='blue', linestyle='--', 
         linewidth=1.5, alpha=0.5)
plt.plot(jahre, amd_mhz, color='red', linestyle=':', 
         linewidth=1.5, alpha=0.5)
```

- **Kombination aus Scatter und Plot**: Scatter zeigt die Datenpunkte, Plot verbindet sie
- `linestyle='--'`: Gestrichelt für Intel
- `linestyle=':'`: Gepunktet für AMD (unterscheidet sich deutlich von gestrichelt)
- `alpha=0.5`: Halbtransparente Linien, damit sie nicht von den Markern ablenken

**Wichtig**: Die Plot-Befehle kommen **nach** den Scatter-Befehlen, damit die Linien **hinter** den Markern liegen. Wenn man die Reihenfolge umkehrt, verdecken die Linien die Marker.

**Alternative mit zorder**:
```python
plt.plot(..., zorder=1)      # Linien im Hintergrund
plt.scatter(..., zorder=2)   # Marker im Vordergrund
```

---

**Teil d) Logarithmische Skalierung**

```python
plt.yscale('log')
```

**Warum logarithmisch?**
Die CPU-Frequenzen reichen von 12 MHz (1985) bis 6000 MHz (2023) – ein **Faktor 500**! 

Auf einer linearen Skala wären die frühen Werte (12, 16, 33 MHz) kaum sichtbar:

**Lineare Skala** (schlecht):
```
6000 |                                     * *
5000 |                                   *
4000 |                                 *
3000 |                              *
2000 |                           *
1000 |                        *
   0 |* * *
     ----------------------
     1985              2023
```
Die ersten 30 Jahre sind nicht erkennbar!

**Logarithmische Skala** (gut):
```
10000|                                   * *
 1000|                    *         *  *
  100|      *    *
   10|*  *
      ----------------------
      1985              2023
```
Alle Datenpunkte sind gut sichtbar und das exponentielle Wachstum wird deutlich.

**Logarithmische Skala bedeutet**:
- Jeder "Schritt" auf der Y-Achse ist eine **Multiplikation** (z.B. Faktor 10)
- Linear: 10, 20, 30, 40, ... (Addition)
- Logarithmisch: 10, 100, 1000, 10000, ... (Multiplikation)

**Gitter bei logarithmischer Skala**:
```python
plt.grid(True, which='both', alpha=0.3)
```
- `which='both'`: Zeigt sowohl Major-Gitterlinien (10, 100, 1000, ...) als auch Minor-Gitterlinien (20, 30, ..., 200, 300, ...) an
- Dies hilft beim Ablesen von Zwischenwerten

---

#### Erwartete Ausgabe:

Ein Scatter-Plot mit logarithmischer Y-Achse, der Folgendes zeigt:

1. **Zwei Datenreihen**: Blaue Kreise (Intel) und rote Quadrate (AMD)
2. **Wachsende Marker**: Frühe Jahre haben kleine Marker (1 Kern), neuere Jahre große Marker (bis zu 24 Kerne)
3. **Verbindungslinien**: Gestrichelte blaue und gepunktete rote Linien verbinden die Punkte
4. **Klare Trends**:
   - **1985-2005**: Exponentielle Frequenzsteigerung (Moore's Law)
   - **2005-2010**: Frequenzen stagnieren ("Power Wall" – CPUs können nicht beliebig schneller getaktet werden wegen Hitzeentwicklung)
   - **2010-2023**: Moderate Frequenzsteigerung, aber massive Kern-Erhöhung
5. **Größen-Annotation**: Erklärt die Marker-Größen

---

#### Interpretation der Daten:

**Phase 1 (1985-2005): Frequenz-Scaling**
- CPU-Frequenzen stiegen exponentiell (Moore's Law)
- Hauptstrategie: "Make it faster" – höhere Taktraten
- Single-Core-Dominanz

**Phase 2 (2005-2010): Power Wall**
- Frequenzen stagnieren bei ~4 GHz
- Grund: Hitzeentwicklung (P ∝ f³) macht höhere Frequenzen unpraktisch
- Paradigmenwechsel: "Make it parallel" – Multi-Core-Architekturen

**Phase 3 (2010-2023): Multi-Core-Ära**
- Frequenzen steigen nur moderat
- Kern-Anzahl explodiert: 1 → 2 → 4 → 8 → 16 → 24+
- Performance durch Parallelisierung statt höherer Taktraten

**Intel vs. AMD**:
- Bis 2017: Intel führend bei Frequenzen
- Ab 2017: AMD Ryzen mit aggressiver Multi-Core-Strategie
- 2023: AMD teilweise höhere Kern-Zahlen, Intel teilweise höhere Boost-Frequenzen

---

#### Häufige Fehler:

> [!WARNING]
> **Fehler 1: Marker-Größen als Liste vs. einzelner Wert**
> ```python
> # FALSCH: Jeder Punkt braucht eine eigene Größe!
> plt.scatter(jahre, intel_mhz, s=kerne)  # Funktioniert nicht wie erwartet
> 
> # RICHTIG: Liste von Größen
> plt.scatter(jahre, intel_mhz, s=[k*20 for k in kerne])
> ```

> [!WARNING]
> **Fehler 2: Logarithmische Skala mit Null- oder Negativ-Werten**
> ```python
> plt.yscale('log')
> plt.plot([0, 1, 2], [0, 10, 100])  # FEHLER! log(0) ist undefiniert!
> ```
> **Lösung**: Logarithmische Skala nur für strikt positive Werte verwenden.

> [!WARNING]
> **Fehler 3: Linien verdecken Marker**
> ```python
> # FALSCH: Scatter nach Plot → Linien liegen oben
> plt.plot(jahre, intel_mhz, ...)
> plt.scatter(jahre, intel_mhz, ...)  # Marker evtl. verdeckt
> 
> # RICHTIG: Scatter vor Plot → Marker liegen oben
> plt.scatter(jahre, intel_mhz, ...)
> plt.plot(jahre, intel_mhz, ...)
> ```
> **Alternative**: `zorder` verwenden.

---

#### Erweiterungsmöglichkeiten:

**1. Colormap für Kern-Anzahl statt Marker-Größe**:
```python
import matplotlib.cm as cm
import matplotlib.colors as mcolors

norm = mcolors.Normalize(vmin=1, vmax=24)
cmap = cm.get_cmap('viridis')

plt.scatter(jahre, intel_mhz, c=kerne, cmap='viridis', 
            s=100, marker='o', edgecolors='black')
plt.colorbar(label='Anzahl Kerne')
```

**2. Zweite Y-Achse für Kern-Anzahl**:
```python
fig, ax1 = plt.subplots()

# Erste Y-Achse: Frequenz
ax1.scatter(jahre, intel_mhz, ...)
ax1.set_ylabel('Taktfrequenz (MHz)')

# Zweite Y-Achse: Kerne
ax2 = ax1.twinx()
ax2.plot(jahre, kerne, 'g-', linewidth=2, label='Kerne')
ax2.set_ylabel('Anzahl Kerne', color='g')
```

**3. Interaktive Tooltips (mit matplotlib widgets)**:
```python
# Zeigt Werte beim Überfahren mit der Maus
from matplotlib.widgets import Cursor
cursor = Cursor(ax, useblit=True, color='red', linewidth=1)
```

---

### Lösung P4: Messdaten-Analyse mit Fehlerbalken (Mittel-Schwer)

**Aufgabenstellung**: Visualisierung von Materialzugfestigkeit bei verschiedenen Temperaturen mit Fehlerbalken, Unsicherheitsbereichen und kritischen Zonen.

#### Vollständige Lösung:

```python
import matplotlib.pyplot as plt
import numpy as np

# Gegeben Daten
temperaturen = [20, 40, 60, 80, 100, 120, 140, 160]  # °C
zugfestigkeit_mittel = [450, 445, 438, 428, 415, 398, 375, 348]  # MPa
zugfestigkeit_std = [12, 15, 18, 22, 25, 30, 35, 40]  # MPa

# Teil a) Plot mit Fehlerbalken
plt.errorbar(temperaturen, zugfestigkeit_mittel, 
             yerr=zugfestigkeit_std, 
             fmt='o-', 
             color='darkblue',
             ecolor='blue',
             capsize=5, 
             capthick=2,
             linewidth=2,
             markersize=8,
             label='Messdaten ± Std',
             zorder=3)

# Teil b) Unsicherheitsbereich (Confidence Band)
obere_grenze = [mittel + std for mittel, std in zip(zugfestigkeit_mittel, zugfestigkeit_std)]
untere_grenze = [mittel - std for mittel, std in zip(zugfestigkeit_mittel, zugfestigkeit_std)]

plt.fill_between(temperaturen, untere_grenze, obere_grenze, 
                 alpha=0.2, 
                 color='blue', 
                 label='±1σ Bereich',
                 zorder=1)

# Teil c) Kritische Bereiche markieren
# Finde Temperaturen, bei denen Zugfestigkeit < 380 MPa
kritisch_start = None
for i, (temp, festigkeit) in enumerate(zip(temperaturen, zugfestigkeit_mittel)):
    if festigkeit < 380 and kritisch_start is None:
        kritisch_start = temp
        # Interpoliere, um genauen Übergang zu finden
        if i > 0:
            # Lineare Interpolation zwischen vorherigem und aktuellem Punkt
            temp_prev = temperaturen[i-1]
            fest_prev = zugfestigkeit_mittel[i-1]
            # Berechne Temperatur, bei der Festigkeit genau 380 ist
            kritisch_start = temp_prev + (380 - fest_prev) * (temp - temp_prev) / (festigkeit - fest_prev)

if kritisch_start is not None:
    kritisch_ende = temperaturen[-1]
    plt.axvspan(kritisch_start, kritisch_ende, 
                color='red', 
                alpha=0.15, 
                label='Kritischer Bereich (<380 MPa)',
                zorder=0)

# Teil d) Trendlinie (lineare Regression)
koeffizienten = np.polyfit(temperaturen, zugfestigkeit_mittel, deg=1)
trendlinie = [koeffizienten[0] * t + koeffizienten[1] for t in temperaturen]

plt.plot(temperaturen, trendlinie, 
         'k--', 
         linewidth=2, 
         label=f'Trendlinie (y = {koeffizienten[0]:.3f}x + {koeffizienten[1]:.1f})',
         zorder=2)

# Achsenbeschriftungen und Titel
plt.xlabel('Temperatur (°C)', fontsize=12)
plt.ylabel('Zugfestigkeit (MPa)', fontsize=12)
plt.title('Temperaturabhängigkeit der Zugfestigkeit', fontsize=14, fontweight='bold')

# Legende und Gitter
plt.legend(loc='upper right', fontsize=9)
plt.grid(True, alpha=0.3, linestyle='--')

# Achsen-Bereich optimieren
plt.xlim(10, 170)
plt.ylim(280, 480)

# Layout optimieren
plt.tight_layout()

plt.show()
```

---

#### Erklärung der Lösung:

**Teil a) Fehlerbalken mit errorbar()**

```python
plt.errorbar(temperaturen, zugfestigkeit_mittel, 
             yerr=zugfestigkeit_std, 
             fmt='o-', 
             color='darkblue',
             ecolor='blue',
             capsize=5, 
             capthick=2,
             linewidth=2,
             markersize=8,
             label='Messdaten ± Std',
             zorder=3)
```

**Was ist `plt.errorbar()`?**

`errorbar()` ist eine spezialisierte Plot-Funktion für Daten mit Unsicherheiten. Sie kombiniert:
- Datenpunkte (wie `plt.plot()`)
- Fehlerbalken in X- und/oder Y-Richtung
- Optionale Verbindungslinien

**Parameter-Erklärung**:

- **`yerr=zugfestigkeit_std`**: Y-Fehlerbalken mit Standardabweichung
  - Kann auch `xerr` für X-Fehler sein
  - Kann symmetrisch (einzelne Liste) oder asymmetrisch (zwei Listen `[unten, oben]`) sein

- **`fmt='o-'`**: Format-String (wie bei `plt.plot()`)
  - `o` = Kreise als Marker
  - `-` = Durchgezogene Verbindungslinie

- **`ecolor='blue'`**: Farbe der **E**rror-Bars (Fehlerbalken)
  - Getrennt von `color` (Farbe der Linie/Marker)
  - Ermöglicht visuelle Unterscheidung

- **`capsize=5`**: Länge der "Caps" (horizontale Linien an den Enden der Fehlerbalken)
  - In Punkten gemessen
  - Verbessert die Ablesbarkeit

- **`capthick=2`**: Dicke der Caps
  - Sollte mit `linewidth` harmonieren

**Visualisierung der Komponenten**:
```
        ───  ← Cap (capsize)
         |   ← Error Bar
         o   ← Marker (fmt)
         |   ← Error Bar
        ───  ← Cap
```

**Wann verwendet man errorbar()?**

- **Experimentelle Daten**: Messungen mit Unsicherheiten
- **Statistische Auswertungen**: Mittelwert ± Standardabweichung
- **Konfidenzintervalle**: Bereich, in dem der wahre Wert mit bestimmter Wahrscheinlichkeit liegt
- **Vergleiche**: Überlappende Fehlerbalken bedeuten statistisch nicht signifikant unterschiedlich

---

**Teil b) Unsicherheitsbereich mit fill_between()**

```python
obere_grenze = [mittel + std for mittel, std in zip(zugfestigkeit_mittel, zugfestigkeit_std)]
untere_grenze = [mittel - std for mittel, std in zip(zugfestigkeit_mittel, zugfestigkeit_std)]

plt.fill_between(temperaturen, untere_grenze, obere_grenze, 
                 alpha=0.2, color='blue', label='±1σ Bereich', zorder=1)
```

**Was ist `plt.fill_between()`?**

Schattiert den Bereich zwischen zwei Kurven. Sehr nützlich für:
- Unsicherheitsbereiche (Confidence Bands)
- Differenzen zwischen zwei Messreihen
- Bereiche oberhalb/unterhalb einer Schwelle

**Syntax**:
```python
plt.fill_between(x, y1, y2, where=None, interpolate=False, step=None, **kwargs)
```

**Berechnung der Grenzen mit zip()**:
```python
# zip() kombiniert zwei Listen elementweise
for mittel, std in zip(zugfestigkeit_mittel, zugfestigkeit_std):
    # Iteration: (450, 12), (445, 15), (438, 18), ...
    obere = mittel + std  # 450 + 12 = 462
    untere = mittel - std  # 450 - 12 = 438
```

**Alternative mit NumPy** (eleganter und schneller):
```python
obere_grenze = np.array(zugfestigkeit_mittel) + np.array(zugfestigkeit_std)
untere_grenze = np.array(zugfestigkeit_mittel) - np.array(zugfestigkeit_std)
```

**Wichtige Parameter**:
- `alpha=0.2`: Transparenz (20% opak) – ermöglicht Überblick ohne Verdeckung
- `zorder=1`: Zeichnet im Hintergrund (unter Fehlerbalken und Trendlinie)

**Unterschied zwischen errorbar() und fill_between()**:
- **errorbar()**: Diskrete Fehlerbalken an jedem Datenpunkt
- **fill_between()**: Kontinuierlicher schattierter Bereich
- **Kombination**: Zeigt sowohl diskrete Messunsicherheiten als auch den Gesamttrend

---

**Teil c) Kritische Bereiche mit axvspan()**

```python
kritisch_start = None
for i, (temp, festigkeit) in enumerate(zip(temperaturen, zugfestigkeit_mittel)):
    if festigkeit < 380 and kritisch_start is None:
        kritisch_start = temp
        if i > 0:
            temp_prev = temperaturen[i-1]
            fest_prev = zugfestigkeit_mittel[i-1]
            kritisch_start = temp_prev + (380 - fest_prev) * (temp - temp_prev) / (festigkeit - fest_prev)

if kritisch_start is not None:
    kritisch_ende = temperaturen[-1]
    plt.axvspan(kritisch_start, kritisch_ende, 
                color='red', alpha=0.15, 
                label='Kritischer Bereich (<380 MPa)', zorder=0)
```

**Was ist `plt.axvspan()`?**

Schattiert einen **vertikalen Bereich** (von xmin bis xmax, über die gesamte Y-Achse).

**Syntax**:
```python
plt.axvspan(xmin, xmax, ymin=0, ymax=1, **kwargs)
```
- `xmin`, `xmax`: Grenzen in Datenkoordinaten
- `ymin`, `ymax`: Relative Position (0-1) auf der Y-Achse (Standard: 0-1 = volle Höhe)

**Lineare Interpolation**:

Die Zugfestigkeit fällt zwischen zwei Messpunkten unter 380 MPa. Um den genauen Übergangspunkt zu finden, nutzen wir lineare Interpolation:

Gegeben:
- Punkt A: (temp_prev, fest_prev) = (120, 398)
- Punkt B: (temp, festigkeit) = (140, 375)
- Gesucht: Temperatur, bei der Festigkeit = 380

Formel:
```
t = t_prev + (380 - f_prev) * (t - t_prev) / (f - f_prev)
t = 120 + (380 - 398) * (140 - 120) / (375 - 398)
t = 120 + (-18) * 20 / (-23)
t = 120 + 15.65
t ≈ 135.65°C
```

**Warum interpolieren?**

Ohne Interpolation würden wir `kritisch_start = 140°C` setzen, was ungenau wäre. Mit Interpolation erhalten wir die präzisere Grenze von ~135.65°C.

**Verwandte Funktionen**:
```python
plt.axhline(y)        # Horizontale Linie
plt.axvline(x)        # Vertikale Linie
plt.axhspan(ymin, ymax)  # Horizontaler Bereich
plt.axvspan(xmin, xmax)  # Vertikaler Bereich
```

---

**Teil d) Trendlinie mit np.polyfit()**

```python
koeffizienten = np.polyfit(temperaturen, zugfestigkeit_mittel, deg=1)
trendlinie = [koeffizienten[0] * t + koeffizienten[1] for t in temperaturen]

plt.plot(temperaturen, trendlinie, 
         'k--', linewidth=2, 
         label=f'Trendlinie (y = {koeffizienten[0]:.3f}x + {koeffizienten[1]:.1f})',
         zorder=2)
```

**Was ist `np.polyfit()`?**

Berechnet die Koeffizienten eines Polynoms, das die Daten am besten approximiert (Least Squares Regression).

**Syntax**:
```python
koeffizienten = np.polyfit(x, y, deg)
```
- `deg`: Grad des Polynoms
  - `deg=1`: Linear (y = ax + b) → 2 Koeffizienten
  - `deg=2`: Quadratisch (y = ax² + bx + c) → 3 Koeffizienten
  - `deg=3`: Kubisch → 4 Koeffizienten

**Rückgabewert**:
```python
koeffizienten = [a, b]  # Für deg=1
# a = Steigung
# b = y-Achsenabschnitt
```

**Beispielrechnung**:

Angenommen `np.polyfit()` liefert: `koeffizienten = [-0.723, 464.5]`

Das bedeutet: y = -0.723x + 464.5

Interpretation:
- **Steigung -0.723**: Pro Grad Temperaturerhöhung sinkt die Zugfestigkeit um 0.723 MPa
- **Y-Achsenabschnitt 464.5**: Bei 0°C hätte das Material (extrapoliert) ~464.5 MPa Zugfestigkeit

**Trendlinie berechnen**:
```python
trendlinie = [koeffizienten[0] * t + koeffizienten[1] for t in temperaturen]
# Für jede Temperatur wird y = -0.723 * t + 464.5 berechnet
```

**Alternative mit np.polyval()** (eleganter):
```python
trendlinie = np.polyval(koeffizienten, temperaturen)
```

**Label mit f-String**:
```python
label=f'Trendlinie (y = {koeffizienten[0]:.3f}x + {koeffizienten[1]:.1f})'
# Beispiel: 'Trendlinie (y = -0.723x + 464.5)'
```
- `.3f`: 3 Dezimalstellen für die Steigung
- `.1f`: 1 Dezimalstelle für den y-Achsenabschnitt

**Erweiterte Regression-Metriken**:
```python
# R² (Bestimmtheitsmaß) berechnen
from sklearn.metrics import r2_score
r2 = r2_score(zugfestigkeit_mittel, trendlinie)
# r2 = 1.0 → Perfekter Fit
# r2 = 0.0 → Kein Zusammenhang
```

---

#### Erweiterte Konzepte:

**1. zorder – Zeichenreihenfolge kontrollieren**

```python
plt.axvspan(..., zorder=0)        # Hintergrund (rot)
plt.fill_between(..., zorder=1)   # Mittlerer Bereich (blau)
plt.plot(..., zorder=2)            # Trendlinie (schwarz)
plt.errorbar(..., zorder=3)       # Datenpunkte (vorne)
```

Höhere `zorder`-Werte werden **über** niedrigeren gezeichnet. Dies verhindert, dass wichtige Elemente verdeckt werden.

**2. tight_layout() – Automatische Layout-Optimierung**

```python
plt.tight_layout()
```

Passt automatisch an:
- Abstände zwischen Subplots
- Ränder um den Plot
- Verhindert, dass Beschriftungen abgeschnitten werden

**Ohne `tight_layout()`**: Titel oder Achsenbeschriftungen können außerhalb des sichtbaren Bereichs liegen.

**Mit `tight_layout()`**: Alles ist sichtbar und optimal positioniert.

---

#### Erwartete Ausgabe:

Ein komplexer Plot mit:

1. **Blauen Fehlerbalken**: Zeigen die Messunsicherheit an jedem Punkt
2. **Hellblauer Unsicherheitsbereich**: Kontinuierlicher schattierter Bereich (±1σ)
3. **Roter kritischer Bereich**: Markiert Temperaturen > ~135.65°C, bei denen das Material kritisch schwach wird
4. **Schwarze gestrichelte Trendlinie**: Zeigt den linearen Abwärtstrend der Zugfestigkeit

**Interpretation**:
- Die Zugfestigkeit sinkt linear mit steigender Temperatur
- Ab ~135.65°C wird das Material kritisch schwach (<380 MPa)
- Die Standardabweichung steigt mit der Temperatur (größere Messunsicherheit bei hohen Temperaturen)

---

#### Häufige Fehler:

> [!WARNING]
> **Fehler 1: yerr als einzelner Wert statt Liste**
> ```python
> # FALSCH: Alle Fehlerbalken haben dieselbe Größe
> plt.errorbar(x, y, yerr=10)
> 
> # RICHTIG: Jeder Punkt hat eigenen Fehler
> plt.errorbar(x, y, yerr=fehler_liste)
> ```

> [!WARNING]
> **Fehler 2: fill_between() mit falscher Reihenfolge**
> ```python
> # FALSCH: untere > obere → Bereich wird nicht gefüllt!
> plt.fill_between(x, obere_grenze, untere_grenze)
> 
> # RICHTIG: untere < obere
> plt.fill_between(x, untere_grenze, obere_grenze)
> ```

> [!WARNING]
> **Fehler 3: np.polyfit() ohne NumPy-Import**
> ```python
> # FEHLER: NameError: name 'np' is not defined
> koeffizienten = np.polyfit(x, y, 1)
> 
> # Lösung: import numpy as np am Anfang
> ```

> [!WARNING]
> **Fehler 4: Division durch Null bei Interpolation**
> ```python
> # Wenn fest - fest_prev == 0:
> kritisch_start = temp_prev + (380 - fest_prev) * (temp - temp_prev) / 0  # FEHLER!
> 
> # Lösung: Prüfung einbauen
> if fest != fest_prev:
>     kritisch_start = ...
> ```

---

#### Erweiterungsmöglichkeiten:

**1. Asymmetrische Fehlerbalken**:
```python
fehler_unten = [10, 12, 15, 18, 20, 25, 30, 35]
fehler_oben = [14, 18, 21, 26, 30, 35, 40, 45]
plt.errorbar(x, y, yerr=[fehler_unten, fehler_oben], ...)
```

**2. Mehrere Trendlinien (linear, quadratisch, kubisch)**:
```python
# Linear
koeff1 = np.polyfit(temperaturen, zugfestigkeit_mittel, 1)
trend1 = np.polyval(koeff1, temperaturen)

# Quadratisch
koeff2 = np.polyfit(temperaturen, zugfestigkeit_mittel, 2)
trend2 = np.polyval(koeff2, temperaturen)

plt.plot(temperaturen, trend1, 'k--', label='Linear')
plt.plot(temperaturen, trend2, 'g--', label='Quadratisch')
```

**3. Konfidenzintervall der Regression**:
```python
from scipy import stats

# Berechne 95% Konfidenzintervall
prediction_interval = 1.96 * np.std(zugfestigkeit_mittel)
plt.fill_between(temperaturen, 
                 trendlinie - prediction_interval, 
                 trendlinie + prediction_interval,
                 alpha=0.1, color='black', label='95% CI')
```

---

### Lösung P5: Lager-Vibrations-Datenanalyse (Schwer/Komplex)

**Aufgabenstellung**: Analyse von realen Vibrationsmessdaten aus CSV-Datei mit 120 Messpunkten und Visualisierung von Zustand, Schadensfaktor und Statistik.

#### Vollständige Lösung:

```python
import matplotlib.pyplot as plt

# Teil a: CSV-Datei einlesen und Daten gruppieren
datei = 'lager_vibrationsdaten.csv'
daten = {
    'Neu': {'drehzahl': [], 'amplitude': [], 'temperatur': []},
    'Leicht_verschlissen': {'drehzahl': [], 'amplitude': [], 'temperatur': []},
    'Stark_verschlissen': {'drehzahl': [], 'amplitude': [], 'temperatur': []},
    'Beschaedigt': {'drehzahl': [], 'amplitude': [], 'temperatur': []}
}

with open(datei, 'r') as f:
    next(f)  # Header überspringen
    for line in f:
        teile = line.strip().split(',')
        drehzahl, zustand, amplitude, temperatur = int(teile[0]), teile[1], float(teile[2]), float(teile[3])
        daten[zustand]['drehzahl'].append(drehzahl)
        daten[zustand]['amplitude'].append(amplitude)
        daten[zustand]['temperatur'].append(temperatur)

# Daten sortieren für saubere Plots
for zustand in daten:
    kombiniert = sorted(zip(daten[zustand]['drehzahl'], daten[zustand]['amplitude'], daten[zustand]['temperatur']))
    daten[zustand]['drehzahl'] = [k[0] for k in kombiniert]
    daten[zustand]['amplitude'] = [k[1] for k in kombiniert]
    daten[zustand]['temperatur'] = [k[2] for k in kombiniert]

# Erstelle Figure mit zwei Subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Teil b: Plot 1 - Vibrationsamplituden
farben = {'Neu': 'green', 'Leicht_verschlissen': 'yellow', 'Stark_verschlissen': 'orange', 'Beschaedigt': 'red'}
linienstile = {'Neu': '-', 'Leicht_verschlissen': '--', 'Stark_verschlissen': '-.', 'Beschaedigt': ':'}

for zustand in daten:
    ax1.plot(daten[zustand]['drehzahl'], daten[zustand]['amplitude'], 
             color=farben[zustand], linestyle=linienstile[zustand], 
             linewidth=2, marker='o', markersize=4, label=zustand.replace('_', ' '))

ax1.set_xscale('log')
ax1.set_xlabel('Drehzahl (U/min)', fontsize=12)
ax1.set_ylabel('Vibrationsamplitude (mm/s)', fontsize=12)
ax1.set_title('Lager-Vibrations-Analyse: Messdaten aus CSV', fontsize=14, fontweight='bold')
ax1.legend(loc='upper left')
ax1.grid(True, which='both', alpha=0.3)

# Teil c: Plot 2 - Schadensfaktor
neu_drehzahlen = daten['Neu']['drehzahl']
neu_amplituden = daten['Neu']['amplitude']

for zustand in ['Leicht_verschlissen', 'Stark_verschlissen', 'Beschaedigt']:
    schadensfaktoren = []
    for i, drehz in enumerate(daten[zustand]['drehzahl']):
        if drehz in neu_drehzahlen:
            idx_neu = neu_drehzahlen.index(drehz)
            faktor = daten[zustand]['amplitude'][i] / neu_amplituden[idx_neu]
            schadensfaktoren.append(faktor)
        else:
            schadensfaktoren.append(None)
    
    # Filtere None-Werte
    drehz_gefiltert = [d for d, f in zip(daten[zustand]['drehzahl'], schadensfaktoren) if f is not None]
    schaden_gefiltert = [f for f in schadensfaktoren if f is not None]
    
    ax2.plot(drehz_gefiltert, schaden_gefiltert, 
             color=farben[zustand], linestyle=linienstile[zustand], 
             linewidth=2, marker='s', markersize=4, label=zustand.replace('_', ' '))

# Kritische Schwelle
ax2.axhline(y=5, color='red', linestyle='--', linewidth=2, label='Kritische Schwelle')

ax2.set_xscale('log')
ax2.set_xlabel('Drehzahl (U/min)', fontsize=12)
ax2.set_ylabel('Schadensfaktor (relativ zu Neu-Lager)', fontsize=12)
ax2.set_title('Schadensfaktor-Entwicklung über Drehzahlbereich', fontsize=14, fontweight='bold')
ax2.legend(loc='upper left')
ax2.grid(True, which='both', alpha=0.3)

plt.tight_layout()
plt.show()

# Teil d: Statistische Auswertung
print("\n=== Statistische Auswertung ===")
for zustand in daten:
    max_ampl = max(daten[zustand]['amplitude'])
    avg_temp = sum(daten[zustand]['temperatur']) / len(daten[zustand]['temperatur'])
    print(f"Max. Amplitude {zustand.replace('_', ' ')}: {max_ampl:.2f} mm/s")
    print(f"Durchschn. Temp. {zustand.replace('_', ' ')}: {avg_temp:.1f}°C")
    print()
```

---

#### Erklärung der Lösung:

**Simulation-Konzept**

Die Simulation modelliert ein vereinfachtes Cache-Verhalten:

1. **Annahme**: Sequenzieller Array-Zugriff (beste Locality)
2. **Modell**: Wenn Array ≤ Cache-Größe → alle Zugriffe sind Cache-Hits
3. **Hit-Rate-Berechnung**: `hit_rate = cache_groesse / array_groesse` (vereinfacht)
4. **Durchschnittliche Zeit**: Gewichteter Mittelwert aus Hit- und Miss-Zeiten

**Wichtig**: Dies ist eine **vereinfachte Simulation**. Reale Caches sind komplexer (Assoziativität, Replacement Policies, Cache Lines, etc.).

---

**Die berechne_zugriffszeit()-Funktion**

```python
def berechne_zugriffszeit(array_groesse_kb, cache_groesse_kb, cache_zyklen, naechster_cache_zyklen):
    if array_groesse_kb <= cache_groesse_kb:
        return cache_zyklen
    else:
        hit_rate = cache_groesse_kb / array_groesse_kb
        miss_rate = 1 - hit_rate
        durchschnitt = hit_rate * cache_zyklen + miss_rate * naechster_cache_zyklen
        return durchschnitt
```

**Beispielrechnung**:

Array-Größe: 128 KB, L1-Cache: 64 KB, L1-Zeit: 4 Zyklen, RAM-Zeit: 100 Zyklen

1. **Array passt nicht in L1**: 128 KB > 64 KB
2. **Hit-Rate**: 64 / 128 = 0.5 (50% der Zugriffe treffen L1)
3. **Miss-Rate**: 1 - 0.5 = 0.5 (50% gehen zu RAM)
4. **Durchschnitt**: 0.5 × 4 + 0.5 × 100 = 2 + 50 = 52 Zyklen

**Interpretation**: Im Durchschnitt dauert ein Zugriff 52 Zyklen – viel besser als 100 (RAM), aber schlechter als 4 (reiner L1-Hit).

---

**Cache-Hierarchie-Simulation**

**Konfiguration 3: L1 + L2 + L3**

```python
if groesse <= L1_KB:
    zeit = L1_ZYKLEN
elif groesse <= L2_KB:
    l1_hit_rate = L1_KB / groesse
    zeit = l1_hit_rate * L1_ZYKLEN + (1 - l1_hit_rate) * L2_ZYKLEN
elif groesse <= L3_KB:
    l1_hit_rate = L1_KB / groesse
    l2_hit_rate = (L2_KB - L1_KB) / groesse
    l3_hit_rate = 1 - l1_hit_rate - l2_hit_rate
    zeit = l1_hit_rate * L1_ZYKLEN + l2_hit_rate * L2_ZYKLEN + l3_hit_rate * L3_ZYKLEN
else:
    # Array größer als L3
    l1_hit_rate = L1_KB / groesse
    l2_hit_rate = (L2_KB - L1_KB) / groesse
    l3_hit_rate = (L3_KB - L2_KB) / groesse
    ram_rate = 1 - l1_hit_rate - l2_hit_rate - l3_hit_rate
    zeit = (l1_hit_rate * L1_ZYKLEN + l2_hit_rate * L2_ZYKLEN + 
            l3_hit_rate * L3_ZYKLEN + ram_rate * RAM_ZYKLEN)
```

**Beispiel: Array-Größe 2048 KB (2 MB)**

Cache-Größen: L1=64 KB, L2=512 KB, L3=8192 KB

1. **L1 Hit-Rate**: 64 / 2048 = 0.03125 (3.125%)
2. **L2 Hit-Rate**: (512 - 64) / 2048 = 448 / 2048 = 0.21875 (21.875%)
3. **L3 Hit-Rate**: 1 - 0.03125 - 0.21875 = 0.75 (75%)
4. **RAM-Rate**: 0% (Array passt in L3)

**Durchschnittliche Zeit**:
```
Zeit = 0.03125 × 4 + 0.21875 × 12 + 0.75 × 40
     = 0.125 + 2.625 + 30
     = 32.75 Zyklen
```

**Interpretation**: Obwohl nur 3% der Zugriffe L1 treffen, ist die durchschnittliche Zeit (32.75) viel besser als RAM (100) dank L3.

---

**Subplots mit plt.subplots()**

```python
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
```

**Was ist plt.subplots()?**

Erstellt eine Figure mit mehreren Subplot-Achsen in einem Raster.

**Syntax**:
```python
fig, axes = plt.subplots(nrows, ncols, figsize=(breite, hoehe))
```

- `nrows=2, ncols=1`: 2 Zeilen, 1 Spalte (übereinander)
- `figsize=(10, 8)`: Gesamtgröße in Zoll (Breite × Höhe)
- **Rückgabe**: `fig` (Figure-Objekt), `axes` (Array oder Tupel von Axes)

**Unpacking**:
```python
fig, (ax1, ax2) = plt.subplots(2, 1)  # Zwei Plots: ax1 (oben), ax2 (unten)
fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2)  # 2×2 Grid
```

**Verwendung**:
```python
ax1.plot(...)      # Plot im ersten Subplot
ax1.set_title(...) # Titel für ersten Subplot
ax2.scatter(...)   # Plot im zweiten Subplot
```

**Unterschied zu plt.subplot()**:
```python
# Alt (einzeln):
plt.subplot(2, 1, 1)  # Aktiviert ersten Subplot
plt.plot(...)
plt.subplot(2, 1, 2)  # Aktiviert zweiten Subplot
plt.plot(...)

# Neu (alle auf einmal):
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(...)
ax2.plot(...)
```

`plt.subplots()` ist moderner und flexibler!

---

**Logarithmische X-Achse mit Basis 2**

```python
ax1.set_xscale('log', base=2)
```

**Warum Basis 2?**

Die Array-Größen sind Potenzen von 2: 1, 2, 4, 8, 16, 32, 64, 128, ..., 16384

Logarithmische Skala mit **Basis 2** bedeutet:
- Jeder "Schritt" ist eine Verdopplung
- Gleichmäßige Abstände: 1, 2, 4, 8, 16, 32, ...

**Alternative**: Basis 10 (Standard)
```python
ax1.set_xscale('log')  # Basis 10
```
Würde aber zu ungleichmäßigen Abständen führen (2, 4, 8 liegen alle zwischen 1 und 10).

**Custom Tick Labels**:
```python
ax1.set_xticks([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384])
ax1.set_xticklabels(['1', '2', '4', '8', '16', '32', '64', '128', '256', '512', 
                      '1K', '2K', '4K', '8K', '16K'], rotation=45)
```

- `set_xticks()`: Position der Tick-Marks
- `set_xticklabels()`: Text für jeden Tick (mit `rotation=45` für bessere Lesbarkeit)
- **1K = 1024 KB**: Lesbarere Darstellung für große Zahlen

---

**Speedup-Berechnung**

```python
speedup_l1_l2_l3 = [RAM_ZYKLEN / zeit for zeit in zugriffszeiten_l1_l2_l3]
```

**Speedup-Definition**:
```
Speedup = Zeit_ohne_Optimierung / Zeit_mit_Optimierung
```

**Beispiel**:
- Ohne Cache (RAM): 100 Zyklen
- Mit L1+L2+L3: 32.75 Zyklen
- Speedup: 100 / 32.75 ≈ 3.05

**Interpretation**: Mit Cache ist das Programm **3,05-mal schneller** als ohne Cache.

**Speedup-Werte**:
- **Speedup = 1**: Keine Verbesserung
- **Speedup = 2**: Doppelt so schnell
- **Speedup = 10**: 10-mal schneller
- **Speedup = 25**: 25-mal schneller (typisch für kleine Arrays in L1)

---

#### Erwartete Ausgabe:

**Plot 1 (Zugriffszeiten)**:

Charakteristische "Stufen"-Form:

```
Zeit
100 |                   ________________ (nur L1, Array > 64 KB)
    |                  |
 40 |        __________|        __________ (L1+L2+L3, Array > 8 MB)
    |       |                  |
 12 |   ____|     ____________| (L1+L2, Array > 512 KB)
    |  |         |
  4 |__|_________|________________________ (alle Konfigurationen, Array ≤ Cache)
    |_____|_____|_____|_____|_____|_____|
         64    512         8192        16384 KB
        L1     L2           L3
```

**Beobachtungen**:
- **Bis 64 KB**: Alle Konfigurationen gleich gut (4 Zyklen)
- **64-512 KB**: Nur L1 verschlechtert sich drastisch; L1+L2 bleibt gut
- **512-8192 KB**: Nur L1+L2+L3 bleibt effizient
- **Ab 8192 KB**: Alle Konfigurationen verschlechtern sich

---

**Plot 2 (Speedup)**:

```
Speedup
 25 |_____________________ (Kleine Arrays: 25× schneller mit L1)
    |                    \
 10 |                     \________ (Mittlere Arrays: L1+L2+L3)
    |                              \
  2 |                               \________ (Große Arrays: L3 hilft noch)
    |                                        \
  1 |________________________________________\______ (Sehr große Arrays: wenig Vorteil)
    |_____|_____|_____|_____|_____|_____|
         64    512         8192        16384 KB
```

**Beobachtungen**:
- **Kleine Arrays (≤ 64 KB)**: Speedup = 25× (100/4)
- **Mittlere Arrays**: Speedup sinkt graduell
- **Große Arrays (> L3)**: Speedup ≈ 1-2× (Cache hilft wenig)

---

#### Interpretation der Ergebnisse:

**1. Cache-Hierarchie ist essentiell**

Ohne L2 und L3 wäre die Performance katastrophal bei größeren Datenstrukturen.

**2. Working Set Size ist kritisch**

Programme sollten ihre Datenstrukturen so designen, dass sie in L1 oder L2 passen:
- **L1 (64 KB)**: 8.000 Integers (int32) oder 8.000 Floats (float32)
- **L2 (512 KB)**: 64.000 Integers
- **L3 (8 MB)**: 1 Million Integers

**3. Cache-Friendly-Programmierung**

```python
# SCHLECHT: Random Access (Cache-Misses)
for i in random_indices:
    result += large_array[i]

# GUT: Sequential Access (Cache-Hits)
for i in range(len(large_array)):
    result += large_array[i]
```

**4. Memory-Bound vs. Compute-Bound**

- **Compute-Bound**: CPU wartet nicht auf Speicher → schnellere CPU hilft
- **Memory-Bound**: CPU wartet ständig auf RAM → Cache-Optimierung essentiell

---

#### Häufige Fehler:

> [!WARNING]
> **Fehler 1: plt.subplots() vs. plt.subplot()**
> ```python
> # FALSCH: Mixing
> fig, (ax1, ax2) = plt.subplots(2, 1)
> plt.plot(...)  # Zeichnet NICHT in ax1!
> 
> # RICHTIG:
> fig, (ax1, ax2) = plt.subplots(2, 1)
> ax1.plot(...)  # Explizit ax1 verwenden
> ```

> [!WARNING]
> **Fehler 2: Division durch Null bei kleinen Arrays**
> ```python
> # Wenn array_groesse_kb = 0:
> hit_rate = cache_groesse_kb / 0  # FEHLER!
> 
> # Lösung: Eingabe validieren
> if array_groesse_kb <= 0:
>     return 0
> ```

> [!WARNING]
> **Fehler 3: Falsche Hit-Rate-Berechnung bei Hierarchien**
> ```python
> # FALSCH: L2-Hit-Rate berücksichtigt nicht L1
> l2_hit_rate = L2_KB / groesse
> 
> # RICHTIG: L2 enthält nur zusätzliche Daten
> l2_hit_rate = (L2_KB - L1_KB) / groesse
> ```

> [!WARNING]
> **Fehler 4: Vergessen, tight_layout() zu callen**
> Ohne `tight_layout()` können sich Subplots überlappen oder Beschriftungen abgeschnitten werden.

---

#### Erweiterungsmöglichkeiten:

**1. Cache Line Effects berücksichtigen**:
```python
CACHE_LINE_BYTES = 64
BYTES_PER_ELEMENT = 8  # Float64

# Bei sequenziellem Zugriff wird eine ganze Cache Line geladen
elemente_pro_line = CACHE_LINE_BYTES / BYTES_PER_ELEMENT  # 8 Elemente

# Effektive Zugriffe reduzieren sich
effektive_zugriffe = array_groesse_kb * 1024 / CACHE_LINE_BYTES
```

**2. Verschiedene Access-Patterns**:
```python
# Sequential: Beste Locality
# Strided: Mittlere Locality (z.B. jede 2. Element)
# Random: Schlechteste Locality

stride = 2  # Jedes zweite Element
hit_rate_strided = hit_rate / stride
```

**3. Multi-Core-Simulation**:
```python
# L1 und L2 sind pro Core, L3 ist shared
# Bei 4 Cores konkurrieren sie um L3-Bandbreite
l3_contention_factor = num_cores * 0.8
zeit_l3_multicore = L3_ZYKLEN * l3_contention_factor
```

**4. Animierte Visualisierung**:
```python
from matplotlib.animation import FuncAnimation

# Zeige, wie sich Cache-Inhalte über Zeit ändern
def animate(frame):
    # Update Cache-Zustand
    ax.clear()
    # Zeichne aktuellen Cache-Inhalt
```

---

#### Zusammenfassung der Aufgabe:

Diese Aufgabe demonstriert:
1. **Komplexe Simulationen** mit Python
2. **Hierarchische Systeme** modellieren
3. **Multi-Plot-Layouts** mit Subplots
4. **Logarithmische Skalierung** für große Wertebereiche
5. **Performance-Analyse** von Hardware-Architekturen
6. **Datenvisualisierung** als Analysetool

**Praktischer Nutzen**: Hilft zu verstehen, warum Cache-freundlicher Code so wichtig ist und wie sich verschiedene Array-Größen auf die Performance auswirken.

---


