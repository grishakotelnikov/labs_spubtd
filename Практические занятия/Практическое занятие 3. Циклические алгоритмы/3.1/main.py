def concatenate_words():
    n = int(input("Введите количество слов: "))
    result = ""
    for _ in range(n):
        word = input("Введите слово: ")
        result += word + " "
    print(result.strip())

concatenate_words()
