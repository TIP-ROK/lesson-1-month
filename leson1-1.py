login = input("Введите ваш логин: ")
password = input("Введите ваш пароль: ")

if login.lower() == "Tip" and len(password) < 9 and "$" in password:
    print("Вы вошли в систему!!!")
    name = input()
    age = input()
    email = input()
    print(name, age, email)
else:
    if login.lower() != "Tip":
        print("Логин введён не правильно!")
    if not len(password) < 9 and "$" in password:
        print("Пароль не подходит")
