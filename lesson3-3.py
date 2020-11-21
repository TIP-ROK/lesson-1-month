def int_input():
    while True:
        try:
            return int(input("Введите ваш возраст "))
        except Exception:
            print("Введите ваш возраст ввиде числа ")



while True:
    name = input("Введите ваше имя ")
    surname = input("Введите вашу фамилию ")
    age = int_input()
    if age < 18:
        print("Нужен родительский контроль!")
        return f"{name},{surname}, {age}

person = input_initial_data()
print(person)