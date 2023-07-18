# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

import itertools

items = {
    "Палатка": 2.2,
    "Тент": 1.1,
    "Спальный мешок": 2.3,
    "Аптечка": 0.3,
    "Термочехол": 1.5,
    "Сидушка": 0.3,
    "Набор посуды": 1.1,
    "Термос": 1.3,
    "Топор": 1.5,
    "Лопата": 1,
    "Фонарь": 0.3,
    "Защита от насекомых": 0.4,
    "Еда": 3,
         }

res = items.keys()
r2 = list(res)
print(r2)


# print(list(items.keys()))

# payload = float(input("Enter a backpack payload: "))
payload = 10
# res = itertools.takewhile(lambda v: v[1] < payload, items.items())#
# print(*res)

# print(len(items))

# weight = 0
# print(weight)
# for k, v in items.items():
#     weight = weight + v
#     if weight > payload:
#         break
#     else:
#         print(k, end=', ')
#         for a, b in items.items():
#             weight = weight + b
#             # print(weight)
#             if weight > payload:
#                 break
#             elif k == a:
#                 continue
#             else:
#                 print(a, end=', ')
#         print(weight)
#     print("---")
#     weight = 0
