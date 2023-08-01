# Создайте функцию генератор чисел Фибоначчи

def fib(num=10):
    first, second = 0, 1
    while num > 0:
        yield first
        first, second = second, first + second
        num -= 1


for i in fib(20):
    print(i, end=' ')
