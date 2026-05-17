# Baustein 07 – Theorie: Test-Driven Development (TDD)

> **Lesezeit:** ca. 20–25 Minuten  
> Lies diesen Text vollständig durch, bevor du mit den Aufgaben beginnst.

---

## Was ist TDD?

**Test-Driven Development (TDD)** dreht die normale Reihenfolge um: Du schreibst **zuerst den Test**, dann erst den Produktionscode. Der amerikanische Entwickler Kent Beck hat TDD als Teil von Extreme Programming (XP) geprägt und in seinem Buch „Test-Driven Development: By Example" beschrieben.

**Goldene TDD-Regel:** Kein Produktionscode ohne vorher einen fehlschlagenden Test.

---

## Der Red-Green-Refactor-Zyklus

TDD läuft in drei streng getrennten Phasen ab:

![TDD Zyklus](../assets/07_tdd_zyklus.png)

**Baby Steps:** Immer nur einen Test auf einmal. Kein „ich implementiere schon mal alles durch". Die kleinen Schritte erzwingen Nachdenken über die Schnittstelle, bevor der Code geschrieben wird.

---

## Warum TDD?

**Vorteile:**
- Du denkst über die Schnittstelle nach, **bevor** du implementierst
- Jeder neue Code ist sofort durch Tests abgesichert
- Regressionstests entstehen automatisch während des Entwickelns
- Führt zu einfacherem, besser strukturiertem Code – schwer testbarer Code zwingt zur Verbesserung

**Typische Widerstände in der Praxis:**
- „Wir haben keine Zeit für TDD" → Fehlersuche kostet später deutlich mehr Zeit
- „Tests bremsen mich aus" → Anfangs ja, nach einer Woche geht es schneller
- „Der Code ist zu komplex für Tests" → Das ist oft ein Zeichen schlechter Struktur

---

## Verbindung zu SOLID-Prinzipien (aus LS 8.2 OOP)

TDD fördert von Natur aus das **Single Responsibility Principle (SRP)**: Wenn du keinen einfachen Test für eine Funktion schreiben kannst, hat sie wahrscheinlich zu viele Verantwortlichkeiten. TDD macht schlechtes Design sofort spürbar.

---

## Codebeispiel: TDD Schritt für Schritt

**Aufgabe:** Implementiere `celsius_zu_fahrenheit(celsius)` nach dem TDD-Zyklus.

### 🔴 Schritt 1 – RED: Erster Test (Funktion existiert noch nicht)

```python
# test_temperatur.py
def test_celsius_null_ergibt_zweiunddreissig():
    assert celsius_zu_fahrenheit(0) == 32
# Ausfuehren: pytest → FEHLER (NameError: nicht definiert)
```

### 🟢 Schritt 2 – GREEN: Minimaler Code

```python
# temperatur.py
def celsius_zu_fahrenheit(celsius):
    return 32   # Einfachstmoegliche Loesung – nur um diesen Test gruenzumachen
# Ausfuehren: pytest → GRUEN
```

### 🔴 Schritt 3 – RED: Zweiter Test

```python
def test_celsius_hundert_ergibt_zweihundertzwoelf():
    assert celsius_zu_fahrenheit(100) == 212
# Ausfuehren: pytest → FEHLER (ergibt 32, nicht 212)
```

### 🟢 Schritt 4 – GREEN: Echte Formel implementieren

```python
def celsius_zu_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32
# Ausfuehren: pytest → beide Tests GRUEN
```

### 🔵 Schritt 5 – REFACTOR: Benennung und Typ-Annotation sind bereits gut

Weitere Tests für Grenzwerte (-273.15 Absolutnullpunkt, negative Werte) anschließen → Zyklus wiederholen.

---

## Weiterführende Links

| Ressource | Beschreibung |
|-----------|-------------|
| [martinfowler.com – TDD](https://martinfowler.com/bliki/TestDrivenDevelopment.html) | Martin Fowlers Erklärung von TDD mit Hintergrund und Einschätzung (englisch) |
| [Kent Beck – Tidy First](https://tidyfirst.substack.com) | Kent Becks aktueller Blog zu Software-Design und TDD (englisch) |
| [t2informatik – TDD](https://t2informatik.de/wissen-kompakt/test-driven-development/) | Kompakte deutschsprachige Einführung mit Zyklus-Erklärung |

---

### 🎮 Lernkarten & Wiederholung
- <a href="https://quizlet.com/user/A__J_35/folders/ls-85-softwaretests?i=20ii9u&x=1xqt" target="_blank" rel="noopener noreferrer">
📦 Alle Lernkarten LS 8.5 – Quizlet Ordner</a>
- <a href="https://quizlet.com/de/1179994835/07-test-driven-development-flash-cards/?i=20ii9u&x=1jqt" target="_blank" rel="noopener noreferrer">
🃏 Quizlet – Baustein 07: TDD</a>

> Nutze die Lernkarten zur Wiederholung nach dem Baustein –
> ideal für Spaced Repetition und IHK-Vorbereitung!

---

## Was kommt als nächstes?

In **Baustein 08 – Testdokumentation** lernst du, wie du deine Tests und deren Ergebnisse professionell dokumentierst. Testplan, Testprotokoll und Testbericht – das sind die Dokumente, die du im Berufsalltag und in der IHK-Prüfung benötigst.

---

*[➡️ Weiter zu aufgaben.md](aufgaben.md) · Bei Problemen → [Stuck Protocol](../stuck_protocol.md)*
