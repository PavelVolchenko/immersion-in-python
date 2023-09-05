# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например, нельзя создавать прямоугольник со сторонами отрицательной длины.
import logging
import argparse

class TypeException(Exception):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'{self.side} не допустимое значение'

class ValueException(Exception):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'{self.side} не допустимое значение.'


class Side:
    @classmethod
    def verify(cls, value):
        try:
            int(value)
        except ValueError:
            logging.warning(TypeException(value))
            raise TypeException(value)
        if int(value) <= 0:
            logging.warning(ValueException(value))
            raise ValueException(value)

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify(value)
        instance.__dict__[self.name] = int(value)


class Square:
    a = Side()
    b = Side()

    def __init__(self, a, b):
        self.a = a
        if b is None:
            self.b = a
        else:
            self.b = b
        logging.info(self)

    def __add__(self, other):
        if isinstance(other, Square):
            return Square(self.a + other.a, self.b + other.b)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Square):
            if other.a > self.a or other.b > self.b:
                raise ValueError('Такой прямоугольник невозможен')
            return Square(self.a - other.a, self.b - other.b)
        return NotImplemented

    def get_area(self):
        logging.info(self.a * self.b)
        return self.a * self.b

    def get_perimetr(self):
        logging.info(2 * (self.a + self.b))
        return 2 * (self.a + self.b)

    def __repr__(self):
        return f"Square({self.a}, {self.b})"

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.get_area() == other.get_area()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.get_area() > other.get_area()
        return NotImplemented


if __name__ == "__main__":

    FORMAT = "| {levelname:<8} {asctime:<25} | LINE {lineno:<5} | FUNC {funcName:<15} | RESULT {message:<20} |"
    logging.basicConfig(level=logging.DEBUG, filename="py_log.log", filemode="a", encoding='utf-8', style="{",
                        format=FORMAT)
    parser = argparse.ArgumentParser(description='Вычисляет площадь и периметр прямоугольника')
    parser.add_argument('a', metavar='a', help='Введите сторону А')
    parser.add_argument('b', metavar='b', help='Введите сторону B')
    args = parser.parse_args()

    s = Square(args.a, args.b)
    s.get_area()
    s.get_perimetr()