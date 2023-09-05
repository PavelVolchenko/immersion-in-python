# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например, нельзя создавать прямоугольник со сторонами отрицательной длины.

from functools import total_ordering
import unittest


class TypeException(Exception):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'Входной параметр стороны прямоугольника должен быть числом.' \
               f'\n\t\t\t\t{self.side} не допустимое значение.'


class ValueException(Exception):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        """
        Входной параметр стороны прямоугольника не может быть отрицательной величиной либо нулем.
        """
        return f'Входной параметр стороны прямоугольника не может быть отрицательной величиной либо нулем.' \
               f'\n\t\t\t\t{self.side} не допустимое значение.'


class Side:
    @classmethod
    def verify(cls, value):
        try:
            int(value)
        except ValueError:
            raise TypeException(value)
        if int(value) <= 0:
            raise ValueException(value)

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify(value)
        instance.__dict__[self.name] = value


class TestSquare(unittest.TestCase):
    def test_value_error(self):
        with self.assertRaises(ValueError):
            Square(3, 5)

    def test_type_error_add(self):
        with self.assertRaises(TypeError):
            Square(4, 5) + Other

    def test_type_error_sub(self):
        with self.assertRaises(TypeError):
            Square(4, 5) - Other


class Other:
    pass


@total_ordering
class Square:
    a = Side()
    b = Side()

    def __init__(self, a, b):
        self.a = a
        if b is None:
            self.b = a
        else:
            self.b = b

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
        return self.a * self.b

    def get_perimetr(self):
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
    import doctest

    unittest.main()
    doctest.testmod(verbose=True)

    square_1 = Square(0, 4)
    square_2 = Square(5, 6)

    square_3 = square_1 + square_2
    square_4 = square_2 - square_1

    print(f"{square_1} + {square_2} = {square_3}")
    print(f"{square_2} - {square_1} = {square_4}")

    print(square_1 > square_2)
    print(square_1 < square_2)
    print(square_1 >= square_2)
    print(square_1 <= square_2)
    print(square_1 == square_2)
    print(square_1 != square_2)
