def divide_by_user_input():
    try:
        number = float(input("Введите число для деления 100: "))
        result = 100 / number
        print(f"Результат деления 100 на {number} = {result}")
    except ValueError:
        print("Ошибка! Введено не число.")
    except ZeroDivisionError:
        print("Ошибка! Деление на ноль невозможно.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

divide_by_user_input()
