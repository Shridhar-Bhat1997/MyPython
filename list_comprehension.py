# list comprehension--> a way to create a new list with less syntax...
# list=[expression for item in iterable]

squares=[]  # create an empty list
for i in range(1,11): # create a for loop
    squares.append(i*i) # define what each loop iteration should do
print(squares)


square=[i*i for i in range(1,11)]
print(square)

students=[100,56,34,90,89,76]

passed_students=[i if i>=60 else "Failed" for i in students]

print(passed_students)
