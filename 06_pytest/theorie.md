# Baustein 06 – Theorie: pytest

> **Lesezeit:** ca. 20–25 Minuten  
> Lies diesen Text vollständig durch, bevor du mit den Aufgaben beginnst.

---

## pytest vs. unittest

In **Baustein 05** hast du mit `unittest` gearbeitet – Pythons eingebautem Testframework. `pytest` ist nicht eingebaut, aber der **de-facto Standard im Berufsalltag**, weil es deutlich weniger Schreibarbeit erfordert und bessere Fehlermeldungen liefert.

| Merkmal | unittest | pytest |
|---------|----------|--------|
| Installation | eingebaut | `pip install pytest` |
| Teststruktur | Klassen (Pflicht) | Funktionen reichen aus |
| Assertion | `self.assertEqual(a, b)` | `assert a == b` |
| Fehlermeldungen | kurz | detailliert (zeigt Variablenwerte) |
| Testvorbereitung | `setUp / tearDown` | `@pytest.fixture` |
| Parametrisierung | komplex | `@pytest.mark.parametrize` |

---

## Einfache Testfunktionen ohne Klasse

Mit pytest braucht es keine Klasse – eine Funktion, die mit `test_` beginnt, reicht:

```bash
# Installation (einmalig):
pip install pytest

# Alle Tests im Verzeichnis ausfuehren:
pytest -v

# Tests nach Name filtern:
pytest -v -k "rechner"

# Kurze Fehlermeldungen:
pytest --tb=short
```

---

## Fixtures: Wiederverwendbare Testvorbereitung

Fixtures ersetzen `setUp()` und `tearDown()`. Sie werden mit `@pytest.fixture` dekoriert und in Testfunktionen als Parameter übergeben – pytest injiziert sie automatisch:

```python
@pytest.fixture
def taschenrechner():
    """Gibt einen frischen Taschenrechner fuer jeden Test zurueck."""
    return Taschenrechner()

def test_addieren(taschenrechner):
    assert taschenrechner.addieren(3, 5) == 8

def test_dividieren(taschenrechner):
    assert taschenrechner.dividieren(10, 2) == 5.0
```

Mit `scope="module"` wird das Fixture nur einmal pro Datei erstellt – sinnvoll bei aufwändiger Datenbankverbindung oder Testdaten-Setup.

---

## Parametrisierte Tests

Statt viele fast identische Testfunktionen zu schreiben, nutze `@pytest.mark.parametrize`. Aus einer Funktion entstehen so beliebig viele unabhängige Tests:

```python
@pytest.mark.parametrize("punkte, note", [
    (100, 1), (92, 1),
    (91, 2),  (81, 2),
    (80, 3),  (67, 3),
])
def test_berechne_note(punkte, note):
    assert berechne_note(punkte) == note
```

pytest benennt die Tests automatisch: `test_berechne_note[100-1]`, `test_berechne_note[92-1]` usw.

---

## Codebeispiele

### Beispiel 1: Taschenrechner-Tests mit pytest (vgl. Baustein 05)

```python
import pytest
from taschenrechner import Taschenrechner

@pytest.fixture
def rechner():
    return Taschenrechner()

def test_addieren_positive_zahlen(rechner):
    assert rechner.addieren(3, 5) == 8

def test_addieren_negative_zahlen(rechner):
    assert rechner.addieren(-2, -3) == -5

def test_dividieren_normaler_fall(rechner):
    # pytest.approx() ersetzt assertAlmostEqual fuer Fliesskommazahlen:
    assert rechner.dividieren(10, 2) == pytest.approx(5.0)

def test_dividieren_durch_null(rechner):
    with pytest.raises(ValueError, match="Null"):
        rechner.dividieren(10, 0)
```

### Beispiel 2: Parametrisierter Test für Grenzwerte aus Baustein 04

```python
@pytest.mark.parametrize("betrag, soll_fehler", [
    (0,    True),   # Grenzwert – ungueltig (unter Minimum)
    (1,    False),  # Grenzwert – gueltig (Minimum)
    (500,  False),  # Repraesentativer Wert
    (999,  False),  # Grenzwert – gueltig (Maximum)
    (1000, True),   # Grenzwert – ungueltig (ueber Maximum)
    (-1,   True),   # Ungueltige Klasse
])
def test_validiere_betrag(betrag, soll_fehler):
    if soll_fehler:
        with pytest.raises(ValueError):
            validiere_betrag(betrag)
    else:
        assert validiere_betrag(betrag) == betrag
```

Sechs Fälle aus Baustein 04 in einer einzigen parametrisierten Funktion – kein Code-Duplikat.

---

## Weiterführende Links

| Ressource | Beschreibung |
|-----------|-------------|
| [pytest Dokumentation](https://docs.pytest.org) | Vollständige offizielle Doku mit Fixtures, Plugins und Konfiguration |
| [Real Python – pytest Tutorial](https://realpython.com/pytest-python-testing/) | Ausführliches englischsprachiges Tutorial mit Fixtures und Parametrisierung |
| [t2informatik – pytest](https://t2informatik.de/wissen-kompakt/pytest/) | Kompakte deutschsprachige Einführung in pytest |

---

## Was kommt als nächstes?

In **Baustein 07 – Test-Driven Development** drehst du den Ablauf um: Du schreibst **zuerst den Test**, dann erst den Code. Der Red-Green-Refactor-Zyklus wird dir zeigen, wie TDD die Codequalität verbessert und gleichzeitig als Entwurfswerkzeug dient.

---

*Zurück zu den [Aufgaben](aufgaben.md) · Bei Problemen → [Stuck Protocol](../stuck_protocol.md)*
