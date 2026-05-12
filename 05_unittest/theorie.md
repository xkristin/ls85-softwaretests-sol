# Baustein 05 – Theorie: Python unittest

> **Lesezeit:** ca. 20–25 Minuten  
> Lies diesen Text vollständig durch, bevor du mit den Aufgaben beginnst.

---

## Was ist unittest?

`unittest` ist Pythons **eingebautes Testframework** – keine Installation notwendig. Es folgt dem **xUnit-Muster**, das ursprünglich aus Java (JUnit) stammt und in fast allen Programmiersprachen existiert (NUnit in C#, PHPUnit in PHP usw.).

```bash
# Tests einer Datei ausfuehren:
python -m unittest 05_unittest/code/starter.py -v

# Alle Tests im Projekt automatisch finden und ausfuehren:
python -m unittest discover -v
```

Das `-v` (verbose) zeigt jeden Testnamen einzeln – hilfreich beim Debuggen.

---

## Aufbau einer Testklasse

Jede Testklasse erbt von `unittest.TestCase`. Alle Methoden, die mit `test_` beginnen, werden automatisch als Tests erkannt und ausgeführt.

```
┌───────────────────────────────────────────┐
│  class TestMeineKlasse(unittest.TestCase) │
│                                           │
│    def setUp(self):    ← vor jedem Test   │
│    def tearDown(self): ← nach jedem Test  │
│                                           │
│    def test_fall_1(self):  ← Test 1       │
│    def test_fall_2(self):  ← Test 2       │
└───────────────────────────────────────────┘
```

---

## setUp() und tearDown()

`setUp()` wird **vor jeder einzelnen Testmethode** aufgerufen – ideal, um Testobjekte frisch anzulegen.  
`tearDown()` wird **nach jeder Testmethode** aufgerufen – z. B. um temporäre Dateien zu löschen.

**Wichtig:** Jeder Test bekommt eine eigene, saubere Instanz – Tests beeinflussen sich dadurch nicht gegenseitig.

---

## Die wichtigsten Assertions

| Assertion | Was wird geprüft |
|-----------|-----------------|
| `assertEqual(a, b)` | a == b |
| `assertNotEqual(a, b)` | a != b |
| `assertTrue(x)` | x ist True |
| `assertFalse(x)` | x ist False |
| `assertIn(a, b)` | a ist in b enthalten |
| `assertRaises(Error, func, args)` | func(args) wirft Error |
| `assertAlmostEqual(a, b)` | a ≈ b (für Fließkommazahlen!) |

**Achtung Fließkommazahlen:** `0.1 + 0.2 != 0.3` in Python wegen Darstellungsungenauigkeiten. Verwende deshalb `assertAlmostEqual` statt `assertEqual` bei float-Werten.

---

## Codebeispiel: Vollständige Testklasse für einen Taschenrechner

### Die zu testende Klasse

```python
class Taschenrechner:
    def addieren(self, a: float, b: float) -> float:
        return a + b

    def dividieren(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division durch Null nicht erlaubt")
        return a / b
```

### Die zugehörige Testklasse

```python
import unittest

class TestTaschenrechner(unittest.TestCase):

    def setUp(self):
        """Wird vor jedem einzelnen Test aufgerufen."""
        self.rechner = Taschenrechner()

    def test_addieren_positive_zahlen(self):
        ergebnis = self.rechner.addieren(3, 5)
        self.assertEqual(ergebnis, 8)

    def test_addieren_negative_zahlen(self):
        ergebnis = self.rechner.addieren(-2, -3)
        self.assertEqual(ergebnis, -5)

    def test_dividieren_normaler_fall(self):
        ergebnis = self.rechner.dividieren(10, 2)
        self.assertAlmostEqual(ergebnis, 5.0)  # Fliesskomma: assertAlmostEqual!

    def test_dividieren_durch_null_wirft_fehler(self):
        with self.assertRaises(ValueError):
            self.rechner.dividieren(10, 0)

    def test_dividieren_ergebnis_mit_nachkommastellen(self):
        ergebnis = self.rechner.dividieren(1, 3)
        self.assertAlmostEqual(ergebnis, 0.333, places=3)


if __name__ == "__main__":
    unittest.main()
```

**Ausgabe bei `python -m unittest -v`:**

```
test_addieren_negative_zahlen ... ok
test_addieren_positive_zahlen ... ok
test_dividieren_durch_null_wirft_fehler ... ok
test_dividieren_ergebnis_mit_nachkommastellen ... ok
test_dividieren_normaler_fall ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

**Bedeutung der Symbole:** `.` = bestanden · `F` = fehlgeschlagen (Assertion falsch) · `E` = Fehler (unerwartete Exception im Testcode selbst)

---

## Weiterführende Links

| Ressource | Beschreibung |
|-----------|-------------|
| [Python Docs – unittest](https://docs.python.org/3/library/unittest.html) | Vollständige offizielle Dokumentation mit allen Assertions und Klassen |
| [Real Python – unittest Tutorial](https://realpython.com/python-unittest/) | Praxisnahes englischsprachiges Tutorial mit schrittweisen Beispielen |
| [t2informatik – Unit-Test](https://t2informatik.de/wissen-kompakt/unit-test/) | Kompakter deutschsprachiger Überblick über Unit-Tests im Allgemeinen |

---

## Was kommt als nächstes?

In **Baustein 06 – pytest** wirst du dasselbe erreichen – aber einfacher und mächtiger. pytest ist der Standard im Berufsalltag: weniger Schreibarbeit, bessere Fehlermeldungen und ein flexibles Fixture-System. Du wirst deine unittest-Tests direkt nach pytest migrieren.

---

*Zurück zu den [Aufgaben](aufgaben.md) · Bei Problemen → [Stuck Protocol](../stuck_protocol.md)*
