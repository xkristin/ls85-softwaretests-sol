# Baustein 08 – Theorie: Testdokumentation

> **Lesezeit:** ca. 20–25 Minuten  
> Lies diesen Text vollständig durch, bevor du mit den Aufgaben beginnst.

---

## Warum dokumentieren?

Im Berufsalltag reicht es nicht, Tests zu schreiben – du musst auch **nachweisen**, dass du getestet hast und was dabei herausgekommen ist. Ohne Dokumentation gibt es keinen Qualitätsnachweis.

Testdokumentation dient der:
- **Nachvollziehbarkeit:** Wer hat was wann getestet?
- **Qualitätssicherung:** Nachweisbar gegenüber Auftraggeber und Kunden
- **Abnahmeentscheidung:** Ist das System bereit für den Produktivbetrieb?
- **Rückverfolgbarkeit:** Welche Anforderung wird durch welchen Test abgedeckt?
- **Wissensweitergabe:** Neue Teammitglieder verstehen, was getestet wurde und warum

---

## Die drei zentralen Testdokumente

### 1. Testplan (vor dem Testen)

Der Testplan beschreibt **was** und **wie** getestet wird, bevor ein einziger Test ausgeführt wird:

| Abschnitt | Inhalt |
|-----------|--------|
| Testziele | Was soll durch Tests nachgewiesen werden? |
| Testumfang | Was wird getestet – und was explizit nicht? |
| Testmethoden | Black-Box, White-Box, Äquivalenzklassen? |
| Ressourcen | Wer testet wann mit welchen Werkzeugen? |
| Abnahmekriterien | Ab wann gilt das System als freigabebereit? |

### 2. Testprotokoll (während des Testens)

Das Testprotokoll dokumentiert jeden einzelnen Testfall mit:
TC-ID · Titel · Vorbedingung · Testeingabe · Testschritte · Erwartetes Ergebnis · Tatsächliches Ergebnis · Status (Bestanden / Fehlgeschlagen / Blockiert)

### 3. Testbericht (nach dem Testen)

Der Testbericht fasst die Ergebnisse für den Auftraggeber zusammen:
- Anzahl Tests gesamt / bestanden / fehlgeschlagen
- Coverage-Statistik pro Modul
- Gefundene Fehler mit Schweregrad und Status
- Empfehlung: Ist das System abnahmebereit?

---

## Codebeispiele

### Beispiel 1: pytest mit automatischem HTML-Report

```bash
# Installation (einmalig):
pip install pytest-html

# HTML-Bericht erstellen:
pytest --html=testbericht.html --self-contained-html -v
```

```python
# conftest.py – Metadaten fuer den HTML-Bericht
def pytest_configure(config):
    config._metadata["Projekt"]  = "Lagerbestandsverwaltung v1.0"
    config._metadata["Tester"]   = "Anna Muster"
    config._metadata["Datum"]    = "2026-05-12"
    config._metadata["Umgebung"] = "Python 3.12, Windows 11"
```

Die Datei `testbericht.html` wird automatisch mit allen Testergebnissen, Laufzeiten und Fehlermeldungen befüllt und ist sofort für Auftraggeber lesbar.

### Beispiel 2: Einfaches Testprotokoll als CSV

```python
import csv
from datetime import date

def testprotokoll_erstellen(ergebnisse: list[dict], datei: str) -> None:
    """Schreibt Testergebnisse als CSV-Protokoll (oeffenbar in Excel)."""
    felder = ["TC_ID", "Titel", "Eingabe", "Erwartet", "Erhalten", "Status"]

    with open(datei, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=felder)
        writer.writeheader()
        writer.writerows(ergebnisse)

# Verwendung nach Testausfuehrung:
protokoll = [
    {"TC_ID": "TC-001", "Titel": "Login gueltig",
     "Eingabe": "admin/geheim123", "Erwartet": "True",
     "Erhalten": "True", "Status": "Bestanden"},
    {"TC_ID": "TC-002", "Titel": "Login ungueltig",
     "Eingabe": "admin/falsch",   "Erwartet": "False",
     "Erhalten": "False", "Status": "Bestanden"},
    {"TC_ID": "TC-003", "Titel": "Leeres Passwort",
     "Eingabe": "admin/",         "Erwartet": "False",
     "Erhalten": "True",  "Status": "Fehlgeschlagen"},
]

testprotokoll_erstellen(protokoll, f"protokoll_{date.today()}.csv")
```

Das CSV-Protokoll öffnet sich direkt in Excel und ist für Auftraggeber ohne Programmierkenntnisse lesbar.

---

## Weiterführende Links

| Ressource | Beschreibung |
|-----------|-------------|
| [ISTQB – Foundation Level Lehrplan](https://www.istqb.org/certifications/certified-tester-foundation-level) | Standard-Lehrplan mit Definitionen für Testplan, Testprotokoll und Testbericht |
| [pytest-html Dokumentation](https://pytest-html.readthedocs.io) | Offizielle Doku des pytest-html Plugins für automatisierte HTML-Berichte |
| [t2informatik – Testbericht](https://t2informatik.de/wissen-kompakt/testbericht/) | Kompakter deutschsprachiger Überblick über Aufbau und Zweck eines Testberichts |

---

## Du hast alle Bausteine abgeschlossen!

Du kennst jetzt die Grundlagen des Softwaretestens – von Begriffen und Grundprinzipien über Testmethoden, Äquivalenzklassen und automatisierte Tests mit `unittest` und `pytest`, Test-Driven Development bis zur professionellen Dokumentation.

**Erstelle jetzt dein persönliches Cheat-Sheet** mit den wichtigsten Befehlen, Begriffen und Konzepten aus allen 8 Bausteinen – als Nachschlagewerk für den Berufsalltag und die IHK-Prüfung.

Öffne anschließend deinen **abschließenden Pull Request** – das ist der offizielle Nachweis deiner Arbeit in diesem Kurs.

---

*Zurück zu den [Aufgaben](aufgaben.md) · Bei Problemen → [Stuck Protocol](../stuck_protocol.md)*
