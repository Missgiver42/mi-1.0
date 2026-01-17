"""
InputParser – MI 1.0
Zuständig für das Erfassen und Vorverarbeiten von Eingaben
"""

class InputParser:
    def __init__(self):
        pass

    def parse(self, raw_input: str) -> dict:
        """
        Nimmt rohe Eingabe entgegen und gibt eine strukturierte Form zurück
        """
        return {
            "original": raw_input,
            "cleaned": raw_input.strip(),
            "length": len(raw_input),
            "is_empty": len(raw_input.strip()) == 0
        }
