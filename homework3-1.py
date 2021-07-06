def division(a, b):
    return a / b
try:
    print(division(int(input("Введите делимое: ")), int(input("Введите делитель: "))))
except ZeroDivisionError:
    print("Err. Нельзяя делить на 0")
except ValueError:
    print("err")
