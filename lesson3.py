from asyncio import tasks


def print_my_name():
    name = input("Введите имя: ")
    print(name)


def add_a_b(a, b):
    #print(a + b)
    return a + b

result = add_a_b(2, 2)
#add_a_b(2, 4)
#print(result)


def add_new_task(tasks):
    task = []
    for i in range(3):
        task.append(input())
    tasks.append(task)

def format_task(task):
    str_result = ""
    for o in task:
        str_result += f"{o} /"
    return str_result

def show_task(task) -> object:
    for i in task:
        print(format_task(i))

while True:
    print("1) Добавить новое задание")
    print("2) Показать задания")

    choice = int(input("Выберите вариант "))

    if choice == 1:
        add_new_task(tasks)
    if choice == 2:
        show_task(tasks)