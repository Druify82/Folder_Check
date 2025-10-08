""" parse_cmdline: Befehlszeile auswerten """

# Funktionen zur Auswertung der Befehlszeile
import argparse
# Auf Funktionen des Betriebssystems zugreifen (z.B. cwd)
import os

# Interpretation der Befehlszeile regeln


def parse_cmdline() -> argparse.Namespace:
    # Diese Funktion hat keine Parameter. Sie nimmt keine Eingaben an. Der
    # Rückgabewert, die Ausgabe, ist ein Namespace-Objekt. Darin sind die
    # eingegebenen Argumente enthalten, die der Benutzer eingegeben hat.
    # Deshalb führt man später nicht die Funktion aus, sondern man befüllt
    # damit eine Variable.
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
    Der Benutzer ruft auf:
    <PythonScript>.py <Befehlszeilenoptionen>
    In dieser Parser-Funktion steht, welche Möglichkeiten zulässig sind, welche
    Hilfetexte angezeigt werden.
    Diese Funktion legt nicht fest, was mit den zulässigen Eingaben passiert.
    """
    # Erstellen des ArgumentParsers
    # parser enthält alles, was zulässig ist auf der Befehlszeile.
    parser = argparse.ArgumentParser(
        # Diese Beschreibung wird auf der Kommandozeile angezeigt.
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
        # möglich
        # cwd = current working directory
        default=os.getcwd(),
        # nargs: number of arguments legt fest, wie viele Eingaben zum Argument
        # gehören.
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
        # action="store_true": Setzt das Flag auf Boolean True, wenn es auf
        # der Befehlszeile vorkommt. Es bleibt sonst False.
        # Dies ist nützlich, um abzufragen, ob der Benutzer das Flag Argument
        # auf der Befehlszeile angegeben hat.
        action="store_true",
        help="Ordner zählen"
    )
    # Dateien zählen
    parser.add_argument(
        "--files", "-f",
        dest="files",
        action="store_true",
        help="Dateien zählen"
    )
    # Eingaben parsen (auswerten)
    # Die Eingaben kann man nun auf zwei Arten auswerten:
    # 1. Lange Variante: Ausgabe des Parsers in einer temporären Variable
    # Notwendig, wenn man das Ergebnis vor der Übergabe weiter auswerten
    # möchte.
    # args = parser.parse_args()
    # return args
    # Die Variable args wird hier befüllt. Man kann sie danach sofort
    # verwenden. Hier wird args ein Namespace-Objekt, das die eingegebenen
    # Argumente als Attribute enthält. parse_args() wertet das Objekt parser
    # aus.
    # Wenn die Eingaben gültig sind, werden  sie in args gespeichert.
    # Wenn die Eingaben ungültig sind, erscheint eine Fehlermeldung und
    # das Programm wird beendet.
    # args = parser.parse_args() allein würde die Argumente parsen und in der
    # Variable args speichern. Erst return macht die Argumente zur Ausgabe
    # dieser Funktion. Dann ist sie für andere Funktionen zugänglich.
    # 2. Kurze Variante: Ausgabe des Parsers direkt
    # Geeignet, wenn hier nichts weiter passiert, z.B. eine Auswertung in
    # einer anderen Funktion oder einem anderen Modul erfolgt.
    # return parser.parse_args()
    return parser.parse_args()
