from rich.console import Console
from rich.table import Table


def print_table():
    """Виводить красиву таблицю."""
    table = Table(title="Студенти")
    table.add_column("Імʼя")
    table.add_column("Оцінка")
    table.add_row("Соня", "100")
    table.add_row("Іван", "95")
    Console().print(table)