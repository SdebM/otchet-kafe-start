def format_kopeks(kopeks: int) -> str:  # noqa: D100, D103
    return f"{kopeks / 100:,.2f} ₽".replace(",", " ").replace(".", ",")


def format_title(text: str, width: int = 40) -> str:  # noqa: D103
    return text.center(width, "=")
