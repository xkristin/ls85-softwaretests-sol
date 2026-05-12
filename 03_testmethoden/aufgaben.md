# Baustein 03 – Testmethoden 🟡

> **Schwierigkeit:** 🟡 Anwendung  
> **Zeitrahmen:** ca. 120 Minuten  
> [Nicht weitergekommen? → Stuck Protocol](../stuck_protocol.md)

---

## Selbsteinschätzung – Vorher

- [ ] 🟢 Ich kenne Black-Box und White-Box-Tests
- [ ] 🟡 Ich habe von diesen Begriffen gehört, bin aber unsicher
- [ ] 🔴 Diese Methoden sind mir unbekannt

---

## Lernziele

Nach diesem Baustein kannst du …

- 🟢 … Black-Box-Tests von White-Box-Tests unterscheiden
- 🟡 … Testfälle nach der Black-Box-Methode ohne Codekenntnis ableiten
- 🟡 … Anweisungsüberdeckung (Statement Coverage) und Zweigüberdeckung (Branch Coverage) erklären
- 🟡 … einen einfachen Kontrollflussgraphen aus Code erstellen
- 🔴 … begründen, welche Testmethode für welches Testziel am besten geeignet ist

---

## Hintergrund

Bei **Black-Box-Tests** (funktionaler Test) kennst du den Quellcode nicht – du testest nur über
Ein- und Ausgaben. Das entspricht der Perspektive des Kunden oder des Testers ohne Codekenntnis.

Bei **White-Box-Tests** (struktureller Test) kennst du den Quellcode und prüfst gezielt,
ob bestimmte Codeabschnitte durchlaufen werden. Ziel ist eine möglichst hohe **Testabdeckung** (Coverage).

**Grey-Box**: Kombination beider Ansätze – du kennst die Architektur, aber nicht alle Details.

---

## Aufgabe 1 – Black-Box-Test: Benutzerauthentifizierung 🟡

In `code/starter.py` ist eine Funktion `authentifiziere_benutzer()` implementiert.
Du darfst den Implementierungstext **nicht** lesen (falte ihn mental weg) –
arbeite nur mit der Schnittstellenbeschreibung:

**Spezifikation:**
- Eingabe: `benutzername` (str), `passwort` (str)
- Ausgabe: `True` wenn gültig, `False` wenn ungültig
- Regeln:
  - Benutzername: 3–20 Zeichen, keine Sonderzeichen außer `_`
  - Passwort: mindestens 8 Zeichen
  - Bekannte gültige Zugangsdaten: `admin` / `geheim123`

**a)** Erstelle eine Testtabelle mit mindestens 6 Black-Box-Testfällen:

| TC-Nr | Eingabe (User/PW) | Erwartete Ausgabe | Kategorie |
|-------|-------------------|------------------|-----------|
| TC01 | admin / geheim123 | True | Gültiger Login |
| TC02 | | | |
| TC03 | | | |
| ... | | | |

**b)** Führe deine Testfälle aus, indem du die Funktion in `starter.py` aufrufst.
Welche Testfälle schlagen fehl? Dokumentiere die Ergebnisse.

---

## Aufgabe 2 – White-Box-Test: Coverage 🟡

In `code/starter.py` findest du die Funktion `kategorisiere_bestellung()`.

**a)** Zeichne den **Kontrollflussgraphen** dieser Funktion auf Papier (oder als ASCII-Art in `03_antworten.md`).
Nummeriere alle Knoten (Anweisungen) und alle Kanten (Bedingungszweige).

**b)** **Anweisungsüberdeckung (Statement Coverage):**
Wie viele Testfälle brauchst du mindestens, um jede Anweisung einmal auszuführen?
Erstelle diese Testfälle.

**c)** **Zweigüberdeckung (Branch Coverage):**
Wie viele Testfälle brauchst du, um jeden Zweig (jedes if/else) mindestens einmal zu durchlaufen?
Warum sind das mehr als bei Statement Coverage?

---

## Aufgabe 3 – Methoden vergleichen 🟡

Fülle die Tabelle aus:

| Merkmal | Black-Box | White-Box |
|---------|-----------|-----------|
| Codekenntnis notwendig? | | |
| Aus wessen Perspektive? | | |
| Was wird geprüft? | | |
| Typische Werkzeuge | | |
| Vorteil | | |
| Nachteil | | |

---

## Aufgabe 4 – IHK-Stil 🔴

**Prüfungsszenario:**

Ein Entwickler hat folgende Python-Funktion geschrieben:

```python
def versandkosten(gewicht_kg: float, express: bool) -> float:
    if gewicht_kg <= 0:
        raise ValueError("Gewicht muss positiv sein")
    if express:
        if gewicht_kg <= 5:
            return 8.90
        else:
            return 14.90
    else:
        if gewicht_kg <= 5:
            return 3.90
        else:
            return 6.90
```

**(a)** Erstellen Sie einen Kontrollflussgraphen für diese Funktion. Benennen Sie alle Knoten und Kanten. *(4 Punkte)*

**(b)** Wie viele Testfälle sind für eine vollständige **Zweigüberdeckung** erforderlich? Listen Sie diese auf. *(4 Punkte)*

**(c)** Welche Testfälle würden Sie zusätzlich aus **Black-Box-Sicht** (Grenzwertanalyse) ergänzen? *(2 Punkte)*

---

## Tandem-Aufgabe 👥

**Code Review mit Testbrille:**

Person A: Schreibt eine kurze Python-Funktion (10–15 Zeilen, mindestens 2 if-Zweige)
Person B: Kennt den Code **nicht** (Black-Box) und erstellt Testfälle nur aus der Beschreibung

Dann tauscht ihr:
Person B liest den Code und prüft mit White-Box-Methode, welche Testfälle fehlen.

Diskutiert: Was hat die Black-Box-Perspektive übersehen? Was hat die White-Box-Analyse ergänzt?

---

## Active Recall 🧠

*Unterlagen zu – beantworte aus dem Gedächtnis:*

1. Was ist der fundamentale Unterschied zwischen Black-Box und White-Box?
2. Was bedeutet 100 % Statement Coverage? Garantiert das fehlerfreie Software?
3. Warum ist Branch Coverage strenger als Statement Coverage?
4. In welcher Teststufe (aus Baustein 02) wird meistens White-Box-Testing eingesetzt?

---

## Reflexion 🚦

- [ ] 🟢 Ich kann beide Methoden anwenden und den Unterschied erklären
- [ ] 🟡 Ich verstehe die Theorie, brauche aber mehr Übung
- [ ] 🔴 Ich brauche Unterstützung bei Coverage-Konzepten

**Was nimmst du mit?**

> _______________________________________________

---

*Bei Problemen → [Stuck Protocol](../stuck_protocol.md)*
