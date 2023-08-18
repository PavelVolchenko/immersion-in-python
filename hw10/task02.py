""" Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра. """
import csv
import json
import os
import pickle
from pprint import pprint


class InspectDirectories:

    def __init__(self):
        self.walk_result = None

    def walk_dir(self, abs_path):
        files_list, result_list = list(), list()
        files_size = 0
        for item in os.listdir(abs_path):
            if item == ".git":
                continue
            elif os.path.isdir(abs_path + "\\" + item):
                result_list.append({os.path.basename(abs_path): self.walk_dir(abs_path + "\\" + item)})
            elif os.path.isfile(abs_path + "\\" + item):
                files_list.append({"file": item, "size": os.path.getsize(abs_path + "\\" + item), 'path': os.path.abspath(item)})
                files_size += os.path.getsize(abs_path + "\\" + item)
        result_list.append(
            {os.path.basename(abs_path): {'files size': files_size}, 'files': files_list})
        self.walk_result = result_list
        return self.walk_result

    def export_json(self):
        with open('json-export.json', 'w', encoding='UTF-8') as f:
            json.dump(self.walk_result, f, indent=2)

    def export_csv(self):
        with open('csv-export.csv', 'w', newline='', encoding='UTF-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.walk_result[0].keys())
            writer.writerows(self.walk_result[:-1])

    def export_pickle(self):
        with open('pickle.pickle', 'wb') as f:
            pickle.dump(self.walk_result, f)


path = os.path.abspath('..\\..')

items = InspectDirectories()
items.walk_dir(path)

pprint(items.walk_result)
items.export_json()
items.export_csv()
items.export_pickle()
