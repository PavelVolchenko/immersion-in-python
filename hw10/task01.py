""" Доработаем задания 5-6. Создайте класс-фабрику.
    Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
    Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики."""


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args, **kwargs):
        if animal_type == "Рыба":
            return Fish(*args, **kwargs)
        elif animal_type == "Собака":
            return Dog(*args, **kwargs)
        elif animal_type == "Птица":
            return Bird(*args, **kwargs)
        else:
            return ValueError("Неверный тип животного!")


class Animal:
    def __init__(self, name, age=None, voice='Аргхх!'):
        self.name = name
        self.age = age
        self.voice = voice

    def make_voice(self):
        print(self.voice)


class Fish(Animal):
    def __init__(self, name, age, scales, voice):
        super().__init__(name, age, voice)
        self.scales = scales

    def swim(self):
        print("Плыву, через жабры дышу!")


class Dog(Animal):
    def __init__(self, name, age, breed, voice):
        super().__init__(name, age, voice)
        self.breed = breed

    def bark(self):
        print('Гаф-Гаф!')


class Bird(Animal):
    def __init__(self, name, age, color, voice):
        super().__init__(name, age, voice)
        self.color = color
        self.voice = voice

    def fly(self):
        print('Грру-грру-у! Грру-грру-у!')


factory = AnimalFactory()

dog = factory.create_animal("Собака", "Ричард", "2", "Мопс", "Р-р-р-Гаф")
bird = factory.create_animal("Птица", "Голубь-Володя", "6", "Серый", "Курлы-Курлы")

print(f"{dog.breed} {dog.name} {dog.voice}")
dog.bark()
print(f"{bird.name}, {bird.age} лет.")
print(bird.voice)