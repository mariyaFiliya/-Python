class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join([f'{item:3}' for item in line]) for line in self.matrix)

    def __add__(self, other):
        try:
            n = [[int(self.matrix[line][item]) + int(other.matrix[line][item]) for item in range(len(self.matrix[line]))] for line in range(len(self.matrix))]
            return Matrix(n)
        except IndexError:
            return "err"


matrix_1 = Matrix([[2, 5, 7], [1, 1, 6], [3, 12, 7]])
matrix_2 = Matrix([[0, 23, 5], [2, 5, 3], [5, 4, 8]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
