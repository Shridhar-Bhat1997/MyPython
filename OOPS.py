from car import Car

car_1=Car("Chevy","Corvette",2021,"blue") # object1
car_2=Car("Ford","Mustang",2022,"black") # object2

car_1.wheels=2

print("----------------Car1----------")
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

print("------------------Car2--------------------")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()

print(car_1.wheels) # class variable
print(Car.wheels)