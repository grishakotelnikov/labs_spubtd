def math_game():
    correct_answers = 0
    wrong_answers = 0
    while wrong_answers < 3:
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        answer = int(input(f"{num1} + {num2} = "))
        if answer == num1 + num2:
            print("Правильно!")
            correct_answers += 1
        else:
            print("Ответ неверный")
            wrong_answers += 1
    print(f"Игра окончена. Правильных ответов: {correct_answers}")

from random import randint
math_game()
