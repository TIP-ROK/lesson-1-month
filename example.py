class Income:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    def __str__(self):
        return f"{self.name} {self.amount}"

def main():
    income = []
    while True:
        print("1) Добавить Рассход")
        print("2) Получить Рассходы")
        print("3) Получить сумму Рассходов")
        print("4) Введите доход")
        print("5) Вывести доходы")
        print("6) Вывести остаток средств")
        print("7) Выход")
        option = int(input("Введите вариант: "))
        if option == 1:
            name = input("Название: ")
            amount = int(input("Сумма: "))
            income.append(Income(name, amount))

main()
