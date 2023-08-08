# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла.
#   Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени.
#   Например, для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
#   К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os.path


def rename_files(new_filename,
                 count_numbers=None,
                 input_file_ext=None,
                 result_file_ext=None,
                 range_original_filename=None):
    pass


print(os.path.abspath('test'))
*_, files = list(*os.walk('test'))
filenames = list()
for filename in files:
    filenames.append(filename.split('.'))

print(files)
print(filenames)
new_filename = input("Введите новое имя файлов: ")
count_numbers = int(input("Введите желаемое кол-во цифр для порядкового номера: "))
# input_file_ext = input("Введите расширение для файлов которые нужно переименовать: ")
# result_file_ext = input("Введите расширение для расширение конечных файлов: ")
# range_original_filename = list(map(int, input("Введите через пробел, диапазон сохраняемого оригинального имени: ").split()))

for i, name in enumerate(filenames, 1):
    count_numbers
    filenames[i-1][0] = new_filename + str(i)

print(filenames)



