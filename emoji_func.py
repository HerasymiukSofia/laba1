import emoji


def get_emoji(text=":thumbs_up: Готово :snake:"):
    """Замінює коди на емодзі."""
    return emoji.emojize(text)