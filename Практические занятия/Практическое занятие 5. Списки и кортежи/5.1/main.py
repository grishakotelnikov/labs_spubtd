def check_number_in_list():
    numbers = [3, 5, 7, 9, 11]
    user_number = int(input("Введите число: "))

    if user_number in numbers:
        print(f"Поздравляю, Вы угадали число! В списке {numbers}")
    else:
        print(f"Нет такого числа! В списке {numbers}")


check_number_in_list()
