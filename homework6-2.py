class Road:
    def __init__(self, l, w):
        self._lenght = l
        self._width = w

    def MassOfAsphalt( ma, t, l, w):
        m = l * w * ma * t
        print(f"{m / 1000} т.")

road = Road
road.MassOfAsphalt(25, 20, 5000, 5)