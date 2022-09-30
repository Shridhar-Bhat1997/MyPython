# multiple inheritance --> when a child class is derived from more that one parent class.

class Prey:
    def flee(self):
        print("This animal flees")
        
class Predator:
    def hunt(self):
        print("This animal is hunting")
        
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

# creating objects

rabbit=Rabbit()
hawk=Hawk()
fish=Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
