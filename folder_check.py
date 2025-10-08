#!/usr/bin/env python3

# Die Shebang-Zeile ist die erste Zeile eines Scripts. Sie legt am
# Anfang des Scripts unabhängig vom Betriebssystem fest, dass dieses Skript
# mit Python 3 ausgeführt werden soll.
# Erforderlich wenn unter Unix als ausführbare Datei markiert.
# Nicht erforderlich für Windows und andere Betriebssysteme.

# Kommentare und DocStrings
#
# Ein docstring, ausgeschrieben Documentation String =
# Dokumentations-Zeichenfolge ist mehrzeiliger Text in jeweils
# dreifachem Anführungszeichen (""") vor und nach dem Dokumentationstext.
# Weniger üblich sind alternativ dreifach einfache Anführungszeichen ('''). Der
# Text darf auf einer Zeile stehen oder mehrzeilig sein. Mehrzeiliger Text
# braucht kein eigenes Kommentarzeichen am Zeilenanfang.
# Am Anfang des Moduls (der Datei) beschreibt man das Programm oder Modul: Nach
# Shebang und Angabe der Codierung, aber vor allen anderen Anweisungen.
# Unter der Definition von Funktionen und Klassen "def" beschreibt man, was die
# Funktion oder Klasse tut.
# Diese Texte kann man für eine automatisierte Dokumentation verwenden.
# An anderen Stellen hat der DocString keine Bedeutung.
#
# Kommentare beginnen am Zeilenanfang oder nach einer Codezeile mit
# Nummernzeichen (#). Abgesehen von der Shebang-Zeile benutzt man sie nur, um
# den Code vor Ort zu erklären. Sie werden in der Regel nicht für die
# Dokumentation ausgelesen.
#
# TODO-Kommentare werden von Editoren hervorgehoben, damit man sich Aufgaben
# notieren kann.

"""
foldercheck.py – Einsteiger-Skript für FolderCheck
Version: 0.2.0-pre, 2025-10-08, 19:45

Kurzbeschreibung: Phase 2: Erste modularisierte Version
Autor: Druify, <waschmasche@gmail.com>
Co-Autor: Künstliche Intelligenz: ChatGPT, <https://chat.openai.com/chat>
Copyright (c) 2025 Druify
Lizenz: GNU General Public License v3.0 (GPL-3.0)

Beschreibung: Ordner überprüfen nach verschiedensten Kriterien

- Funktionen:
  - Zählt alle Dateien rekursiv.
  - Zählt alle Ordner und Unterordner rekursiv.
  - Statistikausgabe
  - CLI
  - Main-Funktion

Struktur:
- Vorbereitung auf mehrere Module
- Kommentare, um den Code als Einsteiger zu verstehen

"""


# Diese Module werden benötigt.
# Funktionen für Statistikerstellung aus Betriebssystem (os = Operating System)
import os

# Befehlszeile auswerten
import fc_cli

# printstats: Global das Wörterbuch mit verschachtelter Liste und enthaltenen
# Typen beschreiben
# Wenn man dies nur in der Funktion festlegt, ist die Wörterbuchstruktur nur
# in dieser Funktion verständlich, wird aber sonst nicht zuverlässig erkannt.
# Wenn man dies nicht festlegt, kann der Linter die Struktur
# unerwartet falsch interpretieren. Dies ist also eine Absicherung.
# Innerhalb der Annotation trennt der Union Operator,
# ein senkrechter Strich (|) die Typen voneinander. In Listen trennt man die
# Elemente weiterhin mit Komma (,).
StatsType = dict[str, list[str | int | bool]]

# Zunächst definiert man die verschiedenen Funktionen. Erst danach erstellt
# man eine Funktion, die tatsächlich etwas ausführt.


# Informationen ermitteln: Andere Funktionen werden die folgenden Informationen
# später abrufen.


def count_files(count_files_path: str) -> int:
    """
    Zählt rekursiv alle Dateien im Verzeichnis einschl. Unterordner.
    :param count_files_path, str: Eingabe Pfad (String) zum Ordner
    :return -> int: Ausgabe Anzahl Integer/Ganzzahl der gefundenen Dateien
    """
    # Man muss die Variable nicht wie in anderen Programmiersprachen
    # initialisieren mit dem Inhaltstypen. Aber man muss einmalig einen
    # Anfangswert angeben.
    count_files_value = 0
    # os muss als übergeordnetes Modul mit der Methode walk benannt werden.
    # os.walk gibt ein Tupel zurück: (root, dirs, files)
    # Wir benutzen die Variablen root und dirs aus dem Tupel nicht. Daher
    # schreiben wir einen Unterstrich (_) davor oder lassen den Namen ganz weg.
    for _, _, files in os.walk(count_files_path):
        # 0 + len(files) gibt Anzahl der Dateien in der Liste files zurück
        count_files_value += len(files)
    return count_files_value


def count_dirs(count_dirs_path: str) -> int:
    """
    Zählt rekursiv alle Ordner im Verzeichnis einschl. Unterordner.
    """
    count_dirs_value = 0
    for _, dirs, _ in os.walk(count_dirs_path):
        count_dirs_value += len(dirs)
    return count_dirs_value


# Ausgabe der Statistik


def print_stats() -> None:
    # -> None: Optional: stellt für  Linter klar, dass es keine Ausgabe gibt.
    """
    Ausgabefunktion
    Diese Funktion gibt die Statistiken der gezählten Dateien und Ordner aus.
    Sie wird aufgerufen, um die Ergebnisse der Zählung anzuzeigen.
    """
    # Momentan erhält die Statistik die Pfadangabe aus der Kommandozeile. Daher
    # muss man zuerst eine Variable befüllen mit der Ausgabe des Parsers. Dann
    # kann die Ausgabe ausgewertet werden.
    # Wäre der Parser Teil dieser Definition, könnte man ohne diesen
    # Zwischenschritt abfragen, was auf der Kommandozeile angegeben wurde.
    args = fc_cli.parse_cmdline()
    # Dictionary (Wörterbuch) für Zählungen
    # Das Dictionary ruft die Funktionen auf, die die Ergebnisse für die
    # Statistik liefern.
    # Die Schlüssel sind die Namen der Statistiken. Die Werte sind eine Liste
    # mit dem Anzeigetext, der ausgeführten Funktion sowie einem boolschen
    # Wert, um die spätere Anzeige zu (de)aktivieren.
    # Die Liste ermöglicht, dass die Einträge veränderlich sind.
    # Standard für die Ankündigung eines Wörterbuchs wäre:
    # stats = {
    # Doch hier wird die Ankündigung um die global typannotierte Beschreibung
    # erweitert. Damit ist die Struktur für den Linter eindeutig.
    stats: StatsType = {
        "stats_files": ["Anzahl Dateien", count_files(args.path), False],
        "stats_dirs": ["Anzahl Ordner", count_dirs(args.path), False]
    }
    # Ausgabe der Ergebnisse
    # Die Ausgabe erfolgt in der Konsole.
    # Teil 1: Statistikausgabe vorbereiten, gewünschte Einträge auf True
    # TODO: Die if-Bedingung soll wie folgt flexibler werden
    # Frage ohne die genauen namen zu wissen ab, welche Befehlszeilenargumente
    # angegeben wurden und stelle sie auf true. Wichtig, wenn immer mehr
    # Einstellungen dazu kommen.
    # Ansonsten stelle standardmäßig alle Ausgaben auf true.
    if args.dirs:
        stats["stats_dirs"][2] = True
    if args.files:
        stats["stats_files"][2] = True
    if not (args.files or args.dirs):
        stats["stats_dirs"][2] = True
        stats["stats_files"][2] = True
    # Teil 2: Ausgabe aller Einträge mit True
    # Variable printed bleibt nur unverändert, wenn nichts gedruckt wurde.
    printed = False
    # Die for-Schleife druckt alles, was auf True steht.
    # Vollständig wäre: Diese Variante würde auch die Schlüssel (ersten Teile)
    # des Wörterbuchs aufzählen, obwohl die Schlüssel nicht benötigt werden.
    # for _key, (stats_text, stats_value, stats_on) in stats.items():
    # Effizienter: Diese Variante ruft nur auf, was benötigt wird.
    for stats_text, stats_value, stats_on in stats.values():
        if stats_on:  # Wenn der Eintrag auf True gesetzt ist
            print(f'{stats_text} in "{args.path}": {stats_value}')
            # Stelle dies auf true, weil etwas gedruckt wurde.
            printed = True
    # Achtung: Dieser if-Teil gehört nicht mehr zur for-Schleife!
    # Die For-Schleife sagt also nur: Gebe etwas aus, oder tue nichts.
    if not printed:
        print(f"Nichts gezählt in {args.path}")


# Hauptfunktion: Dies ist der Startpunkt.

def main() -> None:
    """
    Hauptfunktion des Skripts
    Diese Funktion ist der Einstiegspunkt des Skripts. Sie wird nur aufgerufen,
    wenn das Skript direkt ausgeführt wird.
    """
    # TODO: Main-Funktion Besonderheiten verstehen
    # Hier steht, wo das Programm beginnt.
    #
    # Warum steht hier nicht z.B. die Erzeugung der Statistik?
    # Da die Statistik eine eigene Funktion ist, kann sie auch von anderen
    # Punkten im Script aus aufgerufen werden. Das ist mit der main-Funktion
    # nicht möglich.
    print_stats()


# Ende der Funktionsdefinitionen: main() ist der Einstiegspunkt.


# Hauptfunktion nur aufrufen, wenn das Skript direkt ausgeführt wird
# Die Verwendung dieser Zeile ist eine Good Practice, damit Teile des Scripts
# auch einzeln aufgerufen werden dürfen.
# Mit dieser Code-Zeile startet main() nur beim direkten Ausführen, nicht beim
# Importieren des Moduls.
# Damit ist es möglich, einzelne Funktionen von außen aufzurufen.
if __name__ == "__main__":
    main()

# TODO: Parkplatz für weitere Lernthemen:
# - break vs. „alles ausgeben“ (for/else, printed-Flag).
# • Typing-Feinschliff (NamedTuple/TypedDict, mypy-Konfig).
# • Flags-Aufteilung in getrennte Dictionaries (Daten vs. enabled-States).
# • Unit-Tests mit pytest.
# • .gitignore/Git-Workflows (Split-Commits, amend, tags).
# • VSCode-Accessibility-Shortcuts, Linter/Formatter-Feinschliff.
# • Wie kann ich in Phase2 zunächst die 1-Datei-Version commiten und
#   anschließend
#   die neue Struktur mit völlig anderen Dateinamen erstellen, ohne die Datei
#   weiter zu berücksichtigen?
