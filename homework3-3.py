def my_func(a, b, c):
    return (a + b + c) - min(a, b, c)

a = int(input("первое число: "))
b = int(input("второе число: "))
c = int(input("третье число: "))
print(my_func(a, b, c))
