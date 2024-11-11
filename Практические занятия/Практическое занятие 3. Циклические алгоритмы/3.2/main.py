def concatenate_words_until_stop():
    result = ""
    while True:
        word = input("Введите слово (или 'stop' для завершения): ")
        if word == "stop":
            break
        result += word + " "
    print(result.strip())

concatenate_words_until_stop()
