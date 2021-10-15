##########################################################
##    Single Responsibility Principle
##########################################################

class Animal:
    """
    Класс отвечает за инициализацию объекта "animal" с именем
    """
    def __init__(self, name: str):
        self.name = name

    def get_animal_name(self) -> str:
        return self.name

    def __str__(self):
        return f"{__class__.__name__}:{self.name}"

class Fish:
    """
        Класс отвечает за инициализацию объекта "fish" с именем
        """

    def __init__(self, name: str):
        self.name = name

    def get_animal_name(self) -> str:
        return self.name

    def __str__(self):
        return f"{__class__.__name__}:{self.name}"


class Db:
    """
    Класс отвечает за сохранение объекта "animal" в БД animal_safe
    """
    _safe = []
    _dict = {}

    def save_animal(self, a: object) -> None:
        Db._safe.append(a)

    def save_animal_dict(self, i: str, a: object) -> None:
        Db._dict[i] = a


def display_type(obj: object) -> None:
    """
    Печать данных из условной -БД-
    """
    print("List out")
    for an in enumerate(obj._safe):
        print(an[0], '.', an[1])

    print("-*-" * 18)
    print("Dict out")
    for k, v in obj._dict.items():
        print(k, ".", v)


def main():
    myDb = Db()

    name = ['a1', 'b2', 'c3', 'd4']
    for i in range(4):
        animal = Animal(name[i])
        myDb.save_animal(animal)
        myDb.save_animal_dict(str(i) + "-animal", animal)

    for i in range(4):
        fish = Fish(name[i])
        myDb.save_animal(fish)
        myDb.save_animal_dict(str(i) + "-fish", fish)

    display_type(myDb)


if __name__ == '__main__':
    main()

