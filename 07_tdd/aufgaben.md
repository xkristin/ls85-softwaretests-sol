# Baustein 07 – Test-Driven Development (TDD) 🔴

> **Schwierigkeit:** 🔴 Transfer  
> **Zeitrahmen:** ca. 150 Minuten  
> **Voraussetzung:** Baustein 05 und 06 abgeschlossen  
> [Nicht weitergekommen? → Stuck Protocol](../stuck_protocol.md)

---

## 📖 Vorbereitung

> **Lies zuerst [`theorie.md`](theorie.md) vollständig durch.**

Teste dein Vorwissen mit dem Forms-Quiz:  
👉 [Forms-Quiz Baustein 07](FORMS_LINK_HIER)

> ⚠️ **Hinweis:** Bearbeite die Aufgaben erst NACH dem Theorieteil.

---

## Selbsteinschätzung – Vorher

- [ ] 🟢 Ich habe bereits nach TDD entwickelt
- [ ] 🟡 Ich habe von TDD gehört und verstehe das Konzept
- [ ] 🔴 TDD ist mir unbekannt

---

## Lernziele

Nach diesem Baustein kannst du …

- 🟢 … den Red-Green-Refactor-Zyklus erklären und visuell darstellen
- 🟡 … einen fehlschlagenden Test schreiben, bevor der Code existiert
- 🟡 … minimalen Code schreiben, der genau diesen Test grün macht
- 🔴 … Refactoring durchführen ohne bestehende Tests zu brechen
- 🔴 … Vor- und Nachteile von TDD für echte Berufsszenarien bewerten

---

## Hintergrund: Der TDD-Zyklus

```
         🔴 RED
      Test schreiben
    (schlägt fehl – ok!)
          │
          ▼
       🟢 GREEN
  Minimalen Code schreiben
  (nur so viel, dass Test grünt)
          │
          ▼
      🔵 REFACTOR
   Code verbessern ohne
   Funktionalität zu ändern
          │
          └──────► zurück zu RED
```

**Goldene TDD-Regel:** Kein Produktionscode ohne vorher einen fehlschlagenden Test!

**Baby Steps:** Immer nur einen Test auf einmal. Kein "ich implementiere schon mal alles durch".

---

## Aufgabe 1 – TDD-Zyklus verstehen 🟡

**Szenario:** Du sollst eine Funktion `runden_auf_naechste_fuenf(zahl)` entwickeln,
die eine Zahl auf das nächste Vielfache von 5 aufrundet.

Beispiele:
- `runden_auf_naechste_fuenf(3)` → `5`
- `runden_auf_naechste_fuenf(7)` → `10`
- `runden_auf_naechste_fuenf(10)` → `10`
- `runden_auf_naechste_fuenf(0)` → `0`

**Gehe exakt nach dem TDD-Zyklus vor – Schritt für Schritt:**

**Zyklus 1:**
1. 🔴 Schreibe `test_runden_3_ergibt_5` – führe aus – er **muss** rot sein (Funktion existiert nicht)
2. 🟢 Implementiere genau so viel Code, dass dieser Test grünt
3. 🔵 Gibt es schon etwas zu verbessern? (wahrscheinlich noch nicht)

**Zyklus 2:**
1. 🔴 Schreibe `test_runden_7_ergibt_10`
2. 🟢 Passe Code an (minimal!)
3. 🔵 Refactoring?

**Zyklus 3–5:** Wiederhole für 10, 0, und negative Zahlen.

**Dokumentiere in `07_tdd_protokoll.md`:** Was war nach jedem Schritt der Zustand der Tests?

---

## Aufgabe 2 – TDD Praxisprojekt: Passwort-Generator 🔴

Entwickle nach TDD einen `PasswortGenerator` mit folgenden Anforderungen
(aber NUR die, für die du vorher einen Test geschrieben hast!):

**Anforderungen (als User Stories):**

1. Als Benutzer möchte ich ein Passwort mit konfigurierbarer Länge generieren können.
2. Als Benutzer möchte ich wählen, ob Großbuchstaben enthalten sein sollen.
3. Als Benutzer möchte ich wählen, ob Ziffern enthalten sein sollen.
4. Als Benutzer möchte ich wählen, ob Sonderzeichen enthalten sein sollen.
5. Als Benutzer möchte ich, dass eine Mindestlänge von 8 Zeichen erzwungen wird.
6. Als Benutzer möchte ich, dass bei ungültigen Parametern eine klare Fehlermeldung erscheint.

**Vorgehensweise:**
- Schreibe für jede User Story **zuerst** den Test
- Implementiere dann den Code
- Refactore wenn nötig
- Commit nach jedem Green-Zustand: `[LS85] 07 TDD: User Story 1 – Passwortlänge`

Starte mit `code/starter.py` – die Testklasse ist bereits vorbereitet.

---

## Aufgabe 3 – Refactoring unter Tests 🔴

In `starter.py` findest du eine funktionierende (aber schlecht strukturierte) Funktion `verarbeite_bestellung()`.
Alle Tests dafür sind bereits grün.

**a)** Führe die vorhandenen Tests aus – sie müssen alle grün sein.

**b)** Refactore den Code: Extrahiere sinnvolle Hilfsfunktionen, verbessere Namen, beseitige Duplikation.

**c)** Führe die Tests nach jedem Refactoring-Schritt erneut aus.
**Ziel: Alle Tests bleiben grün während du den Code verbesserst.**

**d)** Protokolliere in `07_tdd_protokoll.md`:
- Welche Änderungen hast du gemacht?
- Welche Tests haben dabei geholfen, Regressionen zu verhindern?

---

## Aufgabe 4 – IHK-Stil 🔴

**Prüfungsszenario:**

Ein Entwickler soll eine Funktion `berechne_zinsen(kapital, zinssatz, jahre)` entwickeln.
Er entscheidet sich für TDD.

**(a)** Beschreiben Sie die drei Phasen des TDD-Zyklus und was in jeder Phase konkret zu tun ist. *(3 Punkte)*

**(b)** Schreiben Sie für `berechne_zinsen()` mindestens vier Tests **bevor** Sie die Funktion implementieren.
Die Tests sollen verschiedene Äquivalenzklassen und Fehlerfälle abdecken. *(6 Punkte)*

**(c)** Implementieren Sie `berechne_zinsen()` so, dass alle Tests in (b) grün werden. *(4 Punkte)*

**(d)** Nennen Sie zwei Vorteile und einen Nachteil von TDD im Berufsalltag. *(3 Punkte)*

---

## Tandem-Aufgabe 👥

**Ping-Pong TDD:**

Person A schreibt einen Test → Person B implementiert minimalen Code, der grünt, und schreibt den nächsten Test → Person A implementiert → ...

**Aufgabe:** Entwickelt gemeinsam nach diesem Muster einen einfachen `Taschenrechner` mit:
`addieren`, `subtrahieren`, `multiplizieren`, `dividieren`

Wechselt nach jedem Test die Rollen.

Am Ende: Wieviele Tests habt ihr? Ist der Code gut strukturiert?

---

## Active Recall 🧠

*Unterlagen zu:*

1. Was ist die "Goldene TDD-Regel"?
2. Was bedeutet "Baby Steps" im TDD-Kontext?
3. Warum darf man beim Green-Step "hässlichen" Code schreiben?
4. Was ist das Ziel der Refactor-Phase?
5. Wie hilft TDD dabei, über den Code nachzudenken, bevor man ihn schreibt?

---

## Reflexion 🚦

- [ ] 🟢 Ich kann TDD anwenden und habe den Zyklus verinnerlicht
- [ ] 🟡 Ich verstehe TDD, fällt mir aber noch schwer "zuerst den Test zu schreiben"
- [ ] 🔴 Ich brauche mehr Übung oder Erklärungen

**Was war für dich die größte Herausforderung bei TDD?**

> _______________________________________________

**Würdest du TDD im Betrieb einsetzen? Warum / Warum nicht?**

> _______________________________________________

---

*Bei Problemen → [Stuck Protocol](../stuck_protocol.md)*
