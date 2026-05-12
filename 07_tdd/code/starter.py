"""
Baustein 07 – Test-Driven Development (TDD)
Startvorlage – bearbeite diese Datei für deine Aufgaben.

TDD-Regel: Kein Code ohne vorherigen Test!

Ausführen:
    pytest 07_tdd/code/starter.py -v
"""

import pytest
import string
import random


# ============================================================
# Aufgabe 1 – runden_auf_naechste_fuenf (TDD-Übung)
# ============================================================

# TODO: Schreibe zuerst die Tests, dann die Implementierung!

# def runden_auf_naechste_fuenf(zahl: int) -> int:
#     pass  # Erst Tests schreiben!


class TestRundenAufNaechsteFuenf:
    """Aufgabe 1 – Entwickle die Funktion Schritt für Schritt nach TDD."""

    def test_runden_3_ergibt_5(self):
        """Zyklus 1: Dieser Test muss zuerst ROT sein."""
        # TODO: Schreibe den Test – führe ihn aus – er wird rot sein
        # Dann: Implementiere runden_auf_naechste_fuenf minimal
        pass  # Entferne 'pass' und schreibe den eigentlichen Test

    def test_runden_7_ergibt_10(self):
        """Zyklus 2: TODO"""
        pass

    def test_runden_10_ergibt_10(self):
        """Zyklus 3: Bereits ein Vielfaches von 5."""
        pass

    def test_runden_0_ergibt_0(self):
        """Zyklus 4: Sonderfall 0."""
        pass

    def test_runden_negativ(self):
        """Zyklus 5: Was passiert mit negativen Zahlen? Definiere zuerst das Verhalten!"""
        pass


# ============================================================
# Aufgabe 2 – PasswortGenerator (TDD Praxisprojekt)
# ============================================================

# SCHRITT 1: Schreibe alle Tests BEVOR du die Klasse implementierst!
# Die Klasse ist absichtlich noch nicht implementiert.

class PasswortGenerator:
    """
    TODO: Implementiere diese Klasse NACH den Tests.

    Anforderungen:
    - generate(laenge, grossbuchstaben, ziffern, sonderzeichen) -> str
    - Standard: laenge=12, grossbuchstaben=True, ziffern=True, sonderzeichen=False
    - Mindestlänge: 8 Zeichen (sonst ValueError)
    - Gibt einen String der gewünschten Länge zurück
    """
    pass  # TODO: Erst alle Tests schreiben!


class TestPasswortGenerator:
    """Aufgabe 2 – TDD: Tests zuerst, dann Implementierung."""

    # User Story 1: Konfigurierbare Länge
    def test_passwort_hat_korrekte_laenge(self):
        """TODO: Schreibe vor der Implementierung!"""
        pass

    def test_passwort_standardlaenge_ist_12(self):
        """TODO"""
        pass

    # User Story 2: Großbuchstaben
    def test_passwort_mit_grossbuchstaben(self):
        """TODO: Mindestens ein Großbuchstabe vorhanden."""
        pass

    def test_passwort_ohne_grossbuchstaben(self):
        """TODO: Kein Großbuchstabe vorhanden wenn deaktiviert."""
        pass

    # User Story 3: Ziffern
    def test_passwort_mit_ziffern(self):
        """TODO"""
        pass

    def test_passwort_ohne_ziffern(self):
        """TODO"""
        pass

    # User Story 4: Sonderzeichen
    def test_passwort_mit_sonderzeichen(self):
        """TODO"""
        pass

    # User Story 5: Mindestlänge
    def test_mindestlaenge_wird_erzwungen(self):
        """TODO: laenge=7 soll ValueError werfen."""
        pass

    def test_laenge_8_ist_erlaubt(self):
        """TODO: Grenzwert – muss funktionieren."""
        pass

    # User Story 6: Fehlermeldungen
    def test_laenge_null_wirft_fehler(self):
        """TODO"""
        pass

    def test_alle_zeichentypen_deaktiviert_wirft_fehler(self):
        """TODO: Was soll passieren, wenn keine Zeichen erlaubt sind?"""
        pass


# ============================================================
# Aufgabe 3 – Refactoring unter Tests
# ============================================================

# Diese Funktion ist funktionierend, aber schlecht strukturiert.
# Refactore sie – die Tests sollen danach noch grün sein!

def verarbeite_bestellung(bestellung: dict) -> dict:
    """
    Verarbeitet eine Bestellung und gibt ein Ergebnis-Dict zurück.
    (Schlecht strukturiert – refactoring notwendig!)
    """
    if not bestellung:
        raise ValueError("Bestellung darf nicht leer sein")

    if "artikel" not in bestellung:
        raise ValueError("Bestellung muss 'artikel' enthalten")

    if not bestellung["artikel"]:
        raise ValueError("Artikelliste darf nicht leer sein")

    gesamtpreis = 0
    for artikel in bestellung["artikel"]:
        if "preis" not in artikel:
            raise ValueError(f"Artikel '{artikel.get('name', '?')}' hat keinen Preis")
        if "menge" not in artikel:
            raise ValueError(f"Artikel '{artikel.get('name', '?')}' hat keine Menge")
        if artikel["preis"] < 0:
            raise ValueError("Preis darf nicht negativ sein")
        if artikel["menge"] <= 0:
            raise ValueError("Menge muss positiv sein")
        gesamtpreis += artikel["preis"] * artikel["menge"]

    rabatt = bestellung.get("rabatt_prozent", 0)
    if not 0 <= rabatt <= 100:
        raise ValueError(f"Rabatt muss zwischen 0 und 100 liegen, war: {rabatt}")

    endpreis = gesamtpreis * (1 - rabatt / 100)

    return {
        "gesamtpreis_brutto": round(gesamtpreis, 2),
        "rabatt_prozent": rabatt,
        "endpreis": round(endpreis, 2),
        "anzahl_artikel": len(bestellung["artikel"]),
    }


class TestVerarbeiteBestellung:
    """Diese Tests sollen nach dem Refactoring noch alle grün sein."""

    def test_normale_bestellung(self):
        bestellung = {
            "artikel": [
                {"name": "USB-Stick", "preis": 9.99, "menge": 2},
                {"name": "Maus", "preis": 19.99, "menge": 1},
            ]
        }
        ergebnis = verarbeite_bestellung(bestellung)
        assert ergebnis["gesamtpreis_brutto"] == 39.97
        assert ergebnis["endpreis"] == 39.97
        assert ergebnis["anzahl_artikel"] == 2

    def test_bestellung_mit_rabatt(self):
        bestellung = {
            "artikel": [{"name": "Monitor", "preis": 300.00, "menge": 1}],
            "rabatt_prozent": 10,
        }
        ergebnis = verarbeite_bestellung(bestellung)
        assert ergebnis["endpreis"] == 270.00

    def test_leere_bestellung_wirft_fehler(self):
        with pytest.raises(ValueError):
            verarbeite_bestellung({})

    def test_negativer_preis_wirft_fehler(self):
        with pytest.raises(ValueError, match="negativ"):
            verarbeite_bestellung({
                "artikel": [{"name": "Fehler", "preis": -5.00, "menge": 1}]
            })

    def test_ungültiger_rabatt_wirft_fehler(self):
        with pytest.raises(ValueError, match="Rabatt"):
            verarbeite_bestellung({
                "artikel": [{"name": "Artikel", "preis": 10.00, "menge": 1}],
                "rabatt_prozent": 150,
            })


# ============================================================
# Aufgabe 4 – IHK: berechne_zinsen (TDD)
# ============================================================

# TODO: Schreibe ZUERST die Testklasse TestBerechneZinsen,
#       DANN die Funktion berechne_zinsen!

# def berechne_zinsen(kapital: float, zinssatz: float, jahre: int) -> float:
#     """Einfache Zinsberechnung: Kapital * (1 + Zinssatz/100) ^ Jahre"""
#     pass


class TestBerechneZinsen:
    """TODO: Schreibe mindestens 4 Tests BEVOR du berechne_zinsen implementierst."""

    def test_placeholder(self):
        """Entferne diesen Platzhalter und schreibe echte Tests."""
        pass
