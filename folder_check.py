#!/usr/bin/env python3

# Die Shebang-Zeile legt am Dokumentanfang unabhängig vom Betriebssystem fest,
# dass dieses Skript mit Python 3 ausgeführt werden soll.

"""
foldercheck.py – Einsteiger-Skript für FolderCheck
Version: 0.2.0, 2025-06-04, 17:53
Kurzbeschreibung: Phase 2: Ausgabe-Modularisierung, Einführung Git
Autor: Druify, <waschmasche@gmail.com>
Co-Autor: Künstliche Intelligenz: ChatGPT, <https://chat.openai.com/chat>
Copyright (c) 2025 Druify
Lizenz: GNU General Public License v3.0 (GPL-3.0)

Beschreibung: Ordner überprüfen nach verschiedensten Kriterien

Funktionen:
- countfiles(countfiles_path): zählt alle Dateien rekursiv.
- countdirs(countdirs_path): zählt alle Ordner rekursiv unter.
- CLI-Grundgerüst mit argparse:
  - Optionales Positionsargument [path], ansonsten aktueller Ordner

Erklärungen zu argparse und Verbindung zu count_files:
- argparse ist ein Modul, das es ermöglicht, Kommandozeilenargumente zu parsen
  und zu verarbeiten.
- Es wird verwendet, um dem Skript die Möglichkeit zu geben, Eingaben von der
  Kommandozeile zu akzeptieren.
- In diesem Skript wird argparse verwendet, um den Pfad zum zu analysierenden
  Ordner zu akzeptieren.
- Die Funktion countfiles wird aufgerufen, um die Anzahl der Dateien im
  angegebenen Ordner zu zählen.
"""


# Diese Module werden benötigt.
import os
import argparse

# Zunächst werden Funktionen definiert, die in diesem Script benötigt werden.


def countfiles(countfiles_path: str) -> int:
    """
    Zählt rekursiv alle Dateien im Verzeichnis `countfiles_path` inkleinschl.
    Unterordner.
    :param countfiles_path, str: Pfad (String) zum zu analysierenden Ordner
    :return -> int: Anzahl Integer/Ganzzahl) der gefundenen Dateien
    """
    totalfiles = 0
    # os muss als übergeordnetes Modul mit der Methode walk benannt werden
    # Da wir die Variablen root und dirs nicht benutzen, schreiben wir einen
    # Unterstrich davor oder lassen den Namen ganz weg.
    for _, _, files in os.walk(countfiles_path):
        # 0 + len(files) gibt Anzahl der Dateien in der Liste files zurück
        # os.walk gibt ein Tupel zurück: (root, dirs, files)
        totalfiles += len(files)
    return totalfiles


def countdirs(countdirs_path: str) -> int:
    """
    Zählt rekursiv alle Ordner im Verzeichnis `countdirs_path` inkl.
    Unterordner.
    :param countdirs_path, str: Pfad (String) zum zu analysierenden Ordner
    :return -> int: Anzahl Integer/Ganzzahl) der gefundenen Dateien
    """
    totaldirs = 0
    for _, dirs, _ in os.walk(countdirs_path):
        # 0 + len gibt Anzahl der ordner in der Liste dirs zurück
        totaldirs += len(dirs)
    return totaldirs


def parse_cmdline() -> argparse.Namespace:
    # Die obige Definition besagt: Die Klasse nimmt keine Eingaben. Die Ausgabe
    # ist ein Namespace-Objekt. Darin sind die eingegebenen Argumente
    # enthalten, die der Benutzer eingegeben hat. Deshalb wird später nicht die
    # Funktion gestartet, sondern eine Variable befüllt.
    """
    CLI-Grundgerüst mit argparse als eigene Funktion
    Diese Funktion erstellt einen ArgumentParser, der die
    Kommandozeilenargumente für das Skript verarbeitet. Sie definiert die
    erwarteten Argumente und gibt ein Namespace-Objekt zurück, das die
    geparsten Argumente enthält.
    :return: argparse.Namespace: Ein Namespace-Objekt, das die geparsten
    Kommandozeilenargumente enthält.
    Diese Funktion wird aufgerufen, um die Kommandozeilenargumente zu parsen
    und zurückzugeben, damit sie in der main-Funktion verwendet werden können.
    Sie ist dafür verantwortlich, die Eingaben des Benutzers zu verarbeiten und
    die entsprechenden Argumente zu definieren, die das Skript akzeptiert.
    Diese Funktion ist wichtig, um die Eingaben des Benutzers zu verarbeiten
    und die entsprechenden Argumente zu definieren, die das Skript akzeptiert.
    Sie ermöglicht es dem Skript, flexibel auf verschiedene Eingaben zu
    reagieren und die gewünschten Informationen zu liefern, wie z.B. die Anzahl
    der Dateien und Ordner im angegebenen Pfad.
    """
    # Erstellen des ArgumentParsers
    # main_parser ist der Parser für die Kommandozeilenargumente. Hier
    # wird das Skript konfiguriert, um Eingaben von der Kommandozeile zu
    # akzeptieren.
    parser = argparse.ArgumentParser(
        # Beschreibung des Skripts
        description="FolderCheck Phase 1: Zählt Dateien in einem Ordner und \
        Unterordnern"
    )
    # Hinzufügen des Arguments --path bzw. -p
    # main_parser wird nun schrittweise konfiguriert, um Eingaben von der
    # Kommandozeile zu akzeptieren.
    parser.add_argument(
        # Der erste string legt fest, dass der Wert in main_args.path
        # gespeichert wird.
        # "-" für Kurzbefehl und "--" für Langbefehl dürfen vorangestellt
        # werden. Dann muss der entsprechende Kurz- oder Langbefehl ebenfalls
        # auf der Kommandozeile erscheinen.
        # Dest= würde benötigt, wenn man einen anderen Namen für das spätere
        # Argument benutzen möchte.
        'path',
        # Eingabetyp Text/String
        type=str,
        # Standardwert: Statt Punkt für aktuellen Arbeitsordner ist os.getcwd()
        # möglich (current working directory)
        default=os.getcwd(),
        # nargs: Numer of arguments legt fest, wie viele Eingaben zum Argument
        # gehören
        nargs='?',
        help="Pfad zum zu analysierenden Ordner. Standard: aktueller Ordner"
    )
    # Optional: Nur Ordner anzeigen
    parser.add_argument(
        "--directories", "-d",
        # action="store_true": standardmäßig ist das Flag gesetzt
        # Wenn Flag angegeben wird, main_args.dirs auf True, andernfalls setze
        # es auf False.
        # Dies ist nützlich, um zu entscheiden, ob nur Ordner oder auch Dateien
        # gezählt werden sollen.
        # Wenn das Flag gesetzt ist, wird die Anzahl der Ordner gezählt.
        # Wenn das Flag nicht gesetzt ist, wird die Anzahl der Dateien gezählt.
        dest="dirs",
        action="store_true",
        help="Nur Ordner zählen"
    )

    # Eingaben parsen:
    # args wird ein Namespace-Objekt, das die Argumente enthält
    # die vom Benutzer eingegeben wurden.
    # parse_args() liest die Kommandozeilenargumente ein und prüft sie gegen
    # die Definitionen.
    # Wenn die Eingaben gültig sind, werden sie in main_args gespeichert.
    # Wenn die Eingaben ungültig sind, wird eine Fehlermeldung ausgegeben und
    # das Programm beendet.
    # Dies wird nun mit return gemacht, damit die Funktion parse_cmdline
    # aufgerufen werden kann, um die Argumente zu parsen und zurückzugeben.
    # parser.parse_args() gibt ein Namespace-Objekt zurück, das die Argumente
    # enthält, die vom Benutzer eingegeben wurden.
    # args = parser.parse_args() würde die Argumente parsen und in der
    # Variable args speichern, aber wir wollen die Argumente in der Funktion
    # parse_cmdline zurückgeben, damit sie in der main-Funktion verwendet
    # werden können.
    # Daher wird hier return verwendet, um die Argumente zurückzugeben.
    # Wenn
    # die Funktion parse_cmdline aufgerufen wird, werden die Argumente geparst
    # und in einem Namespace-Objekt gespeichert, das dann in der main-Funktion
    # verwendet werden kann.
    # parser.parse_args() gibt ein Namespace-Objekt zurück, das die Argumente
    # enthält, die vom Benutzer eingegeben wurden.
    # args = parser.parse_args()
    # Stattdessen die Ausgabe dieser Funktion aktivieren.
    return parser.parse_args()


def print_stats():
    """
    Ausgabefunktion
    Diese Funktion gibt die Statistiken der gezählten Dateien und Ordner aus.
    Sie wird aufgerufen, um die Ergebnisse der Zählung anzuzeigen.
    """
    # Da wir hier die Ausgabe des Parsers brauchen, befüllen wir eine Variable
    # mit dem Namespace. Man ruft hier also nicht die Funktion selbst auf.
    # Wäre der Parser ein Teil der Funktion, so wäre dieser Schritt nicht
    # nötig.
    args = parse_cmdline()
    # Ruft die Zählfunktionen auf, um die Anzahl der Dateien und Ordner im
    # angegebenen Pfad zu zählen.

    # Dictionary für Zählungen
    # Die Schlüssel sind die Namen der Statistiken, die Werte sind Tupel mit
    # dem Text und der Anzahl.
    # Die Tupel enthalten den Text, der ausgegeben werden soll, und die Anzahl
    # der Dateien bzw. Ordner, die gezählt wurden.
    # Diese Form des Dictionaries hat mehrere Vorteile:
    # 1. Es ist einfach, die Statistiken zu erweitern, indem
    # neue Schlüssel-Wert-Paare hinzugefügt werden.
    # 2. Es ist einfach, die Statistiken zu iterieren und auszugeben.
    # 3. Es ist einfach, die Statistiken zu formatieren und auszugeben.
    # 4. Es ist einfach, die Statistiken zu sortieren, wenn nötig.
    # 5. Es ist einfach, die Statistiken zu erweitern, indem neue
    # Schlüssel-Wert-Paare hinzugefügt werden.
    # Nachteile:
    # 1. Es ist etwas komplexer als eine einfache Liste.
    # 2. Es ist etwas weniger performant als eine einfache Liste, da es
    #    ein Dictionary ist.
    stats = {
        "stats_files": ("Anzahl Dateien ", countfiles(args.path)),
        "stats_dirs": ("Anzahl Ordner", countdirs(args.path))
    }
    # Ausgabe der Ergebnisse
    # main_totalfiles enthält die Anzahl der Dateien, die von count_files
    # zurückgegeben wurde.
    # Die Ausgabe erfolgt in der Konsole.
    if args.dirs:
        # Beispiel für einen f-String, der nicht auf eine Code-zeile passt.
        print(
            f'{stats["stats_dirs"][0]} in "{args.path}": '
            f'{stats["stats_dirs"][1]}'
        )
    else:
        # Eine einfachere Form wäre die folgende:
        # for key in stats:
        #     stats_text, stats_count = stats[key]
        # Um gleich das ganze Tupel zu iterieren, ist die folgende
        # Schreibweise besser.
        for _key, (stats_text, stats_count) in stats.items():
            print(f'{stats_text} in "{args.path}": {stats_count}')


def main():
    """
    Hauptfunktion des Skripts, die die Kommandozeilenargumente parst und die
    Zählfunktionen aufruft.
    Diese Funktion ist der Einstiegspunkt des Skripts. Sie wird aufgerufen,
    wenn das Skript direkt ausgeführt wird.
    """
    print_stats()


# Ende der Funktionsdefinitionen: Hier werden sie nun ausgeführt, ausgehend von
# main(), das die anderen Funktionen aufruft.
# Hauptfunktion aufrufen, wenn das Skript direkt ausgeführt wird
# Dies ist der Einstiegspunkt des Skripts. Wenn das Skript direkt ausgeführt
# wird, wird die main-Funktion aufgerufen, um die Argumente zu parsen und die
# Zählfunktion auszuführen.
if __name__ == "__main__":
    main()
# Wenn das Skript als Modul importiert wird, wird die main-Funktion nicht
# aufgerufen. Dies ermöglicht es, die Funktionen count_files und main in
# anderen Skripten zu verwenden, ohne dass die main-Funktion automatisch
# ausgeführt wird.
# Dies ist eine gute Praxis, um die Wiederverwendbarkeit des Codes zu erhöhen.
# Das Skript ist nun bereit.
