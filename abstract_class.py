# prevents a user from creating an object of that class.
# compels the user to override abstract methods in a child class.

# abstract class-->a class which contains one or more abstract methods.
# abstract method--> a method that has a declaration but does not have an implementation.

class Vehicle:
    
    def go(self):
        pass
    
class Car(Vehicle):
    
    def go(self):
        print("you drive the car")
        
class Motorcycle(Vehicle):
    
    def go(self):
        print("You ride the motorcycle")
        
vehicle=Vehicle()
car=Car()
motorcycle=Motorcycle()

vehicle.go()
car.go()
motorcycle.go()