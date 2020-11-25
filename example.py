def write_to_file(line):
    new_file = open("text1", "a")
    new_file.write(f"{line}\n")
    new_file.close()

def read_frome_file():
    file = open("text1", "r")
    lines = file.readlines()
    file.close()
    return lines

while True:
    print("1) Войти")
    print("2) Зарегистрироваться")
    print("3) Забыл пароль или логин")
    print("4) Выход")
    option = int(input("Введите вариант: "))

    if option == 1:
        login = input("Введите логин: ")

        def getPassword():
            password = input("Введите пароль: ")
            return password


        def validPassword(password):
            if len(password) >= 8:
                valid = True
            if password.alnum():
                valid = True
            if password.isdigit < 2:
                valid = True
            else:
                return False

        def main():
            password = validPassword()
            if validPassword(password):
                print(password, "Пароль верный")
            else:
                print(password, "Неверный пароль")

        class Login:

            def __init__(self, _login):
                self._login = login

            def __str__(self):
                return f" {self.login}"

            @property
            def login(self):
                return self.login

            @login.setter
            def login(self, value):
                if value != login:
                    print("Логин не верный")
                else:
                    self._login = value

        class Password:

            def __init__(self, password):
                self.password = password

            def __str__(self):
                return f" {self.password}"

            @property
            def login(self):
                return self.password

            @login.setter
            def login(self, value):
                if value != password:
                    print("Пароль не верный")
                else:
                    self.password = value
    if option == 2:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        write_to_file(f"{login}|{password}")

    if option == 3:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        write_to_file(f"{login}|{password}")

    if option == 4:
        print("Выход...")
        break
    else:
        print("Выберите один из вариантов!!!")

main()