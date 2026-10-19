import pandas as pd


def make_dataframe():
    """Створює DataFrame та рахує середній вік."""
    data = {"name": ["Оля", "Іван", "Макс"], "age": [20, 22, 21]}
    frame = pd.DataFrame(data)
    return frame, frame["age"].mean()