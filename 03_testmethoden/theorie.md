# Baustein 03 – Theorie: Testmethoden

> **Lesezeit:** ca. 20–25 Minuten  
> Lies diesen Text vollständig durch, bevor du mit den Aufgaben beginnst.

---

## Überblick: Wie entwirft man Testfälle?

In **Baustein 02** hast du gelernt, *wann* welche Teststufe eingesetzt wird. In diesem Baustein geht es darum, *wie* man Testfälle gezielt entwirft. Die zentrale Frage: Wie viel weißt du über den Code, den du testest?

---

## Black-Box-Test (Funktionaler Test)

Beim **Black-Box-Test** kennst du den Quellcode **nicht** – du testest ausschließlich über Eingaben und Ausgaben. Das System ist eine „schwarze Box": Du siehst nur, was hineingeht und was herauskommt.

**Perspektive:** Kunde, Endanwender, externer Tester  
**Vorteil:** Unabhängig vom Code – findet fehlende oder falsch umgesetzte Anforderungen  
**Nachteil:** Interne Logikfehler im Code können unentdeckt bleiben

**Typische Techniken:** Äquivalenzklassenbildung, Grenzwertanalyse (→ Baustein 04)

---

## White-Box-Test (Struktureller Test)

Beim **White-Box-Test** kennst du den Quellcode vollständig. Du entwirfst Testfälle so, dass bestimmte Codestrukturen – Anweisungen, Zweige, Pfade – durchlaufen werden. Ziel ist eine möglichst hohe **Testabdeckung (Coverage)**.

**Perspektive:** Entwickler, der den eigenen Code kennt  
**Vorteil:** Findet innere Logikfehler, die extern nicht sichtbar sind  
**Nachteil:** Fehlende Anforderungen werden nicht aufgedeckt

**Kenngrößen:**
- **Anweisungsüberdeckung (Statement Coverage):** Jede Zeile wurde mindestens einmal ausgeführt
- **Zweigüberdeckung (Branch Coverage):** Jedes if/else-Ergebnis wurde mindestens einmal getestet

---

## Grey-Box-Test

Der **Grey-Box-Test** kombiniert beide Ansätze: Du kennst die Architektur und Datenstrukturen, aber nicht die vollständige Implementierung. In der Praxis ist das der häufigste Fall – vor allem bei Integrationstests.

---

## Vergleich auf einen Blick

| Merkmal | Black-Box | White-Box |
|---------|-----------|-----------|
| Codekenntnis notwendig? | Nein | Ja |
| Perspektive | Benutzer/Kunde | Entwickler |
| Findet fehlende Anforderungen? | Ja | Nein |
| Misst Testabdeckung? | Nein | Ja |
| Typische Teststufe | System-/Abnahmetest | Unit-/Integrationstest |

---

## Codebeispiele

### Beispiel 1: Black-Box-Test – nur Spezifikation bekannt

```python
# Spezifikation: pruefe_alter(alter) -> True wenn 18 oder aelter, sonst False
# Wir kennen den Code NICHT – wir testen nur ueber Ein-/Ausgabe

def test_blackbox_volljährig():
    assert pruefe_alter(18) is True    # Grenzwert: genau 18

def test_blackbox_minderjährig():
    assert pruefe_alter(17) is False   # Grenzwert: knapp darunter

def test_blackbox_kind():
    assert pruefe_alter(5) is False    # Repräsentativer Wert der Klasse

def test_blackbox_senior():
    assert pruefe_alter(65) is True    # Repräsentativer Wert der Klasse
```

### Beispiel 2: White-Box-Test – Code ist bekannt

```python
# Jetzt kennen wir die Implementierung:
def pruefe_alter(alter: int) -> bool:
    if alter < 0:           # Zweig A: Fehlerfall
        raise ValueError("Alter kann nicht negativ sein")
    return alter >= 18      # Zweig B: Rückgabe True oder False

# White-Box: alle Zweige abdecken (Branch Coverage)
import pytest

def test_whitebox_zweig_negativ():
    with pytest.raises(ValueError):
        pruefe_alter(-1)    # Zweig A: ValueError-Pfad

def test_whitebox_zweig_volljährig():
    assert pruefe_alter(25) is True    # Zweig B: True-Pfad

def test_whitebox_zweig_minderjährig():
    assert pruefe_alter(10) is False   # Zweig B: False-Pfad
```

Der Black-Box-Ansatz hätte den Negativwert-Zweig möglicherweise übersehen – der White-Box-Test findet ihn gezielt durch Kenntnis der Codestruktur.

---

## Weiterführende Links

| Ressource | Beschreibung |
|-----------|-------------|
| [ISTQB Glossar](https://glossary.istqb.org) | Offizielle Begriffsdefinitionen für Testmethoden und Coverage (englisch/deutsch) |
| [Software Testing Help – Black Box](https://www.softwaretestinghelp.com/black-box-testing/) | Praxisnahe englischsprachige Erklärung mit Beispielen und Techniken |
| [t2informatik – White-Box-Test](https://t2informatik.de/wissen-kompakt/white-box-test/) | Kompakte deutschsprachige Erläuterung mit Kontrollflussgraph-Beispiel |

---

## Was kommt als nächstes?

In **Baustein 04 – Äquivalenzklassen & Grenzwertanalyse** vertiefst du die Black-Box-Methode. Du lernst, wie man aus unendlich vielen möglichen Eingaben systematisch eine kleine, aber aussagekräftige Menge an Testfällen ableitet – eine der wichtigsten Techniken für die IHK-Prüfung.

---

*Zurück zu den [Aufgaben](aufgaben.md) · Bei Problemen → [Stuck Protocol](../stuck_protocol.md)*
