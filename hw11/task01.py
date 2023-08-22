class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.elements = len(matrix[0])
        for column in matrix:
            if len(column) != self.elements:
                assert print("Кол-во элементов в столбцах матрицы не совпадают!")
            else:
                self.columns = len(column)
                self.size = self.rows, self.columns

    def __repr__(self):
        return f"{self.__class__.__name__} {self.rows} x {self.columns}, hash=({hash(self)})"

    def __add__(self, other):
        if self.check_size(other):
            return self.additional_matrix(other)
        else:
            assert print("ОШИБКА! ОШИБКА! ОШИБКА! ОШИБКА! ОШИБКА! ОШИБКА!"
                         "\nСкладывать можно только матрицы одинакового размера!")

    def print_matrix(self):
        print(self.__repr__())
        for i in range(self.rows):
            print("| ", end="")
            for j in range(self.columns):
                print(f"{self.matrix[i][j]:>2}", end=" ")
            print("| ")

    def check_size(self, other):
        return self.size.__eq__(other.size)

    def additional_matrix(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] += other.matrix[i][j]
        return Matrix(self.matrix)


A = Matrix([[1, 0, 12, 2, 4], [1, 0, 8, 18, 4], [1, 8, 0, 2, 4], [1, 0, 9, 2, 4], [1, 3, 0, 2, 4]])
B = Matrix([[1, 0, 45, 2, 4], [1, 22, 0, 2, 4], [10, 8, 0, 22, 4], [1, 21, 0, 2, 4], [1, 3, 38, 2, 4]])

A.print_matrix()
B.print_matrix()
C = A + B
C.print_matrix()

# print(f"{A = }, hash({hash(A)})")
# print(f"{B = }, hash({hash(B)})")
# print(f"{C = }, hash({hash(C)})")
