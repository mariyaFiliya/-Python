class Cell:
    def __init__(self, cell):
        self.cell = cell

    def make_order(self, raw):
        return '\n'.join(["○" * raw for _ in range(self.cell // raw)]) + '\n' + "○" * (self.cell % raw)

    def __str__(self):
        return f'{self.cell}'

    def __add__(self, other):
        print('сумма клеток равна: ')
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        print('разница клеток равна: ')
        return Cell(
            self.cell - other.cell) if self.cell - other.cell > 0 else 'вычитание невозможно, получается отрицательное значение'



cell_1 = Cell(15)
cell_2 = Cell(4)
print(cell_1 + cell_2)
print(cell_1.make_order(5))