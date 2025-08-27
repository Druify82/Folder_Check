#!/usr/bin/env python3

# Die Shebang-Zeile ist die erste Zeile eines Scripts. Sie legt am
# Anfang des Scripts unabhängig vom Betriebssystem fest, dass dieses Skript
# mit Python 3 ausgeführt werden soll.
# Erforderlich für Linux, empfohlen für Windows und andere Betriebssysteme.

# Kommentare und DocStrings
#
# Ein DocString, ausgeschrieben Documentation String =
# Dokumentations-Zeichenfolge ist mehrzeiliger Text in jeweils
# dreifachem Anführungszeichen (""") in der ersten und letzten Zeile. Im
# DocString beschreibt man am Dokumentenanfang das Programm/Modul. Unter der
# Funktionsdefinition "def" beschreibt man, was die Funktion tut. Diese Texte
# kann man für eine automatisierte Dokumentation verwenden.
# Anders als Kommentare mit Nummernzeichen (#) ist der DocString nur am
# Dokumentanfang und unter einer neuen Funktion erlaubt. Er wird später zur
# Dokumentation benutzt.
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
Version: 0.2.0pre, 2025-08-20, 156:04

Kurzbeschreibung: Phase 2: Ausgabe-Modularisierung, Einführung Git
Autor: Druify, <waschmasche@gmail.com>
Co-Autor: Künstliche Intelligenz: ChatGPT, <https://chat.openai.com/chat>
Copyright (c) 2025 Druify
Lizenz: GNU General Public License v3.0 (GPL-3.0)

Beschreibung: Ordner überprüfen nach verschiedensten Kriterien

- Funktionen:
  - Zählt alle Dateien rekursiv.
  - Zählt alle Ordner rekursiv unter.
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
# parse_cmdline: Interpretation der Befehlszeile regeln
import argparse

# printstats: Global das Wörterbuch mit verschachtelter Liste und enthaltenen
# Typen beschreiben
# Wenn man dies nur in der Funktion festlegt, ist die Wörterbuchstruktur nur
# in dieser Funktion verständlich, wird aber sonst nicht zuverlässig erkannt.
# Innerhalb der Liste muss man die Einträge nicht mit Komma (,), sondern mit
# senkrechtem Strich (|) voneinander trennen.
StatsType = dict[str, list[str | int | bool]]

# Zunächst definiert man die verschiedenen Funktionen. Erst danach erstellt
# man eine Funktion, die tatsächlich etwas ausführt.


# Informationen ermitteln: Andere Funktionen werden die folgenden Informationen
# später abrufen.


def countfiles(countfiles_path: str) -> int:
    """
    Zählt rekursiv alle Dateien im Verzeichnis einschl. Unterordner.
    :param countfiles_path, str: Eingabe Pfad (String) zum Ordner
    :return -> int: Ausgabe Anzahl Integer/Ganzzahl) der gefundenen Dateien
    """
    # Variablen müssen zunächst initialisiert werden mit einem Anfangswert.
    countfiles_value = 0
    # os muss als übergeordnetes Modul mit der Methode walk benannt werden.
    # os.walk gibt ein Tupel zurück: (root, dirs, files)
    # Wir benutzen die Variablen root und dirs aus dem Tupel nicht. Daher
    # schreiben wir einen Unterstrich (_) davor oder lassen den Namen ganz weg.
    for _, _, files in os.walk(countfiles_path):
        # 0 + len(files) gibt Anzahl der Dateien in der Liste files zurück
        countfiles_value += len(files)
    return countfiles_value


def countdirs(countdirs_path: str) -> int:
    """
    Zählt rekursiv alle Ordner im Verzeichnis einschl. Unterordner.
    """
    countdirs_value = 0
    for _, dirs, _ in os.walk(countdirs_path):
        countdirs_value += len(dirs)
    return countdirs_value


# Befehlszeile


def parse_cmdline() -> argparse.Namespace:
    # Die obige Definition besagt: Die Klasse nimmt keine Eingaben. Die Ausgabe
    # ist ein Namespace-Objekt. Darin sind die eingegebenen Argumente
    # enthalten, die der Benutzer eingegeben hat. Deshalb wird später nicht die
    # Funktion gestartet, sondern eine Variable befüllt.
    """
    CLI (Command Line Interface / Befehlszeilen-Oberfläche) mit argparse
    Diese Funktion erstellt mit dem importierten Modul argparse einen
    ArgumentParser, der die Kommandozeilenargumente für das Skript verarbeitet.
    Sie definiert die erwarteten Argumente und gibt ein Namespace-Objekt
    zurück, das die geparsten Argumente enthält.
    :return: argparse.Namespace: Ein Namespace-Objekt, das die geparsten
    Kommandozeilenargumente enthält.
    Diese Funktion wird aufgerufen, um die Kommandozeilenargumente zu parsen
    und zurückzugeben. So kann die Main-Funktion sie verwenden.
    Der Benutzer ruft auf: programme.py <Befehlszeilenoptionen>
    In dieser Parser-Funktion steht, welche Möglichkeiten zulässig sind, welche
    Hilfetexte angezeigt werden.
    Diese Funktion legt nicht fest, was mit den zulässigen Eingaben passiert.
    """
    # Erstellen des ArgumentParsers
    # parser enthält alles, was zulässig ist auf der Befehlszeile.
    parser = argparse.ArgumentParser(
        # Beschreibung des Skripts
        # TODO: Aktuell unklar, wie man den Text mit f-Strings oder anderweitig
        # formatiert angeben kann.
        description='FolderCheck Phase 2: Statistiken für Ordner und '
        'Unterordner \n\n'
        'Ohne Parameter: Zeigt alle verfügbaren Statistiken für den aktuellen '
        'Ordner an.\n'
    )
    # Nun wird die Kommandozeile Stück für Stück beschrieben.
    # Hinzufügen des Arguments Path
    parser.add_argument(
        # Positionsargument ohne Flag
        'path',
        # Eingabetyp Text/String
        type=str,
        # Standardwert: Statt Punkt für aktuellen Arbeitsordner ist os.getcwd()
        # möglich (cwd = current working directory)
        default=os.getcwd(),
        # nargs: Numer of arguments legt fest, wie viele Eingaben zum Argument
        # gehören
        nargs='?',
        help="Pfad zum zu analysierenden Ordner. Standard: aktueller Ordner"
    )
    # Optional: Nur Ordner anzeigen
    parser.add_argument(
        # Mit "directories" kann man den Inhalt abrufen.
        "--directories", "-d",
        # dest= benötigt man, wenn man den Inhalt unter einem anderen Namen
        # abrufen möchte.
        dest="dirs",
        # action="store_true": standardmäßig ist das Flag gesetzt
        # TODO: Prüfen, ob richtig verstanden!
        # Wenn Flag angegeben wird, args.dirs auf True, andernfalls setze
        # es auf False.
        # Dies ist nützlich, um zu entscheiden, ob nur Ordner oder auch Dateien
        # gezählt werden sollen.
        # Wenn das Flag gesetzt ist, wird die Anzahl der Ordner gezählt.
        # Wenn das Flag nicht gesetzt ist, wird dies nicht gezählt.
        action="store_true",
        help="Ordner zählen"
    )
    # Dateien zählen
    parser.add_argument(
        "--files", "-f",
        dest="files",
        action="store_true",
        help="Dateien  zählen"
    )
    # Eingaben parsen (auswerten)
    # Die Eingaben werden nun auf zwei Arten ausgewertet:
    # 1. Lange Variante: Ausgabe des Parsers in einer temporären Variable:
    # args = parser.parse_args()
    # return args
    # TODO: Warum muss args nicht initialisiert werden wie andere
    # Variblen/Objekte?
    # Hier wird args ein Namespace-Objekt, das die eingegebenen Argumente
    # enthält. parse_args() wertet das Objekt parser aus.
    # Wenn die Eingaben gültig sind, werden  sie in args gespeichert.
    # Wenn die Eingaben ungültig sind, erscheint eine Fehlermeldung und
    # das Programm wird beendet.
    # args = parser.args() allein würde die Argumente parsen und in der
    # Variable args speichern. Erst return machtdie Argumente zur Ausgabe
    # dieser Funktion. Dann ist sie für andere Funktionen zugänglich.
    # 2. Kurze Variante: Ausgabe des Parsers direkt
    # return parser.parse_args()
    # TODO: Wann ist die kurze Variante besser, wann die lange?
    return parser.parse_args()


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
    args = parse_cmdline()
    # Dictionary (Wörterbuch) für Zählungen
    # Das Dictionary ruft die Funktionen auf, die die Ergebnisse für die
    # Statistik liefern.
    # Die Schlüssel sind die Namen der Statistiken, die Werte sind Tupel mit
    # dem Anzeigetext,  der ausgeführten Funktion sowie einem bool'schen Wert,
    # um die spätere Anzeige zu (de)aktivieren.
    # Die Werte sind Listen, die den Status der Statistik enthalten. Sonst
    # wären sie immutables (Unveränderliche).
    # Standard wäre: stats = {, hier aber um Beschreibung erweitert.
    # Alias legt fest: Dies ist ein Dictionary mit den Typen:
    # str,→ Liste aus str | int | bool
    stats: StatsType = {
        "stats_files": ["Anzahl Dateien", countfiles(args.path), False],
        "stats_dirs": ["Anzahl Ordner", countdirs(args.path), False]
    }
    # Ausgabe der Ergebnisse
    # Die Ausgabe erfolgt in der Konsole.
    # Teil 1: Statistikausgabe vorbereiten, gewünschte Einträge auf True
    # TODO: Die if-Schleife soll wie folgt flexibler werden
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
            print(f"{stats_text} in {args.path}: {stats_value}")
            # Stelle dies auf true, weil etwas gedruckt wurde.
            printed = True
    # Achtung: Dieser if-Teil gehört nicht mehr zur for-SChleife!
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
# Wenn dies fehlt, wird jeder Funktionsaufruf von außen ganze Skript von
# main() aus ausführen, statt nur der jeweiligen Funktion.
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
