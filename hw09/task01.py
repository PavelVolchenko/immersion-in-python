""" Напишите следующие функции:
    - Нахождение корней квадратного уравнения
    - Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
    - Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
    - Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.    """
import csv
from random import randint
from typing import Callable


def from_csv(func: Callable):
    def wrapper(*args):
        result = list()
        with open('numbers.csv', newline='') as file:
            reader = csv.reader(file, quoting=csv.QUOTE_NONE)
            for row in reader:
                a, b, c = map(int, str(*row).split(' '))
                result.append(func(a, b, c))
            return result
    return wrapper

# def safe(func: Callable):
#     def wrapper(*args):
#         result = list()
#         with open('numbers.csv', newline='') as file:
#             reader = csv.reader(file, quoting=csv.QUOTE_NONE)
#             for row in reader:
#                 a, b, c = map(int, str(*row).split(' '))
#                 result.append(func(a, b, c))
#             return result
#     return wrapper


def generate_csv(rows: int = 100) -> str:
    with open('numbers.csv', 'w', encoding='utf-8', newline='') as file:
        numbers_writer = csv.writer(file, delimiter='\n')
        numbers_writer.writerow([f'{randint(-100, 100) or 100} {randint(-100, 100)} {randint(-100, 100)}'
                                 for row in range(rows)])
    return f"Файл csv успешно сгенерирован.\nКол-во строк: {rows}"


@safe
@from_csv
def find_roots(a, b, c: int):
    # print(type(numbers))
    # print(numbers)
    # a, b, c = map(int, numbers.split(' '))

    d = b ** 2 - 4 * a * c
    if d < 0:
        return "Корней нет"
    elif d == 0:
        return f'x: {-b / (2 * a):.2f}'
    elif d > 0:
        # x1 = (-b + d ** 0.5) / (2 * a)
        # x2 = (-b - d ** 0.5) / (2 * a)
        return f'x1: {(-b + d ** 0.5) / (2 * a):.2f}, x2: {(-b - d ** 0.5) / (2 * a):.2f}'


# def find_roots(numbers=None):
#     a, b, c = map(int, f'{randint(-100, 100)} {randint(-100, 100)} {randint(-100, 100)}'.split(' '))
#     d = b ** 2 - 4 * a * c
#     print(f"a = {a}, b = {b}, c = {c}")
#     print("Корней нет" if d < 0 else
#           "Есть один корень" if d == 0 else
#           "Есть два различных корня")
#     if d == 0:
#         x = -b / (2 * a)
#         print(x)
#     elif d > 0:
#         x1 = (-b + d ** 0.5) / (2 * a)
#         x2 = (-b - d ** 0.5) / (2 * a)
#         print(f"x1 = {x1:.2f}, x2 = {x2:.2f}")

generate_csv(10)
# r = find_roots()
# print(r)
# print(generate_csv(10))

# print(f := from_csv("10 100 100"))
# print(f)
