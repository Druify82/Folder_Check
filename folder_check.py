#!/usr/bin/env python3
# Die Shebang-Zeile legt am Dokumentanfang unabhängig vom Betriebssystem fest,
# dass dieses Skript mit Python 3 ausgeführt werden soll.

"""
foldercheck.py – Einsteiger-Skript für FolderCheck
Version: 0.1, 2025-05-28, 15:00
Kurzbeschreibung: Phase 1: Dateien und Ordner zählen, Grundgerüst für CLI
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


def main():
    """
    Hauptfunktion des Skripts, die die Kommandozeilenargumente parst und die
    Zählfunktionen aufruft.
    Diese Funktion ist der Einstiegspunkt des Skripts. Sie wird aufgerufen,
    wenn das Skript direkt ausgeführt wird.
    Sie konfiguriert den ArgumentParser, um die Kommandozeilenargumente zu
    akzeptieren, und ruft die Zählfunktionen auf, um die Anzahl der Dateien
    und Ordner im angegebenen Pfad zu zählen.
    :return: None
    """

    # CLI-Grundgerüst mit argparse
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
        help="Pfad zum zu analysierenden Ordner"
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
        help="Zusätzlich Ordner zählen"
    )

    # Eingaben parsen:
    # args wird ein Namespace-Objekt, das die Argumente enthält
    # die vom Benutzer eingegeben wurden.
    # parse_args() liest die Kommandozeilenargumente ein und prüft sie gegen
    # die Definitionen.
    # Wenn die Eingaben gültig sind, werden sie in main_args gespeichert.
    # Wenn die Eingaben ungültig sind, wird eine Fehlermeldung ausgegeben und
    # das Programm beendet.
    args = parser.parse_args()

    # Zählfunktion aufrufen
    main_totalfiles = countfiles(args.path)
    main_totaldirs = countdirs(args.path)
    # Ausgabe der Anzahl der Dateien und Ordner je nach Angabe von -d
    # main_totalfiles enthält die Anzahl der Dateien, die von count_files
    # zurückgegeben wurde.
    # Die Ausgabe erfolgt in der Konsole.
    if args.dirs:
        print(f"Anzahl Ordner unter '{args.path}': {main_totaldirs}")
    else:
        print(f"Anzahl Ordner unter '{args.path}': {main_totaldirs}")
        print(f"Anzahl Dateien unter '{args.path}': {main_totalfiles}")


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
