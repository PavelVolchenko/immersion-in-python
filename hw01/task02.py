# Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу и на себя».
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

n = -1

while not 0 <= n <= 100000:
    n = int(input("Введите любое положительное число до 100000 включительно: "))

for i in range(2, 11):
    if n == i or i > 9:
        print(f"Число {n} - ПРОСТОЕ!")
        break
    elif n % i == 0:
        print(f"Число {n} - СОСТАВНОЕ!")
        break