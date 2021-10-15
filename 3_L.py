###############################################################################
# Liskov Substitution Principle(Принцип подстановки Барбары Лисков).
#
#  Необходимо, чтобы подклассы могли бы служить заменой для своих суперклассов.
#
#  Цель этого принципа заключаются в том, чтобы классы-наследники могли бы
#  использоваться вместо родительских классов, от которых они образованы,
#  не нарушая работу программы.
#  Если оказывается, что в коде проверяется тип класса,
#  значит принцип подстановки нарушается.
################################################################################



class Animal:
    """
    Класс отвечает за инициализацию объекта "animal" с именем
    """
    def __init__(self, name, age):
        self.attributes = {"name": name, "age": age}

    def eat(self):
        print('Ate some food!')

    def __str__(self):
        return f'{__class__.__name__}: {self.attributes}'

class Cat(Animal):
    def __init__(self, name, age):
        super(Cat, self).__init__(name, age)
    def eat(self, _amount=0.1):
        if _amount > 0.3:
            print("Can`t eat that much!")
        else:
            print('Ate some cat food!')

class Dog(Animal):
    def __init__(self, name, age):
        super(Dog, self).__init__(name, age)
    def eat(self, _amount=0):
        print('Ate some dog food!')


if __name__ == '__main__':
    pluto = Dog('Pluto',  3)
    goofy = Dog('Goofy', 2)
    buttons = Cat('Mr.Buttons', 4)
    animals = (pluto, goofy, buttons)

    for animal in animals:
        if animal.attributes['age'] > 2:
            print(animal.attributes['name'])

