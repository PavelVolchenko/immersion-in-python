""" Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
    Функцию hex используйте для проверки своего результата.                                                  """


number = int(input("Enter a number: "))
result = list()
print(hex(number)[2:])

while number > 15:
    result.append(str(number % 16))
    number //= 16
result.append(str(number))

result.reverse()
result = " ".join(result).replace("10", "A").replace("11", "B").replace("12", "C")\
    .replace("13", "D").replace("14", "E").replace("15", "F").replace(" ", "")
print(result)
