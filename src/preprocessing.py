def clean_text(text: str) -> str:
    """Limpieza básica pendiente de completar."""
    if text is None:
        return ""
    return " ".join(str(text).split())
