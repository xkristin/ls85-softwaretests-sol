# Baustein 01 – Grundlagen der Softwaretests 🟢

> **Schwierigkeit:** 🟢 Grundlagen  
> **Zeitrahmen:** ca. 90 Minuten  
> [Nicht weitergekommen? → Stuck Protocol](../stuck_protocol.md)

---

## Selbsteinschätzung – Vorher

*Bevor du anfängst: Wie sicher fühlst du dich bei diesem Thema?*

- [ ] 🟢 Ich kenne mich schon aus
- [ ] 🟡 Ich habe eine vage Vorstellung
- [ ] 🔴 Das Thema ist mir komplett neu

---

## Lernziele

Nach diesem Baustein kannst du …

- 🟢 … erklären, warum Softwaretests notwendig sind
- 🟢 … die Begriffe **Fehler (Error)**, **Defekt (Defect/Bug)** und **Versagen (Failure)** unterscheiden
- 🟢 … statische und dynamische Testverfahren voneinander abgrenzen
- 🟢 … mindestens vier der sieben Grundprinzipien des Testens benennen
- 🟢 … erklären, warum vollständiges Testen in der Praxis unmöglich ist

---

## Hintergrund

Software ohne Tests ist wie ein Produkt ohne Qualitätskontrolle.
Der Ariane-5-Absturz 1996, der Therac-25-Strahlenunfall und der Y2K-Bug sind reale Beispiele,
bei denen fehlende oder unzureichende Tests zu katastrophalen Folgen führten.

Im Berufsalltag als Fachinformatiker wirst du täglich mit Code konfrontiert,
den du oder andere geschrieben haben – und der Fehler enthalten kann.
Systematisches Testen ist der professionelle Umgang damit.

---

## Aufgabe 1 – Begriffe klären 🟢

In der Datei `code/starter.py` findest du eine Funktion `berechne_rabatt()`.
Der Code hat bewusst einen Fehler eingebaut.

**a)** Lies den Code und identifiziere:
- Wo liegt der **Fehler (Error)** – also die falsche Handlung des Entwicklers?
- Was ist der **Defekt (Defect/Bug)** – die Stelle im Code, die das Problem verursacht?
- Was wäre das **Versagen (Failure)** – was würde der Benutzer bemerken?

Schreibe deine Antworten als Kommentare in `starter.py`.

**b)** Korrigiere den Fehler und füge einen `print()`-Test hinzu, der zeigt, dass die Funktion jetzt korrekt arbeitet.

---

## Aufgabe 2 – Statisch vs. dynamisch 🟢

**a)** Ordne die folgenden Maßnahmen den Kategorien zu:

| Maßnahme | Statisch | Dynamisch |
|----------|----------|-----------|
| Code Review durch einen Kollegen | | |
| Programm mit Testdaten ausführen | | |
| Syntaxprüfung durch den Editor | | |
| Walkthroughs im Team | | |
| Unit-Tests laufen lassen | | |
| Checklisten für Codestruktur | | |

Trage die Tabelle (als Markdown) in einen Kommentarblock in `starter.py` ein oder erstelle eine Datei `01_antworten.md`.

**b)** Erkläre in zwei Sätzen: Warum reicht statisches Testen allein nicht aus?

---

## Aufgabe 3 – Die sieben Grundprinzipien 🟢

Die ISTQB-Norm beschreibt sieben Grundprinzipien des Testens:

1. Testen zeigt die Anwesenheit von Fehlern, nicht deren Abwesenheit
2. Vollständiges Testen ist nicht möglich
3. Frühzeitiges Testen spart Zeit und Geld
4. Fehler häufen sich (Defect Clustering)
5. Beware of the Pesticide Paradox (immer gleiche Tests finden irgendwann nichts mehr)
6. Testen ist kontextabhängig
7. Irrtum: "Keine Fehler" = "Gutes System"

**a)** Erkläre Prinzip 2 und Prinzip 4 mit je einem konkreten Beispiel aus dem Berufsalltag.

**b)** Welches Prinzip überrascht dich am meisten? Begründe kurz.

---

## Aufgabe 4 – IHK-Stil 🟡

> Diese Aufgabe entspricht dem Format der IHK-Abschlussprüfung (Prüfungsteil 1).

**Prüfungsszenario:**

Eine Softwarefirma entwickelt eine Webanwendung für Lagerverwaltung.
Der Teamleiter sagt: "Wir haben keine Zeit für Tests – wir liefern direkt ans Produktivsystem."

**(a)** Nennen Sie zwei konkrete Risiken, die durch das Weglassen von Tests entstehen. *(2 Punkte)*

**(b)** Unterscheiden Sie die Begriffe „Defekt" und „Versagen" anhand eines Beispiels aus dem Lagerverwaltungssystem. *(4 Punkte)*

**(c)** Erläutern Sie, warum frühzeitiges Testen (Grundprinzip 3) wirtschaftlich sinnvoll ist. Nutzen Sie das Schlagwort „Rule of Ten". *(4 Punkte)*

Schreibe deine Antworten in `01_antworten.md`.

---

## Tandem-Aufgabe 👥

**Erkläre deinem Lernpartner:**

> "Stell dir vor, du bist frisch im Betrieb und musst einem Azubi aus einem anderen Beruf erklären, was der Unterschied zwischen einem Bug und einem Fehler ist. Du hast nur 2 Minuten und ein konkretes Beispiel aus dem Alltag."

- Partner A erklärt (2 Minuten)
- Partner B hört zu und stellt eine Rückfrage
- Partner B erklärt zurück mit anderen Worten
- Zusammen: Welche Formulierung war klarer? Warum?

Haltet das Ergebnis in `01_antworten.md` fest (3–5 Sätze).

---

## Active Recall – Brain Dump 🧠

*Schließe alle Unterlagen. Schreibe 5 Minuten lang alles auf, was du zu folgenden Fragen weißt:*

1. Was ist der Unterschied zwischen Error, Defect und Failure?
2. Warum können wir nie sicher sein, dass Software fehlerfrei ist?
3. Nenne 3 reale Beispiele, wo fehlende Softwaretests zu Problemen geführt haben.

*(Öffne erst danach die Unterlagen und vergleiche)*

---

## Reflexion 🚦

*Nach dem Bearbeiten: Wie schätzt du dich jetzt ein?*

- [ ] 🟢 Ich verstehe alle Konzepte und kann sie erklären
- [ ] 🟡 Ich verstehe die meisten Konzepte, habe aber noch Fragen
- [ ] 🔴 Ich brauche noch mehr Zeit oder Unterstützung

**Was nehme ich aus diesem Baustein mit?**

> _______________________________________________

---

*Bei Problemen → [Stuck Protocol](../stuck_protocol.md) · Lösungen im Branch `loesungen` (erst nach eigenem Versuch!)*
