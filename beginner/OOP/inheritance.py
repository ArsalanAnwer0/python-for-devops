
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"This {self.name} can eat")
    def sleep(self):
        print(f"This {self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit("Bugs")
rabbit.flee()

hawk = Hawk("Hello")
hawk.hunt()

fish = Fish("Nemo")
fish.flee()
fish.hunt()

rabbit.eat()