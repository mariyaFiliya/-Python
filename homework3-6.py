def int_func():
    for word in input('введите слово из маленьких латинских букв: ').split():
        symbols: int = 0
        for symbol in word:
            if 97 <= ord(symbol) <= 122:
                symbols += 1
        print(word.title() if symbols == len(word) else "")


int_func()
