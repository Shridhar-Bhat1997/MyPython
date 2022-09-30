class Animal: # parent class
    alive=True
    
    def eat(self):
        print("This animal is eating")
        
    def sleep(self):
        print("This animal is sleeping")
        

class Rabbit(Animal):           # child classes
    def run(self):
        print("This rabbit is running")
        
class Eagle(Animal):
    def fly(self):
        print("This eagle is flying")
        
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
        
rabbit=Rabbit()
eagle=Eagle()
fish=Fish()

rabbit.run()
eagle.fly()
fish.swim()