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

import fc_print  # Ausgabe der Statistik
# Hinweis: Die import-Aufrufe erfolgen immer im Modul, das die jeweiligen
# weiteren Module benötigt. Für dieses Script werden weitere Module benötigt,
# die das Hauptmodul selbst nicht verwendet.

# Zunächst definiert man die verschiedenen Funktionen. Erst danach erstellt
# man eine Funktion, die tatsächlich etwas ausführt.
# Hier sind diese Funktionen ausgelagert in eigenen Modulen. Sie wurden oben
# bereits importiert.

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
    fc_print.print_stats()


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
