# Variable --> a container for a value.

# Datatype --> strings
name= "Dravid"
print(name);
print("Hello " + name) # combining strings
print(type(name))  # type() tells datatype of variable

# String concatenation
first_name="Rahul"
last_name="Dravid"
full_name=first_name + " " + last_name # to add space between strings
print(full_name)

# Datatype --> int
age=27
age=age+1 # to increase age by 1
print(age)
print(type(age))

# TypeError: can only concatenate str(not "int") to str
#print("hello : "+age)

# typecasting can solve this kind of errors
print("Your age is : "+ str(age))

# Datatype --> float
height=240.5
print(height)
print(type(height))
print("Your height is :"+ str(height))

#Datatype --> boolean

human=True
print("Are you a human :" +str(human))
print(type(human))


