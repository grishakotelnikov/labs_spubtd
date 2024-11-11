import os


def create_task_files():
    tasks = [
        {'task': 'Практическое занятие 9. Работа с файлами.',},
        {'task': 'Практическое занятие 10. Работа с файлами. Продолжение', },
        {'task': 'Практическое занятие 11. Объектно-ориентированное программирование', },
        {'task': 'Практическое занятие 12. ООП. Продолжение'},
        {'task': 'Практическое занятие 13. Создание приложений с GUI. TKinter'},
        {'task': 'Практическое занятие 14. Создание приложений с GUI. PyQt'},

    ]

    for task in tasks:
        task_path = os.path.join(task["task"])
        os.makedirs(task_path, exist_ok=True)



if __name__ == "__main__":
    create_task_files()

