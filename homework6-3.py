class Worker:
    def __init__(self, n, s, p, wage, bonus):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.surname, self.name)
    def get_total_income(self):
        print(sum(self._income.values()))


position = Position("Kate", "Wilson", "barmen", 10000, 500)

position.get_full_name()
position.get_total_income()

