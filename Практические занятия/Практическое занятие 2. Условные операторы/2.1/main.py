def check_password():
    password = input("Введите пароль: ")
    confirm_password = input("Подтвердите пароль: ")
    if password == confirm_password:
        print("Пароль принят")
    else:
        print("Пароль не принят")

check_password()
