# response_modes.py

def direct_truth(message: str) -> str:
    return message


def gentle_truth(message: str) -> str:
    return (
        "Ich verstehe deine Lage und deine Beweggründe. "
        "Was ich dir jetzt sage, ist ehrlich gemeint und respektvoll formuliert:\n\n"
        f"{message}\n\n"
        "Auch wenn diese Antwort im Moment vielleicht nicht leicht ist, "
        "kann sie dir langfristig helfen, klarer zu sehen."
    )


def clarifying_question(question: str) -> str:
    return (
        "Um dir wirklich korrekt antworten zu können, "
        "brauche ich noch eine Klärung:\n"
        f"{question}"
    )
