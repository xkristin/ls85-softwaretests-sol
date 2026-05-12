"""
Baustein 01 – Grundlagen der Softwaretests
Startvorlage – bearbeite diese Datei für deine Aufgaben.
"""


# ============================================================
# Aufgabe 1 – Fehlerhafte Funktion
# ============================================================

def berechne_rabatt(preis: float, prozent: float) -> float:
    """
    Berechnet den Preis nach Rabattabzug.

    Beispiel:
        berechne_rabatt(100.0, 20) soll 80.0 zurückgeben.
    """
    # Hier ist ein Defekt eingebaut – findest du ihn?
    rabatt = preis * prozent  # <-- Zeile mit Defekt
    return preis - rabatt


# Aufgabe 1a): Beantworte folgende Fragen als Kommentar:

# Error (falsche Handlung des Entwicklers):
# TODO: Deine Antwort hier

# Defect (fehlerhafte Stelle im Code):
# TODO: Deine Antwort hier

# Failure (was der Benutzer bemerken würde):
# TODO: Deine Antwort hier


# Aufgabe 1b): Korrigiere die Funktion unten und füge print()-Tests hinzu.

def berechne_rabatt_korrigiert(preis: float, prozent: float) -> float:
    """
    Korrigierte Version von berechne_rabatt().
    TODO: Implementiere die korrekte Logik.
    """
    pass  # TODO: Ersetze 'pass' durch deine Implementierung


# Manuelle Tests (werden in Baustein 05 durch echte Unit-Tests ersetzt)
if __name__ == "__main__":
    # TODO: Ergänze print()-Ausgaben, um deine korrigierte Funktion zu testen
    # Erwartete Ergebnisse:
    #   berechne_rabatt_korrigiert(100.0, 20) -> 80.0
    #   berechne_rabatt_korrigiert(200.0, 10) -> 180.0
    #   berechne_rabatt_korrigiert(50.0, 0)   -> 50.0

    print("=== Test: berechne_rabatt (fehlerhaft) ===")
    print(berechne_rabatt(100.0, 20))  # Falsche Ausgabe erwartet

    print("\n=== Test: berechne_rabatt_korrigiert ===")
    # TODO: Deine Tests hier


# ============================================================
# Aufgabe 2 – Statisch vs. dynamisch
# ============================================================

# Trage hier deine ausgefüllte Tabelle als Kommentar ein:
#
# | Maßnahme                            | Statisch | Dynamisch |
# |-------------------------------------|----------|-----------|
# | Code Review durch einen Kollegen    | TODO     | TODO      |
# | Programm mit Testdaten ausführen    | TODO     | TODO      |
# | Syntaxprüfung durch den Editor      | TODO     | TODO      |
# | Walkthroughs im Team                | TODO     | TODO      |
# | Unit-Tests laufen lassen            | TODO     | TODO      |
# | Checklisten für Codestruktur        | TODO     | TODO      |
#
# Warum reicht statisches Testen allein nicht aus?
# TODO: Deine Erklärung hier (2 Sätze)


# ============================================================
# Aufgabe 3 – Grundprinzipien (Antworten als Kommentar)
# ============================================================

# Prinzip 2 – Vollständiges Testen ist unmöglich:
# Beispiel aus dem Berufsalltag:
# TODO: Deine Antwort hier

# Prinzip 4 – Defect Clustering:
# Beispiel aus dem Berufsalltag:
# TODO: Deine Antwort hier

# Welches Prinzip überrascht dich? Warum?
# TODO: Deine Antwort hier
