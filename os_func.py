import os


def list_files(path="."):
    """Повертає список файлів у папці."""
    return os.listdir(path)