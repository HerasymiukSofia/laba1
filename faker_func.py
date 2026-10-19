from faker import Faker


def fake_person():
    """Генерує фейкове імʼя та адресу."""
    fake = Faker("uk_UA")
    return fake.name(), fake.address()