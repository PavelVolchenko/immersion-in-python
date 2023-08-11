# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её
# и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
#   Для дочерних объектов указывайте родительскую директорию.
#   Для каждого объекта укажите файл это или директория.
#   Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
#   с учётом всех вложенных файлов и директорий.

import csv
import json
import os
import pickle
from pprint import pprint


def walk_directory(directory: str) -> list:
    files_list, result_list = list(), list()
    full_size = 0
    for item in os.listdir(directory):
        if os.path.isdir(directory + "\\" + item):
            result_list.append({os.path.basename(directory): walk_directory(directory + "\\" + item)})
        elif os.path.isfile(directory + "\\" + item):
            files_list.append({item: str(os.path.getsize(directory + "\\" + item)) + " bytes"})
            full_size += os.path.getsize(directory + "\\" + item)
    result_list.append({os.path.basename(directory): [files_list, "total size: " + str(full_size) + " bytes"]})
    return result_list


print(homework_path := os.path.abspath('..'))
pprint(result := walk_directory(homework_path)[:-1])

with open('json-export.json', 'w', encoding='UTF-8') as f:
    json.dump(result, f, indent=2)

with open('csv-export.csv', 'w', newline='', encoding='UTF-8') as f:
    writer = csv.DictWriter(f, fieldnames=result[0].keys())
    writer.writerows(result)

with open('pickle.pickle', 'wb') as f:
    pickle.dump(result, f)

