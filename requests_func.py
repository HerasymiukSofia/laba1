import requests


def get_status(url="https://httpbin.org/get"):
    """Повертає HTTP-статус запиту."""
    try:
        return requests.get(url, timeout=5).status_code
    except requests.RequestException as error:
        return f"Помилка: {error}"