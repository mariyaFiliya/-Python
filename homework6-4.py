class Car:
    def __init__(self, s, c, n, i_p):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = i_p
    def go(self):
        print(f'{self.name} машина поехала'.capitalize())

    def stop(self):
        print(f'{self.name} машина остановилась'.capitalize())

    def turn(self, direction):
        print(f'{self.name} машина повернула {direction}'.capitalize())

    def show_speed(self):
        print(f'{self.name} машина едет со скоростью {self.speed} км в час'.capitalize())


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print("Вы превысили скорость!")
            print(f'ваша скорость {self.speed} км в час'.capitalize())
        else:
            print(f'{self.name} car moves at a speed of {self.speed} km per hour'.capitalize())


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Вы превысили скорость!")
            print(f'ваша скорость {self.speed} км в час'.capitalize())
        else:
            print(f'{self.name} car moves at a speed of {self.speed} km per hour')


class PoliceCar(Car):
    pass


t_c = TownCar(80, "Green", "городская", False)
t_c.go()
t_c.show_speed()
t_c.stop()

s_c = SportCar(120, "Red", "спортивная", False)
s_c.go()
s_c.show_speed()
s_c.stop()

w_c = WorkCar(50, "Black", "рабочая", False)
w_c.go()
w_c.show_speed()
w_c.stop()

p_c = PoliceCar(100, "Blue", "полицейская", True)
p_c.go()
p_c.show_speed()
p_c.stop()