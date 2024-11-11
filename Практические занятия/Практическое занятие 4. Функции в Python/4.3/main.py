def is_magic_date():
    date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
    day, month, year = date.split(".")
    day, month, year = int(day), int(month), int(year)

    if day * month == year % 100:
        print("Дата магическая!")
        return True
    else:
        print("Дата не магическая.")
        return False


is_magic_date()
