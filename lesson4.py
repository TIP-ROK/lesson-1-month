def write_to_file(line):
    new_file = open("text", "a")
    new_file.write(f"{line}\n")
    new_file.close()

#lines = new_file.readlines()
#print(lines, "\n", "ABC")

#new_file.write("Hello, World!\n")
#new_file.writelines(["Hello, Wrld2!\n, Hello, World2!\n"])
#new_file.write("Hello, World3!")

#lines = new_file.readlines()
#print(lines)
#new_file.close()

def read_frome_file():
    file = open("text", "r")
    lines = file.readlines()
    file.close()
    return lines

def calc_sum():
    lines = read_frome_file()
    result = 0
    for i in lines:
        line = i.split("|")
        amaunt = int(line[1])
        result += amaunt
    return result

def main():
    while True:
        print("1) Добавить расход")
        print("2) Получить расходы")
        print("3) Сумма расходов")
        print("4) Выход")

        option = int(input("Введите вариант: "))
        if option == 1:
            name = input("Название: ")
            amount = input("Сумма: ")
            date = input("Дата: ")
            write_to_file(f"{name}|{amount}|{date}")
        if option == 2:
            license = input("Название: ")
            for i in license:
                print(i)
        if option == 3:
            print("calc_sum()")

        if option == 4:
            print("Выход...")
            break
        else:
            print("Выберите один из вариантов!!!")

main()