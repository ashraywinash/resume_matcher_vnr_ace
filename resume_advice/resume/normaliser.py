import re

def normalize_resume(text: str) -> str:
    text = re.sub(r"\r", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[•●▪]", "-", text)
    return text.strip()
