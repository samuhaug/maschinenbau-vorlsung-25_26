# Python Topics – Vorlesungs-Tracking

Diese Datei dient der **Konsistenz** über alle Vorlesungen hinweg: Welche **Python-Funktionen/Methoden/Module** wurden **wann** erstmals eingeführt?

## Regeln zur Pflege
- **Eintrag nur bei Erst-Einführung**: Wenn eine Funktion bereits existiert, wird sie nicht erneut eingetragen.
- Einträge möglichst **kanonisch** benennen:
  - Builtins: `print`, `len`, `range`
  - Modul-Funktionen: `math.sqrt`, `random.choice`, `pathlib.Path`
  - Methoden: `str.split`, `list.append`, `dict.get`
- Wenn bekannt: **Python-Version** angeben (z.B. „3.10+“).
- Wenn das Material als neue Vorlesung erzeugt wird: Vorlesungs-ID konsistent halten (z.B. `V01`, `V02`, …).

## Übersicht (Index)
| Vorlesung | Thema | Neu eingeführt (Auszug) |
|---|---|---|
| V01 | Python Get Started: Variablen, print, input | `print()`, `input()`, `int()`, `float()`, `str()`, `len()`, Variablen, Kommentare |
| V02 | Eingaben/Ausgaben & Formatierung | f-Strings, `.format()`, %-Operator, `print(sep, end, flush)`, Escape-Sequenzen, `open()`, `with`, Datei-I/O |
| V03 | Variablen Management & Datentypen | `type()`, `isinstance()`, `bool()`, `round()`, `id()`, `global`, `min()`, `max()`, Immutable vs. Mutable, Scope, Multiple Assignment |
| V04 | Logische Ausdrücke (Boolsche Algebra) | Vergleichsoperatoren (`==`, `!=`, `<`, `>`, `<=`, `>=`), Logische Operatoren (`and`, `or`, `not`), Verkettete Vergleiche, Kurzschlussauswertung, Truthy/Falsy Values, `abs()`, `any()` (Vorschau) |
| V05 | Verzweigungen (if, if-elif-else) | `if`, `else`, `elif`, Ternärer Operator, `pass`, Einrückung als Syntax |
| V06 | Schleifen (for, while) – Teil 1 | `for`-Schleife, `while`-Schleife, `range()`, `enumerate()`, String-Iteration, Akkumulation, Zählen |
| V07 | Schleifen (for, while) – Teil 2 | `break`, `continue`, Loop `else`-Klausel, Verschachtelte Schleifen, List Comprehensions, `string` Modul, `random` Modul |
| V08 | Listen & Datenstrukturen | `list`, `tuple`, List-Methoden (`.append()`, `.insert()`, `.extend()`, `.remove()`, `.pop()`, `.clear()`, `.index()`, `.count()`, `.sort()`, `.reverse()`, `.copy()`), `sorted()`, `sum()`, `all()`, `any()`, `zip()`, Slicing, Unpacking, Aliasing vs. Copying |
| V09 | Try-Catch (Fehlerbehandlung) | `try`, `except`, `else`, `finally`, `raise`, Exception-Hierarchie, `ValueError`, `TypeError`, `KeyError`, `FileNotFoundError`, `PermissionError`, `IndexError`, `ZeroDivisionError`, `json` Modul |
| V10 | Methoden/Funktionen – Teil 1 | `def`-Statement, `return`-Statement, Parameter und Argumente, Default-Parameter, Keyword Arguments, Multiple Return Values, Funktionen als Objekte, Scope und LEGB-Regel, Docstrings |
| V11 | GPTs, LLMs & KI (vereinfacht) | Wiederholung: `print()`, `input()`, `if/else`, `for`-Schleife, Variablen |
| V12 | Prompt Engineering | f-Strings (Wiederholung), `.strip()`, `.upper()`, `.lower()`, `.replace()` |
| V13 | Rechnerarchitektur (vereinfacht) | `matplotlib.pyplot.bar()`, `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.show()` |
| V14 | Betriebssysteme (vereinfacht) | `os.listdir()`, `os.path.isfile()`, `os.path.isdir()`, `os.path.getsize()`, `os.path.join()` |
| V15 | Netzwerk-Grundlagen (vereinfacht) | `def`, `return` (Funktionen), `.split()`, `.startswith()`, `.isdigit()` |
| V16 | APIs und JSON | `requests.get()`, `.json()`, Dictionary-Zugriff `daten["key"]`, f-String URL-Bau |
| V17 | Kryptografie: Caesar-Chiffre | `ord()`, `chr()`, `str.isalpha()`, String-Iteration `for buchstabe in text:` |
| V18 | Passwörter und Hashes | `hashlib.md5()`, `.encode()`, `.hexdigest()`, `.isupper()`, `.islower()`, `.isdigit()`, `.isalnum()` |
| V19 | Datenbanken – Teil 1 (vereinfacht) | `sqlite3.connect()`, `.cursor()`, `.execute()`, `.fetchall()`, `.commit()`, `.close()`, SQL: CREATE TABLE, INSERT, SELECT, UPDATE, DELETE, WHERE |
| V20 | Datenbanken – Teil 2 (vereinfacht) | JOIN ... ON, GROUP BY, COUNT(*), AVG(), ORDER BY, LIMIT, Fremdschlüssel |

---

# Details pro Vorlesung

## V01 (2026-01-01) – Python Get Started: Variablen, print, input

### Neu eingeführt

#### Builtins
- **`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`** (Python 3.0+)
  - Gibt Objekte auf die Standardausgabe (Konsole) aus
  - Mehrere Argumente werden durch `sep` getrennt (Standard: Leerzeichen)
  - Nach der Ausgabe wird `end` angehängt (Standard: Zeilenumbruch `\n`)
  - Signatur: `print(value1, value2, ..., sep=' ', end='\n')`
  - Beispiel: `print("Hallo", "Welt")` → `Hallo Welt`

- **`input(prompt='')`** (Python 3.0+)
  - Liest eine Zeile von der Standardeingabe (Tastatur)
  - Optional: Zeigt einen Prompt-Text an
  - Gibt **immer einen String** zurück
  - Signatur: `input(prompt)` → `str`
  - Beispiel: `name = input("Name: ")` wartet auf Eingabe

- **`int(x, base=10)`** (Built-in)
  - Konvertiert Wert `x` in eine Ganzzahl (Integer)
  - Optional: `base` gibt Zahlensystem an (2-36)
  - Kann Strings, Floats und andere Typen konvertieren
  - Wirft `ValueError` bei ungültiger Konvertierung
  - Beispiel: `int("42")` → `42`, `int(3.7)` → `3`

- **`float(x)`** (Built-in)
  - Konvertiert Wert `x` in eine Fließkommazahl
  - Akzeptiert Strings, Integers und andere numerische Typen
  - Wirft `ValueError` bei ungültiger Konvertierung
  - Beispiel: `float("3.14")` → `3.14`, `float(5)` → `5.0`

- **`str(object='')`** (Built-in)
  - Konvertiert ein Objekt in seine String-Repräsentation
  - Funktioniert mit nahezu allen Datentypen
  - Beispiel: `str(42)` → `"42"`, `str(3.14)` → `"3.14"`

- **`len(s)`** (Built-in)
  - Gibt die Länge (Anzahl der Elemente) eines Objekts zurück
  - Funktioniert mit Strings, Listen, Tuples, Dictionaries, etc.
  - Beispiel: `len("Hallo")` → `5`, `len("1011")` → `4`

#### Operatoren
- **Zuweisungsoperator `=`**
  - Weist einer Variable einen Wert zu
  - Syntax: `variable = wert`
  - Beispiel: `x = 42`

- **Arithmetische Operatoren: `+`, `-`, `*`, `/`**
  - Addition, Subtraktion, Multiplikation, Division
  - Beispiel: `5 + 3` → `8`, `10 / 2` → `5.0`

- **Potenzoperator `**`**
  - Berechnet Potenzen
  - Syntax: `basis ** exponent`
  - Beispiel: `2 ** 3` → `8`, `9 ** 0.5` → `3.0` (Quadratwurzel)

- **Zusammengesetzte Zuweisungsoperatoren: `+=`, `-=`, `*=`, `/=`**
  - Kurzschreibweise für `x = x op y`
  - Beispiel: `x += 1` entspricht `x = x + 1`

#### Konzepte und Sprachmerkmale
- **Variablen**
  - Benannte Speicherplätze für Werte
  - Keine explizite Deklaration notwendig
  - Naming-Regeln: Buchstaben, Ziffern, Unterstriche; nicht mit Ziffer beginnen; keine Keywords
  - Konvention: `snake_case` für Variablennamen

- **Dynamische Typisierung**
  - Typ einer Variable wird automatisch aus dem zugewiesenen Wert abgeleitet
  - Variablen können ihren Typ zur Laufzeit ändern
  - Keine Typdeklaration erforderlich

- **Kommentare**
  - Einzeilige Kommentare: `# Text`
  - Mehrzeilige Kommentare (Docstrings): `"""Text"""` oder `'''Text'''`
  - Werden vom Interpreter ignoriert
  - Dienen der Code-Dokumentation

- **String-Indexierung**
  - Zugriff auf einzelne Zeichen: `text[index]`
  - Indizes beginnen bei 0
  - Beispiel: `"Hallo"[0]` → `"H"`

#### Datentypen
- **`int`**: Ganzzahlen (beliebiger Größe in Python 3)
- **`float`**: Fließkommazahlen (IEEE 754 double precision)
- **`str`**: Zeichenketten (Unicode-Strings)
- **`bool`**: Wahrheitswerte `True` und `False` (werden in V04 ausführlich behandelt)

### Notizen
- Python 3.0+ verwendet automatisch Unicode-Strings
- Division `/` ergibt immer `float`, auch bei ganzzahligem Ergebnis
- Integer haben in Python 3 unbegrenzte Größe (nur durch Speicher limitiert)
- `input()` hat sich zwischen Python 2 und 3 geändert (Python 2: `raw_input()`)
- Empfohlene IDE für diese Vorlesung: Visual Studio Code mit Python-Extension

---

## V02 (2026-01-01) – Eingaben/Ausgaben & Formatierung

### Neu eingeführt

#### String-Formatierung

- **f-Strings (Formatted String Literals)** (Python 3.6+)
  - Moderne Methode zur String-Formatierung mit direkter Variablen-Einbettung
  - Syntax: `f"Text {variable}"` oder `f"Text {expression}"`
  - Formatspezifikationen nach Doppelpunkt: `f"{x:.2f}"` für 2 Dezimalstellen
  - Signatur: `f"...{expression:format_spec}..."`
  - Beispiel: `f"Pi ist {pi:.2f}"` → `"Pi ist 3.14"`

- **Formatspezifikationen in f-Strings**:
  - `{x:.2f}` – Fließkommazahl mit 2 Dezimalstellen (fixed-point)
  - `{x:.3e}` – Wissenschaftliche Notation (exponential) mit 3 Dezimalstellen
  - `{x:10.2f}` – Rechtsbündig in Feld der Breite 10 mit 2 Dezimalstellen
  - `{x:<10.2f}` – Linksbündig in Feld der Breite 10
  - `{x:^10.2f}` – Zentriert in Feld der Breite 10
  - `{x:,}` – Tausender-Trennzeichen (Komma)
  - `{x:_}` – Tausender-Trennzeichen (Unterstrich)
  - `{x:.1%}` – Prozentangabe (multipliziert mit 100, fügt % hinzu)
  - `{x:+.2f}` – Mit Vorzeichen anzeigen
  - `{x:08.2f}` – Mit führenden Nullen auffüllen auf Breite 8

- **`.format()`-Methode** (Python 2.6+, String-Methode)
  - Ältere, aber immer noch verwendete Formatierungsmethode
  - Platzhalter `{}` werden durch übergebene Argumente ersetzt
  - Positionsangabe: `"{0} {1}".format(a, b)` oder `"{1} {0}".format(a, b)`
  - Benannte Argumente: `"{name} ist {alter}".format(name="Ada", alter=25)`
  - Formatspezifikationen wie bei f-Strings: `"{:.2f}".format(pi)`
  - Signatur: `str.format(*args, **kwargs)` → `str`
  - Beispiel: `"Hallo {0}, du bist {1} Jahre alt".format("Bob", 30)`

- **%-Operator (Legacy, String Formatting)** (Python 1.x+)
  - Veraltete C-style Formatierung
  - Platzhalter: `%s` (String), `%d` (Integer), `%f` (Float), `%.2f` (Float mit 2 Dezimalstellen)
  - Syntax: `"Text %s" % (wert,)` oder `"Text %s %d" % (str_wert, int_wert)`
  - Signatur: `format_string % values` → `str`
  - Beispiel: `"Pi: %.2f" % (pi,)` → `"Pi: 3.14"`
  - **Nicht empfohlen für neuen Code** – verwende stattdessen f-Strings

#### Erweiterte `print()`-Funktionalität

- **`print()`-Parameter `sep`** (Python 3.0+)
  - Legt das Trennzeichen zwischen mehreren Argumenten fest
  - Standard: `sep=' '` (Leerzeichen)
  - Signatur: `print(*objects, sep=' ')`
  - Beispiel: `print("A", "B", "C", sep="-")` → `A-B-C`

- **`print()`-Parameter `end`** (Python 3.0+)
  - Legt an, was am Ende der Ausgabe angefügt wird
  - Standard: `end='\n'` (Zeilenumbruch)
  - Signatur: `print(*objects, end='\n')`
  - Beispiel: `print("Text", end="")` → kein Zeilenumbruch danach

- **`print()`-Parameter `flush`** (Python 3.3+)
  - Erzwingt sofortiges Schreiben der Ausgabe (ohne Pufferung)
  - Standard: `flush=False`
  - Signatur: `print(*objects, flush=False)`
  - Nützlich für Fortschrittsanzeigen oder Log-Ausgaben
  - Beispiel: `print("Lade...", end="", flush=True)`

#### Escape-Sequenzen und Spezial-Strings

- **Escape-Sequenzen**
  - `\n` – Zeilenumbruch (Newline)
  - `\t` – Tabulator (Tab)
  - `\\` – Backslash selbst
  - `\'` – Einfaches Anführungszeichen
  - `\"` – Doppeltes Anführungszeichen
  - `\r` – Carriage Return (Wagenrücklauf)
  - `\b` – Backspace
  - Beispiel: `"Zeile 1\nZeile 2"` → zwei Zeilen

- **Raw Strings (r-Strings)** (Python 2.0+)
  - Strings, in denen Backslashes nicht als Escape-Zeichen interpretiert werden
  - Syntax: `r"Text mit \backslash"`
  - Nützlich für Windows-Pfade und reguläre Ausdrücke
  - Beispiel: `r"C:\Users\Ada"` → `"C:\Users\Ada"` (keine Escape-Interpretation)

- **Mehrzeilige Strings (Triple Quotes)** (Python 1.0+)
  - Strings über mehrere Zeilen mit `"""..."""` oder `'''...'''`
  - Behalten alle Zeilenumbrüche und Einrückungen
  - Können auch als Docstrings verwendet werden
  - Beispiel:
    ```python
    text = """Zeile 1
    Zeile 2
    Zeile 3"""
    ```

#### Datei-Ein- und Ausgabe

- **`open(filename, mode='r', encoding=None)`** (Built-in)
  - Öffnet eine Datei und gibt ein File-Objekt zurück
  - Parameter `mode`:
    - `"r"` – Read (Lesen, Standard, Datei muss existieren)
    - `"w"` – Write (Schreiben, überschreibt existierende Datei, erstellt neue)
    - `"a"` – Append (Anhängen am Ende, erstellt neue Datei falls nicht existent)
    - `"r+"` – Read/Write (Lesen und Schreiben)
    - `"b"` – Binär-Modus (z.B. `"rb"`, `"wb"`)
  - Parameter `encoding`: z.B. `"utf-8"` (empfohlen für Textdateien)
  - Signatur: `open(file, mode='r', encoding=None, ...)` → `TextIOWrapper` (File-Objekt)
  - Beispiel: `datei = open("daten.txt", "r")`
  - **Wichtig**: Datei muss mit `.close()` geschlossen werden oder via `with`-Statement

- **File-Objekt-Methoden**:
  
  - **`.write(string)`** – Schreibt String in Datei
    - Gibt Anzahl geschriebener Zeichen zurück
    - Fügt **keine** automatischen Zeilenumbrüche hinzu (manuell `\n` anfügen)
    - Signatur: `file.write(s)` → `int`
    - Beispiel: `datei.write("Hallo Welt\n")`
  
  - **`.read(size=-1)`** – Liest gesamten Dateiinhalt (oder `size` Zeichen)
    - Parameter `size`: Anzahl zu lesender Zeichen (-1 = alles)
    - Gibt String zurück
    - Signatur: `file.read(size=-1)` → `str`
    - Beispiel: `inhalt = datei.read()`
  
  - **`.readline(size=-1)`** – Liest eine einzelne Zeile
    - Inkludiert den Zeilenumbruch `\n` am Ende
    - Gibt leeren String zurück bei EOF (End of File)
    - Signatur: `file.readline(size=-1)` → `str`
    - Beispiel: `zeile = datei.readline()`
  
  - **`.readlines(hint=-1)`** – Liest alle Zeilen als Liste von Strings
    - Jeder String endet mit `\n` (außer ggf. letzte Zeile)
    - Signatur: `file.readlines(hint=-1)` → `list[str]`
    - Beispiel: `zeilen = datei.readlines()`
  
  - **`.close()`** – Schließt die Datei
    - Gibt Ressourcen frei und schreibt gepufferte Daten
    - Nach `.close()` können keine weiteren Operationen durchgeführt werden
    - Signatur: `file.close()` → `None`
    - Beispiel: `datei.close()`

- **`with`-Statement (Context Manager)** (Python 2.5+)
  - Garantiert automatisches Schließen von Ressourcen (z.B. Dateien)
  - Syntax: `with open(filename, mode) as variable:`
  - Datei wird automatisch geschlossen, auch bei Fehlern im Block
  - **Best Practice**: Immer `with` verwenden statt manuellem `open()` und `.close()`
  - Signatur: `with expression as target:`
  - Beispiel:
    ```python
    with open("daten.txt", "r") as datei:
        inhalt = datei.read()
    # Datei ist hier automatisch geschlossen
    ```

#### String-Methoden (Ergänzungen)

- **`.upper()`** (String-Methode)
  - Konvertiert alle Buchstaben zu Großbuchstaben
  - Signatur: `str.upper()` → `str`
  - Beispiel: `"hallo".upper()` → `"HALLO"`

- **`.lower()`** (String-Methode)
  - Konvertiert alle Buchstaben zu Kleinbuchstaben
  - Signatur: `str.lower()` → `str`
  - Beispiel: `"HALLO".lower()` → `"hallo"`

- **`.strip(chars=None)`** (String-Methode)
  - Entfernt Whitespace (Leerzeichen, Tabs, Zeilenumbrüche) vom Anfang und Ende
  - Optional: Entfernt spezifische Zeichen aus `chars`
  - Signatur: `str.strip(chars=None)` → `str`
  - Beispiel: `"  Hallo  \n".strip()` → `"Hallo"`

- **`.split(sep=None, maxsplit=-1)`** (String-Methode)
  - Teilt String an Trennzeichen `sep` in Liste von Strings
  - Standard: `sep=None` (teilt an jedem Whitespace)
  - Signatur: `str.split(sep=None, maxsplit=-1)` → `list[str]`
  - Beispiel: `"a,b,c".split(",")` → `["a", "b", "c"]`

### Konzepte und Best Practices

- **f-Strings sind die empfohlene Methode** für String-Formatierung in Python 3.6+
  - Lesbarer, schneller und weniger fehleranfällig als `.format()` oder `%`
  - Verwende `.format()` nur, wenn der Format-String wiederverwendet wird
  - Verwende `%` nur bei Legacy-Code-Wartung

- **Dateien immer mit `with`-Statement öffnen**
  - Garantiert korrektes Schließen auch bei Fehlern
  - Verhindert Ressourcen-Lecks und Datenverlust
  - Bessere Lesbarkeit durch klare Scope-Definition

- **Escape-Sequenzen und Raw Strings**
  - Raw Strings (`r"..."`) für Windows-Pfade und reguläre Ausdrücke
  - Normale Strings mit Escape-Sequenzen für Text mit Spezialzeichen
  - Triple Quotes für mehrzeilige Texte und Docstrings

- **Append-Modus für Log-Dateien**
  - Verwende `"a"` statt `"w"` zum Anhängen, um Datenverlust zu vermeiden
  - `"w"` löscht existierenden Inhalt komplett

### Notizen

- f-Strings wurden in Python 3.6 eingeführt und sind seit Python 3.8 die empfohlene Methode
- Der `flush`-Parameter von `print()` ist erst seit Python 3.3 verfügbar
- `open()` unterstützt seit Python 3 standardmäßig Text-Modus mit Unicode (UTF-8)
- In Python 2 musste `io.open()` für Unicode-Support verwendet werden
- Windows verwendet `\r\n` als Zeilenumbruch, Unix/Linux/Mac `\n` – Python normalisiert dies automatisch im Text-Modus
- CSV-Dateien sollten ohne Leerzeichen nach Kommas geschrieben werden (Standard-Konvention)

---

## V03 (2026-01-01) – Variablen Management & Datentypen

### Neu eingeführt

#### Type Checking und Introspection

- **`type(obj)`** (Built-in)
  - Gibt den Datentyp des übergebenen Objekts zurück
  - Rückgabewert ist ein Typ-Objekt (z.B. `<class 'int'>`)
  - Signatur: `type(obj)` → `type`
  - Beispiel: `type(42)` → `<class 'int'>`, `type("Hallo")` → `<class 'str'>`
  - Verwendung für Typ-Vergleiche: `if type(x) == int:`

- **`isinstance(obj, classinfo)`** (Built-in)
  - Prüft, ob `obj` eine Instanz von `classinfo` ist
  - Berücksichtigt Vererbung (z.B. `bool` ist Subtyp von `int`)
  - `classinfo` kann auch Tupel von Typen sein
  - Signatur: `isinstance(obj, classinfo)` → `bool`
  - Beispiel: `isinstance(42, int)` → `True`, `isinstance(True, int)` → `True`
  - Bevorzugt gegenüber `type()` für Typ-Checks
  - Mehrere Typen: `isinstance(x, (int, float))` prüft, ob `x` int ODER float ist

- **`id(obj)`** (Built-in)
  - Gibt die Identität (Speicheradresse) eines Objekts zurück
  - Rückgabewert ist eine eindeutige Integer-ID
  - Nützlich zur Demonstration von Mutability/Immutability
  - Signatur: `id(obj)` → `int`
  - Beispiel: `id("Hallo")` → `140234567890123` (Adresse variiert)
  - Zwei Objekte mit gleicher ID sind **dasselbe** Objekt im Speicher

#### Type Casting (Erweitert)

- **`bool(x)`** (Built-in)
  - Konvertiert Wert `x` in Boolean (`True` oder `False`)
  - Bereits in V01 als Datentyp erwähnt, hier als Casting-Funktion vertieft
  - **Falsy Values**: `0`, `0.0`, `""`, `[]`, `None`, `False` → `False`
  - **Truthy Values**: Alle anderen Werte → `True`
  - Signatur: `bool(x)` → `bool`
  - Beispiel: `bool(0)` → `False`, `bool(42)` → `True`, `bool("")` → `False`
  - Wichtig: `bool("0")` → `True` (String "0" ist nicht leer!)

- **`round(number, ndigits=None)`** (Built-in)
  - Rundet eine Zahl auf `ndigits` Dezimalstellen
  - Ohne `ndigits`: Rundet zur nächsten Ganzzahl
  - Verwendet "Banker's Rounding" (Round Half to Even) bei `.5`
  - Signatur: `round(number, ndigits=None)` → `float` oder `int`
  - Beispiel: `round(3.14159, 2)` → `3.14`, `round(2.5)` → `2` (Banker's Rounding!)
  - Unterschied zu `int()`: `round()` rundet mathematisch, `int()` schneidet ab

#### Min/Max-Funktionen

- **`min(iterable)` / `min(*args)`** (Built-in)
  - Gibt das kleinste Element aus einem Iterable oder mehreren Argumenten zurück
  - Signatur: `min(iterable)` → Element oder `min(arg1, arg2, ...)` → Element
  - Beispiel: `min([5, 2, 8])` → `2`, `min(5, 2, 8)` → `2`
  - Funktioniert mit allen vergleichbaren Typen (int, float, str, etc.)
  - Bei Strings: Lexikographischer Vergleich

- **`max(iterable)` / `max(*args)`** (Built-in)
  - Gibt das größte Element aus einem Iterable oder mehreren Argumenten zurück
  - Signatur: `max(iterable)` → Element oder `max(arg1, arg2, ...)` → Element
  - Beispiel: `max([5, 2, 8])` → `8`, `max(5, 2, 8)` → `8`
  - Funktioniert analog zu `min()`

#### String-Methoden (Validierung und Analyse)

- **`str.isdigit()`** (String-Methode)
  - Prüft, ob alle Zeichen im String Ziffern sind (0-9)
  - Gibt `False` zurück bei leerem String
  - Signatur: `str.isdigit()` → `bool`
  - Beispiel: `"123".isdigit()` → `True`, `"12.3".isdigit()` → `False`, `"-5".isdigit()` → `False`
  - Nützlich zur Validierung vor `int()`-Konvertierung

- **`str.isalpha()`** (String-Methode)
  - Prüft, ob alle Zeichen im String Buchstaben sind (a-z, A-Z, Unicode-Buchstaben)
  - Gibt `False` zurück bei leerem String oder wenn Ziffern/Leerzeichen enthalten
  - Signatur: `str.isalpha()` → `bool`
  - Beispiel: `"Hallo".isalpha()` → `True`, `"Hallo123".isalpha()` → `False`

- **`str.isupper()`** (String-Methode)
  - Prüft, ob alle Buchstaben im String Großbuchstaben sind
  - Ignoriert Nicht-Buchstaben-Zeichen (Ziffern, Leerzeichen, etc.)
  - Gibt `False` zurück, wenn keine Buchstaben vorhanden
  - Signatur: `str.isupper()` → `bool`
  - Beispiel: `"HALLO".isupper()` → `True`, `"HALLO123".isupper()` → `True`, `"Hallo".isupper()` → `False`

- **`str.islower()`** (String-Methode)
  - Prüft, ob alle Buchstaben im String Kleinbuchstaben sind
  - Ignoriert Nicht-Buchstaben-Zeichen
  - Gibt `False` zurück, wenn keine Buchstaben vorhanden
  - Signatur: `str.islower()` → `bool`
  - Beispiel: `"hallo".islower()` → `True`, `"hallo123".islower()` → `True`, `"Hallo".islower()` → `False`

- **`str.lstrip(chars=None)`** (String-Methode)
  - Entfernt Zeichen vom **linken** Ende des Strings
  - Parameter `chars`: Zu entfernende Zeichen (Standard: Whitespace)
  - Signatur: `str.lstrip(chars=None)` → `str`
  - Beispiel: `"  Hallo".lstrip()` → `"Hallo"`, `"-42".lstrip('-')` → `"42"`
  - Verwandt: `.rstrip()` (rechts), `.strip()` (beide Seiten, bereits in V02)

- **`str.count(sub)`** (String-Methode)
  - Zählt, wie oft der Substring `sub` im String vorkommt
  - Überlappungen werden nicht gezählt
  - Signatur: `str.count(sub)` → `int`
  - Beispiel: `"Hallo".count('l')` → `2`, `"3.14.15".count('.')` → `2`

#### Variablen-Scope

- **`global`-Keyword** (Keyword)
  - Deklariert eine Variable als global innerhalb einer Funktion
  - Ermöglicht Modifikation globaler Variablen aus Funktionen heraus
  - Syntax: `global variable_name`
  - Verwendung:
    ```python
    counter = 0
    def increment():
        global counter  # Ohne global würde neue lokale Variable erzeugt
        counter += 1
    ```
  - **Warnung**: Sparsam verwenden! Globale Variablen erschweren Debugging und Testing
  - Bevorzuge Funktionsparameter und Rückgabewerte

#### Konzepte und Sprachmerkmale

- **Immutable vs. Mutable**
  - **Immutable (unveränderlich)**: Objekte können nach Erzeugung nicht geändert werden
    - Typen: `int`, `float`, `str`, `bool`, `tuple`
    - Operationen erzeugen neue Objekte
    - Beispiel: `text = text + "!"` erzeugt neuen String
  - **Mutable (veränderlich)**: Objekte können nach Erzeugung modifiziert werden
    - Typen: `list`, `dict`, `set` (werden in V08 ausführlich behandelt)
    - Operationen ändern Objekt in-place
    - Beispiel: `liste.append(4)` ändert existierende Liste
  - Bedeutung: Beeinflusst Performance, Seiteneffekte und Verwendbarkeit als Dictionary-Keys

- **Variablen-Scope**
  - **Globaler Scope**: Variablen außerhalb von Funktionen, überall sichtbar
  - **Lokaler Scope**: Variablen innerhalb von Funktionen, nur dort sichtbar
  - **LEGB-Regel**: Local → Enclosing → Global → Built-in (Reihenfolge der Namensauflösung)
  - Lokale Variablen überdecken gleichnamige globale Variablen

- **Multiple Assignment**
  - Mehreren Variablen gleichzeitig denselben Wert zuweisen
  - Syntax: `x = y = z = wert`
  - Beispiel: `a = b = c = 0` setzt alle drei auf 0
  - **Vorsicht bei mutable Typen**: `a = b = []` → beide zeigen auf dieselbe Liste!

- **Value Unpacking (Tuple Unpacking)**
  - Mehrere Werte gleichzeitig verschiedenen Variablen zuweisen
  - Syntax: `x, y, z = wert1, wert2, wert3`
  - Intern arbeitet Python mit Tupeln: `(x, y) = (1, 2)`
  - Beispiel: `a, b = 10, 20` oder Variablen tauschen: `a, b = b, a`
  - Funktioniert auch mit Funktionsrückgaben: `min_val, max_val = min(liste), max(liste)`
  - **Fehler**: Anzahl der Variablen muss mit Anzahl der Werte übereinstimmen

### Konzepte und Best Practices

- **`isinstance()` bevorzugen**: Für Typ-Checks bevorzuge `isinstance()` statt `type()`, da es Vererbung berücksichtigt
- **Banker's Rounding beachten**: `round(2.5)` ergibt `2`, nicht `3` (Round Half to Even Strategie)
- **Unveränderlichkeit verstehen**: String-Operationen sind ineffizient in Schleifen, da neue Objekte erzeugt werden
- **`global` sparsam verwenden**: Globale Variablen erschweren Wartung. Bevorzuge Parameter und Rückgabewerte
- **Validierung vor Konvertierung**: Prüfe mit `.isdigit()` oder ähnlichen Methoden vor `int()`/`float()`, um `ValueError` zu vermeiden
- **Falsy Values kennen**: `bool("0")` ist `True` (nicht-leerer String), aber `bool(0)` ist `False`

### Notizen

- `isinstance()` wurde in Python 2.2 eingeführt und ist seit Python 3 die empfohlene Methode für Typ-Checks
- `round()` verwendet seit Python 3 "Banker's Rounding" (IEEE 754), in Python 2 war es "Round Half Up"
- `id()` gibt die CPython-Speicheradresse zurück; in anderen Python-Implementierungen kann es eine andere eindeutige ID sein
- Boolean-Datentyp `bool` ist ein Subtyp von `int`: `True + True` ergibt `2`
- Listen-Operationen (`.append()`, etc.) werden in V08 ausführlich behandelt, hier nur für Mutability-Demonstration verwendet
- String-Methoden für Validierung (`.isdigit()`, `.isalpha()`) sind hilfreich, decken aber nicht alle Fälle ab (z.B. negative Zahlen benötigen `.lstrip('-')`)
---

## V04 (2026-01-02) – Logische Ausdrücke (Boolsche Algebra)

### Neu eingeführt

#### Vergleichsoperatoren

- **`==` (Gleichheit / Equality)**
  - Prüft, ob zwei Werte gleich sind
  - Gibt `True` oder `False` zurück
  - Signatur: `a == b` → `bool`
  - Beispiel: `5 == 5` → `True`, `5 == 10` → `False`
  - **Wichtig**: `==` ist Vergleich, `=` ist Zuweisung!

- **`!=` (Ungleichheit / Not Equal)**
  - Prüft, ob zwei Werte unterschiedlich sind
  - Signatur: `a != b` → `bool`
  - Beispiel: `5 != 10` → `True`, `5 != 5` → `False`

- **`<` (Kleiner als / Less Than)**
  - Prüft, ob linker Wert kleiner als rechter ist
  - Signatur: `a < b` → `bool`
  - Beispiel: `5 < 10` → `True`, `10 < 5` → `False`

- **`>` (Größer als / Greater Than)**
  - Prüft, ob linker Wert größer als rechter ist
  - Signatur: `a > b` → `bool`
  - Beispiel: `10 > 5` → `True`, `5 > 10` → `False`

- **`<=` (Kleiner oder gleich / Less or Equal)**
  - Prüft, ob linker Wert kleiner oder gleich rechter ist
  - Signatur: `a <= b` → `bool`
  - Beispiel: `5 <= 10` → `True`, `5 <= 5` → `True`, `10 <= 5` → `False`

- **`>=` (Größer oder gleich / Greater or Equal)**
  - Prüft, ob linker Wert größer oder gleich rechter ist
  - Signatur: `a >= b` → `bool`
  - Beispiel: `10 >= 5` → `True`, `5 >= 5` → `True`, `5 >= 10` → `False`

**Eigenschaften:**
- Funktionieren mit Zahlen, Strings (lexikographisch), und anderen vergleichbaren Typen
- Liefern immer Boolean-Werte (`True` oder `False`)
- Können verkettet werden (siehe unten)

#### Logische Operatoren

- **`and` (Logisches UND / Logical AND)**
  - Gibt `True` zurück, wenn **beide** Operanden `True` sind
  - Nutzt Kurzschlussauswertung: Stoppt bei erstem `False`
  - Signatur: `a and b` → `bool`
  - Beispiel: `True and True` → `True`, `True and False` → `False`
  - Wahrheitstabelle:
    | A | B | A and B |
    |---|---|---------|
    | False | False | False |
    | False | True | False |
    | True | False | False |
    | True | True | True |

- **`or` (Logisches ODER / Logical OR)**
  - Gibt `True` zurück, wenn **mindestens ein** Operand `True` ist
  - Nutzt Kurzschlussauswertung: Stoppt bei erstem `True`
  - Signatur: `a or b` → `bool`
  - Beispiel: `True or False` → `True`, `False or False` → `False`
  - Wahrheitstabelle:
    | A | B | A or B |
    |---|---|--------|
    | False | False | False |
    | False | True | True |
    | True | False | True |
    | True | True | True |

- **`not` (Logische Negation / Logical NOT)**
  - Kehrt Boolean-Wert um (`True` → `False`, `False` → `True`)
  - Signatur: `not a` → `bool`
  - Beispiel: `not True` → `False`, `not False` → `True`
  - Wahrheitstabelle:
    | A | not A |
    |---|-------|
    | False | True |
    | True | False |

#### Bitweise Operatoren (Einführung)

- **`^` (Bitweises XOR für Integer)**
  - Führt XOR-Operation auf Bit-Ebene durch
  - Signatur: `a ^ b` → `int`
  - Beispiel: `5 ^ 3` → `6` (binär: `0101 ^ 0011 = 0110`)
  - Nützlich für Bit-Manipulation, Verschlüsselung, Paritätsprüfung
  - **Hinweis**: Für Boolean-XOR verwende `a != b`

#### Konzepte und Sprachmerkmale

- **Verkettete Vergleiche (Chained Comparisons)** (Python-spezifisches Feature)
  - Python erlaubt mathematische Notation für Bereichsprüfungen
  - Syntax: `a < b < c` statt `a < b and b < c`
  - Beispiel: `10 <= alter <= 100` prüft Bereich [10, 100]
  - Funktioniert mit beliebig vielen Vergleichen: `a < b < c < d`
  - **Vorteil**: Lesbarer und effizienter (Mittelwert wird nur einmal ausgewertet)
  - Beispiele:
    ```python
    18 <= alter < 65   # Erwachsen, nicht Senior
    0 < x <= 100       # Positiv und nicht über 100
    x == y == z        # Alle drei gleich
    ```

- **Kurzschlussauswertung (Short-Circuit Evaluation / Lazy Evaluation)**
  - Python wertet logische Ausdrücke von links nach rechts aus
  - Bricht ab, sobald Ergebnis feststeht
  - **Bei `and`**: Wenn linker Operand `False`, wird rechter **nicht** ausgewertet
    - `False and x` → `False` (x wird ignoriert)
    - `True and x` → x wird ausgewertet
  - **Bei `or`**: Wenn linker Operand `True`, wird rechter **nicht** ausgewertet
    - `True or x` → `True` (x wird ignoriert)
    - `False or x` → x wird ausgewertet
  - **Vorteile**:
    - Performance: Spart unnötige Berechnungen
    - Sicherheit: Verhindert Fehler (z.B. Division durch Null)
  - Beispiel:
    ```python
    if x != 0 and y / x > 10:  # Kein ZeroDivisionError!
        # Division wird nur ausgeführt, wenn x != 0
    ```

- **Operator-Präzedenz (Operator Precedence)**
  - Reihenfolge der Auswertung logischer Operatoren (höchste → niedrigste Priorität):
    1. **Vergleichsoperatoren**: `==`, `!=`, `<`, `>`, `<=`, `>=`
    2. **`not`**: Negation
    3. **`and`**: Konjunktion
    4. **`or`**: Disjunktion
  - Beispiel:
    ```python
    not x and y     # = (not x) and y
    x or y and z    # = x or (y and z)
    ```
  - **Best Practice**: Klammern verwenden für Klarheit!
    ```python
    (x > 0 and y > 0) or (z > 0 and w > 0)  # Explizit und lesbar
    ```

- **Truthy und Falsy Values (Truth Value Testing)**
  - Jedes Python-Objekt kann in Boolean-Kontext als `True` oder `False` interpretiert werden
  - **Falsy Values** (werden als `False` interpretiert):
    - `False` (der Boolean-Wert selbst)
    - `None` (das Null-Objekt)
    - Numerische Nullen: `0`, `0.0`, `0j` (komplexe Null)
    - Leere Sequenzen: `""` (leerer String), `[]` (leere Liste), `()` (leeres Tupel)
    - Leere Collections: `{}` (leeres Dictionary), `set()` (leeres Set)
  - **Truthy Values** (werden als `True` interpretiert):
    - Alle anderen Werte!
    - Nicht-null Zahlen: `1`, `-5`, `3.14`
    - Nicht-leere Strings: `"Hallo"`, `"0"` (String "0" ist **truthy**!)
    - Nicht-leere Collections: `[1, 2]`, `{"key": "value"}`
  - **Anwendung**: Kompakte Existenz- und Leerprüfungen
    ```python
    if liste:              # Statt: if len(liste) > 0:
        print("Nicht leer")
    
    if not benutzer:       # Statt: if benutzer is None:
        print("Nicht angemeldet")
    ```
  - **Wichtig**: `if x:` ist nicht das gleiche wie `if x is not None:`
    - `if x:` ist `False` für `0`, `""`, `[]`, etc.
    - `if x is not None:` ist nur `False` für `None`

- **De Morgan'sche Gesetze in Python**
  - Umformungsregeln für logische Ausdrücke
  - **Gesetz 1**: `not (a and b)` = `(not a) or (not b)`
  - **Gesetz 2**: `not (a or b)` = `(not a) and (not b)`
  - Nützlich zur Vereinfachung komplexer Bedingungen
  - Beispiel:
    ```python
    # Kompliziert:
    if not (ist_student or ist_senior):
        pass
    
    # Vereinfacht mit De Morgan:
    if not ist_student and not ist_senior:
        pass
    ```

#### Built-in Funktionen (Vorschau/Erwähnt)

- **`abs(x)`** (Built-in) - *Erwähnt in Beispielen*
  - Gibt den Absolutbetrag (Betrag ohne Vorzeichen) einer Zahl zurück
  - Signatur: `abs(x)` → `number`
  - Beispiel: `abs(-5)` → `5`, `abs(3.14)` → `3.14`
  - Nützlich für Distanzberechnungen und Toleranzprüfungen bei Floats

- **`any(iterable)`** (Built-in) - *Als Vorschau erwähnt, wird in V08 ausführlich behandelt*
  - Gibt `True` zurück, wenn mindestens ein Element im Iterable `True` ist
  - Signatur: `any(iterable)` → `bool`
  - Beispiel: `any([False, True, False])` → `True`
  - Äquivalent zu mehrfachen `or`-Verknüpfungen
  - Wird in V04 in Passwort-Beispielen verwendet (Vorschau)

### Konzepte und Best Practices

- **Klammern für Lesbarkeit**: Auch wenn Python klare Präzedenzregeln hat, verbessern Klammern die Lesbarkeit erheblich
  ```python
  # Funktioniert, aber schwer lesbar:
  if x > 0 and y > 0 or z > 0
  
  # Besser mit Klammern:
  if (x > 0 and y > 0) or z > 0
  ```

- **`==` vs. `=` nicht verwechseln**:
  - `=` ist Zuweisung: `x = 5`
  - `==` ist Vergleich: `x == 5`
  - Häufiger Anfängerfehler: `if x = 5:` → `SyntaxError`

- **Verkettete Vergleiche nutzen**: Pythonischer und lesbarer als `and`-Verknüpfungen
  ```python
  # Gut:
  if 18 <= alter < 65:
  
  # Funktioniert, aber weniger lesbar:
  if alter >= 18 and alter < 65:
  ```

- **Kurzschlussauswertung für Performance**: "Billige" Checks zuerst bei `and`
  ```python
  # Gut: Einfacher Check zuerst
  if benutzer_eingeloggt and aufwaendige_berechnung():
      pass
  
  # Schlecht: Teure Operation wird immer ausgeführt
  if aufwaendige_berechnung() and benutzer_eingeloggt:
      pass
  ```

- **Truthy/Falsy idiomatisch nutzen**:
  ```python
  # Pythonisch:
  if liste:
      print("Liste nicht leer")
  
  # Explizit (umständlich):
  if len(liste) > 0:
      print("Liste nicht leer")
  ```

- **Float-Vergleiche mit Toleranz**: Wegen Rundungsfehlern nie direkt `==` verwenden
  ```python
  # Problematisch:
  if 0.1 + 0.2 == 0.3:  # False!
  
  # Richtig mit Toleranz:
  if abs((0.1 + 0.2) - 0.3) < 1e-10:  # True
  ```

- **Explizite None-Checks**: Unterscheide zwischen Falsy und None
  ```python
  # Prüft auf Falsy (0, "", [], None, etc.):
  if not x:
      pass
  
  # Prüft nur auf None:
  if x is None:
      pass
  ```

### Notizen

- Verkettete Vergleiche sind ein Python-spezifisches Feature (in vielen anderen Sprachen nicht verfügbar)
- Kurzschlussauswertung ist in Python garantiert (im Gegensatz zu manchen anderen Sprachen)
- Die Unterscheidung zwischen Truthy/Falsy ist fundamental für pythonischen Code-Stil
- `bool` ist ein Subtyp von `int` in Python: `True == 1` und `False == 0` sind wahr
- Bei `and`/`or` mit nicht-Boolean-Werten: Rückgabewert ist der zuletzt ausgewertete Wert, nicht zwingend `True`/`False`
  - `"" or "Hallo"` → `"Hallo"` (nicht `True`!)
  - `5 and 10` → `10` (nicht `True`!)
  - Dieses Verhalten wird für Default-Werte genutzt: `x = eingabe or "Standard"`
- XOR gibt es nicht als logischen Operator für Booleans; verwende `!=` für Boolean-XOR
- Float-Vergleiche sind problematisch wegen IEEE 754 Rundungsfehlern (siehe V02)

---

## V05 (2026-01-02) – Verzweigungen (if, if-elif-else)

### Neu eingeführt

#### Kontrollstrukturen: Bedingte Ausführung

- **`if`-Anweisung** (Python Keyword)
  - Führt einen Codeblock nur aus, wenn eine Bedingung `True` ist
  - Syntax: `if Bedingung:`
  - Erfordert Doppelpunkt nach der Bedingung
  - Der Codeblock muss eingerückt sein (Standard: 4 Leerzeichen)
  - Signatur: `if expression:`
  - Beispiel:
    ```python
    if alter >= 18:
        print("Volljährig")
    ```

- **`else`-Klausel** (Python Keyword)
  - Definiert einen alternativen Codeblock, der ausgeführt wird, wenn die if-Bedingung `False` ist
  - Syntax: `else:`
  - Kein Bedingungsausdruck (keine Klammer nach else)
  - Signatur: `else:`
  - Beispiel:
    ```python
    if temperatur <= 0:
        print("Gefroren")
    else:
        print("Nicht gefroren")
    ```
  - **Wichtig**: else ist optional – eine if-Anweisung kann auch ohne else existieren

- **`elif`-Klausel** (Python Keyword, Abkürzung für "else if")
  - Fügt zusätzliche Bedingungen nach einem `if` hinzu
  - Syntax: `elif Bedingung:`
  - Wird nur geprüft, wenn alle vorherigen Bedingungen `False` waren
  - Ermöglicht mehrfache Verzweigungen (mehr als zwei Pfade)
  - Beliebig viele elif-Klauseln möglich
  - Signatur: `elif expression:`
  - Beispiel:
    ```python
    if punkte >= 90:
        note = "Sehr gut"
    elif punkte >= 80:
        note = "Gut"
    elif punkte >= 70:
        note = "Befriedigend"
    else:
        note = "Nicht bestanden"
    ```
  - **Wichtig**: Nur der erste erfüllte Zweig wird ausgeführt, alle weiteren werden übersprungen

#### Ternärer Operator (Conditional Expression)

- **Ternärer Operator** (Python 2.5+, Sprachkonstrukt)
  - Kompakte Schreibweise für einfache if-else-Zuweisungen in einer Zeile
  - Syntax: `wert_wenn_wahr if Bedingung else wert_wenn_falsch`
  - Die Bedingung steht in der Mitte, davor der True-Wert, danach der False-Wert
  - Signatur: `expression1 if condition else expression2` → Wert
  - Beispiel:
    ```python
    # Normale Schreibweise:
    if x >= 0:
        absolut = x
    else:
        absolut = -x
    
    # Ternärer Operator:
    absolut = x if x >= 0 else -x
    ```
  - Weitere Beispiele:
    ```python
    status = "Aktiv" if ist_eingeloggt else "Inaktiv"
    maximum = a if a > b else b
    print(f"Du bist {'volljährig' if alter >= 18 else 'minderjährig'}")
    ```
  - **Best Practice**: Nur für einfache, einzeilige Entscheidungen verwenden

#### Platzhalter-Statement

- **`pass`-Statement** (Python Keyword)
  - Eine Null-Operation, die nichts tut
  - Dient als syntaktischer Platzhalter für leere Codeblöcke
  - Python erlaubt keine leeren Blöcke – `pass` verhindert `IndentationError`
  - Syntax: `pass`
  - Signatur: `pass`
  - Beispiel:
    ```python
    if benutzer_rolle == "Admin":
        pass  # TODO: Admin-Funktionen implementieren
    elif benutzer_rolle == "Moderator":
        pass  # TODO: Moderator-Funktionen implementieren
    else:
        print("Normaler Benutzer")
    ```
  - **Verwendungszwecke**:
    - Platzhalter während der Entwicklung
    - Explizites "nichts tun" (z.B. in Ausnahmebehandlung)
    - Syntaxanforderung bei leeren Funktionen/Klassen (wird in späteren Vorlesungen relevant)

#### Konzepte und Sprachmerkmale

- **Einrückung als Syntax** (Python-spezifisches Merkmal)
  - Python verwendet **Whitespace (Einrückung)** zur Definition von Codeblöcken
  - Standard: 4 Leerzeichen pro Einrückungsebene
  - **Konsistenz ist verpflichtend**: Mische niemals Leerzeichen und Tabs
  - Alle Zeilen eines Blocks müssen gleich eingerückt sein
  - Falsche Einrückung führt zu `IndentationError`
  - Beispiel:
    ```python
    if bedingung:
        # Dieser Block ist eingerückt (Teil des if)
        anweisung1
        anweisung2
        if nested_bedingung:
            # Verschachtelt: doppelte Einrückung
            anweisung3
    # Hier endet der Block (keine Einrückung mehr)
    ```
  - **Vorteil**: Erzwingt lesbaren Code, keine geschweiften Klammern nötig
  - **Nachteil**: Kann bei Copy-Paste zu Fehlern führen, wenn Einrückung nicht passt

- **Verschachtelte Bedingungen** (Nesting)
  - if-Anweisungen können innerhalb anderer if-Anweisungen platziert werden
  - Jede Verschachtelungsebene erhöht die Einrückung um 4 Leerzeichen
  - Beispiel:
    ```python
    if ist_premium:
        if bestellwert >= 100:
            rabatt = 0.20
        else:
            rabatt = 0.10
    else:
        if bestellwert >= 100:
            rabatt = 0.05
        else:
            rabatt = 0.0
    ```
  - **Best Practice**: Vermeide zu tiefe Verschachtelung (max. 2-3 Ebenen)
  - **Alternative**: Logische Operatoren (`and`, `or`) oder frühe Returns (in Funktionen)

- **Reihenfolge der Bedingungen** (Evaluation Order)
  - Bei if-elif-else werden Bedingungen **von oben nach unten** geprüft
  - **Sobald eine Bedingung `True` ist**, wird der Block ausgeführt und alle weiteren Bedingungen übersprungen
  - Wichtig für **überlappende Bedingungen**: Spezifischere Bedingungen zuerst
  - Beispiel:
    ```python
    # Richtig: Von spezifisch zu allgemein
    if x > 100:
        print("Sehr groß")
    elif x > 50:
        print("Groß")
    elif x > 0:
        print("Positiv")
    
    # Falsch: Zu allgemeine Bedingung zuerst
    if x > 0:
        print("Positiv")  # Fängt ALLE positiven Zahlen, auch > 100
    elif x > 100:
        print("Sehr groß")  # Wird nie erreicht!
    ```

- **Mehrere separate if vs. if-elif-else**
  - **Mehrere separate if**: Alle Bedingungen werden immer geprüft
    ```python
    if temperatur < 0:
        print("Gefroren")
    if temperatur >= 0 and temperatur < 20:
        print("Kühl")
    if temperatur >= 20:
        print("Warm")
    # Alle drei if-Blöcke werden geprüft (ineffizient)
    ```
  - **if-elif-else**: Nur bis zur ersten erfüllten Bedingung
    ```python
    if temperatur < 0:
        print("Gefroren")
    elif temperatur < 20:
        print("Kühl")
    else:
        print("Warm")
    # Nur die erste zutreffende Bedingung wird ausgeführt (effizienter)
    ```
  - **Wann welches?**
    - Verwende **separate if**, wenn Bedingungen **unabhängig** sind (mehrere können gleichzeitig zutreffen)
    - Verwende **if-elif-else**, wenn Bedingungen **sich gegenseitig ausschließen**

### Konzepte und Best Practices

- **Doppelpunkt nicht vergessen**: Nach `if`, `elif`, `else` ist der Doppelpunkt syntaktisch erforderlich
- **Konsistente Einrückung**: Immer 4 Leerzeichen verwenden, keine Tabs mischen
- **`==` für Vergleiche, `=` für Zuweisungen**: Häufiger Anfängerfehler
- **Spezifische Bedingungen zuerst**: Bei if-elif-else von spezifisch zu allgemein prüfen
- **elif statt mehrerer if**: Für sich ausschließende Fälle effizienter
- **Ternärer Operator sparsam**: Nur für einfache, gut lesbare Fälle
- **Verschachtelung begrenzen**: Nicht tiefer als 2-3 Ebenen, sonst refaktorieren

### Notizen

- Python 2.5 führte den ternären Operator ein (PEP 308), vorher gab es nur `and`/`or`-Workarounds
- Die Einrückungssyntax ist eine der charakteristischen Eigenschaften von Python, inspiriert von ABC
- `pass` ist auch in Funktionen, Klassen und Exception-Handling nützlich (wird in späteren Vorlesungen behandelt)
- Die Kombination von if-elif-else mit logischen Operatoren aus V04 ermöglicht sehr ausdrucksstarke Bedingungen
- Bedingte Ausführung ist eine der drei Grundstrukturen der strukturierten Programmierung (Sequenz, Verzweigung, Schleife)

---

## V06 (2026-01-02) – Schleifen (for, while) – Teil 1

### Neu eingeführt

#### Kontrollstrukturen: Schleifen

- **`for`-Schleife** (Python Keyword)
  - Iteriert über alle Elemente einer Sequenz (Iterable)
  - Syntax: `for variable in iterable:`
  - Der Schleifenkörper muss eingerückt sein (Standard: 4 Leerzeichen)
  - Die Schleifenvariable erhält in jedem Durchlauf den Wert des aktuellen Elements
  - Signatur: `for variable in iterable:`
  - Beispiel:
    ```python
    for i in range(5):
        print(i)  # Gibt 0, 1, 2, 3, 4 aus
    ```
  - **Wichtig**: Die Schleifenvariable sollte nicht im Schleifenkörper modifiziert werden (hat keine Auswirkung auf die Iteration)

- **`while`-Schleife** (Python Keyword)
  - Wiederholt einen Codeblock, solange eine Bedingung `True` ist
  - Syntax: `while bedingung:`
  - Kopfgesteuerte Schleife: Bedingung wird vor jedem Durchlauf geprüft
  - Der Schleifenkörper muss eingerückt sein
  - Signatur: `while condition:`
  - Beispiel:
    ```python
    x = 0
    while x < 5:
        print(x)
        x += 1  # Wichtig: Bedingung muss irgendwann False werden
    ```
  - **Warnung**: Ohne korrekte Abbruchbedingung entsteht eine Endlos-Schleife

#### Built-in Funktionen

- **`range(start=0, stop, step=1)`** (Built-in, Python 3.0+)
  - Erzeugt eine Sequenz von Ganzzahlen
  - In Python 3 ist `range()` ein spezieller Typ (kein Generator), der speicher-effizient arbeitet
  - Parameter:
    - `start`: Startwert (inklusive, Standard: 0)
    - `stop`: Endwert (exklusive, erforderlich)
    - `step`: Schrittweite (Standard: 1, kann auch negativ sein)
  - Signatur: `range(stop)` oder `range(start, stop)` oder `range(start, stop, step)` → `range`
  - Beispiel: `range(5)` → 0, 1, 2, 3, 4
  - Beispiel: `range(1, 6)` → 1, 2, 3, 4, 5
  - Beispiel: `range(0, 10, 2)` → 0, 2, 4, 6, 8
  - Beispiel: `range(10, 0, -1)` → 10, 9, 8, ..., 1 (Countdown)
  - **Wichtig**: `stop` ist immer exklusive

- **`enumerate(iterable, start=0)`** (Built-in)
  - Gibt ein Iterator-Objekt zurück, das Tupel aus Index und Wert erzeugt
  - Ermöglicht gleichzeitigen Zugriff auf Index und Element beim Iterieren
  - Parameter:
    - `iterable`: Die Sequenz, über die iteriert wird
    - `start`: Startwert für den Index (Standard: 0)
  - Signatur: `enumerate(iterable, start=0)` → `enumerate`
  - Rückgabe: Iterator von Tupeln `(index, element)`
  - Beispiel: 
    ```python
    fruechte = ['Apfel', 'Banane', 'Kirsche']
    for i, frucht in enumerate(fruechte):
        print(f"{i}: {frucht}")
    # Ausgabe:
    # 0: Apfel
    # 1: Banane
    # 2: Kirsche
    ```
  - Beispiel mit `start=1`:
    ```python
    for nr, frucht in enumerate(fruechte, start=1):
        print(f"{nr}. {frucht}")
    # Ausgabe:
    # 1. Apfel
    # 2. Banane
    # 3. Kirsche
    ```

#### Konzepte und Sprachmerkmale

- **String-Iteration**
  - Strings sind in Python Sequenzen von Zeichen
  - Die `for`-Schleife kann direkt über Zeichen eines Strings iterieren
  - Syntax: `for zeichen in text:`
  - Beispiel:
    ```python
    for buchstabe in "Python":
        print(buchstabe)  # P, y, t, h, o, n
    ```
  - Nützlich für Textanalyse, Validierung, Zeichenzählung

- **Akkumulation (Accumulation)**
  - Schrittweises Aufbauen eines Ergebnisses über mehrere Schleifendurchläufe
  - Variable wird vor der Schleife initialisiert und in jedem Durchlauf aktualisiert
  - **Summation**: `summe = 0`, dann `summe += wert`
  - **Produkt**: `produkt = 1`, dann `produkt *= wert`
  - **String-Konkatenation**: `text = ""`, dann `text += zeichen` (ineffizient, siehe Warnung in V06-Skript)
  - **Wichtig**: Korrekte Initialisierung (0 für Addition, 1 für Multiplikation)

- **Zählen (Counting)**
  - Spezialfall der Akkumulation: Häufigkeit von Ereignissen zählen
  - Variable wird mit 0 initialisiert
  - Bei jedem relevanten Ereignis: `zaehler += 1`
  - Beispiel: Gerade Zahlen zählen mit `if zahl % 2 == 0: anzahl_gerade += 1`

- **Endlos-Schleifen vermeiden**
  - Eine `while`-Schleife muss eine Abbruchbedingung haben, die irgendwann `False` wird
  - Häufiger Fehler: Schleifenvariable wird nicht im Schleifenkörper modifiziert
  - Checkliste:
    1. Wird die relevante Variable im Schleifenkörper geändert?
    2. Führt die Änderung dazu, dass die Bedingung irgendwann `False` wird?
    3. Gibt es einen garantierten Abbruch?
  - Notfall-Abbruch in der Konsole: Strg+C (KeyboardInterrupt)

- **`for` vs. `while`: Wann welche?**
  - **`for`**: Wenn Anzahl der Durchläufe bekannt oder über Sequenz iteriert wird
  - **`while`**: Wenn Anzahl der Durchläufe unbekannt, abhängig von dynamischer Bedingung
  - **`for`** ist idiomatischer für Iterationen über Collections
  - **`while`** ist idiomatischer für Eingabevalidierung und ereignisgesteuerte Schleifen

### Konzepte und Best Practices

- **`range()` exklusive Obergrenze**: `range(10)` erzeugt 0-9, nicht 0-10. Für 1-10: `range(1, 11)`
- **Schleifenvariable in `for` nicht modifizieren**: Hat keine Auswirkung auf die Iteration, da sie in jedem Durchlauf neu zugewiesen wird
- **Akkumulation richtig initialisieren**: `summe = 0` für Addition, `produkt = 1` für Multiplikation
- **String-Konkatenation in Schleifen vermeiden**: Ineffizient wegen Immutability. Besser: Liste aufbauen und mit `.join()` verbinden (V08)
- **`enumerate()` statt manueller Indexzählung**: Pythonischer und fehlerresistenter
- **Abbruchbedingungen in `while` sorgfältig prüfen**: Endlos-Schleifen sind ein häufiger Fehler

### Notizen

- `range()` in Python 2 erzeugte eine Liste, in Python 3 ein spezielles Range-Objekt (speicher-effizienter)
- `enumerate()` wurde in Python 2.3 eingeführt
- Die `for`-Schleife in Python entspricht eher einer "for-each"-Schleife in anderen Sprachen (iteriert über Elemente, nicht über Indizes)
- Python hat keine klassische C-Style `for(i=0; i<n; i++)`-Schleife, `for i in range(n)` ist das Äquivalent
- `while True:` mit `break` ist ein idiomatisches Muster für "mindestens einmal ausführen" (fußgesteuerte Schleife)
- Fortgeschrittene Schleifenkonzepte (`break`, `continue`, `else` bei Schleifen, List Comprehensions) werden in V07 behandelt

---

## V07 (2026-01-03) – Schleifen (for, while) – Teil 2

### Neu eingeführt

#### Schleifensteuerungs-Statements

- **`break`-Statement** (Python Keyword, Python 1.0+)
  - Bricht die umschließende Schleife sofort ab
  - Führt zur Ausführung des Codes nach der Schleife
  - Bei verschachtelten Schleifen: Bricht nur die innerste Schleife ab
  - Syntax: `break`
  - Signatur: `break`
  - Beispiel:
    ```python
    for i in range(10):
        if i == 5:
            break  # Schleife endet bei i=5
        print(i)  # Gibt 0, 1, 2, 3, 4 aus
    ```
  - **Verwendung**: Vorzeitiger Schleifenabbruch bei erfüllter Bedingung (z.B. Suche erfolgreich)

- **`continue`-Statement** (Python Keyword, Python 1.0+)
  - Überspringt den Rest des aktuellen Schleifendurchlaufs
  - Springt sofort zur nächsten Iteration (bei `for`) oder zur Bedingungsprüfung (bei `while`)
  - Syntax: `continue`
  - Signatur: `continue`
  - Beispiel:
    ```python
    for i in range(10):
        if i % 2 == 0:
            continue  # Überspringe gerade Zahlen
        print(i)  # Gibt nur 1, 3, 5, 7, 9 aus
    ```
  - **Verwendung**: Überspringen ungültiger/ungewünschter Elemente ohne tiefe Verschachtelung

#### Loop `else`-Klausel

- **Loop `else`-Klausel** (Python Sprachfeature, Python 1.0+)
  - `else`-Block nach Schleife wird ausgeführt, wenn Schleife **normal** beendet wurde (ohne `break`)
  - Funktioniert sowohl mit `for` als auch `while`-Schleifen
  - Syntax: 
    ```python
    for item in iterable:
        if bedingung:
            break
    else:
        # Wird nur ausgeführt, wenn break NICHT aufgerufen wurde
        pass
    ```
  - Signatur: `for/while ... else:`
  - Beispiel (Primzahl-Test):
    ```python
    n = 29
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} ist keine Primzahl")
            break
    else:
        # else wird nur ausgeführt, wenn kein break kam
        print(f"{n} ist eine Primzahl")
    ```
  - **Semantik**: "Wenn Schleife nicht unterbrochen wurde, dann..."
  - **Verwendung**: Suchen mit Erfolgsprüfung, Validierung aller Elemente

#### List Comprehensions

- **List Comprehension** (Python Sprachfeature, Python 2.0+, PEP 202)
  - Kompakte Syntax zum Erstellen von Listen aus Iterables
  - Syntax: `[expression for item in iterable]`
  - Mit Bedingung: `[expression for item in iterable if condition]`
  - Signatur: `[expr for var in iterable if condition]` → `list`
  - Beispiel:
    ```python
    # Klassische Schleife:
    quadrate = []
    for i in range(10):
        quadrate.append(i ** 2)
    
    # List Comprehension:
    quadrate = [i ** 2 for i in range(10)]
    ```
  - Mit Filter:
    ```python
    # Nur gerade Quadrate:
    gerade_quadrate = [i ** 2 for i in range(10) if i % 2 == 0]
    ```
  - **Vorteile**: Kürzer, lesbarer, oft schneller als explizite Schleife
  - **Wichtig**: Nur für einfache Transformationen verwenden; bei komplexer Logik normale Schleife bevorzugen

- **Verschachtelte List Comprehensions** (Python 2.0+)
  - Mehrere `for`-Klauseln für mehrdimensionale Iteration
  - Syntax: `[expr for item1 in iter1 for item2 in iter2]`
  - Entspricht verschachtelten Schleifen: äußere Schleife zuerst, innere danach
  - Beispiel:
    ```python
    # Klassisch:
    paare = []
    for x in [1, 2, 3]:
        for y in ['a', 'b']:
            paare.append((x, y))
    
    # List Comprehension:
    paare = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
    # Ergebnis: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]
    ```

#### Set und Dictionary Comprehensions (Vorschau)

- **Set Comprehension** (Python 2.7+ / 3.0+, PEP 274)
  - Analog zu List Comprehension, erstellt aber ein Set (eindeutige Elemente)
  - Syntax: `{expression for item in iterable if condition}`
  - Beispiel: `eindeutige_buchstaben = {c.lower() for c in "Hallo Welt"}`
  - **Hinweis**: Wird in V07 erwähnt, aber erst in V08 ausführlich behandelt

- **Dictionary Comprehension** (Python 2.7+ / 3.0+, PEP 274)
  - Erstellt Dictionaries mit Schlüssel-Wert-Paaren
  - Syntax: `{key_expr: value_expr for item in iterable if condition}`
  - Beispiel: `quadrate_dict = {x: x**2 for x in range(5)}`  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
  - **Hinweis**: Wird in V07 erwähnt, aber erst in V08 ausführlich behandelt

#### Module: `string`

- **`string`-Modul** (Standard Library)
  - Enthält vordefinierte Konstanten für Zeichensets
  - Import: `import string`
  
  - **`string.ascii_uppercase`** (Konstante)
    - String mit allen Großbuchstaben: `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`
    - Beispiel: `import string; print(string.ascii_uppercase)`
  
  - **`string.ascii_lowercase`** (Konstante)
    - String mit allen Kleinbuchstaben: `'abcdefghijklmnopqrstuvwxyz'`
    - Beispiel: `kleinbuchstaben = string.ascii_lowercase`
  
  - **`string.ascii_letters`** (Konstante)
    - Kombination aus `ascii_lowercase` und `ascii_uppercase`
    - Beispiel: `buchstaben = string.ascii_letters`
  
  - **`string.digits`** (Konstante)
    - String mit allen Ziffern: `'0123456789'`
    - Beispiel: `ziffern = string.digits`
  
  - **`string.punctuation`** (Konstante)
    - String mit allen ASCII-Satzzeichen: `!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`
    - Beispiel: `sonderzeichen = string.punctuation`
  
  - **Verwendung**: Nützlich für Passwortgenerierung, Validierung, Zeichenfilterung

#### Module: `random`

- **`random`-Modul** (Standard Library)
  - Funktionen zur Erzeugung von Zufallszahlen und zufälligen Auswahlen
  - Import: `import random`
  
  - **`random.choice(seq)`** (Funktion)
    - Wählt ein zufälliges Element aus einer nicht-leeren Sequenz
    - Signatur: `random.choice(seq)` → Element
    - Beispiel: `zufalls_buchstabe = random.choice('ABCDE')`
    - Wirft `IndexError` bei leerer Sequenz
  
  - **`random.shuffle(liste)`** (Funktion)
    - Mischt die Liste **in-place** (modifiziert Original)
    - Gibt `None` zurück
    - Signatur: `random.shuffle(x)` → `None`
    - Beispiel:
      ```python
      karten = ['A', 'K', 'D', 'B']
      random.shuffle(karten)
      print(karten)  # ['D', 'A', 'B', 'K'] (zufällige Reihenfolge)
      ```
    - **Wichtig**: Funktioniert nur mit veränderbaren Sequenzen (Listen, nicht Strings/Tupel)
  
  - **`random.randint(a, b)`** (Funktion)
    - Gibt zufällige Ganzzahl N mit `a <= N <= b` zurück (beide Grenzen inklusive!)
    - Signatur: `random.randint(a, b)` → `int`
    - Beispiel: `wuerfel = random.randint(1, 6)`  # 1, 2, 3, 4, 5 oder 6
    - **Unterschied zu `range()`**: Beide Grenzen sind inklusive!

#### Reguläre Ausdrücke (Einführung)

- **`re`-Modul** (Standard Library)
  - Modul für reguläre Ausdrücke (Pattern Matching)
  - Import: `import re`
  
  - **`re.split(pattern, string)`** (Funktion)
    - Teilt String an allen Stellen, die dem Pattern entsprechen
    - Signatur: `re.split(pattern, string, maxsplit=0, flags=0)` → `list[str]`
    - Beispiel:
      ```python
      import re
      text = "Hallo! Wie geht es? Gut."
      saetze = re.split(r'[.!?]+', text)
      # Ergebnis: ['Hallo', ' Wie geht es', ' Gut', '']
      ```
    - Pattern `r'[.!?]+'`: Ein oder mehr Satzzeichen (`.`, `!`, `?`)
  
  - **`re.findall(pattern, string)`** (Funktion)
    - Findet alle nicht-überlappenden Vorkommen des Patterns
    - Gibt Liste von Strings zurück
    - Signatur: `re.findall(pattern, string, flags=0)` → `list[str]`
    - Beispiel:
      ```python
      zahlen = re.findall(r'\b\d+(?:[.,]\d+)?\b', "Preis: 19,99 und 5.50")
      # Ergebnis: ['19,99', '5.50']
      ```
    - Pattern-Erklärung:
      - `\b`: Wortgrenze
      - `\d+`: Eine oder mehr Ziffern
      - `(?:[.,]\d+)?`: Optional: Komma/Punkt gefolgt von Ziffern
  
  - **Hinweis**: Reguläre Ausdrücke werden in V07 nur grundlegend eingeführt; ausführliche Behandlung erfolgt in späteren Vorlesungen

#### Konzepte und Sprachmerkmale

- **Verschachtelte Schleifen (Nested Loops)**
  - Schleife innerhalb einer anderen Schleife
  - Jede Iteration der äußeren Schleife führt alle Iterationen der inneren Schleife aus
  - Syntax:
    ```python
    for i in range(3):
        for j in range(3):
            print(f"({i}, {j})")
    ```
  - **Komplexität**: O(n × m) für zwei Schleifen mit n und m Iterationen
  - **Verwendung**: Mehrdimensionale Datenstrukturen, Kombinationen, Muster

- **`break` in verschachtelten Schleifen**
  - `break` bricht nur die **innerste** Schleife ab
  - Äußere Schleife läuft weiter
  - Beispiel:
    ```python
    for i in range(3):
        for j in range(3):
            if j == 1:
                break  # Bricht nur die j-Schleife ab
            print(f"({i}, {j})")
    # Ausgabe: (0, 0), (1, 0), (2, 0)
    ```
  - **Workaround für "break beide Schleifen"**: Flag-Variable oder Funktion mit `return`

- **Generator Expressions** (Python 2.4+, Vorschau)
  - Ähnlich List Comprehension, aber mit runden Klammern: `(expr for item in iter)`
  - Erzeugt Generator statt Liste (lazy evaluation, speicher-effizienter)
  - Beispiel: `summe = sum(i**2 for i in range(1000000))`
  - **Hinweis**: Wird in V07 nur erwähnt, ausführliche Behandlung in späteren Vorlesungen

### Konzepte und Best Practices

- **`break` für Erfolgsprüfung mit `else`**: Idiomatisches Pattern für "element gefunden" vs. "nicht gefunden"
- **`continue` statt tiefer Verschachtelung**: Verbessert Lesbarkeit durch "early skip"
- **List Comprehensions für einfache Transformationen**: Kürzer und oft performanter als explizite Schleifen
- **Reguläre Schleifen für komplexe Logik**: List Comprehensions sollten nicht zu komplex werden (max. 1-2 Zeilen)
- **`string`-Modul für Zeichensets**: Besser als manuelles `'ABCDEFG...'` (weniger fehleranfällig, internationale Unterstützung)
- **`random.shuffle()` modifiziert in-place**: Keine Zuweisung nötig (`random.shuffle(liste)`, nicht `liste = random.shuffle(liste)`)

### Notizen

- `break` und `continue` existieren seit Python 1.0
- Loop `else` ist ein einzigartiges Python-Feature, das in vielen anderen Sprachen nicht existiert
- List Comprehensions wurden in Python 2.0 eingeführt (PEP 202)
- Set und Dict Comprehensions wurden in Python 2.7/3.0 hinzugefügt (PEP 274)
- `random.randint(a, b)` ist **inklusive** beider Grenzen (anders als `range()`)
- Generator Expressions wurden in Python 2.4 eingeführt (PEP 289)
- Reguläre Ausdrücke sind mächtiges Werkzeug, können aber schwer lesbar werden – verwende sie sparsam

---

## V08 (2026-01-03) – Listen & Datenstrukturen

### Neu eingeführt

#### Datentypen

- **`list`** (Built-in Typ, Python 1.0+)
  - Veränderbare (mutable) Sequenz, die beliebige Objekte aufnehmen kann
  - Elemente können unterschiedliche Datentypen haben
  - Zugriff über Index (0-basiert)
  - Syntax: `[element1, element2, ...]` oder `list(iterable)`
  - Signatur: `list()` → leere Liste oder `list(iterable)` → Liste aus Iterable
  - Beispiel: `zahlen = [1, 2, 3, 4, 5]`, `gemischt = [1, "Hallo", 3.14, True]`
  - **Wichtig**: Listen sind mutable – Änderungen wirken auf das Original-Objekt

- **`tuple`** (Built-in Typ, Python 1.0+)
  - Unveränderbare (immutable) Sequenz, ähnlich wie Listen
  - Nach Erstellung können Elemente nicht mehr geändert, hinzugefügt oder entfernt werden
  - Verwendung: Für Daten, die nicht verändert werden sollen (z.B. Koordinaten)
  - Syntax: `(element1, element2, ...)` oder `tuple(iterable)`
  - Bei einem Element: `(element,)` – Komma erforderlich!
  - Signatur: `tuple()` → leeres Tupel oder `tuple(iterable)` → Tupel aus Iterable
  - Beispiel: `koordinaten = (3, 4)`, `farbe = (255, 128, 0)`, `ein_element = (42,)`
  - **Vorteile**: Schneller als Listen, können als Dictionary-Keys verwendet werden, schützen vor unbeabsichtigten Änderungen

---

## V09 (2026-01-03) – Listen & Datenstrukturen – Teil 2 / Try-Catch (Fehlerbehandlung)

### Neu eingeführt

#### Fehlerbehandlung (Exception Handling)

- **`try`-Statement** (Python Keyword, Python 1.0+)
  - Definiert einen Codeblock, in dem Fehler (Exceptions) auftreten können
  - Syntax: `try:`
  - Muss mindestens einen `except`-Block oder einen `finally`-Block haben
  - Signatur: `try:`
  - Beispiel:
    ```python
    try:
        zahl = int(input("Zahl: "))
        ergebnis = 10 / zahl
        print(f"Ergebnis: {ergebnis}")
    except ValueError:
        print("Ungültige Eingabe!")
    except ZeroDivisionError:
        print("Division durch 0!")
    ```
  - **Wichtig**: Exceptions werden vom engsten passenden `except`-Block abgefangen

- **`except`-Klausel** (Python Keyword, Python 1.0+)
  - Definiert Fehlerbehandlung für spezifische Exception-Typen
  - Syntax: `except ExceptionType:` oder `except (Type1, Type2):` oder `except ExceptionType as e:`
  - Kann mehrfach verwendet werden für verschiedene Exception-Typen
  - Signatur: `except [ExceptionType [as variable]]:`
  - Beispiele:
    ```python
    except ValueError:                    # Fängt ValueError ab
        pass
    
    except (TypeError, KeyError):         # Fängt beide Typen ab
        pass
    
    except FileNotFoundError as e:        # Zugriff auf Exception-Objekt
        print(f"Fehler: {e}")
    ```
  - **Best Practice**: Spezifische Exceptions vor generischen abfangen

- **`else`-Klausel (bei try)** (Python Keyword, Python 1.0+)
  - Wird ausgeführt, wenn **keine** Exception im `try`-Block auftritt
  - Syntax: `else:` (nach allen `except`-Klauseln, vor `finally`)
  - Optional, aber nützlich zur Trennung von "erfolgreicher Code" und "Fehlerbehandlung"
  - Signatur: `else:`
  - Beispiel:
    ```python
    try:
        datei = open("daten.txt", "r")
    except FileNotFoundError:
        print("Datei nicht gefunden")
    else:
        # Wird nur ausgeführt, wenn open() erfolgreich war
        inhalt = datei.read()
        datei.close()
    ```
  - **Vorteil**: Code im `else`-Block wird nicht von `except` abgefangen

- **`finally`-Klausel** (Python Keyword, Python 2.5+)
  - Wird **immer** ausgeführt, unabhängig davon, ob Exception auftrat oder nicht
  - Syntax: `finally:` (nach allen `except` und `else`-Klauseln)
  - Verwendung: Aufräumarbeiten (Dateien schließen, Verbindungen trennen)
  - Signatur: `finally:`
  - Beispiel:
    ```python
    try:
        datei = open("daten.txt", "r")
        inhalt = datei.read()
    except FileNotFoundError:
        print("Datei nicht gefunden")
    finally:
        # Wird IMMER ausgeführt, auch bei Exception
        if 'datei' in locals():
            datei.close()
    ```
  - **Wichtig**: Wird auch ausgeführt bei `return`, `break` oder `continue` im `try`-Block

- **`raise`-Statement** (Python Keyword, Python 1.0+)
  - Wirft eine Exception (explizit)
  - Syntax: `raise ExceptionType(message)` oder `raise` (in `except`-Block zum Weiterwerfen)
  - Signatur: `raise [ExceptionType[(args)]]`
  - Beispiele:
    ```python
    raise ValueError("Ungültiger Wert")
    
    if alter < 0:
        raise ValueError("Alter darf nicht negativ sein")
    
    try:
        # Code...
    except ValueError:
        print("Fehler aufgetreten")
        raise  # Wirft die gleiche Exception weiter
    ```
  - **Verwendung**: Validierung, benutzerdefinierte Fehler signalisieren

#### Exception-Typen (Built-in)

- **`Exception`** (Built-in Klasse)
  - Basisklasse für alle benutzerdefinierten Exceptions
  - Sollte nicht direkt geworfen werden, sondern als Basis für eigene Exceptions dienen
  - Signatur: `class MeineException(Exception):`
  - Beispiel:
    ```python
    class AlterFehler(Exception):
        """Exception für ungültige Alterswerte."""
        pass
    ```

- **`ValueError`** (Built-in Exception)
  - Wird geworfen, wenn Funktion richtigen Typ, aber ungültigen Wert erhält
  - Beispiele: `int("abc")`, `math.sqrt(-1)` (ohne complex)
  - Signatur: `ValueError(message)`
  - Verwendung: Validierung von Werten
  - Beispiel: `raise ValueError("Zahl muss positiv sein")`

- **`TypeError`** (Built-in Exception)
  - Wird geworfen bei falschen Datentypen
  - Beispiele: `"5" + 5`, `len(42)`, `dict[0]` (bei nicht-dict)
  - Signatur: `TypeError(message)`
  - Verwendung: Typ-Validierung
  - Beispiel: `raise TypeError("Argument muss String sein")`

- **`KeyError`** (Built-in Exception)
  - Wird geworfen bei Zugriff auf nicht-existierenden Dictionary-Key
  - Beispiel: `{'a': 1}['b']`
  - Signatur: `KeyError(key)`
  - Verwendung: Dictionary-Zugriff absichern
  - Alternative: `.get(key, default)` statt `[key]`

- **`FileNotFoundError`** (Built-in Exception, Python 3.3+)
  - Wird geworfen, wenn Datei nicht existiert
  - Unterklasse von `OSError`
  - Beispiel: `open("nicht_vorhanden.txt")`
  - Signatur: `FileNotFoundError(message)`
  - Verwendung: Datei-Operationen absichern

- **`PermissionError`** (Built-in Exception, Python 3.3+)
  - Wird geworfen bei fehlenden Zugriffsrechten
  - Unterklasse von `OSError`
  - Beispiel: `open("/root/secret.txt")` ohne Root-Rechte
  - Signatur: `PermissionError(message)`
  - Verwendung: Datei-/Verzeichnis-Operationen absichern

- **`IndexError`** (Built-in Exception)
  - Wird geworfen bei Zugriff außerhalb der Sequenz-Grenzen
  - Beispiel: `[1, 2, 3][10]`
  - Signatur: `IndexError(message)`
  - Verwendung: List-/Tupel-Zugriff validieren

- **`ZeroDivisionError`** (Built-in Exception)
  - Wird geworfen bei Division durch Null
  - Beispiel: `10 / 0`
  - Signatur: `ZeroDivisionError(message)`
  - Verwendung: Division absichern

#### Module und Funktionen

- **`json`-Modul** (Standard Library, Python 2.6+)
  - Modul zum Arbeiten mit JSON-Daten (JavaScript Object Notation)
  - Import: `import json`
  
  - **`json.load(file_object)`** (Funktion)
    - Liest JSON aus einer geöffneten Datei
    - Signatur: `json.load(fp)` → `object` (dict, list, str, int, float, bool, None)
    - Beispiel:
      ```python
      with open("config.json", "r") as datei:
          daten = json.load(datei)
      ```
    - Wirft `json.JSONDecodeError` bei ungültigem JSON
  
  - **`json.dump(obj, file_object)`** (Funktion)
    - Schreibt Python-Objekt als JSON in eine Datei
    - Signatur: `json.dump(obj, fp, indent=None, ensure_ascii=True)`
    - Parameter:
      - `indent`: Anzahl Leerzeichen für Formatierung (z.B. `4`)
      - `ensure_ascii`: `False` für Umlaute/Unicode-Zeichen
    - Beispiel:
      ```python
      daten = {"name": "Alice", "alter": 25}
      with open("daten.json", "w") as datei:
          json.dump(daten, datei, indent=4, ensure_ascii=False)
      ```
  
  - **`json.JSONDecodeError`** (Exception, Python 3.5+)
    - Exception bei ungültigem JSON-Format
    - Unterklasse von `ValueError`
    - Enthält Details über Fehlerposition
    - Beispiel:
      ```python
      try:
          daten = json.loads("{invalid json}")
      except json.JSONDecodeError as e:
          print(f"JSON-Fehler in Zeile {e.lineno}, Spalte {e.colno}")
      ```

#### Konzepte und Sprachmerkmale

- **Exception-Hierarchie**
  - Alle Exceptions erben von `BaseException`
  - Benutzerdefinierte Exceptions sollten von `Exception` erben
  - Hierarchie-Beispiel:
    ```
    BaseException
    ├── Exception
    │   ├── ValueError
    │   ├── TypeError
    │   ├── KeyError
    │   ├── OSError
    │   │   ├── FileNotFoundError
    │   │   └── PermissionError
    │   └── ... (viele weitere)
    └── SystemExit, KeyboardInterrupt, ... (sollten selten abgefangen werden)
    ```
  - **Best Practice**: Fange niemals `BaseException` ab (würde auch `KeyboardInterrupt` abfangen)

- **Benutzerdefinierte Exceptions**
  - Eigene Exception-Klassen durch Ableitung von `Exception`
  - Syntax:
    ```python
    class MeineException(Exception):
        """Docstring erklärt den Zweck."""
        pass
    ```
  - Erweiterte Version mit `__init__`:
    ```python
    class ValidationError(Exception):
        def __init__(self, feld, wert):
            self.feld = feld
            self.wert = wert
            super().__init__(f"Ungültiger Wert '{wert}' für Feld '{feld}'")
    ```
  - **Verwendung**: Domänenspezifische Fehler modellieren

- **Exception-Objekt zugreifen**
  - `except ExceptionType as e:` ermöglicht Zugriff auf Exception-Objekt
  - Exception-Objekte haben `.args`-Attribut (Tupel mit Argumenten)
  - String-Repräsentation: `str(e)` gibt Fehlermeldung zurück
  - Beispiel:
    ```python
    try:
        int("abc")
    except ValueError as e:
        print(f"Fehlertyp: {type(e).__name__}")  # ValueError
        print(f"Fehlermeldung: {e}")             # invalid literal...
        print(f"Args: {e.args}")                  # ("invalid literal...",)
    ```

- **Multiple Exception-Typen**
  - Syntax: `except (Type1, Type2, Type3) as e:`
  - Fängt alle genannten Typen mit einem Block ab
  - Beispiel:
    ```python
    try:
        # Code...
    except (ValueError, TypeError, KeyError) as e:
        print(f"Eingabefehler: {e}")
    ```

- **Best Practices für Exception Handling**
  - **Spezifisch abfangen**: `except ValueError:` statt `except:`
  - **Nicht leer lassen**: `pass` nur wenn bewusst nichts getan werden soll
  - **Nicht alles abfangen**: `except Exception:` nur in seltenen Fällen
  - **Exceptions dokumentieren**: Docstrings sollten mögliche Exceptions auflisten
  - **Fail Fast**: Validiere früh, wirf Exceptions sofort
  - **else für Erfolgsfall**: Trenne normalen Code von Fehlerbehandlung
  - **finally für Cleanup**: Ressourcen immer freigeben

### Notizen

- `try-except` existiert seit Python 1.0, `finally` seit Python 2.5, `else` seit Python 1.5
- `FileNotFoundError` und `PermissionError` wurden in Python 3.3 eingeführt (vorher: `IOError` oder `OSError`)
- `json.JSONDecodeError` wurde in Python 3.5 hinzugefügt
- `with`-Statement (Context Manager) ist oft besser als manuelles `try-finally` für Ressourcen-Management
- Exception-Handling hat Overhead – verwende es nur wo nötig, nicht für normalen Programmfluss
- Python folgt dem EAFP-Prinzip: "Easier to Ask for Forgiveness than Permission" (try-except statt vorherige Prüfung)
- Alternativen zu try-except:
  - `.get(key, default)` für Dictionaries statt `try-except KeyError`
  - `.isdigit()` vor `int()` statt `try-except ValueError`
  - `if os.path.exists()` vor `open()` (aber Race Condition möglich!)

#### List-Methoden

- **`.append(element)`** (List-Methode)
  - Fügt ein Element am Ende der Liste hinzu (in-place)
  - Gibt `None` zurück (modifiziert Original)
  - Signatur: `list.append(x)` → `None`
  - Beispiel: `zahlen = [1, 2, 3]; zahlen.append(4)` → `zahlen` ist jetzt `[1, 2, 3, 4]`
  - **Zeitkomplexität**: O(1) – Amortized Constant Time

- **`.insert(index, element)`** (List-Methode)
  - Fügt ein Element an einer bestimmten Position ein (in-place)
  - Elemente ab `index` werden nach rechts verschoben
  - Signatur: `list.insert(i, x)` → `None`
  - Beispiel: `zahlen = [1, 3, 4]; zahlen.insert(1, 2)` → `zahlen` ist jetzt `[1, 2, 3, 4]`
  - **Zeitkomplexität**: O(n) – Linear, da Elemente verschoben werden müssen

- **`.extend(iterable)`** (List-Methode)
  - Fügt alle Elemente aus einem Iterable am Ende der Liste hinzu (in-place)
  - Gibt `None` zurück
  - Signatur: `list.extend(iterable)` → `None`
  - Beispiel: `a = [1, 2]; a.extend([3, 4])` → `a` ist jetzt `[1, 2, 3, 4]`
  - Unterschied zu `.append()`: `.append([3, 4])` würde die Liste als **ein** Element hinzufügen → `[1, 2, [3, 4]]`
  - **Zeitkomplexität**: O(k), wobei k die Länge des Iterables ist

- **`.remove(element)`** (List-Methode)
  - Entfernt das **erste** Vorkommen eines Elements (in-place)
  - Wirft `ValueError`, wenn Element nicht gefunden
  - Signatur: `list.remove(x)` → `None`
  - Beispiel: `zahlen = [1, 2, 3, 2]; zahlen.remove(2)` → `zahlen` ist jetzt `[1, 3, 2]`
  - **Zeitkomplexität**: O(n) – Muss Liste durchsuchen

- **`.pop(index=-1)`** (List-Methode)
  - Entfernt und gibt das Element an Position `index` zurück (in-place)
  - Standard: `index=-1` (letztes Element)
  - Wirft `IndexError`, wenn Index außerhalb des Bereichs
  - Signatur: `list.pop([i])` → Element
  - Beispiel: `zahlen = [1, 2, 3]; x = zahlen.pop()` → `x` ist `3`, `zahlen` ist `[1, 2]`
  - Beispiel: `zahlen = [1, 2, 3]; x = zahlen.pop(0)` → `x` ist `1`, `zahlen` ist `[2, 3]`
  - **Zeitkomplexität**: O(1) für letztes Element, O(n) für andere Positionen
  - **Verwendung**: Stack-Operationen (Push mit `.append()`, Pop mit `.pop()`)

- **`.clear()`** (List-Methode, Python 3.3+)
  - Entfernt alle Elemente aus der Liste (in-place)
  - Gibt `None` zurück
  - Signatur: `list.clear()` → `None`
  - Beispiel: `zahlen = [1, 2, 3]; zahlen.clear()` → `zahlen` ist jetzt `[]`
  - Äquivalent zu `del zahlen[:]` oder `zahlen = []` (aber `.clear()` ist expliziter)

- **`.index(element, start=0, end=len(liste))`** (List-Methode)
  - Gibt den Index des **ersten** Vorkommens eines Elements zurück
  - Wirft `ValueError`, wenn Element nicht gefunden
  - Optional: Suche in Slice `[start:end]`
  - Signatur: `list.index(x[, start[, end]])` → `int`
  - Beispiel: `zahlen = [1, 2, 3, 2]; zahlen.index(2)` → `1`
  - Beispiel: `zahlen.index(2, 2)` → `3` (Suche ab Index 2)
  - **Zeitkomplexität**: O(n) – Lineare Suche

- **`.count(element)`** (List-Methode)
  - Zählt, wie oft ein Element in der Liste vorkommt
  - Signatur: `list.count(x)` → `int`
  - Beispiel: `zahlen = [1, 2, 3, 2, 2]; zahlen.count(2)` → `3`
  - **Zeitkomplexität**: O(n) – Muss gesamte Liste durchlaufen

- **`.sort(key=None, reverse=False)`** (List-Methode)
  - Sortiert die Liste **in-place** (modifiziert Original)
  - Gibt `None` zurück
  - Parameter:
    - `key`: Funktion, die auf jedes Element angewendet wird zur Sortierung (z.B. `key=len` für Sortierung nach Länge)
    - `reverse`: `True` für absteigende Sortierung
  - Signatur: `list.sort(key=None, reverse=False)` → `None`
  - Beispiel: `zahlen = [3, 1, 4, 1, 5]; zahlen.sort()` → `zahlen` ist `[1, 1, 3, 4, 5]`
  - Beispiel: `zahlen.sort(reverse=True)` → `zahlen` ist `[5, 4, 3, 1, 1]`
  - Beispiel: `woerter = ['aa', 'bbb', 'c']; woerter.sort(key=len)` → `['c', 'aa', 'bbb']`
  - **Zeitkomplexität**: O(n log n) – Timsort-Algorithmus
  - **Unterschied zu `sorted()`**: `.sort()` modifiziert Liste, `sorted()` gibt neue Liste zurück

- **`.reverse()`** (List-Methode)
  - Kehrt die Reihenfolge der Elemente um **in-place**
  - Gibt `None` zurück
  - Signatur: `list.reverse()` → `None`
  - Beispiel: `zahlen = [1, 2, 3]; zahlen.reverse()` → `zahlen` ist `[3, 2, 1]`
  - **Zeitkomplexität**: O(n)

- **`.copy()`** (List-Methode, Python 3.3+)
  - Erstellt eine **flache Kopie** (shallow copy) der Liste
  - Gibt neue Liste zurück
  - Signatur: `list.copy()` → `list`
  - Beispiel: `original = [1, 2, 3]; kopie = original.copy(); kopie.append(4)` → `original` ist `[1, 2, 3]`, `kopie` ist `[1, 2, 3, 4]`
  - Äquivalent zu `liste[:]` oder `list(liste)`
  - **Wichtig**: Bei verschachtelten Listen werden nur die äußeren Referenzen kopiert (shallow copy)!

#### Built-in Funktionen

- **`sorted(iterable, key=None, reverse=False)`** (Built-in, Python 2.4+)
  - Gibt eine **neue sortierte Liste** zurück (Original bleibt unverändert)
  - Funktioniert mit jedem Iterable (Listen, Tupel, Strings, etc.)
  - Parameter wie bei `.sort()`: `key` und `reverse`
  - Signatur: `sorted(iterable, key=None, reverse=False)` → `list`
  - Beispiel: `zahlen = [3, 1, 4]; sortiert = sorted(zahlen)` → `sortiert` ist `[1, 3, 4]`, `zahlen` ist `[3, 1, 4]`
  - Beispiel: `sorted("python")` → `['h', 'n', 'o', 'p', 't', 'y']`
  - **Unterschied zu `.sort()`**: `sorted()` gibt neue Liste zurück, `.sort()` modifiziert Original
  - **Zeitkomplexität**: O(n log n)

- **`sum(iterable, start=0)`** (Built-in)
  - Berechnet die Summe aller Elemente in einem Iterable
  - Parameter `start`: Startwert (Standard: 0), wird zur Summe addiert
  - Signatur: `sum(iterable, start=0)` → `number`
  - Beispiel: `sum([1, 2, 3, 4, 5])` → `15`
  - Beispiel: `sum([1, 2, 3], 10)` → `16` (10 + 1 + 2 + 3)
  - **Funktioniert nicht** mit Strings (verwende `.join()` stattdessen)
  - **Zeitkomplexität**: O(n)

- **`all(iterable)`** (Built-in, Python 2.5+)
  - Gibt `True` zurück, wenn **alle** Elemente im Iterable `True` sind (oder Iterable leer)
  - Nutzt Kurzschlussauswertung: Stoppt bei erstem `False`
  - Signatur: `all(iterable)` → `bool`
  - Beispiel: `all([True, True, True])` → `True`
  - Beispiel: `all([True, False, True])` → `False`
  - Beispiel: `all([])` → `True` (Leeres Iterable ist `True`)
  - **Verwendung**: Prüfung, ob alle Bedingungen erfüllt sind
  - Beispiel: `all(x > 0 for x in zahlen)` prüft, ob alle Zahlen positiv

- **`any(iterable)`** (Built-in, Python 2.5+)
  - Gibt `True` zurück, wenn **mindestens ein** Element im Iterable `True` ist
  - Nutzt Kurzschlussauswertung: Stoppt bei erstem `True`
  - Signatur: `any(iterable)` → `bool`
  - Beispiel: `any([False, True, False])` → `True`
  - Beispiel: `any([False, False, False])` → `False`
  - Beispiel: `any([])` → `False` (Leeres Iterable ist `False`)
  - **Verwendung**: Prüfung, ob mindestens eine Bedingung erfüllt ist
  - Beispiel: `any(c.isupper() for c in passwort)` prüft, ob Passwort Großbuchstaben enthält
  - **Hinweis**: Wurde in V04 als Vorschau erwähnt, hier vollständig eingeführt

- **`zip(*iterables)`** (Built-in, Python 2.0+)
  - Verknüpft mehrere Iterables zu einem Iterator von Tupeln
  - Jedes Tupel enthält die i-ten Elemente aller Iterables
  - Stoppt bei kürzestem Iterable
  - Signatur: `zip(*iterables)` → `zip`
  - Beispiel: 
    ```python
    namen = ["Alice", "Bob", "Charlie"]
    alter = [25, 30, 35]
    for name, age in zip(namen, alter):
        print(f"{name} ist {age} Jahre alt")
    # Alice ist 25 Jahre alt
    # Bob ist 30 Jahre alt
    # Charlie ist 35 Jahre alt
    ```
  - Beispiel: `list(zip([1, 2, 3], ['a', 'b', 'c']))` → `[(1, 'a'), (2, 'b'), (3, 'c')]`
  - **Verwendung**: Paralleles Iterieren über mehrere Listen, Verknüpfung von Daten
  - **Zeitkomplexität**: O(1) pro Element (lazy evaluation)

#### Operatoren

- **`+` (Konkatenation)** – Für Listen
  - Verknüpft zwei Listen zu einer neuen Liste
  - Original-Listen bleiben unverändert
  - Signatur: `list1 + list2` → `list`
  - Beispiel: `[1, 2] + [3, 4]` → `[1, 2, 3, 4]`
  - **Unterschied zu `.extend()`**: `+` erstellt neue Liste, `.extend()` modifiziert Original

- **`*` (Repetition)** – Für Listen
  - Wiederholt eine Liste n-mal
  - Signatur: `list * n` → `list`
  - Beispiel: `[0] * 5` → `[0, 0, 0, 0, 0]`
  - Beispiel: `[1, 2] * 3` → `[1, 2, 1, 2, 1, 2]`
  - **Warnung**: Bei verschachtelten Listen werden Referenzen kopiert!
    - `[[0]] * 3` erstellt **drei Referenzen** auf dieselbe innere Liste!
    - Änderungen an einer wirken auf alle: `liste[0].append(1)` ändert alle drei!

- **`in` (Membership-Operator)** – Prüfung auf Enthaltensein
  - Prüft, ob ein Element in einer Sequenz enthalten ist
  - Signatur: `element in sequence` → `bool`
  - Beispiel: `2 in [1, 2, 3]` → `True`
  - Beispiel: `5 in [1, 2, 3]` → `False`
  - **Zeitkomplexität**: O(n) für Listen (lineares Durchsuchen)

- **`del`-Statement** – Löschen von Elementen
  - Löscht Elemente oder Slices aus einer Liste (in-place)
  - Syntax: `del liste[index]` oder `del liste[start:end]`
  - Beispiel: `zahlen = [1, 2, 3, 4]; del zahlen[1]` → `zahlen` ist `[1, 3, 4]`
  - Beispiel: `del zahlen[1:3]` → `zahlen` ist `[1, 4]`
  - **Unterschied zu `.remove()`**: `del` arbeitet mit Index, `.remove()` mit Wert

#### Konzepte und Sprachmerkmale

- **Slicing (Ausschnitte)** – Teile einer Sequenz extrahieren
  - Syntax: `sequence[start:end:step]`
  - Parameter:
    - `start`: Startindex (inklusive, Standard: 0)
    - `end`: Endindex (exklusive, Standard: len(sequence))
    - `step`: Schrittweite (Standard: 1)
  - Beispiel: `zahlen = [0, 1, 2, 3, 4, 5]`
    - `zahlen[1:4]` → `[1, 2, 3]` (Elemente 1 bis 3)
    - `zahlen[:3]` → `[0, 1, 2]` (Erste drei)
    - `zahlen[3:]` → `[3, 4, 5]` (Ab Index 3)
    - `zahlen[::2]` → `[0, 2, 4]` (Jedes zweite)
    - `zahlen[::-1]` → `[5, 4, 3, 2, 1, 0]` (Umgekehrt)
    - `zahlen[-3:]` → `[3, 4, 5]` (Letzte drei)
  - **Wichtig**: Slicing erstellt eine **Kopie**, modifiziert nicht das Original
  - **Zeitkomplexität**: O(k), wobei k die Länge des Slices ist

- **Unpacking (Entpacken)** – Tupel/Listen in Variablen zerlegen
  - Bereits in V03 für Tupel erwähnt, hier für Listen erweitert
  - Syntax: `a, b, c = [1, 2, 3]`
  - Beispiel: `koordinaten = (3, 4); x, y = koordinaten` → `x` ist `3`, `y` ist `4`
  - **Extended Unpacking** (Python 3.0+, PEP 3132):
    - Syntax: `a, *rest, c = [1, 2, 3, 4, 5]`
    - `rest` sammelt alle mittleren Elemente als Liste
    - Beispiel: `erste, *mitte, letzte = [1, 2, 3, 4, 5]` → `erste` ist `1`, `mitte` ist `[2, 3, 4]`, `letzte` ist `5`
  - **Verwendung**: Funktionsrückgaben, Datenaustausch, parallele Zuweisungen

- **Aliasing vs. Copying (Referenzen vs. Kopien)**
  - **Aliasing**: Zwei Variablen zeigen auf dasselbe Objekt
    ```python
    a = [1, 2, 3]
    b = a  # b ist Alias von a
    b.append(4)  # Ändert auch a!
    # a ist jetzt [1, 2, 3, 4]
    ```
  - **Copying**: Neue unabhängige Liste erstellen
    ```python
    a = [1, 2, 3]
    b = a.copy()  # oder b = a[:] oder b = list(a)
    b.append(4)  # Ändert nur b
    # a ist weiterhin [1, 2, 3], b ist [1, 2, 3, 4]
    ```
  - **Shallow vs. Deep Copy**:
    - **Shallow Copy**: Kopiert nur äußere Struktur, innere Objekte werden referenziert
      ```python
      a = [[1, 2], [3, 4]]
      b = a.copy()
      b[0].append(99)  # Ändert auch a[0]!
      # a ist [[1, 2, 99], [3, 4]]
      ```
    - **Deep Copy**: Rekursive Kopie aller Ebenen (Modul `copy.deepcopy()`, wird später behandelt)

- **Listen als Stacks (LIFO)** – Last In, First Out
  - `.append(element)` für Push (Element hinzufügen)
  - `.pop()` für Pop (letztes Element entfernen und zurückgeben)
  - Beispiel:
    ```python
    stack = []
    stack.append(1)  # Push
    stack.append(2)  # Push
    x = stack.pop()  # Pop → x ist 2
    ```
  - **Zeitkomplexität**: O(1) für beide Operationen

- **Listen als Queues (FIFO)** – First In, First Out
  - `.append(element)` für Enqueue (am Ende hinzufügen)
  - `.pop(0)` für Dequeue (erstes Element entfernen)
  - **Warnung**: `.pop(0)` ist ineffizient (O(n)), da alle Elemente verschoben werden
  - **Bessere Alternative**: `collections.deque` (wird später behandelt)

### Konzepte und Best Practices

- **`.sort()` vs. `sorted()`**: 
  - `.sort()` für In-Place-Sortierung (spart Speicher, Original verloren)
  - `sorted()` für neue sortierte Liste (Original bleibt erhalten)
- **`.append()` vs. `.extend()`**:
  - `.append(x)` fügt `x` als **ein** Element hinzu (auch wenn `x` eine Liste ist)
  - `.extend(iterable)` fügt alle Elemente von `iterable` hinzu
- **Slicing für Kopien**: `kopie = original[:]` ist idiomatisch für flache Kopie
- **Negative Indizes**: `liste[-1]` ist letztes Element, `liste[-2]` ist vorletztes
- **Vorsicht bei Aliasing**: `b = a` erstellt **keine** Kopie, sondern nur eine weitere Referenz
- **`in` für Existenzprüfung**: Idiomatischer als manuelles Durchsuchen mit Schleife
- **List Comprehensions** (aus V07) kombinieren gut mit neuen Funktionen:
  - `[x for x in zahlen if x > 0]` – Filtern
  - `[x**2 for x in zahlen]` – Transformieren
- **`zip()` für parallele Listen**: Eleganter als manuelle Index-Verwaltung

### Notizen

- Listen wurden in Python 1.0 eingeführt und sind eine der grundlegendsten Datenstrukturen
- `.clear()` und `.copy()` wurden erst in Python 3.3 hinzugefügt
- `sorted()`, `all()`, `any()` wurden in Python 2.4/2.5 hinzugefügt
- `zip()` in Python 2 gab eine Liste zurück, in Python 3 einen Iterator (speicher-effizienter)
- Extended Unpacking (`*rest`) wurde in Python 3.0 eingeführt (PEP 3132)
- Timsort (der Sortieralgorithmus in `.sort()` und `sorted()`) ist ein hybrider Algorithmus (Merge Sort + Insertion Sort)
- Listen haben dynamische Größe und amortisierte O(1) Append-Zeit (Speicher wird bei Bedarf verdoppelt)
- Tupel sind immutable, aber wenn sie mutable Objekte enthalten (z.B. Listen), können diese modifiziert werden
- `collections.deque` (Double-Ended Queue) ist effizienter für Queue-Operationen als Listen (wird in späteren Vorlesungen behandelt)
---

## V10 (2026-01-03) – Methoden/Funktionen – Teil 1

### Neu eingeführt

#### Funktions-Definition und Aufruf

- **`def`-Statement** (Python Keyword, Python 1.0+)
  - Definiert eine neue Funktion (benutzerdefinierten Code-Block)
  - Syntax: `def funktionsname(parameter1, parameter2, ...):`
  - Funktionskörper muss eingerückt sein (Standard: 4 Leerzeichen)
  - Signatur: `def name(params):` → Funktion wird erstellt, aber nicht ausgeführt
  - Beispiel:
    ```python
    def begruesse(name):
        print(f"Hallo, {name}!")
    ```
  - **Wichtig**: Funktion wird erst bei Aufruf ausgeführt: `begruesse("Ada")`

- **`return`-Statement** (Python Keyword, Python 1.0+)
  - Beendet die Funktionsausführung und gibt einen Wert zurück
  - Syntax: `return wert` oder `return wert1, wert2, ...` (mehrere Werte als Tupel)
  - Ohne `return`: Funktion gibt implizit `None` zurück
  - Signatur: `return [expression]`
  - Beispiel:
    ```python
    def addiere(a, b):
        return a + b  # Gibt Summe zurück
    ```
  - **Wichtig**: Code nach `return` wird nicht ausgeführt (unreachable code)

#### Parameter und Argumente

- **Positionaler Parameter** (Konzept)
  - Parameter werden durch ihre Position in der Funktionsdefinition identifiziert
  - Beim Aufruf müssen Argumente in derselben Reihenfolge übergeben werden
  - Beispiel:
    ```python
    def teile(zaehler, nenner):
        return zaehler / nenner
    
    teile(10, 2)  # zaehler=10, nenner=2 → 5.0
    teile(2, 10)  # zaehler=2, nenner=10 → 0.2 (andere Reihenfolge!)
    ```

- **Keyword Argument** (Konzept, Python 1.0+)
  - Argumente werden mit Parameternamen übergeben: `funktionsname(param=wert)`
  - Reihenfolge spielt keine Rolle, wenn alle Argumente als Keywords übergeben werden
  - Syntax: `funktionsname(param1=wert1, param2=wert2)`
  - Beispiel:
    ```python
    def teile(zaehler, nenner):
        return zaehler / nenner
    
    teile(zaehler=10, nenner=2)  # 5.0
    teile(nenner=2, zaehler=10)  # 5.0 (gleiche Reihenfolge egal)
    ```
  - **Regel**: Positionale Argumente müssen vor Keyword-Argumenten stehen
  - **Fehler**: `teile(zaehler=10, 2)` → `SyntaxError`
  - **Richtig**: `teile(10, nenner=2)`

- **Default-Parameter** (Konzept, Python 1.0+)
  - Parameter mit Standard-Wert in der Funktionsdefinition
  - Syntax: `def funktion(param=default_wert):`
  - Können beim Aufruf weggelassen werden → Default-Wert wird verwendet
  - Beispiel:
    ```python
    def berechne_preis(netto, mwst=0.19):
        return netto * (1 + mwst)
    
    berechne_preis(100)          # 119.0 (Standard-MwSt 19%)
    berechne_preis(100, 0.07)    # 107.0 (reduzierte MwSt 7%)
    berechne_preis(100, mwst=0)  # 100.0 (keine MwSt)
    ```
  - **Regel**: Parameter ohne Default müssen vor Parametern mit Default stehen
  - **Fehler**: `def funktion(a=10, b):` → `SyntaxError`
  - **Richtig**: `def funktion(b, a=10):`

- **Multiple Return Values** (Konzept, nutzt Tuples)
  - Funktion kann mehrere Werte als Tupel zurückgeben
  - Syntax: `return wert1, wert2, wert3`
  - Beim Aufruf: Tuple Unpacking verwenden
  - Beispiel:
    ```python
    def min_max(liste):
        return min(liste), max(liste)
    
    # Unpacking:
    minimum, maximum = min_max([3, 1, 4, 1, 5])
    # minimum=1, maximum=5
    
    # Oder als Tupel:
    ergebnis = min_max([3, 1, 4, 1, 5])
    # ergebnis=(1, 5)
    ```

#### Funktionen als Objekte

- **Funktionen als First-Class Objects** (Konzept)
  - Funktionen sind in Python reguläre Objekte (wie int, str, list)
  - Können Variablen zugewiesen werden
  - Können als Argumente übergeben werden (Higher-Order Functions)
  - Können als Rückgabewerte verwendet werden
  - Beispiel:
    ```python
    def verdopple(x):
        return x * 2
    
    # Funktion einer Variable zuweisen (ohne Klammern!):
    meine_funktion = verdopple
    print(meine_funktion(5))  # 10
    
    # Als Argument übergeben:
    def wende_an(funktion, wert):
        return funktion(wert)
    
    print(wende_an(verdopple, 7))  # 14
    ```
  - **Wichtig**: `verdopple` (ohne Klammern) ist die Funktion selbst, `verdopple()` ruft sie auf

#### Scope und Namensauflösung

- **LEGB-Regel** (Konzept, Python 2.0+)
  - Reihenfolge der Namensauflösung in Python
  - **L**ocal: Lokale Variablen innerhalb der aktuellen Funktion
  - **E**nclosing: Variablen in umschließenden Funktionen (Closures)
  - **G**lobal: Globale Variablen auf Modul-Ebene
  - **B**uilt-in: Eingebaute Namen (print, len, etc.)
  - Python sucht Namen in dieser Reihenfolge von innen nach außen
  - Beispiel:
    ```python
    x = "global"  # Global
    
    def aeussere():
        x = "enclosing"  # Enclosing
        
        def innere():
            x = "local"  # Local
            print(x)  # "local" (findet zuerst Local)
        
        innere()
        print(x)  # "enclosing"
    
    aeussere()
    print(x)  # "global"
    ```
  - **Built-in Beispiel**: `len` ist Built-in, kann aber überschrieben werden (nicht empfohlen!)
    ```python
    len([1, 2, 3])  # 3 (Built-in)
    len = "Hallo"   # Überschreibt Built-in (schlecht!)
    # len([1, 2, 3])  # TypeError: 'str' object is not callable
    ```

#### Dokumentation

- **Docstring** (Konzept, Python 1.0+)
  - Dokumentations-String direkt nach Funktionsdefinition
  - Wird in Triple-Quotes geschrieben: `"""..."""` oder `'''...'''`
  - Beschreibt Funktion, Parameter, Rückgabewert, Beispiele
  - Syntax: Erste Zeile nach `def` muss der Docstring sein
  - Zugriff: `funktionsname.__doc__` oder `help(funktionsname)`
  - Beispiel:
    ```python
    def berechne_flaeche(laenge, breite):
        """
        Berechnet die Fläche eines Rechtecks.
        
        Parameter:
            laenge (float): Länge des Rechtecks
            breite (float): Breite des Rechtecks
        
        Rückgabewert:
            float: Fläche (Länge × Breite)
        
        Beispiele:
            >>> berechne_flaeche(5, 3)
            15
            >>> berechne_flaeche(10, 2.5)
            25.0
        """
        return laenge * breite
    
    # Docstring anzeigen:
    print(berechne_flaeche.__doc__)
    help(berechne_flaeche)
    ```
  - **Best Practice**: Immer Docstrings für öffentliche Funktionen schreiben
  - **Format**: Google Style, NumPy Style oder reStructuredText sind verbreitet

#### Module (Verwendung)

- **`time`-Modul** (Standard Library)
  - Modul für Zeit-bezogene Funktionen
  - Import: `import time`
  
  - **`time.time()`** (Funktion)
    - Gibt aktuelle Zeit in Sekunden seit Unix-Epoch (1. Januar 1970) zurück
    - Signatur: `time.time()` → `float`
    - Verwendung: Zeitmessung durch Differenz von zwei `time.time()`-Aufrufen
    - Beispiel:
      ```python
      import time
      
      start = time.time()
      # ... Code, dessen Laufzeit gemessen werden soll ...
      ende = time.time()
      
      dauer = ende - start
      print(f"Laufzeit: {dauer:.4f} Sekunden")
      ```
    - **Genauigkeit**: System-abhängig, typischerweise Mikrosekunden-Bereich

### Konzepte und Best Practices

- **Funktionsnamen**: Verwende `snake_case` (Kleinbuchstaben mit Unterstrichen)
- **Einzeilige Funktionen**: Nur wenn wirklich trivial, sonst mehrzeilig für Lesbarkeit
- **Return vs. Print**: Funktionen sollten Werte zurückgeben, nicht ausgeben (testbarer, wiederverwendbarer)
- **Reine Funktionen**: Bevorzuge Funktionen ohne Seiteneffekte (keine globalen Variablen ändern)
- **Parameterzahl**: Max. 4-5 Parameter empfohlen, sonst Dictionary oder Objekt übergeben
- **Default-Parameter Warnung**: Mutable Defaults (`def func(liste=[]):`) sind gefährlich! Verwende `None` stattdessen:
  ```python
  # Falsch:
  def fuege_hinzu(element, liste=[]):
      liste.append(element)
      return liste
  
  # Richtig:
  def fuege_hinzu(element, liste=None):
      if liste is None:
          liste = []
      liste.append(element)
      return liste
  ```

### Notizen

- `def` und `return` existieren seit Python 1.0
- Keyword Arguments existieren seit Python 1.0
- LEGB-Regel wurde in Python 2.0 formalisiert mit Nested Scopes (PEP 227)
- Docstrings existieren seit Python 1.0, aber PEP 257 (Docstring Conventions) kam später
- Type Hints (PEP 484, Python 3.5+) sind optional und werden in V11 behandelt
- `*args` und `**kwargs` für variable Argumentanzahl werden in V11 behandelt
- Lambda-Funktionen (anonyme Funktionen) werden in V11 behandelt
- Decorators und Generator-Funktionen sind fortgeschrittene Themen für spätere Vorlesungen

---

## V11 – GPTs, LLMs & KI (vereinfacht)

### Neu eingeführt
- **Wiederholung** aller bisherigen Basics: `print()`, `input()`, `if/else`, `for`-Schleife, Variablen
- Keine neuen Python-Konzepte — Fokus auf Theorie (Was ist KI, LLM als Wort-Vorhersage-Maschine, Halluzinationen, Bias)

### Notizen
- Bewusst keine neuen Python-Funktionen, damit Studierende den Stoff aus V01-V10 festigen
- Einfache Übungen: Variablen, f-Strings, if/else

---

## V12 – Prompt Engineering

### Neu eingeführt

#### String-Methoden (Wiederholung + Neu)
- **`str.strip()`** — Entfernt Leerzeichen am Anfang und Ende
- **`str.upper()`** — Alle Buchstaben groß
- **`str.lower()`** — Alle Buchstaben klein
- **`str.replace(old, new)`** — Text ersetzen
- f-Strings (Vertiefung aus V02)

### Notizen
- Prompt = Kontext + Aufgabe + Format
- Übungen kombinieren String-Methoden mit Prompt-Bau

---

## V13 – Rechnerarchitektur (vereinfacht)

### Neu eingeführt

#### Matplotlib (Einstieg)
- **`import matplotlib.pyplot as plt`**
- **`plt.bar(x, y)`** — Balkendiagramm
- **`plt.title()`** — Diagramm-Titel
- **`plt.xlabel()`** / **`plt.ylabel()`** — Achsenbeschriftungen
- **`plt.show()`** — Diagramm anzeigen

### Notizen
- Nur `plt.bar()` als einziger Plot-Typ (nicht scatter, line, etc.)
- CPU/RAM/Festplatte erklärt mit Küchen-Analogie
- Stark reduziert gegenüber Original (kein Von-Neumann, kein Cache, keine Heatmaps)

---

## V14 – Betriebssysteme (vereinfacht)

### Neu eingeführt

#### os-Modul
- **`import os`**
- **`os.listdir(pfad)`** — Dateien/Ordner auflisten
- **`os.path.isfile(pfad)`** — Ist es eine Datei?
- **`os.path.isdir(pfad)`** — Ist es ein Ordner?
- **`os.path.getsize(pfad)`** — Dateigröße in Bytes
- **`os.path.join(a, b)`** — Pfade zusammenbauen

### Notizen
- Betriebssystem erklärt als "3 Aufgaben: Programme/Dateien/Hardware verwalten"
- Terminal-Basics: ls, cd, pwd, cat, mkdir
- Kein Scheduling, kein Paging, keine komplexen Algorithmen

---

## V15 – Netzwerk-Grundlagen (vereinfacht)

### Neu eingeführt

#### Funktionen (Einstieg)
- **`def funktionsname(parameter):`** — Funktion definieren
- **`return wert`** — Wert zurückgeben

#### String-Methoden
- **`str.split(sep)`** — String an Trennzeichen aufteilen
- **`str.startswith(prefix)`** — Prüft ob String mit prefix beginnt
- **`str.isdigit()`** — Prüft ob nur Ziffern

### Notizen
- Client-Server mit Restaurant-Analogie
- IP-Adressen, Ports, DNS vereinfacht
- Kein OSI-Modell, kein TCP/IP-Stack, kein Socket-Programmierung

---

## V16 – APIs und JSON

### Neu eingeführt

#### requests-Modul
- **`import requests`**
- **`requests.get(url)`** — HTTP-GET-Anfrage senden
- **`antwort.json()`** — JSON-Antwort als Dictionary einlesen

#### Dictionary-Zugriff (Vertiefung)
- **`daten["key"]`** — Wert aus Dictionary lesen
- **`daten["key1"]["key2"]`** — Verschachtelt zugreifen
- **`:,`** in f-Strings — Tausender-Trennzeichen

### Notizen
- Open-Meteo API (Wetter, kostenlos, kein API-Key)
- REST Countries API
- HTTP GET vs POST nur konzeptionell

---

## V17 – Kryptografie: Caesar-Chiffre

### Neu eingeführt

#### Builtins
- **`ord(zeichen)`** — Buchstabe → ASCII-Zahl
- **`chr(zahl)`** — ASCII-Zahl → Buchstabe

#### String-Methoden
- **`str.isalpha()`** — Prüft ob nur Buchstaben

#### String-Iteration
- **`for buchstabe in text:`** — Durch jeden Buchstaben iterieren

### Notizen
- Caesar-Chiffre als einfachste Verschlüsselung
- Symmetrisch vs. Asymmetrisch nur konzeptionell
- Brute-Force-Angriff (alle 26 Verschiebungen ausprobieren)

---

## V18 – Passwörter und Hashes

### Neu eingeführt

#### hashlib-Modul
- **`import hashlib`**
- **`hashlib.md5(text.encode()).hexdigest()`** — MD5-Hash berechnen
- **`str.encode()`** — String in Bytes umwandeln
- **`.hexdigest()`** — Hash als Hex-String

#### String-Methoden (Zeichen-Typ-Prüfung)
- **`str.isupper()`** — Ist Großbuchstabe?
- **`str.islower()`** — Ist Kleinbuchstabe?
- **`str.isdigit()`** — Ist Ziffer?
- **`str.isalnum()`** — Ist Buchstabe oder Ziffer?

### Notizen
- Hash als digitaler Fingerabdruck (Einweg, deterministisch, Lawineneffekt)
- Passwort-Speicherung als Hash
- Wörterbuch-Angriff als Übung

---

## V19 – Datenbanken Teil 1 (vereinfacht)

### Neu eingeführt

#### sqlite3-Modul
- **`import sqlite3`**
- **`sqlite3.connect("datei.db")`** — Datenbankverbindung
- **`verbindung.cursor()`** — Cursor erstellen
- **`cursor.execute("SQL")`** — SQL-Befehl ausführen
- **`cursor.fetchall()`** — Alle Ergebnisse als Liste
- **`verbindung.commit()`** — Änderungen speichern
- **`verbindung.close()`** — Verbindung schließen

#### SQL-Befehle
- **CREATE TABLE IF NOT EXISTS** — Tabelle erstellen
- **INSERT INTO ... VALUES (...)** — Daten einfügen
- **SELECT * FROM ...** — Daten abfragen
- **SELECT ... WHERE ...** — Filtern
- **UPDATE ... SET ... WHERE ...** — Daten ändern
- **DELETE FROM ... WHERE ...** — Daten löschen
- **Prepared Statements `(?, ?)`** — Sichere Parameter-Übergabe

### Notizen
- SQLite = Datenbank in einer einzigen Datei
- Nur 4 SQL-Befehle: SELECT, INSERT, UPDATE, DELETE
- Maschinenfabrik als durchgängiges Beispiel
- Kein ORM, keine Transaktionen, keine komplexen Queries

---

## V20 – Datenbanken Teil 2 (vereinfacht)

### Neu eingeführt

#### SQL-Konzepte
- **Fremdschlüssel (Foreign Key)** — Spalte die auf ID in anderer Tabelle verweist
- **JOIN ... ON ...** — Zwei Tabellen über Fremdschlüssel verknüpfen
- **GROUP BY spalte** — Ergebnisse gruppieren
- **COUNT(*)** — Zeilen pro Gruppe zählen
- **AVG(spalte)** — Durchschnitt berechnen
- **ORDER BY spalte DESC** — Sortieren
- **LIMIT n** — Nur n Ergebnisse zurückgeben

### Notizen
- Fabrik-Datenbank mit hallen + maschinen + wartungen
- "Datenbank-Detektiv" als spielerische Übung
- Nur INNER JOIN (kein LEFT/RIGHT/OUTER)
- Keine Subqueries, keine Transaktionen, kein HAVING
