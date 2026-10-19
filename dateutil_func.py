from dateutil import parser
from dateutil.relativedelta import relativedelta


def date_plus_months(date_str="2026-10-19", months=3):
    """Додає місяці до дати."""
    date = parser.parse(date_str)
    return (date + relativedelta(months=months)).date()