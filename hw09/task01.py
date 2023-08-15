""" Напишите следующие функции:
    - Нахождение корней квадратного уравнения
    - Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
    - Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
    - Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.    """

import csv
import json
from random import randint


def from_csv():
    result = list()
    with open('numbers.csv', newline='') as file:
        reader = csv.reader(file, quoting=csv.QUOTE_NONE)
        for row in reader:
            result.append(str(*row))
        return result


def json_writer(result):
    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=2, ensure_ascii=False)


def generate_csv(rows: int = 100) -> str:
    with open('numbers.csv', 'w', encoding='utf-8', newline='') as file:
        numbers_writer = csv.writer(file, delimiter='\n')
        numbers_writer.writerow([f'{randint(-100, 100) or 100} {randint(-100, 100)} {randint(-100, 100)}'
                                 for row in range(rows)])
    return f"Файл csv успешно сгенерирован.\nКол-во строк: {rows}"


def deco_roots(func):
    abc_list = from_csv()

    def inner():
        result = dict()
        for abc in abc_list:
            a, b, c = map(int, abc.split(' '))
            result[f'{a=}, {b=}, {c=}'] = func(a, b, c)
        return result

    return inner


def deco_json_writer(func):

    def inner():
        result = func()
        json_writer(result)
        return result

    return inner


@deco_json_writer
@deco_roots
def find_roots(a: int, b: int, c: int):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return "Корней нет"
    elif d == 0:
        return f'x: {-b / (2 * a):.2f}'
    elif d > 0:
        return f'x1: {(-b + d ** 0.5) / (2 * a):.2f}, x2: {(-b - d ** 0.5) / (2 * a):.2f}'


generate_csv(100)
print(find_roots())
