###################################################################
##    Single Responsibility Principle
##
##  Класс должен быть ответственен лишь за что-то одно.
##
##  Если класс отвечает за решение нескольких задач,
##  оказываются связанными друг с другом.
##  Изменения в одной такой подсистеме ведут к изменениям в другой.
##
##
###################################################################

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
    Класс отвечает за сохранение объекта в БД
    """
    _safe = []
    _dict = {}

    def save_animal(self, a: object) -> None:
        """
        Сохранение в список
        """
        Db._safe.append(a)

    def save_animal_dict(self, i: str, a: object) -> None:
        """
        Сохранение в словарь
        """
        Db._dict[i] = a

class DisplayData:
    """
        Класс отвечает за вывод на экран содержимого БД
    """
    def display_type(self, obj: object) -> None:
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


class Lion(Animal):
    def __str__(self):
        return f"{__class__.__name__}:{self.name}"


def main():
    myDb = Db()
    dyTp = DisplayData()

    name = ['First', 'Second', 'Third', 'Fourth']
    for i in name:
        animal = Animal(i)
        myDb.save_animal(animal)
        myDb.save_animal_dict(str(i) + "-animal", animal)

    for i in range(4):
        fish = Fish(name[i])
        myDb.save_animal(fish)
        myDb.save_animal_dict(str(i) + "-fish", fish)

    for i in range(4):
        fish = Lion(name[i])
        myDb.save_animal(fish)
        myDb.save_animal_dict(str(i) + "-lion", fish)

    dyTp.display_type(myDb)



if __name__ == '__main__':
    main()

