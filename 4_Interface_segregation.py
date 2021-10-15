##################################################################################
#   Interface Segregation Principle (Принцип разделения интерфейса).
#
#
##################################################################################

class Creature:
    def __init__(self, name):
        self.name = name

class SwimerInterface:
    def swim(self):
        print(f"Если у кота не реализован метод плавания, то будет взят из интерфейса")

class WalkerInterface:
    def walk(self):
        pass

class TalkerInterface:
    def talk(self):
        pass

class Human(Creature, SwimerInterface, WalkerInterface, TalkerInterface):
    def __init__(self, name):
        super(Human, self).__init__(name)

    def swim(self):
        print(f'I am {self.name} and I can swim!')

    def walk(self):
        print(f'I am {self.name} and I can walk!')

    def talk(self):
        print(f'I am {self.name} and i can talk!')

class Fish(Creature, SwimerInterface):
    def __init__(self, name):
        super(Fish, self).__init__(name)

    def swim(self):
        print(f'I am {self.name} and I can swim!')

class Cat(Creature, SwimerInterface, WalkerInterface):
    def __init__(self, name):
        super(Cat, self).__init__(name)


    def walk(self):
        print(f'I am {self.name} and I can walk!')

if __name__ == '__main__':
    human = Human('person')
    human.swim()
    human.walk()
    human.talk()

    fish = Fish('fishka')
    fish.swim()

    cat = Cat('Barsik')
    cat.swim()
    cat.walk()

