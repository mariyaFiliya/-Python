class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        pass

    def __add__(self, other):
        pass


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix_1)
print(matrix_1 + matrix_2)
