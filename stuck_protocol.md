# Stuck Protocol – Was tun, wenn ihr nicht weiterkommt?

> Dieses Protokoll gilt für alle Bausteine in LS 8.5.
> Arbeitet die Stufen **der Reihe nach** ab. Kein Überspringen.

---

## Warum dieses Protokoll?

Im Berufsalltag als Fachinformatiker werdet ihr regelmäßig auf Probleme stoßen, für die es keine direkte Antwort im Internet gibt. Die Fähigkeit, systematisch zu debuggen und Hilfe sinnvoll einzusetzen, ist genauso wichtig wie das Programmieren selbst.

---

## Die 5 Stufen

### Stufe 1 – Selbst debuggen (20 Minuten)

**Bevor ihr irgendwas anderes macht:**

- [ ] Fehlermeldung komplett lesen – nicht nur die letzte Zeile
- [ ] Code Zeile für Zeile durchgehen: Was erwartet ihr? Was passiert wirklich?
- [ ] `print()`-Ausgaben an kritischen Stellen einfügen
- [ ] Variablenwerte zur Laufzeit prüfen
- [ ] Den Code laut vorlesen (Rubber Duck Debugging)
- [ ] Tipp: Git-Diff anschauen – was habt ihr zuletzt geändert?

**Zeitlimit: 20 Minuten ernsthaftes Probieren**

---

### Stufe 2 – Dokumentation & Kursunterlagen (10 Minuten)

**Schaut nach in:**

- [ ] Der `aufgaben.md` des aktuellen Bausteins – habt ihr alle Hinweise gelesen?
- [ ] Python-Dokumentation: [docs.python.org](https://docs.python.org/3/)
- [ ] `unittest`-Dokumentation: [docs.python.org/3/library/unittest.html](https://docs.python.org/3/library/unittest.html)
- [ ] `pytest`-Dokumentation: [docs.pytest.org](https://docs.pytest.org/)
- [ ] Euren eigenen Code aus früheren Bausteinen

**Konkrete Suchbegriffe notieren, die ihr verwendet habt:**

> _______________________________________________

---

### Stufe 3 – Suche & Community (10 Minuten)

**Sucht gezielt:**

- [ ] Stack Overflow mit dem genauen Fehlermeldungstext suchen
- [ ] GitHub Issues des verwendeten Tools durchsuchen
- [ ] Real Python, W3Schools, GeeksForGeeks

**Suchstrategie:**
```
[Fehlermeldung] + "python" + [Modulname]
Beispiel: "AssertionError python unittest expected actual"
```

**Wichtig:** Gefundene Lösungen verstehen, nicht einfach kopieren!

**Was habt ihr gefunden?** (kurz notieren)

> _______________________________________________

---

### Stufe 4 – KI-Unterstützung (erlaubt ab hier)

**Erst nach Stufen 1–3 dürft ihr KI-Tools nutzen:**

- ChatGPT, GitHub Copilot, Claude oder andere

**So nutzt ihr KI sinnvoll:**

1. Beschreibt das Problem präzise (nicht: "Mein Code funktioniert nicht")
2. Fügt den relevanten Code-Ausschnitt ein
3. Fügt die Fehlermeldung vollständig ein
4. Fragt nach Erklärungen, nicht nur nach der Lösung
5. Versteht jeden Vorschlag, bevor ihr ihn übernehmt

**Gutes Prompt-Beispiel:**
```
Ich versuche einen Unit-Test für eine Python-Funktion zu schreiben.
Die Funktion soll Negativzahlen ablehnen und einen ValueError werfen.
Mein Test:

    def test_negative(self):
        self.assertRaises(ValueError, meine_funktion, -1)

Fehler: Der Test schlägt fehl, obwohl die Funktion einen ValueError wirft.
Was mache ich falsch?
```

**Im PR dokumentieren:** Wo habt ihr KI genutzt? Was hat sie vorgeschlagen?

---

### Stufe 5 – Lehrer fragen

**Jetzt dürft ihr zum Lehrer / zur Lehrerin:**

**Bringt mit:**
- [ ] Was habt ihr in Stufe 1 probiert?
- [ ] Welche Quellen habt ihr in Stufe 2 und 3 durchsucht?
- [ ] Was hat die KI in Stufe 4 vorgeschlagen?
- [ ] Euren aktuellen Code (kein leeres Dokument!)
- [ ] Die genaue Fehlermeldung

> Wer ohne diese Vorbereitung kommt, wird zurückgeschickt.
> Das ist kein Bösewillen – es ist Training für den Berufsalltag.

---

## Protokollvorlage (für euren PR-Kommentar)

Wenn ihr das Stuck Protocol genutzt habt, fügt folgendes in euren PR ein:

```
### Stuck Protocol Protokoll

**Stufe 1 – Selbst debuggen:**
Ich habe ... probiert. Das Ergebnis war ...

**Stufe 2 – Dokumentation:**
Ich habe nachgeschaut in ... Die Suche hat ergeben ...

**Stufe 3 – Suche:**
Suchbegriffe: ... / Gefunden: ...

**Stufe 4 – KI:**
Prompt war: ... / KI hat vorgeschlagen: ... / Ich habe übernommen: ...

**Gelöst durch:** ...
```

---

## Denkt daran

Das Stuck Protocol ist kein Bürokratismus. Es ist ein echtes Berufsmodell:

| Stufe | Entspricht im Beruf |
|-------|---------------------|
| 1 | Selbst debuggen, Logs lesen |
| 2 | Dokumentation des Produkts lesen |
| 3 | Stack Overflow, Community |
| 4 | Copilot, ChatGPT im Berufsalltag |
| 5 | Senior-Entwickler oder Team fragen |

Wer direkt zu Stufe 5 springt, wird im Betrieb als "junior" wahrgenommen.
Wer Stufen 1–4 professionell durchläuft, wächst schnell.
