# tuples --> collection which is ordered and unchangeable..(immutable)

student=("john",25,"male")

print(student.count("male"))

print(student.index("john"))

#iterate over the tuple

for x in student:
    print(x)
    
if "john" in student:
    print("john is here!")
    
    