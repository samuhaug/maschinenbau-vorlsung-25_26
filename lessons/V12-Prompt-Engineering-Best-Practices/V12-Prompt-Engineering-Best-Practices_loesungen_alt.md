# V12: Lösungen - Prompt Engineering & Imports

> [!NOTE]
> Diese Lösungen dienen als Referenz. Deine Lösung kann abweichen und trotzdem korrekt sein.
> Wichtig ist, dass du die Konzepte verstanden hast.

---

## Teil A: Theorie-Lösungen

### Lösung T1: Prompt-Anatomie analysieren

**Analyse des Prompts**:

```
Du bist ein erfahrener Python-Entwickler. Erstelle eine Funktion zur 
Berechnung der Fakultät einer Zahl. Die Funktion soll Type Hints haben, 
einen Docstring im Google Style enthalten und rekursiv implementiert 
sein. Maximale Länge: 15 Zeilen.
```

**1. Kontext**:
Der Kontext ist: **"Du bist ein erfahrener Python-Entwickler."**

Dieser Kontext definiert die Rolle des Modells. Das Modell soll sich wie ein erfahrener Entwickler verhalten, was bedeutet, dass es Best Practices, idiomatischen Code und professionelle Standards anwenden soll.

**2. Aufgabe**:
Die konkrete Aufgabe ist: **"Erstelle eine Funktion zur Berechnung der Fakultät einer Zahl."**

Dies ist die zentrale Aktion, die ausgeführt werden soll. Die Aufgabe ist klar und spezifisch definiert.

**3. Format**:
Das geforderte Format umfasst mehrere Anforderungen:
- Type Hints verwenden
- Docstring im Google Style
- Rekursive Implementierung

Diese Formatvorgaben definieren die strukturellen und stilistischen Eigenschaften der Lösung.

**4. Constraints**:
Der definierte Constraint ist: **"Maximale Länge: 15 Zeilen."**

Diese Einschränkung setzt eine Obergrenze für den Umfang der Lösung und erzwingt Prägnanz.

> [!TIP]
> **Warum ist diese Analyse wichtig?**
> 
> Durch das Zerlegen eines Prompts in seine Komponenten erkennst du:
> - Welche Informationen dem Modell helfen, die Aufgabe zu verstehen (Kontext)
> - Was genau erreicht werden soll (Aufgabe)
> - Wie das Ergebnis strukturiert sein soll (Format)
> - Welche Grenzen gesetzt sind (Constraints)
> 
> Diese vier Komponenten sollten in jedem gut strukturierten Prompt enthalten sein.

**Häufige Fehler**:
- Kontext und Aufgabe verwechseln: Der Kontext beschreibt die Rolle, die Aufgabe die Aktion
- Format mit Constraints verwechseln: Format beschreibt Struktur, Constraints setzen Grenzen
- Implizite Anforderungen übersehen: Hier ist "rekursiv" eine Formatvorgabe, die die Implementierungsart festlegt

---

### Lösung T2: Prompt-Verbesserung

**Ursprünglicher Prompt** (vage):
```
Erkläre Sortieralgorithmen.
```

**Probleme des ursprünglichen Prompts**:
- Kein Kontext (Wer ist die Zielgruppe? Welches Vorwissen?)
- Aufgabe zu allgemein (Welche Sortieralgorithmen? Wie tief?)
- Kein Format (Text? Code? Tabelle? Visualisierung?)
- Keine Constraints (Länge? Komplexität?)

**Verbesserter Prompt**:

```
Du bist ein Informatik-Dozent an einer Hochschule und erklärst Erstsemstern 
im Bachelor Informatik die Grundlagen der Algorithmik. Die Studierenden haben 
bereits Programmierkenntnisse in Python, aber noch keine formale Ausbildung 
in Algorithmik.

Erstelle eine strukturierte Übersicht über die drei grundlegenden 
Sortieralgorithmen Bubble Sort, Insertion Sort und Quick Sort. 

Für jeden Algorithmus:
1. Erkläre die Funktionsweise in maximal 3 Sätzen
2. Gib die Zeit-Komplexität an (Best Case, Average Case, Worst Case)
3. Zeige ein minimales Python-Code-Beispiel (max. 10 Zeilen)
4. Nenne einen praktischen Anwendungsfall

Formatiere die Ausgabe als Markdown-Tabelle mit den Spalten: 
Algorithmus | Funktionsweise | Komplexität | Anwendungsfall

Beschränke die gesamte Ausgabe auf maximal 500 Wörter.
```

**Erklärung der Verbesserungen**:

**Kontext-Ergänzung**:
- Rolle definiert: Informatik-Dozent
- Zielgruppe spezifiziert: Erstsemester mit Python-Kenntnissen
- Vorwissen geklärt: Programmierung ja, Algorithmik nein

Diese Informationen helfen dem Modell, den richtigen Abstraktionslevel zu wählen.

**Aufgaben-Präzisierung**:
- Konkrete Algorithmen genannt (Bubble Sort, Insertion Sort, Quick Sort)
- Vier spezifische Anforderungen pro Algorithmus definiert
- Klare Struktur vorgegeben (1-4 durchnummeriert)

Die Aufgabe ist jetzt messbar und vollständig spezifiziert.

**Format-Definition**:
- Markdown-Tabelle als Ausgabeformat
- Spaltenstruktur vorgegeben
- Code-Beispiele mit Zeilenlimit

Das Format ist präzise und maschinell umsetzbar.

**Constraints gesetzt**:
- Funktionsweise: Max. 3 Sätze
- Code-Beispiele: Max. 10 Zeilen
- Gesamte Ausgabe: Max. 500 Wörter

Diese Einschränkungen verhindern ausufernde Antworten und erzwingen Prägnanz.

> [!TIP]
> **Prompt-Verbesserungs-Checkliste**:
> 
> ✅ Kontext:
> - Ist die Rolle des Modells klar?
> - Ist die Zielgruppe definiert?
> - Ist das Vorwissen spezifiziert?
> 
> ✅ Aufgabe:
> - Ist die Aufgabe konkret und messbar?
> - Sind alle erwarteten Ausgaben aufgelistet?
> - Gibt es eine klare Struktur?
> 
> ✅ Format:
> - Ist das Ausgabeformat definiert (Text, Code, Tabelle, etc.)?
> - Sind Stil und Ton spezifiziert?
> 
> ✅ Constraints:
> - Sind Längen-Limits gesetzt?
> - Sind Komplexitäts-Grenzen definiert?
> - Gibt es Ausschluss-Kriterien?

**Alternative Ansätze**:

Je nach Ziel könnte der Prompt auch anders verbessert werden:

**Für Anfänger mit visueller Präferenz**:
```
Erkläre die drei Sortieralgorithmen Bubble Sort, Insertion Sort und Quick Sort 
mit ASCII-Art-Visualisierungen der Sortierschritte. Zeige für jede Methode 
eine Beispiel-Sortierung des Arrays [64, 34, 25, 12, 22].
```

**Für fortgeschrittene Studierende**:
```
Vergleiche Bubble Sort, Insertion Sort und Quick Sort hinsichtlich ihrer 
Worst-Case-Laufzeit, Cache-Effizienz und Eignung für parallele Verarbeitung. 
Begründe deine Analyse formal mit Komplexitätstheorie.
```

Die Wahl der Verbesserung hängt vom tatsächlichen Bedarf ab.

---

### Lösung T3: Few-Shot Learning Design

**Vollständiger Few-Shot-Prompt**:

```
Du bist ein KI-Assistent für Kundenservice-Automatisierung. 
Deine Aufgabe ist es, aus Kunden-Reviews folgende Informationen zu extrahieren:

1. Sentiment: positiv | neutral | negativ
2. Hauptthema: Produkt | Lieferung | Service | Preis
3. Handlungsempfehlung: keine | Antworten | Eskalieren

Analysiere Reviews und gib die Extraktion im folgenden Format aus:
Sentiment: [Wert] | Thema: [Wert] | Empfehlung: [Wert]

Hier sind drei Beispiele:

---
Review: "Das Produkt ist qualitativ hochwertig und funktioniert einwandfrei. 
Der Preis ist zwar etwas hoch, aber das ist es wert. Bin sehr zufrieden!"

Sentiment: positiv | Thema: Produkt | Empfehlung: keine

---
Review: "Die Lieferung kam 2 Wochen zu spät, und die Verpackung war beschädigt. 
Das Produkt selbst ist okay, aber dieser Service ist inakzeptabel."

Sentiment: negativ | Thema: Lieferung | Empfehlung: Eskalieren

---
Review: "Ich habe eine Frage zur Garantie gestellt, aber noch keine Antwort 
erhalten. Das Produkt funktioniert soweit gut."

Sentiment: neutral | Thema: Service | Empfehlung: Antworten

---
Analysiere nun das folgende Review:
[BENUTZER-EINGABE]
```

**Erklärung der Beispiel-Wahl**:

**Beispiel 1 - Positives Sentiment**:
- Sentiment: Klar positiv ("sehr zufrieden", "hochwertig", "einwandfrei")
- Thema: Produkt (Fokus auf Produktqualität)
- Empfehlung: Keine (zufriedener Kunde, keine Aktion nötig)
- Besonderheit: Erwähnt Preis als Nebenaspekt, aber Hauptthema bleibt Produkt

Dieses Beispiel zeigt dem Modell, dass positive Reviews oft keine Aktion erfordern und wie man das Hauptthema identifiziert, auch wenn mehrere Aspekte erwähnt werden.

**Beispiel 2 - Negatives Sentiment**:
- Sentiment: Klar negativ ("inakzeptabel", "beschädigt", "zu spät")
- Thema: Lieferung (Lieferzeit und Verpackung im Fokus)
- Empfehlung: Eskalieren (schwerwiegendes Problem, Entschädigung/Management-Intervention nötig)
- Besonderheit: Gemischte Erwähnung (Produkt okay, aber Lieferung problematisch)

Dieses Beispiel demonstriert, dass negative Sentiments oft Eskalation erfordern und wie man das Hauptthema bei gemischten Reviews identifiziert.

**Beispiel 3 - Neutrales Sentiment**:
- Sentiment: Neutral (weder lobend noch kritisch, sachlich)
- Thema: Service (unbeantwortete Frage zum Kundenservice)
- Empfehlung: Antworten (aktive Kommunikation erforderlich)
- Besonderheit: Zeigt, dass neutrale Reviews trotzdem Aktion erfordern können

Dieses Beispiel zeigt dem Modell, dass neutrale Reviews oft offene Fragen enthalten, die beantwortet werden müssen, und dass Sentiment und Handlungsempfehlung nicht immer korrelieren.

**Warum diese Beispiele gut funktionieren**:

1. **Abdeckung aller Sentiments**: Positiv, neutral, negativ sind alle vertreten
2. **Vielfältige Themen**: Produkt, Lieferung, Service werden demonstriert
3. **Verschiedene Empfehlungen**: Alle drei Handlungsoptionen werden gezeigt
4. **Edge Cases**: Gemischte Reviews (positives Produkt + negative Lieferung) werden behandelt
5. **Konsistentes Format**: Alle Beispiele folgen exakt demselben Ausgabeformat
6. **Realitätsnähe**: Die Reviews klingen authentisch und repräsentieren echte Kundenszenarien

> [!WARNING]
> **Häufige Fehler bei Few-Shot-Prompts**:
> 
> ❌ **Zu ähnliche Beispiele**: Wenn alle Beispiele sehr ähnlich sind, lernt das Modell nicht zu generalisieren
> ```
> # Schlecht:
> "Das Produkt ist super!" → positiv
> "Das Produkt ist toll!" → positiv
> "Das Produkt ist großartig!" → positiv
> ```
> 
> ❌ **Inkonsistentes Format**: Wenn Beispiele unterschiedliche Formate haben, ist das Modell verwirrt
> ```
> # Schlecht:
> Beispiel 1: "Review: ... | Sentiment: positiv"
> Beispiel 2: "Text: ... Stimmung: gut"
> ```
> 
> ❌ **Keine Edge Cases**: Wenn nur einfache Fälle gezeigt werden, scheitert das Modell bei Komplexität
> ```
> # Schlecht: Nur klare Fälle, keine gemischten Reviews
> ```
> 
> ❌ **Zu viele Beispiele**: Bei Few-Shot sind 3-5 Beispiele optimal, mehr verwirrt oft
> 
> ✅ **Best Practice**: 3-5 diverse, konsistente, realistische Beispiele mit unterschiedlichen Edge Cases

**Alternative Lösungsansätze**:

**Zero-Shot-Ansatz** (ohne Beispiele, nur mit klarer Instruktion):
```
Extrahiere aus Kunden-Reviews: Sentiment (positiv/neutral/negativ), 
Hauptthema (Produkt/Lieferung/Service/Preis), Handlungsempfehlung (keine/Antworten/Eskalieren). 
Format: "Sentiment: X | Thema: Y | Empfehlung: Z"
```

**One-Shot-Ansatz** (ein sehr repräsentatives Beispiel):
```
Beispiel:
Review: "Gutes Produkt, aber Lieferung zu spät."
Sentiment: neutral | Thema: Lieferung | Empfehlung: Antworten

Analysiere nun: [EINGABE]
```

**Chain-of-Thought Few-Shot** (mit Begründung):
```
Review: "Das Produkt ist qualitativ hochwertig..."
Analyse:
- "qualitativ hochwertig", "sehr zufrieden" → Sentiment: positiv
- Fokus auf Produkteigenschaften → Thema: Produkt
- Keine Beschwerde oder offene Frage → Empfehlung: keine
Ergebnis: Sentiment: positiv | Thema: Produkt | Empfehlung: keine
```

Der Chain-of-Thought-Ansatz hilft bei komplexeren Fällen, benötigt aber mehr Tokens.

---

## Teil B: Python-Lösungen

### Lösung P1: CNC-Maschinenparameter-Modul

**`cnc_parameter.py`**:

```python
"""
Modul zur Berechnung von CNC-Schnittparametern für Maschinenbauanwendungen.
"""
import math

def berechne_schnittgeschwindigkeit(durchmesser_mm: float, drehzahl_min: float) -> float:
    """Berechnet Schnittgeschwindigkeit in m/min."""
    return (math.pi * durchmesser_mm * drehzahl_min) / 1000

def berechne_vorschubgeschwindigkeit(drehzahl_min: float, vorschub_pro_umdrehung_mm: float) -> float:
    """Berechnet Vorschubgeschwindigkeit in mm/min."""
    return drehzahl_min * vorschub_pro_umdrehung_mm

def berechne_zeitspanvolumen(schnitttiefe_mm: float, schnittbreite_mm: float, vorschub_mm_min: float) -> float:
    """Berechnet Zeitspanvolumen in cm³/min."""
    return (schnitttiefe_mm * schnittbreite_mm * vorschub_mm_min) / 1000
```

**`main.py`**:

```python
"""Testprogramm für CNC-Parameter-Modul."""
import cnc_parameter

# Beispiel: Fräsoperation mit Hartmetall-Fräser
durchmesser = 20.0  # mm
drehzahl = 1500.0  # U/min
vorschub_pro_umdrehung = 0.1  # mm

vc = cnc_parameter.berechne_schnittgeschwindigkeit(durchmesser, drehzahl)
vf = cnc_parameter.berechne_vorschubgeschwindigkeit(drehzahl, vorschub_pro_umdrehung)
Q = cnc_parameter.berechne_zeitspanvolumen(2.0, 10.0, vf)

print(f"Schnittgeschwindigkeit: {vc:.2f} m/min")
print(f"Vorschubgeschwindigkeit: {vf:.1f} mm/min")
print(f"Zeitspanvolumen: {Q:.2f} cm³/min")
```

**Erklärung**: Modul-Docstring definiert Zweck, Type Hints dokumentieren Parameter/Rückgabewerte, f-Strings formatieren Ausgabe. `math.pi` stellt π-Wert bereit.

---

### Lösung P2: Werkstoff-Rechner mit `if __name__ == "__main__":`

**`werkstoff_rechner.py`**:

```python
"""
Werkstoff-Rechner für Festigkeitsberechnungen in Maschinenbauanwendungen.
"""

def berechne_spannung(kraft_n: float, flaeche_mm2: float) -> float:
    """Berechnet Spannung σ = F/A in MPa."""
    if flaeche_mm2 == 0:
        raise ZeroDivisionError("Fläche darf nicht Null sein")
    return kraft_n / flaeche_mm2

def berechne_dehnung(laenge_mm: float, laengenaenderung_mm: float) -> float:
    """Berechnet Dehnung ε = ΔL/L₀."""
    if laenge_mm == 0:
        raise ZeroDivisionError("Ausgangslänge darf nicht Null sein")
    return laengenaenderung_mm / laenge_mm

def berechne_e_modul(spannung_mpa: float, dehnung: float) -> float:
    """Berechnet E-Modul E = σ/ε in GPa."""
    if dehnung == 0:
        raise ZeroDivisionError("Dehnung darf nicht Null sein")
    return (spannung_mpa / dehnung) / 1000

def berechne_sicherheitsfaktor(zugfestigkeit_mpa: float, betriebsspannung_mpa: float) -> float:
    """Berechnet Sicherheitsfaktor S = Rm/σ."""
    if betriebsspannung_mpa == 0:
        raise ZeroDivisionError("Betriebsspannung darf nicht Null sein")
    return zugfestigkeit_mpa / betriebsspannung_mpa

if __name__ == "__main__":
    print("=== Werkstoff-Festigkeitsrechner ===")
    try:
        kraft = float(input("Kraft (N): "))
        flaeche = float(input("Querschnittsfläche (mm²): "))
        
        spannung = berechne_spannung(kraft, flaeche)
        print(f"Spannung: {spannung:.1f} MPa")
        
        zugfestigkeit = float(input("Zugfestigkeit des Materials (MPa): "))
        sicherheit = berechne_sicherheitsfaktor(zugfestigkeit, spannung)
        print(f"Sicherheitsfaktor: {sicherheit:.1f}")
        
    except ValueError:
        print("Fehler: Bitte gültige Zahlen eingeben.")
    except ZeroDivisionError as e:
        print(f"Fehler: {e}")
```

**Erklärung**: `if __name__ == "__main__":` Block wird nur bei direkter Ausführung ausgeführt, nicht beim Import. Error Handling fängt `ValueError` (ungültige Eingabe) und `ZeroDivisionError` ab.

---

### Lösung P3: Fertigungs-Tools-Package

**Verzeichnisstruktur**:
```
fertigungs_tools/
├── __init__.py
├── toleranzen.py
└── kosten.py
main.py
```

**`fertigungs_tools/__init__.py`**:

```python
"""Fertigungs-Tools Package für Toleranzprüfung und Kostenberechnung."""

from .toleranzen import pruefe_toleranz, berechne_passungsart
from .kosten import berechne_fertigungskosten, berechne_stueckpreis

__all__ = ['pruefe_toleranz', 'berechne_passungsart', 'berechne_fertigungskosten', 'berechne_stueckpreis']
```

**`fertigungs_tools/toleranzen.py`**:

```python
"""Funktionen für Toleranzprüfungen und Passungsarten."""

def pruefe_toleranz(ist_wert: float, soll_wert: float, toleranz: float) -> bool:
    """Prüft ob Ist-Wert innerhalb der Toleranz liegt."""
    return abs(ist_wert - soll_wert) <= toleranz

def berechne_passungsart(bohrung_mm: float, welle_mm: float) -> str:
    """Bestimmt Passungsart (Spiel/Übermaß/Übergang)."""
    differenz = bohrung_mm - welle_mm
    if differenz > 0.01:
        return "Spiel"
    elif differenz < -0.01:
        return "Übermaß"
    else:
        return "Übergangspassung"
```

**`fertigungs_tools/kosten.py`**:

```python
"""Funktionen für Fertigungskostenberechnung."""

def berechne_fertigungskosten(stueckzahl: int, stueckkosten_eur: float, ruestkosten_eur: float) -> float:
    """Berechnet Gesamtkosten K = n × k + Kr."""
    return stueckzahl * stueckkosten_eur + ruestkosten_eur

def berechne_stueckpreis(gesamtkosten_eur: float, stueckzahl: int) -> float:
    """Berechnet Stückpreis p = K/n."""
    if stueckzahl == 0:
        raise ZeroDivisionError("Stückzahl darf nicht Null sein")
    return gesamtkosten_eur / stueckzahl
```

**`main.py`**:

```python
"""Testprogramm für fertigungs_tools Package."""
from fertigungs_tools import pruefe_toleranz, berechne_passungsart, berechne_fertigungskosten, berechne_stueckpreis

# Test Toleranzprüfung
print(f"Toleranz OK: {pruefe_toleranz(50.2, 50.0, 0.5)}")  # True

# Test Passungsart
print(f"Passungsart: {berechne_passungsart(50.1, 49.9)}")  # Spiel

# Test Kostenberechnung
kosten = berechne_fertigungskosten(100, 15.0, 500.0)
stueckpreis = berechne_stueckpreis(kosten, 100)
print(f"Gesamtkosten: {kosten:.2f} EUR, Stückpreis: {stueckpreis:.2f} EUR")
```

**Erklärung**: `__init__.py` ermöglicht direkten Import aus Package. Relative Imports (`.toleranzen`) referenzieren Module innerhalb des Packages. `__all__` definiert öffentliche API.

---

### Lösung P4: Produktionsdaten-Verarbeitung (Kurzversion)

Aufgrund der Komplexität hier nur Kerncode. Vollständige Lösung siehe P3-ähnliche Struktur.

**`produktionsdaten/analyse/oee.py`** (Relativer Import-Beispiel):

```python
"""OEE-Berechnung für Produktionsanalyse."""
from .qualitaet import berechne_ausschussquote  # Relativer Import!

def berechne_qualitaetsrate(gesamt: int, ausschuss: int) -> float:
    """Berechnet Qualitätsrate Q = (1 - Ausschussquote/100) × 100."""
    ausschussquote = berechne_ausschussquote(gesamt, ausschuss)
    return (1 - ausschussquote / 100) * 100

def berechne_oee(verfuegbarkeit: float, leistung: float, qualitaet: float) -> float:
    """Berechnet OEE = V × L × Q."""
    return (verfuegbarkeit * leistung * qualitaet) / 1000000
```

**`main.py`** (Absolute Imports):

```python
"""Hauptprogramm mit absoluten Imports."""
from produktionsdaten.io.reader import lese_produktionsdaten
from produktionsdaten.analyse.oee import berechne_oee, berechne_qualitaetsrate

# Beispielnutzung
oee_wert = berechne_oee(95.0, 85.0, 98.0)  # OEE = ~79%
print(f"OEE: {oee_wert:.1f}%")
```

**Hinweis**: Relativer Import (`.qualitaet`) funktioniert nur innerhalb von Packages. Absoluter Import (`produktionsdaten.io.reader`) funktioniert überall.

---

### Lösung P5: CNC-Überwachungs-CLI (Kurzversion)

**`cnc_monitor/sensor.py`**:

```python
"""Mock-Sensordaten für CNC-Maschinen."""

def lese_maschinendaten(maschinen_id: str) -> dict:
    """Gibt Mock-Maschinendaten zurück."""
    # Einfacher Hash für variierende Daten
    id_hash = sum(ord(c) for c in maschinen_id) % 5
    temp_basis = [65, 72, 58, 85, 68]
    drehzahl_basis = [1200, 1500, 800, 2000, 1000]
    
    return {
        "id": maschinen_id,
        "temperatur_c": temp_basis[id_hash],
        "drehzahl_rpm": drehzahl_basis[id_hash],
        "vibration_mm_s": 2.5 + id_hash * 0.5,
        "werkzeugverschleiss_prozent": 35 + id_hash * 10
    }
```

**`cnc_monitor/analyzer.py`**:

```python
"""Zustandsanalyse für Maschinendaten."""

def analysiere_zustand(daten: dict) -> str:
    """Bewertet Maschinenzustand basierend auf Grenzwerten."""
    if daten["temperatur_c"] > 90 or daten["werkzeugverschleiss_prozent"] > 90:
        return "Kritisch"
    elif daten["temperatur_c"] > 80 or daten["vibration_mm_s"] > 5 or daten["werkzeugverschleiss_prozent"] > 80:
        return "Warnung"
    return "OK"
```

**`cnc_monitor/cli.py`**:

```python
"""CLI für CNC-Überwachung."""
import argparse
from .sensor import lese_maschinendaten
from .analyzer import analysiere_zustand

def main():
    parser = argparse.ArgumentParser(description='CNC-Maschinenüberwachung')
    parser.add_argument('--maschine', required=True, help='Maschinen-ID')
    args = parser.parse_args()
    
    daten = lese_maschinendaten(args.maschine)
    zustand = analysiere_zustand(daten)
    status_emoji = "✅" if zustand == "OK" else "⚠️" if zustand == "Warnung" else "🔴"
    
    print("╔════════════════════════════════════════╗")
    print("║  CNC-Maschinenüberwachung              ║")
    print("╠════════════════════════════════════════╣")
    print(f"║  Maschine: {daten['id']:<27}║")
    print(f"║  Temperatur: {daten['temperatur_c']}°C{' ' * (26 - len(str(daten['temperatur_c'])))}║")
    print(f"║  Drehzahl: {daten['drehzahl_rpm']} U/min{' ' * (23 - len(str(daten['drehzahl_rpm'])))}║")
    print(f"║  Vibration: {daten['vibration_mm_s']} mm/s{' ' * (22 - len(str(daten['vibration_mm_s'])))}║")
    print(f"║  Werkzeugverschleiß: {daten['werkzeugverschleiss_prozent']}%{' ' * (17 - len(str(daten['werkzeugverschleiss_prozent'])))}║")
    print(f"║  Status: {status_emoji} {zustand}{' ' * (30 - len(zustand))}║")
    print("╚════════════════════════════════════════╝")
```

**`main.py`**:

```python
"""Einstiegspunkt."""
from cnc_monitor.cli import main
if __name__ == "__main__":
    main()
```

**Setup**: `python -m venv venv`, `venv\Scripts\activate`, `python main.py --maschine CNC-001`

---

## Zusammenfassung

V12 demonstriert Modularisierung mit Maschinenbau-Fokus:
- **P1**: CNC-Parameter-Modul (Schnittgeschwindigkeit, Vorschub)
- **P2**: Werkstoff-Rechner mit `if __name__` (Spannung, Sicherheitsfaktor)
- **P3**: Fertigungs-Tools-Package (Toleranzen, Kosten)
- **P4**: Produktionsdaten-Verarbeitung (relative/absolute Imports, OEE)
- **P5**: CNC-Monitor-CLI (venv, argparse, Mock-Sensoren)

Alle Lösungen sind 40-50% kürzer als Originalaufgaben und fokussieren auf Maschinenbau-Anwendungsfälle.
    
    # Mock-Daten basierend auf Stadt (simuliert verschiedene Wetterbedingungen)
    stadt = stadt.strip().capitalize()
    
    # Einfache Hash-Funktion für konsistente, aber variierende Mock-Daten
    stadt_hash = sum(ord(c) for c in stadt) % 5
    
    bedingungen_optionen = ["Sonnig", "Bewölkt", "Regnerisch", "Neblig", "Windig"]
    temperatur_basis = [22, 15, 12, 18, 25]
    luftfeuchtigkeit_basis = [45, 70, 85, 90, 40]
    wind_basis = [10, 15, 20, 5, 30]
    
    # Simuliere API-Call (requests würde hier verwendet werden)
    # Beispiel für echten API-Call (auskommentiert):
    # API_KEY = "dein_api_key"
    # url = f"http://api.openweathermap.org/data/2.5/weather?q={stadt}&appid={API_KEY}&units=metric&lang=de"
    # try:
    #     response = requests.get(url, timeout=10)
    #     response.raise_for_status()
    #     data = response.json()
    #     return {
    #         "stadt": data["name"],
    #         "temperatur": round(data["main"]["temp"]),
    #         "bedingungen": data["weather"][0]["description"],
    #         "luftfeuchtigkeit": data["main"]["humidity"],
    #         "wind": round(data["wind"]["speed"] * 3.6)
    #     }
    # except requests.RequestException as e:
    #     raise ConnectionError(f"Fehler beim Abrufen der Wetterdaten: {e}")
    
    # Mock-Daten zurückgeben
    return {
        "stadt": stadt,
        "temperatur": temperatur_basis[stadt_hash],
        "bedingungen": bedingungen_optionen[stadt_hash],
        "luftfeuchtigkeit": luftfeuchtigkeit_basis[stadt_hash],
        "wind": wind_basis[stadt_hash]
    }

def check_api_verfuegbar() -> bool:
    """
    Prüft, ob die requests-Library verfügbar ist.
    
    Returns:
        True wenn requests importiert werden kann, False sonst
    """
    try:
        import requests
        return True
    except ImportError:
        return False
```

**`weather_cli/formatter.py`**:

```python
"""
Formatierungs-Modul für Wetterausgaben.
"""

from typing import Dict

def formatiere_wetter(wetter: Dict[str, any]) -> str:
    """
    Formatiert Wetterdaten als lesbaren Text.
    
    Args:
        wetter: Dictionary mit Wetterdaten (von hole_wetter())
    
    Returns:
        Formatierter String mit Wetterinformationen
    
    Raises:
        KeyError: Wenn erforderliche Schlüssel fehlen
        TypeError: Wenn wetter nicht vom Typ dict ist
    
    Examples:
        >>> wetter = {"stadt": "Berlin", "temperatur": 20, "bedingungen": "Sonnig", 
        ...           "luftfeuchtigkeit": 45, "wind": 10}
        >>> print(formatiere_wetter(wetter))
        ╔════════════════════════════════════════╗
        ║  Wetter in Berlin                      ║
        ╠════════════════════════════════════════╣
        ║  🌡️  Temperatur:     20°C              ║
        ║  ☁️  Bedingungen:    Sonnig            ║
        ║  💧  Luftfeuchtigkeit: 45%             ║
        ║  💨  Wind:           10 km/h           ║
        ╚════════════════════════════════════════╝
    """
    if not isinstance(wetter, dict):
        raise TypeError("Wetter muss ein Dictionary sein")
    
    # Prüfe erforderliche Schlüssel
    erforderliche_keys = ["stadt", "temperatur", "bedingungen", "luftfeuchtigkeit", "wind"]
    for key in erforderliche_keys:
        if key not in wetter:
            raise KeyError(f"Erforderlicher Schlüssel '{key}' fehlt in Wetterdaten")
    
    # Wähle Emoji basierend auf Bedingungen
    bedingung = wetter["bedingungen"].lower()
    wetter_emoji = "☀️" if "sonn" in bedingung else \
                   "🌧️" if "regen" in bedingung else \
                   "🌫️" if "nebel" in bedingung else \
                   "💨" if "wind" in bedingung else "☁️"
    
    # Formatierung mit Box-Drawing-Characters
    breite = 40
    output = []
    output.append("╔" + "═" * (breite - 2) + "╗")
    output.append(f"║ {wetter_emoji} Wetter in {wetter['stadt']:<{breite - 12}}║")
    output.append("╠" + "═" * (breite - 2) + "╣")
    output.append(f"║  🌡️  Temperatur:     {wetter['temperatur']}°C{' ' * (breite - 22 - len(str(wetter['temperatur'])))}║")
    output.append(f"║  ☁️  Bedingungen:    {wetter['bedingungen']:<{breite - 22}}║")
    output.append(f"║  💧  Luftfeuchtigkeit: {wetter['luftfeuchtigkeit']}%{' ' * (breite - 25 - len(str(wetter['luftfeuchtigkeit'])))}║")
    output.append(f"║  💨  Wind:           {wetter['wind']} km/h{' ' * (breite - 21 - len(str(wetter['wind'])))}║")
    output.append("╚" + "═" * (breite - 2) + "╝")
    
    return "\n".join(output)

def formatiere_wetter_einfach(wetter: Dict[str, any]) -> str:
    """
    Einfache Formatierung ohne Box (für ältere Terminals).
    
    Args:
        wetter: Dictionary mit Wetterdaten
    
    Returns:
        Einfach formatierter String
    """
    return f"""Wetter in {wetter['stadt']}:
Temperatur: {wetter['temperatur']}°C
Bedingungen: {wetter['bedingungen']}
Luftfeuchtigkeit: {wetter['luftfeuchtigkeit']}%
Wind: {wetter['wind']} km/h"""
```

**`weather_cli/cli.py`**:

```python
"""
Command-Line Interface für das Weather CLI Tool.
"""

import argparse
import sys
from typing import Optional

from .api import hole_wetter, check_api_verfuegbar
from .formatter import formatiere_wetter, formatiere_wetter_einfach

def parse_arguments(args: Optional[list[str]] = None) -> argparse.Namespace:
    """
    Parst Kommandozeilen-Argumente.
    
    Args:
        args: Optionale Liste von Argumenten (für Tests)
    
    Returns:
        Namespace-Objekt mit geparsten Argumenten
    """
    parser = argparse.ArgumentParser(
        prog='weather-cli',
        description='Ruft Wetterinformationen für eine Stadt ab.',
        epilog='Beispiel: python main.py --stadt Berlin'
    )
    
    parser.add_argument(
        '--stadt',
        type=str,
        required=True,
        help='Name der Stadt, für die Wetterinformationen abgerufen werden sollen'
    )
    
    parser.add_argument(
        '--einfach',
        action='store_true',
        help='Verwendet einfache Formatierung ohne Box-Drawing'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )
    
    return parser.parse_args(args)

def main(args: Optional[list[str]] = None) -> int:
    """
    Hauptfunktion des CLI-Tools.
    
    Args:
        args: Optionale Kommandozeilen-Argumente (für Tests)
    
    Returns:
        Exit-Code (0 = Erfolg, 1 = Fehler)
    """
    # Prüfe, ob requests verfügbar ist
    if not check_api_verfuegbar():
        print("❌ Fehler: requests-Library nicht gefunden.")
        print("Installiere mit: pip install requests")
        return 1
    
    try:
        # Parse Argumente
        parsed_args = parse_arguments(args)
        
        # Wetterdaten abrufen
        print(f"📡 Rufe Wetterdaten für {parsed_args.stadt} ab...")
        wetter = hole_wetter(parsed_args.stadt)
        
        # Formatieren und ausgeben
        print()
        if parsed_args.einfach:
            print(formatiere_wetter_einfach(wetter))
        else:
            print(formatiere_wetter(wetter))
        
        return 0
    
    except ValueError as e:
        print(f"❌ Eingabefehler: {e}")
        return 1
    
    except KeyError as e:
        print(f"❌ Datenfehler: {e}")
        return 1
    
    except Exception as e:
        print(f"❌ Unerwarteter Fehler: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

**`main.py`** (Einstiegspunkt):

```python
"""
Einstiegspunkt für das Weather CLI Tool.

Verwendung:
    python main.py --stadt Berlin
    python main.py --stadt München --einfach
"""

import sys
from weather_cli.cli import main

if __name__ == "__main__":
    sys.exit(main())
```

**`README.md`**:

```markdown
# Weather CLI Tool

Ein einfaches Kommandozeilen-Tool zum Abrufen von Wetterinformationen.

## Features

- Abrufen von Wetterinformationen für beliebige Städte
- Übersichtliche, formatierte Ausgabe
- Einfacher Modus für ältere Terminals
- Mock-API für Übungszwecke (kein API-Key erforderlich)

## Installation

### 1. Repository klonen oder herunterladen

```bash
cd weather_cli
```

### 2. Virtuelle Umgebung erstellen

```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```

### 3. Virtuelle Umgebung aktivieren

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

Nach Aktivierung sollte `(venv)` vor deiner Kommandozeile erscheinen.

### 4. Dependencies installieren

```bash
pip install -r requirements.txt
```

## Verwendung

### Grundlegende Verwendung

```bash
python main.py --stadt Berlin
```

Ausgabe:
```
📡 Rufe Wetterdaten für Berlin ab...

╔════════════════════════════════════════╗
║ ☀️ Wetter in Berlin                    ║
╠════════════════════════════════════════╣
║  🌡️  Temperatur:     22°C              ║
║  ☁️  Bedingungen:    Sonnig            ║
║  💧  Luftfeuchtigkeit: 45%             ║
║  💨  Wind:           10 km/h           ║
╚════════════════════════════════════════╝
```

### Einfacher Modus

Für Terminals, die Box-Drawing-Characters nicht unterstützen:

```bash
python main.py --stadt München --einfach
```

### Hilfe anzeigen

```bash
python main.py --help
```

### Version anzeigen

```bash
python main.py --version
```

## Projekt-Struktur

```
weather_cli/
├── venv/                    # Virtuelle Umgebung (git-ignored)
├── weather_cli/             # Haupt-Package
│   ├── __init__.py          # Package-Initialisierung
│   ├── api.py               # Mock-API für Wetterdaten
│   ├── formatter.py         # Formatierungs-Funktionen
│   └── cli.py               # Command-Line Interface
├── tests/                   # Unit-Tests (optional)
│   ├── __init__.py
│   └── test_formatter.py
├── .gitignore               # Git-Ignore-Konfiguration
├── requirements.txt         # Python-Dependencies
├── README.md                # Diese Datei
└── main.py                  # Einstiegspunkt
```

## Virtuelle Umgebung deaktivieren

Wenn du fertig bist:

```bash
deactivate
```

## Hinweise für Entwickler

### Requirements exportieren

Nach Installation neuer Packages:

```bash
pip freeze > requirements.txt
```

### Tests ausführen (Bonus)

```bash
pip install pytest
pytest tests/
```

### Mock-Daten

Dieses Tool verwendet Mock-Daten für Übungszwecke. Für eine reale Anwendung:
1. Registriere dich bei einem Wetterdienst (z.B. OpenWeatherMap)
2. Erhalte einen API-Key
3. Passe `api.py` an, um echte API-Calls zu machen

## Häufige Probleme

### `ModuleNotFoundError: No module named 'requests'`

→ Stelle sicher, dass die virtuelle Umgebung aktiviert ist und installiere Dependencies:
```bash
pip install -r requirements.txt
```

### `requests` ist installiert, aber Fehler tritt trotzdem auf

→ Prüfe, ob die virtuelle Umgebung aktiviert ist:
```bash
# Windows
where python
# Sollte auf venv\Scripts\python.exe zeigen

# macOS/Linux
which python
# Sollte auf venv/bin/python zeigen
```

## Lizenz

MIT License - Frei verwendbar für Bildungszwecke.
```

**`tests/__init__.py`** (leer):

```python
"""Test-Package für weather_cli."""
```

**`tests/test_formatter.py`** (Bonus):

```python
"""
Unit-Tests für das formatter-Modul.

Verwendung:
    pip install pytest
    pytest tests/
"""

import pytest
from weather_cli.formatter import formatiere_wetter, formatiere_wetter_einfach

def test_formatiere_wetter_vollstaendig():
    """Testet Formatierung mit vollständigen Daten."""
    wetter = {
        "stadt": "Berlin",
        "temperatur": 20,
        "bedingungen": "Sonnig",
        "luftfeuchtigkeit": 45,
        "wind": 10
    }
    
    ergebnis = formatiere_wetter(wetter)
    
    # Prüfe, ob wichtige Elemente enthalten sind
    assert "Berlin" in ergebnis
    assert "20°C" in ergebnis
    assert "Sonnig" in ergebnis
    assert "45%" in ergebnis
    assert "10 km/h" in ergebnis
    assert "╔" in ergebnis  # Box-Character

def test_formatiere_wetter_einfach():
    """Testet einfache Formatierung."""
    wetter = {
        "stadt": "München",
        "temperatur": 15,
        "bedingungen": "Bewölkt",
        "luftfeuchtigkeit": 70,
        "wind": 15
    }
    
    ergebnis = formatiere_wetter_einfach(wetter)
    
    assert "München" in ergebnis
    assert "15°C" in ergebnis
    assert "Bewölkt" in ergebnis

def test_formatiere_wetter_fehlende_keys():
    """Testet Fehlerbehandlung bei fehlenden Schlüsseln."""
    wetter_unvollstaendig = {
        "stadt": "Hamburg",
        "temperatur": 12
        # bedingungen, luftfeuchtigkeit, wind fehlen
    }
    
    with pytest.raises(KeyError):
        formatiere_wetter(wetter_unvollstaendig)

def test_formatiere_wetter_falscher_typ():
    """Testet Fehlerbehandlung bei falschem Typ."""
    with pytest.raises(TypeError):
        formatiere_wetter("nicht ein dict")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

**Ausführung des Programms**:

```bash
# 1. Setup (einmalig)
$ python -m venv venv
$ venv\Scripts\activate  # Windows
$ pip install -r requirements.txt

# 2. Programm ausführen
$ python main.py --stadt Berlin
📡 Rufe Wetterdaten für Berlin ab...

╔════════════════════════════════════════╗
║ ☀️ Wetter in Berlin                    ║
╠════════════════════════════════════════╣
║  🌡️  Temperatur:     22°C              ║
║  ☁️  Bedingungen:    Sonnig            ║
║  💧  Luftfeuchtigkeit: 45%             ║
║  💨  Wind:           10 km/h           ║
╚════════════════════════════════════════╝

# 3. Einfacher Modus
$ python main.py --stadt München --einfach
📡 Rufe Wetterdaten für München ab...

Wetter in München:
Temperatur: 15°C
Bedingungen: Bewölkt
Luftfeuchtigkeit: 70%
Wind: 15 km/h

# 4. Tests ausführen (Bonus)
$ pip install pytest
$ pytest tests/ -v
```

**Erklärung der Lösung**:

**Virtuelle Umgebung (venv)**:

Eine virtuelle Umgebung isoliert Python-Packages pro Projekt. Vorteile:
- Keine Konflikte zwischen Projekt-Dependencies
- Reproduzierbare Umgebungen
- Sauberes System-Python

**Warum `python -m venv venv`?**
- `python -m venv`: Ruft das venv-Modul der Standard-Library auf
- Zweites `venv`: Name des Verzeichnisses für die virtuelle Umgebung

**Aktivierung**:
- **Windows**: `venv\Scripts\activate`
- **macOS/Linux**: `source venv/bin/activate`

Nach Aktivierung:
- `(venv)` erscheint vor der Eingabeaufforderung
- `python` zeigt auf venv-Python, nicht System-Python
- `pip install` installiert nur in venv

**requirements.txt**:

Definiert alle Projekt-Dependencies mit Versionen:
```txt
requests==2.31.0
```

**Best Practice**: Versions-Pinning für Reproduzierbarkeit
- `==`: Exakte Version (empfohlen für Production)
- `>=`: Mindestversion
- `~=`: Kompatible Version

**Erstellen**: `pip freeze > requirements.txt`  
**Installieren**: `pip install -r requirements.txt`

**argparse - Command-Line Interface**:

`argparse` ist Teil der Standard-Library und ermöglicht professionelle CLIs:

```python
parser = argparse.ArgumentParser(description='...')
parser.add_argument('--stadt', required=True, help='...')
```

Features:
- Automatische `--help` Generation
- Type Checking
- Required vs. optional Arguments
- Default Values
- Custom Actions

**Design-Entscheidungen**:

**1. Package-Struktur (weather_cli/)**:
- Trennung von Concerns: API, Formatierung, CLI
- Jedes Modul hat eine klare Verantwortung
- Testbar und wiederverwendbar

**2. Mock-API statt echter API**:
- Keine API-Key-Registrierung nötig (Übungszweck)
- Konsistente Ergebnisse für Demonstration
- Kommentar zeigt, wie echter API-Call aussehen würde

**3. Zwei Formatierungs-Modi**:
- Standard: Box-Drawing für moderne Terminals
- Einfach: Fallback für ältere Terminals
- User-Experience-Optimierung

**4. Error Handling auf mehreren Ebenen**:
- API-Modul: Validierung der Eingabe
- Formatter: Type und Key Checks
- CLI: Catch-All für unerwartete Fehler

**5. Exit Codes**:
```python
sys.exit(0)  # Erfolg
sys.exit(1)  # Fehler
```
Ermöglicht Shell-Scripting und Automatisierung.

> [!WARNING]
> **Häufige Fehler mit venv**:
> 
> ❌ **Fehler 1: venv nicht aktiviert**
> ```bash
> # Falsch:
> $ python -m venv venv
> $ pip install requests  # Installiert in System-Python!
> ```
> ✅ **Richtig**: Immer aktivieren vor pip install
> 
> ❌ **Fehler 2: venv in Git committen**
> ```bash
> # venv/ sollte in .gitignore!
> git add venv/  # NICHT tun!
> ```
> ✅ **Richtig**: Nur requirements.txt committen
> 
> ❌ **Fehler 3: requirements.txt nicht aktualisieren**
> ```bash
> $ pip install neue-library
> # requirements.txt vergessen zu aktualisieren!
> ```
> ✅ **Richtig**: `pip freeze > requirements.txt` nach jeder Installation
> 
> ❌ **Fehler 4: Falsche Python-Version**
> ```bash
> # System hat Python 3.8, aber Projekt braucht 3.11
> $ python -m venv venv  # Nutzt System-Python!
> ```
> ✅ **Richtig**: Spezifische Version nutzen:
> ```bash
> $ python3.11 -m venv venv
> ```

**Warum diese Lösung gut ist**:
- Vollständige Demonstration von venv-Workflow
- Professionelle CLI mit argparse
- Saubere Package-Struktur mit Separation of Concerns
- Umfassendes README mit Setup-Anweisungen
- .gitignore für saubere Versionskontrolle
- Error Handling und Exit Codes
- Bonus: Unit-Tests mit pytest
- Gut dokumentierter Code mit Docstrings
- Mock-API ermöglicht Übung ohne externe Abhängigkeiten
- Zwei Formatierungs-Modi für bessere UX

---

## Zusammenfassung

Diese Übungsaufgaben haben folgende Konzepte vertieft:

**Theorie - Prompt Engineering**:
- Anatomie guter Prompts (Kontext, Aufgabe, Format, Constraints)
- Prompt-Verbesserung durch SMART-Kriterien
- Few-Shot Learning mit repräsentativen Beispielen
- Iteratives Prompt-Design

**Python - Imports & Modularisierung**:
- **P1**: Einfache Module erstellen mit Docstrings und Type Hints
- **P2**: `if __name__ == "__main__"` Pattern für Dual-Use-Module
- **P3**: Packages mit `__init__.py` und `__all__`
- **P4**: Relative vs. absolute Imports in Package-Hierarchien
- **P5**: Virtuelle Umgebungen, requirements.txt, professionelle CLI-Tools

**Neue Python-Konzepte**:
- `import`, `from ... import`, `as`
- `if __name__ == "__main__"`
- `__init__.py`, `__all__`
- Relative Imports (`.`, `..`)
- `python -m venv`
- `pip freeze > requirements.txt`
- `argparse` für CLIs
- Package-Strukturen und Hierarchien

Diese Lösungen zeigen Best Practices für strukturierten, wartbaren Python-Code.

