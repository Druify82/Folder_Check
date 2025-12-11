# FolderCheck – Roadmap (Version 1.0)

## Phase 1 – Grundfunktionen (Abgeschlossen, v0.1.0)
- Dateien zählen
- Ordner zählen
- Rekursive Traversierung
- Basis-CLI mit argparse
- Erste Strukturierung & Kommentare
- Git-Initialisierung + Tags

## Phase 2 – Modularisierung (Abgeschlossen, v0.2.0)
- Aufteilen in fc_cli, fc_stats, fc_print
- Boolean-Flags: -d, -f
- Erweiterte Dictionary-Struktur
- Verbessertes Fehlerverständnis (argparse, Pylance, Immutable vs Mutable)
- DocStrings + Kommentare harmonisieren
- Git-Workflow vertiefen (Branches, Releases)

## Phase 3 – Erweiterte Funktionen (Aktuell)
Ziele:
- Neues Output-System (mehr Optionen, sauberere Logik)
- Zusätzliche Flags:
  - `-n` (no output)
  - `-e` (extended info oder error info)
  - evtl. `--json` Export
- Weitere statistische Werte:
  - Anzahl Dateien pro Endung
  - Tiefste Ebene
  - Größtes File
  - Kleinste File
- Vorbereitung auf spätere Testbarkeit

## Phase 4 – Fehlerbehandlung & Robustheit
- try/except um Eingaben
- Saubere Fehlermeldungen
- Testfälle für falsche Pfade, fehlende Rechte
- Logging-Basis mit logging-Modul
- Saubere Exit-Codes

## Phase 5 – Testing & QA
- Unittests (pytest)
- Struktur für Tests einrichten (tests/)
- Coverage (optional)
- Linter-Konfiguration optimieren
- Automatisierte Checks (später GitHub Actions optional)

## Phase 6 – Erweiterte CLI (professioneller Stil)
- Subcommands (z. B. `foldercheck stats`, `foldercheck find`, `foldercheck tree`)
- Gemeinsame Optionen (global args)
- Hilfe-Text strukturieren
- Farbige Ausgabe (optional)

## Phase 7 – Persistenz & Konfiguration
- Config-Dateien (YAML oder TOML)
- Default-Verhalten konfigurierbar
- Speicherung letzter Pfade
- Optionaler interaktiver Modus

## Phase 8 – Export & Integration
- JSON-Export
- CSV-Export
- Ausgabe in Dateien
- Schnittstellen für weitere Tools
- Möglicher GUI-Startpunkt (tkinter oder webbasierte Konsole)

## Phase 9 – Optimierung & Parallelisierung (optional)
- Beschleunigte Directory-Scans
- Thread- oder Process-basierte Parallelisierung
- Caching für wiederkehrende Durchläufe

## Phase 10 – Finalisierung & Packaging
- packaging (setup.cfg, pyproject.toml)
- pip-installierbares Paket
- Offizielle Releases
- README, ROADMAP, CHANGELOG
