from datetime import datetime


class Expense:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.date = datetime.now()

    def __str__(self):
        return f"{self.name} {self.amount} {self.date}"


def calc_sum(expenses):
    result = 0
    for expense in expenses:
        result += expense.amount
    return result


class Income:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.date = datetime.now()

    def __str__(self):
        return f"{self.name} {self.amount} {self.date}"


#def calc_sum(incomes):
 #   result = 0
  #  for income in incomes:
   #     result += income.amount
    #return result

def main():
    expenses = []
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
            expenses.append(Expense(name, amount))

        if option == 2:
            for expense in expenses:
                print(expense)

        if option == 3:
            print(calc_sum(expenses))

        if option == 4:
            name = input("Название дохода: ")
            amount = int(input("Сумма: "))
            income.append(Income(name, amount))

        if option == 5:
            for income in income:
                print(income)

        if option == 6:
            print()

        if option == 7:
            print("Выход...")
            break

        else:
            print("Выберите один из вариантов!!!!!!!!!")


main()
