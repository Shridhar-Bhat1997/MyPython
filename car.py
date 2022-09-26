class Car:
    
    def __init__(self,make,model,year,color): # construct objects for us
        self.make=make   # self refers to current object
        self.model=model # attributes
        self.year=year
        self.color=color
        
    def drive(self):  # methods
        print("This car is driving")
        
    def stop(self):
        print("This "+self.model+" is stopped")