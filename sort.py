# sort() method=used with lists
# sort() method=used with literables

students=["ganesh","vighnesh","mahesh","yogesh"]

students.sort(reverse=True) # descending order

for i in students:
    print(i)
    
    
students2=[("shri",60,"A"),("sandy",56,"C"),("sir",67,"B")] 
age=lambda age:age[1] # sorting based on age
students2.sort(key=age)

for i in students2:
    print(i)
    
