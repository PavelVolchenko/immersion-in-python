# Функция принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

from os import path


def file_path(full_file_path: str):
    absolute_path = full_file_path.split("\\")
    return "\\".join(absolute_path[:-1]), absolute_path[-1].split(".")[0], absolute_path[-1].split(".")[1]


print(file_path(path.abspath("task01.py")))
