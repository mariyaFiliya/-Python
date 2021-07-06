def my_funk(x, y):
    return 1 / x ** (-y)
x = int(input("введите положительное число: "))
y = int(input("введите отрицательное число: "))

print(my_funk(x, y))


def my_funk(x, y, i=1):
    while i < abs(y):
        x = x * x
        i += 1
    x = 1 / x
    print(x)


x = int(input("введите положительное число: "))
y = int(input("введите отрицательное число: "))

print(my_funk(x, y))
