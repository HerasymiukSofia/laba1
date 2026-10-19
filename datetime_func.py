from datetime import datetime


def current_time():
    """Поточний час у форматі рядка."""
    return datetime.now().strftime("%d.%m.%Y %H:%M:%S")