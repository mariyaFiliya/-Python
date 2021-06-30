winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
mounth = int(input("Введите номер месяца: "))
if winter.count(mounth) > 0:
    print("Зима")
elif spring.count(mounth) > 0:
    print("Весна")
elif summer.count(mounth) > 0:
    print("Лето")
elif autumn.count(mounth) > 0:
    print("Осень")
else:
    print("Вы ввели неверное значение.")

mounths = {1: 'Зима', 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}
mounth = int(input("Введите номер месяца: "))
print(mounths.get[mounth])