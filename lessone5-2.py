from datetime import datetime


class Expense:

    def __init__(self, name, amount, date):
        self.name = name
        self.amount = amount
        self.date = date


    def __str__(self):
        return f"{self.name} {self.amount} {self.date}"

expense1 = Expense