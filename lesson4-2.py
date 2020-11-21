from datetime import datetime
from random import randint
from math import pi

def int_input():
    while True:
        try:
            return int(input("Введите ваш {text} "))
        except Exception:
            print("Введите ваш {text} ввиде числа ")

def main():
    while True:
        start = 0
        end = 21
        random_num = randint(start, end)

        for i in range(5):
            user_num = int_input(f"Число от {start} до {end - 1}")
            if user_num == random_num:
                print(f"Вы выйиграли! кол-во {i+1}")
                break
            else:
                print("Попробуй ещё раз")
    print(f"Вы проиграли число было - {randome_num}")

main()