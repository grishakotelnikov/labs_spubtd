def seat_type():
    seat = int(input("Введите номер места: "))

    if 1 <= seat <= 36:
        if seat % 2 != 0:
            print("Место в нижнем уровне купе.")
        else:
            print("Место в верхнем уровне купе.")
    elif 37 <= seat <= 54:
        print("Место в боковом.")
    else:
        print("Некорректный номер места.")


seat_type()
