"""Ausgabe der Statistiken in der Konsole"""

import fc_cli  # Befehlszeile auswerten
import fc_stats  # Statistiken erstellen

# StatsType: Global das Wörterbuch mit verschachtelter Liste und enthaltenen
# Typen beschreiben
# Wenn man dies nur in der Funktion festlegt, ist die Wörterbuchstruktur nur
# in dieser Funktion verständlich, wird aber sonst nicht zuverlässig erkannt.
# Wenn man dies nicht festlegt, kann der Linter die Struktur
# unerwartet falsch interpretieren. Dies ist also eine Absicherung.
# Innerhalb der Annotation trennt der Union Operator,
# ein senkrechter Strich (|) die Typen voneinander. In Listen trennt man die
# Elemente weiterhin mit Komma (,).
StatsType = dict[str, list[str | int | bool]]


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
        "stats_files": [
            "Anzahl Dateien", fc_stats.count_files(
                args.path), False], "stats_dirs": [
            "Anzahl Ordner", fc_stats.count_dirs(
                args.path), False]}
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
