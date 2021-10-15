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
        return f"Animal:{self.name}"

class AnimalDb:
    """
    Класс отвечает за сохранение объекта "animal" в БД animal_safe
    """
    animal_safe = []
    animal_dict = {}

    def save_animal(self, a: object) -> None:
        AnimalDb.animal_safe.append(a)

    def save_animal_dict(self, i: int, a: object) -> None:
        AnimalDb.animal_dict[i] = a

# Press the green button in the gutter to run the script.

def display_type(obj: object) -> None:
    for an in enumerate(obj.animal_safe):
        print(an[0], '.', an[1])

    print("-*-" * 18)

    for k, v in obj.animal_dict.items():
        print(k, ".", v)


def main():
    anDb = AnimalDb()

    name = ['a1', 'b2', 'c3', 'd4']
    for i in range(4):
        animal = Animal(name[i])
        anDb.save_animal(animal)
        anDb.save_animal_dict(i, animal)

    display_type(anDb)


if __name__ == '__main__':
    main()

