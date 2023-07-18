# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c — стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

from itertools import permutations

triangle = map(int, input("Enter the three sides of the triangle separated by a space: ").split())

for i in permutations(triangle, r=3):
    if i[0] > i[1] + i[2]:
        print("Длина отрезка треугольника больше суммы двух других.\n"
              f"a={i[0]}, b={i[1]}, c={i[2]}\n"
              "Треугольника с такими сторонами не существует.")
        break

    elif i[0] != i[1] and i[0] != i[2] and i[1] != i[2]:
        print("Отрезки всех трех сторон треугольника имеют разную длину.\n"
              f"a={i[0]}, b={i[1]}, c={i[2]}\n"
              "Такой треугольник называется - Разносторонним")
        break

    elif i[0] == i[1] and i[1] == i[2]:
        print("Отрезки всех трех сторон треугольника имеют равную длину.\n"
              f"a={i[0]}, b={i[1]}, c={i[2]}\n"
              "Такой треугольник называется - Равносторонним")
        break

    elif i[0] == i[1] and i[1] != i[2]:
        print("Отрезки двух сторон треугольника имеют равную длину.\n"
              f"a={i[0]}, b={i[1]}, c={i[2]}\n"
              "Такой треугольник называется - Равнобедренный")
        break