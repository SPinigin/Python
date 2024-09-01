import Class


def main():
    # Создаем экземпляры животных
    animals = [
        Class.Dog("Барбос"),
        Class.Cat("Барсик"),
        Class.Bear("Винни")
    ]

    # Ветеринар
    vet = Class.Veterinarian()

    for animal in animals:
        vet.treatAnimal(animal)
        print()

    # Вызов методов makeNoise и eat для каждого животного
    for animal in animals:
        animal.makeNoise()
        animal.eat()
        print()


if __name__ == "__main__":
    main()
