users = {
    "sofia": {
        "password": "1234",
        "grades": [12, 10, 8, 5, 11, 3]
    },
    "anna": {
        "password": "qwerty",
        "grades": [9, 7, 12, 10, 4]
    },
    "max": {
        "password": "1111",
        "grades": [5, 6, 8, 3, 2, 10]
    },
    "dima": {
        "password": "pass123",
        "grades": [12, 11, 9, 6, 4, 1]
    },
    "misha67": {
        "password": "metal",
        "grades": [12, 12, 12, 12, 4, 5]
    }
}

login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login in users and users[login]["password"] == password:
    print("\nВхід виконано успішно!")

    grades = users[login]["grades"]

    print("Ваші оцінки:", grades)

    satisfactory = 0
    unsatisfactory = 0

    for grade in grades:
        if 5 <= grade <= 12:
            satisfactory += 1
        elif 1 <= grade <= 4:
            unsatisfactory += 1

    print("Кількість задовільних оцінок (5-12):", satisfactory)
    print("Кількість незадовільних оцінок (1-4):", unsatisfactory)

else:
    print("\nНеправильний логін або пароль!")