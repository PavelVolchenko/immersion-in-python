# Напишите функцию для транспонирования матрицы

def transport_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(i, len(matrix)):
            if i != j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def pr(mx):
    for i in range(len(mx)):
        for j in range(len(mx)):
            print(mx[i][j], end=' ')
        print()


x = [[10, 10, 10, 10], [22, 22, 22, 22], [33, 33, 33, 33], [77, 77, 77, 77]]

result = transport_matrix(x)
pr(result)
