def weekend_days():
    weekdays = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    weekend_count = int(input("Сколько выходных дней на неделе хотите? "))

    weekend_days = weekdays[-weekend_count:]
    work_days = weekdays[:-weekend_count]

    print(f"Ваши выходные дни: {', '.join(weekend_days)}")
    print(f"Ваши рабочие дни: {', '.join(work_days)}")


weekend_days()
