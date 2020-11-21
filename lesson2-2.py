print("Здорово!!!")

expenses = []
while True:
    print("1) Вывести все раходы")
    print("2) Сумма всех расходов")
    print("3) Добавить новый расход")
    print("4) закрыть программу")
    option = int(input("Выберите вариант: "))
    if option == 3:
        amaunt = int(input("Введите сумму: "))
        name = input("На что потратил: ")
        date = input("Когда потратил: ")
        expenses.append([amaunt, name, date])

    if option == 2:
        list_len = len(expenses)
        d = 0
        result = 0
        while d < list_len:
            result += expenses [d] [0]
            d += 1
        print(f"Сумма ваших расходов: {result}")

    if option == 1:
        list_len = len(expenses)
        d = 0
        print()
        while d < list_len:
            print(f"{expenses[d] [0]} | {expenses[d] [1]} | {expenses[d] [2]}")
            d = d + 1

    if option == 4:
        print("Завершение!")
        break

    if option == 5:
        print("вариант выбран не верно")
    continue