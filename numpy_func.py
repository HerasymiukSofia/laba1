import numpy as np


def array_stats():
    """Створює масив і повертає його середнє та суму."""
    arr = np.arange(1, 11)
    return float(arr.mean()), int(arr.sum())