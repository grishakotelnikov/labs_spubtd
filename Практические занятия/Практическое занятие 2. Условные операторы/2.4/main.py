def mix_colors():
    color1 = input("Введите первый цвет: ").lower()
    color2 = input("Введите второй цвет: ").lower()

    if (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
        print("Получается фиолетовый")
    elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
        print("Получается оранжевый")
    elif (color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий"):
        print("Получается зеленый")
    else:
        print("Ошибка: неверный ввод цвета")

mix_colors()
