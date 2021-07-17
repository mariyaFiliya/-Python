class Stationery:
    def __init__(self, title):
        self.title = title

    def draw():
        print("Запуск отрисовки")
class Pen:

    def draw():
        print("Рисуем ручкой")

class Pencil:
    def draw():
        print("Рисуем карандашом")

class Handle:
    def draw():
        print("Рисуем маркером")


stationery = Stationery
stationery.draw()

pen = Pen
pen.draw()

pencil = Pencil
pencil.draw()

handle = Handle
handle.draw()