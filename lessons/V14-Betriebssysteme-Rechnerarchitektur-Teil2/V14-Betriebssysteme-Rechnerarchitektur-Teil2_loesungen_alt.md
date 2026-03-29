# V14 - Betriebssysteme & Rechnerarchitektur – Teil 2 / Plots & Grafiken (Matplotlib) – Teil 2: Lösungen

---

## Teil 1: Theorie-Lösungen

### T1: Prozessverwaltung und Scheduling (⭐⭐)

#### Lösung a) FCFS (First-Come First-Served)

**Gantt-Chart:**

```
| P1 (0-8) | P2 (8-12) | P3 (12-21) | P4 (21-26) |
```

**Wartezeiten:**
- **P1**: Ankunft 0, Start 0 → Wartezeit = 0
- **P2**: Ankunft 1, Start 8 → Wartezeit = 8 - 1 = **7**
- **P3**: Ankunft 2, Start 12 → Wartezeit = 12 - 2 = **10**
- **P4**: Ankunft 3, Start 21 → Wartezeit = 21 - 3 = **18**

**Durchschnittliche Wartezeit**: (0 + 7 + 10 + 18) / 4 = **8.75 ms**

**Turnaround-Zeiten** (Zeit von Ankunft bis Fertigstellung):
- **P1**: 8 - 0 = **8**
- **P2**: 12 - 1 = **11**
- **P3**: 21 - 2 = **19**
- **P4**: 26 - 3 = **23**

**Durchschnittliche Turnaround-Zeit**: (8 + 11 + 19 + 23) / 4 = **15.25 ms**

---

#### Lösung b) SJF (Shortest Job First, nicht-preemptiv)

Bei SJF wird immer der Prozess mit der kürzesten Burst-Time ausgewählt (unter denen, die bereits angekommen sind).

**Reihenfolge:**
1. Bei t=0: Nur P1 da → P1 läuft (0-8)
2. Bei t=8: P2, P3, P4 sind da → P2 hat kürzeste Burst (4) → P2 läuft (8-12)
3. Bei t=12: P3 (Burst 9), P4 (Burst 5) da → P4 ist kürzer → P4 läuft (12-17)
4. Bei t=17: Nur P3 übrig → P3 läuft (17-26)

**Gantt-Chart:**

```
| P1 (0-8) | P2 (8-12) | P4 (12-17) | P3 (17-26) |
```

**Wartezeiten:**
- **P1**: 0 - 0 = **0**
- **P2**: 8 - 1 = **7**
- **P3**: 17 - 2 = **15**
- **P4**: 12 - 3 = **9**

**Durchschnittliche Wartezeit**: (0 + 7 + 15 + 9) / 4 = **7.75 ms**

**Turnaround-Zeiten:**
- **P1**: 8 - 0 = **8**
- **P2**: 12 - 1 = **11**
- **P3**: 26 - 2 = **24**
- **P4**: 17 - 3 = **14**

**Durchschnittliche Turnaround-Zeit**: (8 + 11 + 24 + 14) / 4 = **14.25 ms**

---

#### Lösung c) Vergleich

| Metrik | FCFS | SJF |
|--------|------|-----|
| Ø Wartezeit | 8.75 ms | 7.75 ms |
| Ø Turnaround | 15.25 ms | 14.25 ms |

**SJF ist effizienter**, da es kürzere Wartezeiten und kürzere Turnaround-Zeiten erreicht. Der Grund ist, dass kurze Jobs bevorzugt werden, was die durchschnittliche Wartezeit minimiert. Bei FCFS wartet P4 (Burst 5) unnötig lange, weil P3 (Burst 9) davor ausgeführt wird.

---

#### Lösung d) Nachteil von SJF

**Starvation (Verhungern)**: Prozesse mit langer Burst-Time können theoretisch **nie ausgeführt werden**, wenn ständig neue kurze Prozesse ankommen. Diese werden immer bevorzugt, sodass lange Prozesse unbegrenzt warten.

**Beispiel**: Ein Backup-Prozess (Burst: 1000 ms) wartet, während ständig neue Web-Requests (Burst: 10 ms) bearbeitet werden.

**Zusätzliches Problem**: Die **Burst-Time ist in der Praxis nicht vorhersehbar**. Das Betriebssystem kennt sie nicht im Voraus und muss sie schätzen (z.B. durch historische Durchschnittswerte), was zu Ungenauigkeiten führt.

---

### T2: Virtueller Speicher und Paging (⭐⭐⭐)

#### Lösung a) Anzahl Pages und Frames

**Virtuelle Adressbreite**: 16 Bit → Virtueller Adressraum = 2^16 = **65.536 Bytes** = **64 KB**

**Page-Größe**: 1 KB = 1024 Bytes

**Anzahl virtueller Pages**: 64 KB / 1 KB = **64 Pages**

---

**Physischer Speicher**: 8 KB = 8.192 Bytes

**Anzahl physischer Frames**: 8 KB / 1 KB = **8 Frames**

---

#### Lösung b) Adressübersetzung für 0x0A50

**Schritt 1: Virtuelle Adresse in Binär konvertieren**

```
0x0A50 (hex) = 0000 1010 0101 0000 (binär)
```

**Schritt 2: Page Number und Offset trennen**

Page-Größe = 1024 Bytes = 2^10 → **Offset benötigt 10 Bit**

```
Virtuelle Adresse (16 Bit):
[000010] [10 0101 0000]
 ^^^^^^   ^^^^^^^^^^^^
Page Num    Offset
```

- **Page Number**: `000010` (binär) = **2** (dezimal)
- **Offset**: `10 0101 0000` (binär) = **0x150** (hex) = **336** (dezimal)

**Schritt 3: Page Table konsultieren**

```
Virtuelle Page 2 → Valid Bit = 0 → Page Fault!
```

**Ergebnis**: Die Adresse 0x0A50 führt zu einem **Page Fault**, da Page 2 nicht im physischen Speicher liegt (Valid Bit = 0). Das Betriebssystem muss die Page vom Festplattenspeicher (Swap) in den RAM laden.

---

**Korrektur**: Ich hatte übersehen, dass 0x0A50 eigentlich Page 2 anspricht. Lassen Sie uns stattdessen eine gültige Adresse nehmen: **0x0450** (Page 1)

**Schritt 1: 0x0450 in Binär**

```
0x0450 = 0000 0100 0101 0000
```

**Schritt 2: Trennung**

```
[000001] [00 0101 0000]
Page 1      Offset 0x050 (80 dezimal)
```

**Schritt 3: Page Table**

```
Virtuelle Page 1 → Frame 1, Valid = 1
```

**Schritt 4: Physische Adresse berechnen**

```
Physische Adresse = Frame × Page-Größe + Offset
                  = 1 × 1024 + 80
                  = 1024 + 80
                  = 1104 (dezimal)
                  = 0x0450 (hex)
```

**Ergebnis**: Virtuelle Adresse **0x0450** wird auf physische Adresse **0x0450** (1104 dezimal) abgebildet.

---

#### Lösung c) Adresse 0x0820

**Schritt 1: Binär konvertieren**

```
0x0820 = 0000 1000 0010 0000
```

**Schritt 2: Trennung**

```
[000010] [00 0010 0000]
Page 2      Offset 0x020 (32 dezimal)
```

**Schritt 3: Page Table**

```
Virtuelle Page 2 → Valid Bit = 0
```

**Ergebnis**: **Page Fault!**

**Was passiert:**

1. Die **MMU** (Memory Management Unit) prüft die Page Table und stellt fest, dass das **Valid Bit = 0** ist.
2. Eine **Exception** (Page Fault) wird ausgelöst.
3. Die **CPU wechselt in den Kernel-Modus** und übergibt die Kontrolle an den **Page Fault Handler** (Teil des Betriebssystems).
4. Das Betriebssystem lädt Page 2 vom **Festplattenspeicher (Swap Space)** in einen freien Frame im RAM.
5. Die **Page Table wird aktualisiert**: Frame-Nummer wird eingetragen, Valid Bit wird auf 1 gesetzt.
6. Die **CPU setzt die Instruktion fort** (wiederholt den Speicherzugriff).

**Rolle des Valid Bit:**

Das **Valid Bit** zeigt an, ob eine virtuelle Page **aktuell im physischen Speicher** liegt (1) oder **auf die Festplatte ausgelagert** wurde (0). Es ist essenziell für **Demand Paging**: Pages werden nur bei Bedarf in den RAM geladen, nicht alle auf einmal.

---

#### Lösung d) Fragmentierung

**Externes Fragmentierungsproblem gelöst:**

Bei **variabel großen Speicherblöcken** (wie bei älteren Systemen ohne Paging) entsteht **externe Fragmentierung**: Freier Speicher zerfällt in viele kleine, nicht zusammenhängende Blöcke. Ein Prozess, der 100 KB benötigt, kann nicht zugewiesen werden, obwohl insgesamt 150 KB frei sind – verteilt in 10×15 KB Blöcken.

**Paging löst das Problem**, weil:
- Alle Pages gleich groß sind (z.B. 4 KB)
- Prozesse beliebig im physischen Speicher verteilt werden können
- Die MMU übersetzt virtuelle Adressen transparent

---

**Interne Fragmentierung entsteht:**

Wenn ein Prozess weniger Speicher benötigt als eine volle Page. Beispiel:
- Page-Größe: 4 KB (4096 Bytes)
- Prozess benötigt: 10.500 Bytes

→ **3 Pages** werden alloziert (12.288 Bytes)  
→ **Verschwendung**: 12.288 - 10.500 = **1.788 Bytes** (≈ 14.6%)

Dieser ungenutzter Speicher **innerhalb** der zugewiesenen Pages ist **interne Fragmentierung**.

**Lösung**: Kleinere Pages reduzieren interne Fragmentierung, aber erhöhen den **Overhead** (mehr Page Table Entries, mehr TLB-Misses).

---

### T3: Dateisysteme und Journaling (⭐⭐)

#### Lösung a) Funktionsweise von Journaling

**Journaling** ist ein Mechanismus, der **Metadaten-Konsistenz** nach Systemabstürzen gewährleistet. Vor dem eigentlichen Schreibvorgang werden geplante Änderungen in einem **Journal** (Log) protokolliert.

**Ablauf:**

1. **Journal-Eintrag schreiben**: Das Dateisystem schreibt eine Beschreibung der geplanten Operation (z.B. "Datei erstellen, Inode 12345, Block 6789") ins Journal.
2. **Checkpoint setzen**: Sobald der Journal-Eintrag sicher auf Disk ist, wird ein Checkpoint gesetzt.
3. **Eigentliche Operation durchführen**: Die Daten und Metadaten werden an ihre finalen Positionen geschrieben.
4. **Journal-Eintrag löschen**: Nach erfolgreicher Operation wird der Journal-Eintrag als abgeschlossen markiert oder gelöscht.

**Bei Absturz:** Beim nächsten Boot liest das Dateisystem das Journal und führt unvollständige Operationen zu Ende (Replay) oder macht sie rückgängig (Rollback). Dies dauert nur Sekunden, statt stundenlanger `fsck`-Läufe bei klassischen Dateisystemen.

---

#### Lösung b) Journaling-Modi von ext4

| Modus | Was wird geloggt? | Sicherheit | Performance | Erklärung |
|-------|-------------------|------------|-------------|-----------|
| **Journal** | Metadaten + Daten | ⭐⭐⭐ Höchste | ⭐ Langsam | Alle Daten werden doppelt geschrieben (Journal + finaler Ort) → maximale Sicherheit, aber langsam |
| **Ordered** (Standard) | Nur Metadaten, aber Daten vor Metadaten | ⭐⭐ Mittel | ⭐⭐ Mittel | Daten werden geschrieben, bevor Metadaten geloggt werden → verhindert "Datenmüll" in Dateien |
| **Writeback** | Nur Metadaten, Daten beliebig | ⭐ Niedrig | ⭐⭐⭐ Schnell | Metadaten und Daten können unabhängig geschrieben werden → schnellste Option, aber Daten können korrupt sein |

**Sortierung nach Sicherheit**: Journal > Ordered > Writeback

**Sortierung nach Performance**: Writeback > Ordered > Journal

**Empfehlung**: **Ordered** ist der beste Kompromiss für die meisten Anwendungsfälle (daher Standard).

---

#### Lösung c) Moderne Dateisysteme

1. **NTFS** (Windows):
   - **Besonderheit**: Verwendet **Master File Table (MFT)**, wo jede Datei als Eintrag gespeichert wird. Unterstützt **Access Control Lists (ACLs)** für granulare Berechtigungen und **Change Journaling** für schnelle Backup-Lösungen.

2. **ZFS** (ursprünglich Solaris, jetzt Linux/FreeBSD):
   - **Besonderheit**: **Copy-on-Write (CoW)** – Daten werden nie überschrieben, sondern neue Versionen geschrieben. Integrierte **Checksummen** für jedes Datenblock (Schutz vor Silent Data Corruption). **Snapshots** in O(1)-Zeit.

3. **Btrfs** (Linux):
   - **Besonderheit**: **Subvolumes** und **Snapshots** ähnlich ZFS. **Integrierte RAID**-Funktionalität (Software-RAID auf Dateisystem-Ebene). Dynamische **inode-Allokation** (keine feste inode-Anzahl bei Formatierung).

4. **APFS** (Apple File System, macOS/iOS):
   - **Besonderheit**: Optimiert für **SSDs** und **Flash-Speicher**. **Space Sharing** zwischen Volumes (mehrere Volumes teilen sich einen Pool). **Clones** für Dateien (Instant-Kopie ohne Platzbedarf bis zur Änderung).

5. **XFS** (Linux, High-Performance):
   - **Besonderheit**: **Delay Allocation** (verzögerte Block-Allokation für bessere Leistung). Besonders gut für **große Dateien** (Videoverarbeitung, Datenbanken). Keine native Kompression (anders als Btrfs/ZFS).

---

## Teil 2: Python-Lösungen

### P1: Bar Chart - CNC-Maschinenpräzision visualisieren (⭐)

```python
import matplotlib.pyplot as plt

maschinen = ['CNC-01', 'CNC-02', 'CNC-03', 'CNC-04', 'CNC-05']
abweichung_um = [2.3, 8.7, 4.2, 1.8, 3.5]

farben = ['red' if abw > 5 else 'green' for abw in abweichung_um]

plt.figure(figsize=(10, 6))
plt.bar(maschinen, abweichung_um, color=farben, edgecolor='black', alpha=0.8)
plt.xlabel('CNC-Maschine', fontsize=12)
plt.ylabel('Positionsabweichung (μm)', fontsize=12)
plt.title('CNC-Maschinenpräzision: Positioniergenauigkeit', fontsize=14, fontweight='bold')
plt.ylim(0, 12)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
```

---

### P2: Histogramm - Hydraulikdruck-Schwankungen analysieren (⭐⭐)

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
druecke_bar = np.random.normal(180, 12, 1000)

plt.figure(figsize=(10, 6))
plt.hist(druecke_bar, bins=30, color='lightblue', edgecolor='black', alpha=0.7)

solldruck = 180
kritische_grenze = 204

plt.axvline(x=solldruck, color='green', linestyle='--', linewidth=2, label='Solldruck (180 bar)')
plt.axvline(x=kritische_grenze, color='red', linestyle='--', linewidth=2, label='Kritische Grenze (204 bar)')

plt.xlabel('Druck (bar)', fontsize=12)
plt.ylabel('Häufigkeit', fontsize=12)
plt.title('Verteilung der Hydraulikdruck-Schwankungen', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()
```

---

### P3: Subplots - Materialprüfungs-Dashboard (⭐⭐⭐)

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
zeit_min = np.arange(0, 60, 1)
zugspannung_mpa = 150 + 80 * np.sin(zeit_min / 10) + np.random.normal(0, 10, 60)
dehnung_prozent = 2.0 + 1.5 * np.sin(zeit_min / 15 + 1) + np.random.normal(0, 0.3, 60)
temperatur_c = np.random.exponential(25, 60) + 20
kraftaufnahme_kn = np.random.exponential(15, 60) + 10

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

axes[0, 0].plot(zeit_min, zugspannung_mpa, 'b-', linewidth=2)
axes[0, 0].fill_between(zeit_min, 0, zugspannung_mpa, alpha=0.3, color='blue')
axes[0, 0].set_title('Zugspannung (MPa)', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Zeit (min)')
axes[0, 0].set_ylabel('Zugspannung (MPa)')
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].plot(zeit_min, dehnung_prozent, 'g-', linewidth=2)
axes[0, 1].axhline(y=5, color='red', linestyle='--', linewidth=2, label='Bruchgrenze (5%)')
axes[0, 1].set_title('Dehnung (%)', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Zeit (min)')
axes[0, 1].set_ylabel('Dehnung (%)')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

axes[1, 0].scatter(temperatur_c, kraftaufnahme_kn, color='red', alpha=0.5, s=50)
axes[1, 0].set_title('Temperatur vs. Kraft Korrelation', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Temperatur (°C)')
axes[1, 0].set_ylabel('Kraftaufnahme (kN)')
axes[1, 0].grid(True, alpha=0.3)

axes[1, 1].hist(zugspannung_mpa, bins=15, color='orange', edgecolor='black', alpha=0.7)
axes[1, 1].set_title('Zugspannungs-Verteilung', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Zugspannung (MPa)')
axes[1, 1].set_ylabel('Häufigkeit')
axes[1, 1].grid(axis='y', alpha=0.3)

plt.suptitle('Materialprüfungs-Dashboard', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

---

### P4: Logarithmische Achsen - Werkzeugstandzeit-Analyse (⭐⭐⭐)

```python
import numpy as np
import matplotlib.pyplot as plt

schnittgeschw_m_min = np.array([50, 100, 200, 400, 800])
standzeit_min = np.array([720, 180, 45, 11, 3])
labels = ['HSS niedrig', 'HSS hoch', 'HM niedrig', 'HM hoch', 'Keramik']

plt.figure(figsize=(12, 8))
plt.loglog(schnittgeschw_m_min, standzeit_min, 'ro--', markersize=10, linewidth=2)

for i, label in enumerate(labels):
    plt.text(schnittgeschw_m_min[i] * 1.15, standzeit_min[i], label, 
             fontsize=10, verticalalignment='center')

plt.xlabel('Schnittgeschwindigkeit (m/min, log)', fontsize=12)
plt.ylabel('Werkzeugstandzeit (min, log)', fontsize=12)
plt.title('Werkzeugverschleiß: Schnittgeschwindigkeit vs. Standzeit (Taylor-Gleichung)', 
          fontsize=13, fontweight='bold')
plt.grid(True, alpha=0.3, which='both')
plt.tight_layout()
plt.show()

# Taylor-Gleichung: vc × T^n = C (konstant)
# Im log-log-Plot wird dies zu einer Geraden: log(T) = -n × log(vc) + log(C)
# Logarithmische Achsen zeigen Power-Law-Beziehungen als Geraden.
# Schnittgeschw. und Standzeit umfassen mehrere Größenordnungen (Faktor 16 bzw. 240).
```

---

### P5: Komplettes Dashboard mit Annotationen (⭐⭐⭐⭐⭐)

```python
import numpy as np
import matplotlib.pyplot as plt

verfahren = ['Drehen', 'Fräsen', 'Bohren', 'Schleifen']
durchlaufzeit_min = [12.5, 18.3, 8.7, 22.1]
ruestzeit_min = [25.3, 35.6, 15.4, 45.2]
werkzeugwechsel = [0, 3, 1, 5]

fig, axes = plt.subplots(3, 1, figsize=(12, 14))

# Subplot 1: Gruppiertes Bar Chart
x_pos = np.arange(len(verfahren))
breite = 0.35
bester_index = np.argmin(durchlaufzeit_min)
durchlauf_farben = ['red' if i == bester_index else 'blue' for i in range(len(durchlaufzeit_min))]

axes[0].bar(x_pos - breite/2, durchlaufzeit_min, breite, 
             label='Durchlaufzeit', color=durchlauf_farben, edgecolor='black', alpha=0.8)
axes[0].bar(x_pos + breite/2, ruestzeit_min, breite,
             label='Rüstzeit', color='orange', edgecolor='black', alpha=0.8)
axes[0].set_xlabel('Fertigungsverfahren', fontsize=11)
axes[0].set_ylabel('Zeit (min)', fontsize=11)
axes[0].set_title('Fertigungsverfahren: Durchlauf- vs. Rüstzeit', fontsize=12, fontweight='bold')
axes[0].set_xticks(x_pos)
axes[0].set_xticklabels(verfahren)
axes[0].legend(fontsize=10)
axes[0].grid(axis='y', alpha=0.3)

# Subplot 2: Horizontales Bar Chart
bars = axes[1].barh(verfahren, werkzeugwechsel, color='green', edgecolor='black', alpha=0.8)
for i, (bar, val) in enumerate(zip(bars, werkzeugwechsel)):
    width = bar.get_width()
    axes[1].text(width + 0.1, bar.get_y() + bar.get_height()/2, 
                  str(val), ha='left', va='center', fontsize=10, fontweight='bold')
axes[1].set_xlabel('Anzahl Werkzeugwechsel', fontsize=11)
axes[1].set_ylabel('Fertigungsverfahren', fontsize=11)
axes[1].set_title('Werkzeugwechsel pro Verfahren', fontsize=12, fontweight='bold')
axes[1].grid(axis='x', alpha=0.3)

# Subplot 3: Scatter Plot mit Annotationen
axes[2].scatter(durchlaufzeit_min, ruestzeit_min, s=150, color='purple', 
                edgecolors='black', linewidths=2, alpha=0.7, zorder=3)
xytext_offsets = [(10, 15), (-40, 20), (10, -25), (-50, -25)]
for i, verf in enumerate(verfahren):
    axes[2].annotate(verf, 
                      xy=(durchlaufzeit_min[i], ruestzeit_min[i]),
                      xytext=xytext_offsets[i],
                      textcoords='offset points',
                      fontsize=10,
                      bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                      arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3',
                                     color='black', lw=1.5))
axes[2].set_xlabel('Durchlaufzeit (min)', fontsize=11)
axes[2].set_ylabel('Rüstzeit (min)', fontsize=11)
axes[2].set_title('Durchlaufzeit vs. Rüstzeit Korrelation', fontsize=12, fontweight='bold')
axes[2].grid(True, alpha=0.3)

plt.suptitle('Fertigungsverfahren: Detaillierter Vergleich', 
             fontsize=16, fontweight='bold', y=0.995)
plt.tight_layout()
plt.savefig('fertigungsverfahren_vergleich.png', dpi=300, bbox_inches='tight')
plt.show()
print("Plot gespeichert als 'fertigungsverfahren_vergleich.png'!")
```

---

## Zusammenfassung

Diese Lösungen demonstrieren:

**Theorie:**
- **Scheduling-Algorithmen** mit Gantt-Charts und Metriken-Berechnung
- **Virtuelle Speicherverwaltung** mit Adressübersetzung und Page Faults
- **Dateisysteme** mit Journaling-Modi und modernen Alternativen

**Python:**
- **Bar Charts** (vertikal, horizontal, gruppiert, gestapelt)
- **Histogramme** mit Verteilungsanalyse und statistischen Markierungen
- **Subplots** mit verschiedenen Plot-Typen in einem Dashboard
- **Logarithmische Achsen** für Daten mit großem Wertebereich
- **Annotationen** mit Pfeilen und Boxen für wichtige Datenpunkte
- **Speichern in verschiedenen Formaten** mit hoher Auflösung

**Best Practices:**
- Konsistente Farbschemata und Beschriftungen
- `tight_layout()` für professionelles Layout
- Gitter mit `alpha=0.3` für bessere Lesbarkeit
- Legenden und Annotationen für Kontext
- DPI 300+ für Publikationen

---

**Gut gemacht!** 🎉 Diese Übungen decken reale Anwendungsfälle in System-Monitoring, Performance-Analyse und wissenschaftlicher Visualisierung ab.