# 23/11/2023 First steps developed by ChatGPT
# Welcher Ordner hat die meisten Dateien?
# Code von ChatGPT

import os

# def count_files_in_directory(directory):
    """ Zählt die Dateien in einem gegebenen Verzeichnis. """
    return sum([len(files) for r, d, files in os.walk(directory)])

def get_directories_with_most_files(root_directory, top_n=10):
    """ Findet die Top-N-Verzeichnisse mit den meisten Dateien. """
    directory_counts = {}
    for directory in [d for d in os.listdir(root_directory) if os.path.isdir(os.path.join(root_directory, d))]:
        full_path = os.path.join(root_directory, directory)
        directory_counts[full_path] = count_files_in_directory(full_path)

    # Sortiert die Verzeichnisse nach der Anzahl der Dateien
    sorted_directories = sorted(directory_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_directories[:top_n]

# Benutzereingabe für das Hauptverzeichnis, Standard ist das aktuelle Verzeichnis
root_directory = input("Bitte geben Sie den Pfad zum Hauptverzeichnis ein (leer lassen für aktuelles Verzeichnis): ")
if not root_directory:
    root_directory = os.getcwd()

top_directories = get_directories_with_most_files(root_directory)

for dir_path, count in top_directories:
    print(f"Ordner: {dir_path}, Anzahl der Dateien: {count}")
