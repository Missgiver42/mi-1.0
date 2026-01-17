"""
SafetyEngine – MI 1.0
Verantwortlich für Sicherheits- und Ethikregeln
"""

class SafetyEngine:
    def __init__(self):
        pass

    def check(self, state: dict) -> dict:
        """
        Prüft, ob eine Antwort erlaubt, eingeschränkt oder blockiert ist
        """
        decision = {
            "allowed": True,
            "reason": "OK"
        }

        if state.get("state") == "EMPTY":
            decision["allowed"] = False
            decision["reason"] = "Leere Eingabe"

        return decision
