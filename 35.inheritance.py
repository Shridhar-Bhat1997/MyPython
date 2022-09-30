class Animal: # Parent class attributes & methods
    alive=True
    
    def eat(self):
        print("This animal is eating")
        
    def sleep(self):
        print("This animal is sleeping")
        
# Inheritance

class Rabbit(Animal): # Rabbit-->child & Animal-->Parent class
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")   # child class attributes & methods

class Snake(Animal):
    def move(self):
        print("This snake is moving")

rabbit=Rabbit()
fish=Fish()
snake=Snake()

#print(rabbit.alive)
#print(fish.sleep())
#print(snake.eat())

rabbit.run()
fish.swim()
snake.move()
    