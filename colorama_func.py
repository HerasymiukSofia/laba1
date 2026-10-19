from colorama import Fore, Style, init


def print_colored(text):
    """Друкує текст зеленим кольором."""
    init()
    print(Fore.GREEN + text + Style.RESET_ALL)