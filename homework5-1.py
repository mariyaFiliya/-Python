with open("text-1.txt", "a", encoding="utf-8") as user_data:
    while True:
        line = input('Введите строку данных: ')
        if not line:
            break
        print(line, file=user_data)
