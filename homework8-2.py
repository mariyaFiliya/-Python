class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        num_1 = int(input('Введите делимое: '))
        num_2 = int(input('Введите делитель: '))
        if num_2 == 0:
            raise OwnError("Деление на ноль невозможно.")
        else:
            result = num_1 / num_2
            return result
    except ValueError:
        return "Введённые данные некорректны"
    except OwnError as err:
        return err


print(div())
