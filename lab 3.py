# товари магазину
products = [
    {"name": "Ноутбук", "price": 25000.00, "quantity": 5},
    {"name": "Мишка", "price": 750.50, "quantity": 10},
    {"name": "Клавіатура", "price": 1200.00, "quantity": 8},
    {"name": "Навушники", "price": 1800.75, "quantity": 6}
]

# кошик покупця
cart = []

# дані адміністратора
ADMIN_LOGIN = "sofia67"
ADMIN_PASSWORD = "6767"

# формат ціни
price_format = lambda x: f"{x:.2f} грн"


# показати каталог
def show_catalog():
    print("\n--- Каталог ---")

    for i, product in enumerate(products, 1):
        print(
            f"{i}. {product['name']} - "
            f"{price_format(product['price'])} - "
            f"{product['quantity']} шт."
        )


# показати кошик
def show_cart():
    print("\n--- Кошик ---")

    if not cart:
        print("Кошик порожній")
        return

    total = 0

    for i, item in enumerate(cart, 1):
        cost = item["price"] * item["quantity"]
        total += cost

        print(
            f"{i}. {item['name']} - "
            f"{item['quantity']} шт. - "
            f"{price_format(cost)}"
        )

    print(f"Разом: {price_format(total)}")


# додати товар
def add_to_cart():
    show_catalog()

    try:
        number = int(input("Номер товару: "))
        amount = int(input("Кількість: "))

        if number < 1 or number > len(products):
            print("Такого товару немає")
            return

        product = products[number - 1]

        if amount <= 0:
            print("Неправильна кількість")
            return

        item = next(
            (x for x in cart if x["name"] == product["name"]),
            None
        )

        in_cart = item["quantity"] if item else 0

        if in_cart + amount > product["quantity"]:
            print("Недостатньо товару на складі")
            return

        if item:
            item["quantity"] += amount
        else:
            cart.append({
                "name": product["name"],
                "price": product["price"],
                "quantity": amount
            })

        print("Товар додано")

    except ValueError:
        print("Введіть число")


# видалити товар
def remove_from_cart():
    show_cart()

    if not cart:
        return

    try:
        number = int(input("Номер товару для видалення: "))

        if 1 <= number <= len(cart):
            cart.pop(number - 1)
            print("Товар видалено")
        else:
            print("Неправильний номер")

    except ValueError:
        print("Введіть число")


# купити товари
def buy():
    if not cart:
        print("Кошик порожній")
        return

    show_cart()

    answer = input("Купити? (так/ні): ").lower()

    if answer == "так":
        for item in cart:
            for product in products:
                if product["name"] == item["name"]:
                    product["quantity"] -= item["quantity"]

        cart.clear()
        print("Покупку здійснено")

    else:
        print("Покупку скасовано")


# вхід адміністратора
def admin():
    login = input("Логін: ")
    password = input("Пароль: ")

    if login == ADMIN_LOGIN and password == ADMIN_PASSWORD:
        print("\n--- Залишки товарів ---")

        for product in sorted(
            products,
            key=lambda x: x["name"]
        ):
            print(
                f"{product['name']} - "
                f"{product['quantity']} шт."
            )

    else:
        print("Неправильний логін або пароль")


# головне меню
def main():
    while True:
        print("\n--- Магазин ---")
        print("1. Каталог")
        print("2. Додати в кошик")
        print("3. Переглянути кошик")
        print("4. Видалити з кошика")
        print("5. Купити")
        print("6. Адміністратор")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            show_catalog()

        elif choice == "2":
            add_to_cart()

        elif choice == "3":
            show_cart()

        elif choice == "4":
            remove_from_cart()

        elif choice == "5":
            buy()

        elif choice == "6":
            admin()

        elif choice == "0":
            print("До побачення!")
            break

        else:
            print("Такого пункту немає")


if __name__ == "__main__":
    main()