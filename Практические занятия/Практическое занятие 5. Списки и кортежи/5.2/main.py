def check_duplicates_in_list():

    my_list = [1, 2, 3, 4, 2, 5, 1]
    duplicates = set()

    for x in my_list:
        if my_list.count(x) > 1:
            duplicates.add(x)


    if duplicates:
        print(f"Повторяющиеся элементы: {duplicates}")
    else:
        print("Повторяющихся элементов нет.")


check_duplicates_in_list()
