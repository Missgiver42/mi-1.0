"""
ResponsePlanner – MI 1.0
Plant die Art der Antwort basierend auf Analyse und Safety
"""

class ResponsePlanner:
    def __init__(self):
        pass

    def plan(self, state: dict, safety: dict) -> dict:
        """
        Entscheidet, wie die MI antworten soll
        """
        if not safety.get("allowed", True):
            return {
                "type": "blocked",
                "message": f"Keine Antwort erlaubt: {safety.get('reason')}"
            }

        state_type = state.get("state", "UNKNOWN")

        if state_type == "EMPTY":
            return {
                "type": "prompt",
                "message": "Bitte gib eine Eingabe ein."
            }

        elif state_type in ("VERY_SHORT", "SHORT"):
            return {
                "type": "clarify",
                "message": "Kannst du das bitte etwas genauer erklären?"
            }

        else:
            return {
                "type": "normal",
                "message": "Eingabe verstanden. Verarbeitung läuft."
            }
