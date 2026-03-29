# V16: Lösungen - Netzwerktechnik Grundlagen & Protokolle Teil 2

> [!WARNING]
> Versuche die Aufgaben zuerst selbstständig zu lösen, bevor du die Lösungen ansiehst!

---

## Python-Lösungen

### Lösung P1: Pandas-Grundlagen - Sensordaten einlesen

**Lösung** (`sensordaten_grundlagen.py`):

```python
import pandas as pd

# a) CSV erstellen (manuell oder mit Python)
csv_content = """Sensor_ID,Maschine,Typ,Wert,Einheit,Timestamp,Status
S001,CNC-01,Temperatur,85.5,°C,2024-01-15 08:00:00,Normal
S002,CNC-01,Drehzahl,2500,RPM,2024-01-15 08:00:00,Normal
S003,Presse-01,Druck,150.2,bar,2024-01-15 08:00:00,Normal
S004,Presse-01,Temperatur,105.8,°C,2024-01-15 08:00:00,Warnung
S005,CNC-02,Temperatur,72.3,°C,2024-01-15 08:00:00,Normal
S006,CNC-02,Drehzahl,3200,RPM,2024-01-15 08:00:00,Normal
S007,Presse-02,Druck,142.5,bar,2024-01-15 08:00:00,Normal
S008,Presse-02,Temperatur,98.1,°C,2024-01-15 08:00:00,Normal"""

with open('sensoren_daten.csv', 'w') as f:
    f.write(csv_content)

# b) CSV einlesen
df = pd.read_csv('sensoren_daten.csv')

# c) Erste 3 Zeilen
print("Erste 3 Zeilen:")
print(df.head(3))

# d) Detaillierte Informationen
print("\nDataFrame Info:")
print(df.info())

# e) Deskriptive Statistiken
print("\nDeskriptive Statistiken:")
print(df.describe())

# f) Zeilen und Spalten
print(f"\nShape: {df.shape} (Zeilen: {df.shape[0]}, Spalten: {df.shape[1]})")

# g) Spaltennamen
print(f"\nSpaltennamen: {list(df.columns)}")

# h) Timestamp konvertieren
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
print(f"\nDatentyp Timestamp: {df['Timestamp'].dtype}")
```

**Erklärung**: Grundlegende Pandas-Operationen zum Laden und Inspizieren von DataFrames. `pd.to_datetime()` konvertiert Strings zu Datetime-Objekten.

---

### Lösung P2: Qualitätskontrolle - Filtern und Sortieren (25 lines)

```python
import pandas as pd

df = pd.read_csv('sensoren_daten.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# a) Filter: Maschine CNC-01
print("Sensoren von CNC-01:")
print(df[df['Maschine'] == 'CNC-01'])

# b) Filter: Wert > 100
print("\nWert > 100:")
print(df[df['Wert'] > 100])

# c) Filter: Temperatur 70-90°C
temp_filter = (df['Typ'] == 'Temperatur') & (df['Wert'] >= 70) & (df['Wert'] <= 90)
print("\nTemperatur 70-90°C:")
print(df[temp_filter])

# d) Kombinierter Filter: Druck > 145 bar
druck_filter = (df['Typ'] == 'Druck') & (df['Wert'] > 145)
print("\nDruck > 145 bar:")
print(df[druck_filter])

# e) Filter mit isin: CNC-01 oder CNC-02
print("\nCNC-Maschinen:")
print(df[df['Maschine'].isin(['CNC-01', 'CNC-02'])])

# f) Sortierung nach Wert (absteigend)
print("\nSortiert nach Wert (absteigend):")
print(df.sort_values('Wert', ascending=False))

# g) Sortierung nach Maschine und Wert
print("\nSortiert nach Maschine, dann Wert:")
print(df.sort_values(['Maschine', 'Wert'], ascending=[True, False]))

# h) Qualitätskontrolle: Warnungen
print("\nWarnungen (sortiert nach Wert):")
print(df[df['Status'] == 'Warnung'].sort_values('Wert', ascending=False))
```

**Erklärung**: Filterung mit Boolean-Indexing. Kombinierte Bedingungen mit `&` (und) und `|` (oder). Sortierung mit `sort_values()`.

---

### Lösung P3: Wartungsplanung - Aggregation (30 lines)

```python
import pandas as pd

df = pd.read_csv('sensoren_daten.csv')

# Zusätzliche Zeilen hinzufügen
zusatz = pd.DataFrame([
    ['S009', 'CNC-01', 'Schwingung', 0.8, 'mm/s', '2024-01-15 08:00:00', 'Normal'],
    ['S010', 'Presse-01', 'Schwingung', 1.2, 'mm/s', '2024-01-15 08:00:00', 'Warnung'],
    ['S011', 'CNC-02', 'Schwingung', 0.5, 'mm/s', '2024-01-15 08:00:00', 'Normal'],
    ['S012', 'Presse-02', 'Schwingung', 0.9, 'mm/s', '2024-01-15 08:00:00', 'Normal']
], columns=df.columns)
df = pd.concat([df, zusatz], ignore_index=True)

# a) Durchschnittlicher Wert
print(f"Durchschnittlicher Wert: {df['Wert'].mean():.2f}")

# b) Durchschnitt pro Maschine
print("\nDurchschnitt pro Maschine:")
print(df.groupby('Maschine')['Wert'].mean())

# c) Höchster Wert pro Maschine
print("\nHöchster Wert pro Maschine:")
print(df.groupby('Maschine')['Wert'].max())

# d) Sensoren pro Maschine
print("\nSensoren pro Maschine:")
print(df.groupby('Maschine').size())

# e) Wartungsübersicht
wartung = df.groupby('Maschine').agg({
    'Sensor_ID': 'count',
    'Wert': ['mean', 'min', 'max'],
    'Status': lambda x: (x == 'Warnung').sum()
})
wartung.columns = ['Anzahl_Sensoren', 'Avg_Wert', 'Min_Wert', 'Max_Wert', 'Anzahl_Warnungen']
print("\nWartungsübersicht:")
print(wartung)

# f) Maschine mit meisten Warnungen
print(f"\nMaschine mit meisten Warnungen: {wartung['Anzahl_Warnungen'].idxmax()}")

# g) Bonus: Durchschnittstemperatur > 80°C
temp_df = df[df['Typ'] == 'Temperatur']
avg_temp = temp_df.groupby('Maschine')['Wert'].mean()
print("\nMaschinen mit Durchschnittstemperatur > 80°C:")
print(avg_temp[avg_temp > 80])
```

**Erklärung**: `groupby()` gruppiert Daten nach Spalten. `agg()` wendet mehrere Aggregationsfunktionen an. Lambda-Funktionen für custom Aggregationen.

---

### Lösung P4: Performance-Optimierung (35 lines)

```python
import pandas as pd
import numpy as np
import time

# a) DataFrame erstellen
n = 100000
df = pd.DataFrame({
    'Maschine_ID': np.random.randint(1, 51, n),
    'Zykluszeit_s': np.random.randint(10, 121, n),
    'Ausschuss': np.random.randint(0, 6, n)
})

# b) Methode 1: Schleife (LANGSAM)
start_time = time.time()
netto_schleife = []
for idx, row in df.iterrows():
    netto = (row['Zykluszeit_s'] * (100 - row['Ausschuss'])) / 100
    netto_schleife.append(netto)
df['Netto_Schleife'] = netto_schleife
zeit_schleife = time.time() - start_time
print(f"Schleife: {zeit_schleife:.4f} Sekunden")

# c) Methode 2: Vektorisierung (SCHNELL)
start_time = time.time()
df['Netto_Vektorisiert'] = (df['Zykluszeit_s'] * (100 - df['Ausschuss'])) / 100
zeit_vektorisiert = time.time() - start_time
print(f"Vektorisiert: {zeit_vektorisiert:.4f} Sekunden")

# d) Faktor-Vergleich
faktor = zeit_schleife / zeit_vektorisiert
print(f"\nVektorisierung ist {faktor:.1f}x schneller!")

# e) Erklärung
print("\nWarum ist Vektorisierung schneller?")
print("Pandas/NumPy führt Operationen in C-Code auf optimierten Arrays aus.")
print("Schleifen nutzen langsamen Python-Bytecode und prüfen jeden Wert einzeln.")
print("Vektorisierung vermeidet Python-Overhead durch Batch-Verarbeitung.")

# f) Bonus: Durchschnitt pro Maschine
avg_netto = df.groupby('Maschine_ID')['Netto_Vektorisiert'].mean()
beste_maschine = avg_netto.idxmax()
print(f"\nEffizienteste Maschine: {beste_maschine} mit {avg_netto[beste_maschine]:.2f}s Netto-Zykluszeit")
```

**Erklärung**: Vektorisierung ist schneller, weil Operationen auf C-Level auf ganzen Arrays ausgeführt werden, statt Element-für-Element in Python.

---

### Lösung P5: Produktionsplanung (45 lines)

```python
import pandas as pd

# a) CSV erstellen und einlesen
csv_content = """Auftrag_ID,Maschine,Bauteil,Zielmenge,Produziert,Ausschuss,Zykluszeit_s,Datum,Status
A001,CNC-01,Welle-A,100,98,2,12.5,2024-01-15,Abgeschlossen
A002,CNC-02,Flansch-B,200,195,5,8.3,2024-01-15,Abgeschlossen
A003,CNC-01,Welle-A,150,148,2,12.8,2024-01-16,Abgeschlossen
A004,Presse-01,Gehaeuse-C,80,75,5,25.0,2024-01-16,Verzoegert
A005,CNC-02,Flansch-B,180,178,2,8.1,2024-01-17,Abgeschlossen
A006,Presse-02,Gehaeuse-C,100,98,2,24.5,2024-01-17,Abgeschlossen
A007,CNC-01,Welle-A,120,118,2,12.6,2024-01-18,Abgeschlossen
A008,Drehbank-01,Bolzen-D,300,285,15,5.2,2024-01-18,Abgeschlossen
A009,CNC-02,Flansch-B,160,158,2,8.4,2024-01-19,Abgeschlossen
A010,Presse-01,Gehaeuse-C,90,80,10,26.0,2024-01-19,Verzoegert
A011,Drehbank-01,Bolzen-D,350,340,10,5.1,2024-01-20,Abgeschlossen
A012,CNC-01,Welle-A,110,109,1,12.4,2024-01-20,Abgeschlossen"""

with open('produktion_auftrage.csv', 'w') as f:
    f.write(csv_content)

df = pd.read_csv('produktion_auftrage.csv')
df['Datum'] = pd.to_datetime(df['Datum'])

# b) Neue Spalten hinzufügen
df['Ausschussrate'] = (df['Ausschuss'] / df['Zielmenge']) * 100
df['Gutmenge'] = df['Produziert'] - df['Ausschuss']
df['OEE_Availability'] = (df['Produziert'] / df['Zielmenge']) * 100

# c) Gesamtgutmenge (abgeschlossen)
gesamt_gutmenge = df[df['Status'] == 'Abgeschlossen']['Gutmenge'].sum()
print(f"Gesamtgutmenge: {gesamt_gutmenge}")

# d) Top 3 Maschinen
top_maschinen = df.groupby('Maschine')['Gutmenge'].sum().nlargest(3)
print("\nTop 3 Maschinen:")
print(top_maschinen)

# e) Bauteil-Analyse
bauteil_stats = df.groupby('Bauteil').agg({
    'Produziert': 'sum',
    'Ausschussrate': 'mean'
}).sort_values('Produziert', ascending=False)
print("\nBauteil-Statistiken:")
print(bauteil_stats)

# f) Tägliche Gutmenge
taeglich = df[df['Status'] == 'Abgeschlossen'].groupby('Datum')['Gutmenge'].sum()
print("\nTägliche Gutmenge:")
print(taeglich)

# g) Qualitätskontrolle
hohe_ausschussrate = df[df['Ausschussrate'] > 5]
print(f"\nAufträge mit Ausschussrate > 5%: {len(hohe_ausschussrate)}")
print(hohe_ausschussrate[['Auftrag_ID', 'Maschine', 'Bauteil', 'Ausschussrate']])

# h) Effizienz-Analyse
oee_by_maschine = df.groupby('Maschine')['OEE_Availability'].mean().nlargest(3)
print("\nTop 3 Maschinen nach OEE:")
print(oee_by_maschine)

# i) Bonus: Visualisierung
try:
    import matplotlib.pyplot as plt
    gutmenge_by_maschine = df.groupby('Maschine')['Gutmenge'].sum()
    gutmenge_by_maschine.plot(kind='bar', title='Gutmenge pro Maschine')
    plt.ylabel('Gutmenge')
    plt.tight_layout()
    plt.savefig('gutmenge_analyse.png')
    print("\n✓ Diagramm gespeichert: gutmenge_analyse.png")
except ImportError:
    print("\nMatplotlib nicht verfügbar")
```

**Erklärung**: Umfassende Produktionsanalyse mit Pandas. Berechnung von OEE-Kennzahlen (Overall Equipment Effectiveness). Gruppierung und Aggregation für verschiedene Analysen.

---

## Zusammenfassung

Die refaktorierten Lösungen demonstrieren:
- **Maschinenbau-Szenarien**: Sensordaten, Qualitätskontrolle, Wartungsplanung, Produktionseffizienz
- **Pandas-Grundlagen**: DataFrame-Operationen, Filtering, Sortierung
- **Aggregation**: `groupby()`, `agg()`, statistische Kennzahlen
- **Performance**: Vektorisierung vs. Schleifen
- **OEE-Kennzahlen**: Ausschussrate, Gutmenge, Verfügbarkeit
- **Praktische Anwendung**: Qualitätskontrolle, Wartungsplanung, Produktionsoptimierung
