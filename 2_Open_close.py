################################################################
##     Open-Closed Principle (Принцип открытости-закрытости)
##
##     Программные сущности (классы, модули, функции)
##     должны быть открыты для РАСШИРЕНИЯ,
##     но НЕ для МОДИФИКАЦИИ.
################################################################

class Animal:
    """
    Класс отвечает за инициализацию объекта "animal" с именем
    """
    def __init__(self, name: str):
        self.name = name

    def get_animal_name(self) -> str:
        return self.name

    def make_sound(self):
        """
        метод который нужно определить в дочерних классах
        """
        raise NotImplementedError

    def __str__(self):
        return f"{__class__.__name__}: {self.name}"


class Lion(Animal):
    def make_sound(self):
        return '< рычание льва! >'

class Mouse(Animal):
    def make_sound(self):
        return '< пищание мышки! >'

class Horse(Animal):
    def make_sound(self):
        return '< ржанье коня! >'

class Dog(Animal):
    def make_sound(self):
        return '< лай собаки! >'

class Cat(Animal):
    def make_sound(self):
        return '< мяуканье кошки! >'


class BD:
    lst_obj = []
    def add_obj_list(self, lst_obj_name):
        for i in lst_obj_name:
            self.lst_obj.append(i)

class Sound:
    def sound_lst(self, lst_obj):
        for i in lst_obj:
            print(i.make_sound())

def main():
    lst_obj_name = [Lion('lion'), Mouse('mouse'),
                    Horse('horse'), Dog('dog'),
                    Cat('cat')]
    bd = BD()
    animalsound = Sound()
    bd.add_obj_list(lst_obj_name)
    animalsound.sound_lst(bd.lst_obj)

if __name__ == '__main__':
    main()

