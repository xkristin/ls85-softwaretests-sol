"""
Baustein 06 – pytest
Startvorlage – bearbeite diese Datei für deine Aufgaben.

Installation:
    pip install pytest

Ausführen:
    pytest 06_pytest/code/starter.py -v
    pytest 06_pytest/code/ -v --tb=short
"""

import pytest


# ============================================================
# Zu testende Klassen / Funktionen
# ============================================================

class Kontorechner:
    """Aus Baustein 05 – für pytest-Migration (Aufgabe 1)."""

    def __init__(self):
        self._kontostand = 0.0

    @property
    def kontostand(self) -> float:
        return self._kontostand

    def einzahlen(self, betrag: float) -> None:
        if betrag <= 0:
            raise ValueError(f"Einzahlung muss positiv sein, war: {betrag}")
        self._kontostand += betrag

    def abheben(self, betrag: float) -> None:
        if betrag <= 0:
            raise ValueError(f"Abhebungsbetrag muss positiv sein, war: {betrag}")
        if betrag > self._kontostand:
            raise ValueError(
                f"Unzureichendes Guthaben: {self._kontostand:.2f} < {betrag:.2f}"
            )
        self._kontostand -= betrag


class BenutzerkontoService:
    """Verwaltung von Benutzerkonten (vereinfacht)."""

    def __init__(self):
        self._benutzer = {}

    def benutzer_anlegen(self, name: str, passwort: str) -> None:
        if name in self._benutzer:
            raise ValueError(f"Benutzer '{name}' existiert bereits.")
        if len(passwort) < 8:
            raise ValueError("Passwort zu kurz (mind. 8 Zeichen).")
        self._benutzer[name] = passwort

    def anmelden(self, name: str, passwort: str) -> bool:
        return self._benutzer.get(name) == passwort

    def benutzer_loeschen(self, name: str) -> None:
        if name not in self._benutzer:
            raise ValueError(f"Benutzer '{name}' nicht gefunden.")
        del self._benutzer[name]

    def benutzeranzahl(self) -> int:
        return len(self._benutzer)


def berechne_note(punkte: int) -> int:
    """Notenberechnung aus Baustein 04."""
    if not isinstance(punkte, int) or punkte < 0 or punkte > 100:
        raise ValueError(f"Punkte müssen zwischen 0 und 100 liegen, war: {punkte}")
    if punkte >= 92:
        return 1
    elif punkte >= 81:
        return 2
    elif punkte >= 67:
        return 3
    elif punkte >= 50:
        return 4
    elif punkte >= 30:
        return 5
    else:
        return 6


def validiere_menge(menge) -> bool:
    """Aus Baustein 04."""
    if not isinstance(menge, int):
        return False
    return 1 <= menge <= 999


def berechne_versandkosten(gewicht_kg: float, express: bool = False) -> float:
    """
    Aufgabe 5 – TODO: Implementiere diese Funktion.

    Preistabelle:
        Standard ≤ 5 kg:   3.90
        Standard > 5 kg:   6.90
        Express  ≤ 5 kg:   8.90
        Express  > 5 kg:  14.90

    Raises:
        ValueError: Wenn gewicht_kg <= 0.
        TypeError:  Wenn gewicht_kg kein float/int ist.
    """
    # TODO: Deine Implementierung
    pass


# ============================================================
# Aufgabe 1 – Von unittest zu pytest migrieren
# ============================================================

def test_einzahlen_positiver_betrag():
    """TODO: Migriere aus Baustein 05."""
    pass  # TODO


def test_abheben_kein_guthaben():
    """TODO: Migriere aus Baustein 05, nutze pytest.raises."""
    pass  # TODO


# ============================================================
# Aufgabe 2 – Fixtures
# ============================================================

@pytest.fixture
def kontoservice():
    """TODO: Fixture für BenutzerkontoService."""
    # TODO: Service anlegen, Testbenutzer hinzufügen, Service zurückgeben
    pass


# TODO: Mindestens 4 Testfunktionen, die das Fixture nutzen

def test_anmelden_gueltig(kontoservice):
    """TODO"""
    pass


def test_anmelden_falsches_passwort(kontoservice):
    """TODO"""
    pass


def test_benutzer_doppelt_anlegen_wirft_fehler(kontoservice):
    """TODO"""
    pass


def test_benutzeranzahl_nach_loeschen(kontoservice):
    """TODO"""
    pass


# ============================================================
# Aufgabe 3 – Parametrisierung: berechne_note
# ============================================================

@pytest.mark.parametrize("punkte, erwartete_note", [
    # TODO: Füge alle Grenzwerte und je 2 Vertreter pro Klasse ein
    # Format: (Punktzahl, erwartete Note)
    (100, 1),   # Beispiel – ergänze mindestens 13 weitere
])
def test_berechne_note(punkte, erwartete_note):
    """TODO: Parametrisierter Test für berechne_note."""
    assert berechne_note(punkte) == erwartete_note


# ============================================================
# Aufgabe 3b – Parametrisierung: validiere_menge
# ============================================================

@pytest.mark.parametrize("menge, erwartet", [
    # TODO: Gültige Klassen, ungültige Klassen, alle Grenzwerte
    (1, True),    # Beispiel – ergänze weitere
    (0, False),   # Grenzwert
])
def test_validiere_menge(menge, erwartet):
    """TODO: Parametrisierter Test für validiere_menge."""
    assert validiere_menge(menge) == erwartet


# ============================================================
# Aufgabe 4 – pytest.raises mit match
# ============================================================

def test_einzahlung_null_fehlermeldung():
    """TODO: Nutze pytest.raises mit match-Parameter."""
    konto = Kontorechner()
    with pytest.raises(ValueError, match="positiv"):
        konto.einzahlen(0)


# TODO: Zwei weitere Tests mit pytest.raises und match


# ============================================================
# Aufgabe 5 – IHK: berechne_versandkosten
# ============================================================

@pytest.mark.parametrize("gewicht, express, erwartet", [
    # TODO: Alle vier gültigen Kombinationen
])
def test_berechne_versandkosten_gueltig(gewicht, express, erwartet):
    """TODO: Implementiere nach Fertigstellung von berechne_versandkosten."""
    pass


def test_versandkosten_negatives_gewicht():
    """TODO: Teste, dass negatives Gewicht ValueError wirft."""
    pass


def test_versandkosten_falscher_typ():
    """TODO: Teste, dass falscher Typ TypeError wirft."""
    pass
