""" Создайте класс студента.
    ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
        наличие только букв.
    ○ Названия предметов должны загружаться из файла CSV при создании
        экземпляра. Другие предметы в экземпляре недопустимы.
    ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
        тестов (от 0 до 100).
    ○ Также экземпляр должен сообщать средний балл по тестам для каждого
        предмета и по оценкам всех предметов вместе взятых."""
import csv


class Name:
    def __set_name__(self, owner, name):
        self.storage_name = name

    def __set__(self, instance, value):
        if value.istitle():
            for c in value:
                c.isascii()
            instance.__dict__[self.storage_name] = value
        else:
            msg = "ФИО должно начинаться с заглавной буквы и не содержать символов!"
            raise ValueError(msg)


class Score:
    def __set_name__(self, owner, score):
        self.storage_score = score

    def __set__(self, instance, value):
        if 1 < value < 6:
            instance.__dict__[self.storage_score] = value
        else:
            msg = "Оценка по предмету должна быть от 2 до 5 баллов включительно!"
            raise ValueError(msg)


class Mark:
    def __set_name__(self, owner, mark):
        self.storage_mark = mark

    def __set__(self, instance, value):
        if 0 <= value < 101:
            instance.__dict__[self.storage_mark] = value
        else:
            msg = "Балл по тесту должен быть от 0 до 100 включительно!"
            raise ValueError(msg)


class Student:
    lastname = Name()
    firstname = Name()
    patronymic = Name()
    score = Score()
    mark = Mark()

    def __init__(self, lastname, firstname, patronymic):
        self.lastname = lastname
        self.firstname = firstname
        self.patronymic = patronymic
        self.courses = self.load_courses()

    def __str__(self):
        return f"{'=' * 38}\n\t{one.lastname} {one.firstname} {one.patronymic}"

    def set_score(self, course, score):
        self.score = score
        score_list = self.courses[course]
        score_list["Оценка"].append(score)
        self.courses[course] = score_list
        return self.courses

    def set_mark(self, course, mark):
        self.mark = mark
        mark_list = self.courses[course]
        mark_list["Тест"].append(mark)
        self.courses[course] = mark_list
        return self.courses

    # def average_mark(self):
    #     total = 0
    #     print("=" * 38)
    #     print("\t\tРЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
    #     print("=" * 38)
    #     for course, mark in self.courses.items():
    #         if len(mark['Тест']) == 0:
    #             continue
    #         else:
    #             for m in mark['Тест']:
    #                 total += m
    #             print(f"{course}. Средний балл: {total / len(mark['Тест']):.2f}")
    #             print(f"Результаты тестирования: {str(mark['Тест']).replace('[', '').replace(']', '')}")

    def average_mark(self):
        total = 0
        for course, mark in self.courses.items():
            if len(mark['Тест']) == 0:
                continue
            else:
                for m in mark['Тест']:
                    total += m
            return total / len(mark['Тест'])

    # def average_score(self):
    #     # print("=" * 38)
    #     # print("\t\tУСПЕВАЕМОСТЬ ПО ПРЕДМЕТАМ")
    #     # print("=" * 38)
    #     total = 0
    #     total_average_score = 0
    #     courses_count = 0
    #     for course, score in self.courses.items():
    #         if len(score['Оценка']) == 0:
    #             continue
    #         else:
    #             for s in score['Оценка']:
    #                 total += s
    #             print(f"{course}. Оценки: {str(score['Оценка']).replace('[', '').replace(']', '')}")
    #         courses_count += 1
    #         course_average_score = total / len(score['Оценка'])
    #         total_average_score += course_average_score
    #         total = 0
    #     # print("_" * 38)
    #     print(f"Средняя оценка по всем предметам: {total_average_score / courses_count:.2f}")

    def average_score(self):
        total = 0
        total_average_score = 0
        courses_count = 0
        for course, score in self.courses.items():
            if len(score['Оценка']) == 0:
                continue
            else:
                for s in score['Оценка']:
                    total += s
            courses_count += 1
            course_average_score = total / len(score['Оценка'])
            total_average_score += course_average_score
            total = 0
            return total_average_score / courses_count

    def report(self):
        print(self)
        print(self.average_score())
        print(self.average_mark())

    @staticmethod
    def load_courses():
        courses = list()
        with open('course.csv', 'r', encoding="UTF-8", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                courses.append(*row)
            return {item: {"Оценка": list(), "Тест": list()} for item in courses}


# course = ['Русский язык', 'Математика', 'Физика', 'История', 'Информатика', 'Литература']
# with open('course.csv', "w", newline='', encoding="UTF-8") as file:
#     writer = csv.writer(file, delimiter='\n')
#     writer.writerow(course)

one = Student('Волченко', 'Павел', "Александрович")
two = Student('Коротун', 'Андрей', "Викторович")
three = Student('Rротун', 'Rдрей', "Rкторович")

one.set_score("Математика", 5)
one.set_score("Математика", 4)
one.set_score("Математика", 3)
one.set_mark("Математика", 89)
one.set_mark("Математика", 75)
one.set_mark("Математика", 60)
one.set_mark("Математика", 100)
one.set_mark("Русский язык", 55)
one.set_mark("Русский язык", 35)
one.set_mark("Русский язык", 27)
one.set_mark("Русский язык", 26)
one.set_mark("Русский язык", 75)
one.set_score("Русский язык", 4)
one.set_score("Русский язык", 2)
one.set_score("Русский язык", 3)
one.set_score("Русский язык", 4)
one.set_score("История", 4)
one.set_score("История", 5)
one.set_score("История", 4)
one.set_score("История", 3)
one.set_score("История", 5)
one.set_score("История", 5)
one.set_score("Информатика", 5)
one.set_score("Информатика", 5)
one.set_score("Информатика", 5)
one.set_score("Информатика", 5)
one.set_score("Информатика", 5)

two.set_score("Математика", 5)
two.set_score("Математика", 4)
two.set_score("Математика", 3)
two.set_mark("Математика", 89)
two.set_mark("Математика", 75)
two.set_mark("Математика", 60)
two.set_mark("Математика", 100)
two.set_mark("Русский язык", 55)
two.set_mark("Русский язык", 35)
two.set_mark("Русский язык", 27)
two.set_mark("Русский язык", 26)
two.set_mark("Русский язык", 75)
two.set_score("Русский язык", 4)
two.set_score("Русский язык", 2)
two.set_score("Русский язык", 3)
two.set_score("Русский язык", 4)
two.set_score("История", 4)
two.set_score("История", 5)
two.set_score("История", 4)
two.set_score("История", 3)
two.set_score("История", 5)
two.set_score("История", 5)


# print(one)
# one.average_mark()
# one.average_score()
# pprint(one.courses)

one.report()
two.report()
three.report()
