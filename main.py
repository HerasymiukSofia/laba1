from colorama_func import print_colored
from dateutil_func import date_plus_months
from datetime_func import current_time
from emoji_func import get_emoji
from faker_func import fake_person
from json_func import to_json
from math_func import circle_area
from numpy_func import array_stats
from os_func import list_files
from pandas_func import make_dataframe
from pyfiglet_func import print_banner
from random_func import random_numbers
from requests_func import get_status
from rich_func import print_table
from tqdm_func import progress_demo


def main():
    """Запускає всі функції по черзі."""
    print_banner("Lab 4")
    print_colored("Старт програми")
    print("requests:", get_status())
    print("numpy:", array_stats())
    frame, mean_age = make_dataframe()
    print(frame)
    print("pandas, середній вік:", mean_age)
    print_table()
    print(get_emoji())
    progress_demo()
    print("faker:", fake_person())
    print("dateutil:", date_plus_months())
    print("random:", random_numbers())
    print("math:", round(circle_area(), 2))
    print("datetime:", current_time())
    print(to_json())
    print("os:", list_files())


if __name__ == "__main__":
    main()