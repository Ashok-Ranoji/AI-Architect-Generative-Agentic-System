def sanitize_input(text: str):
    blocked = ["ignore previous instructions", "system prompt"]
    for b in blocked:
        if b in text.lower():
            raise ValueError("Prompt injection detected")
    return text