import random


def random_numbers(count=5):
    """Повертає список випадкових чисел."""
    return [random.randint(1, 100) for _ in range(count)]