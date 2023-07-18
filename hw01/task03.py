# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код: from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

number = randint(0, 1000)
print("======= Угадай число =======\n"
      "Я загадал число от 0 до 1000!")
user = -1
count = 0
while user != number:
    user = int(input(" -> "))
    if user > number:
        print("<<<<< Меньше <<<<<")
        count += 1
    elif user < number:
        print(">>>>> Больше >>>>>>")
        count += 1
    else:
        print(f"========= УГАДАЛ =========\n"
              f"Я загадал число {number}.\n"
              f"Количество попыток: {count}.")

