"""Statistiken erstellen"""
# Funktionen für Statistikerstellung aus Betriebssystem (os = Operating System)
import os

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
