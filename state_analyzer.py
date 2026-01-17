"""
StateAnalyzer – MI 1.0
Analysiert den Zustand der Eingabe und leitet Basismerkmale ab
"""

class StateAnalyzer:
    def __init__(self):
        pass

    def analyze(self, parsed_input: dict) -> dict:
        """
        Analysiert strukturierte Eingaben und erzeugt einen Zustandsvektor
        """
        length = parsed_input.get("length", 0)
        is_empty = parsed_input.get("is_empty", True)

        state = {
            "has_content": not is_empty,
            "complexity": self._estimate_complexity(length),
            "emotional_load": "neutral",  # Platzhalter für spätere Erweiterung
        }

        return state

    def _estimate_complexity(self, length: int) -> str:
        if length == 0:
            return "none"
        elif length < 20:
            return "low"
        elif length < 100:
            return "medium"
        else:
            return "high"
