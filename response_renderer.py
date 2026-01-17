"""
ResponseRenderer – MI 1.0
Erzeugt die finale Ausgabe für den Nutzer
"""

class ResponseRenderer:
    def __init__(self):
        pass

    def render(self, plan: dict) -> str:
        """
        Wandelt den Antwortplan in eine Textausgabe um
        """
        response_type = plan.get("type", "unknown")
        message = plan.get("message", "")

        if response_type == "blocked":
            return f"[BLOCKIERT] {message}"

        elif response_type == "prompt":
            return message

        elif response_type == "clarify":
            return message

        elif response_type == "normal":
            return message

        else:
            return "Unbekannter Antworttyp."
