# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её
# и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
#   Для дочерних объектов указывайте родительскую директорию.
#   Для каждого объекта укажите файл это или директория.
#   Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
#   с учётом всех вложенных файлов и директорий.
import os
from pprint import pprint


def walk_directory(directory: str) -> list:
    files_list = list()
    res = list()
    for item in os.listdir(directory):
        if os.path.isdir(directory + "\\" + item):
            res.append({os.path.basename(directory): walk_directory(directory + "\\" + item)})
        elif os.path.isfile(directory + "\\" + item):
            files_list.append(item)
    res.append({os.path.basename(directory): files_list})
    return res


print(hw_path := os.path.abspath('..'))

pprint(walk_directory(hw_path))