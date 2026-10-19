import time

from tqdm import tqdm


def progress_demo(count=10):
    """Показує прогрес-бар."""
    for _ in tqdm(range(count), desc="Обробка"):
        time.sleep(0.1)