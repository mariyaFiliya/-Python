def user_data(name, surname, year, city, email, phone_number):
    return name, surname, year, city, email, phone_number


print(user_data(name=input("Введите ваше имя: "), surname=input("Введите вашу фамилию: "),
                year=input("Введите год вашего рождения: "), city=input("Введите город ващего проживания: "),
                email=input("Введите ваш e-mail: "), phone_number=input("Введите ваш номер телефона: ")))
