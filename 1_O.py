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
        return f"{__class__.__name__}: {self.name}"
