
def numbers_sum():
    # a = map(int, input("Введите числа через пробел, если хотите выйти из цикла, введите 'stop': ").split())
    result = 0
    while True:
        a = input("Введите числа через пробел, если хотите выйти из цикла, введите 'stop': ").split()
        for element in a:
            if element == 'stop':
                return result
            else:
                try:
                    result += int(element)
                except ValueError:
                    print("Вы ввели неверное значение")
        print(result)
print(numbers_sum())