# Базовый класс Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def makeNoise(self):
        pass

    def eat(self):
        pass

    def getDescription(self):
        return "Это животное по имени " + self.name


# Класс Dog, наследующий от Animal
class Dog(Animal):
    def makeNoise(self):
        print(f"{self.name} говорит: Гав-гав!")

    def eat(self):
        print(f"{self.name} ест: мясо, кости, корм для собак.")

    def getDescription(self):
        return f"Собака по имени {self.name}. Очень дружелюбная и преданная."


# Класс Cat, наследующий от Animal
class Cat(Animal):
    def makeNoise(self):
        print(f"{self.name} говорит: Мяу-мяу!")

    def eat(self):
        print(f"{self.name} ест: рыбу, молоко, корм для кошек.")

    def getDescription(self):
        return f"Кот по имени {self.name}. Независимый и любит играть."


# Класс Bear, наследующий от Animal
class Bear(Animal):
    def makeNoise(self):
        print(f"{self.name} говорит: Ррррр!")

    def eat(self):
        print(f"{self.name} ест: рыбу, ягоды, мясо.")

    def getDescription(self):
        return f"Медведь по имени {self.name}. Сильный и мощный."


# Класс Ветеринар
class Veterinarian:
    def treatAnimal(self, animal):
        print(f"Ветеринар лечит животное по имени {animal.name}.")
        print(animal.getDescription())
