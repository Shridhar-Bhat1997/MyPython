# filter() --> creates a collection of elements from an iterable for which a function
#              returns true.

# filter(function,iterable)

friends=[("jitu",23),
         ("monica",55),
         ("nitya",43),
         ("joel",56),
         ("joy",12),
         ("suhan",10)]

age=lambda data:data[1] >=18

drinking_buddies=list(filter(age,friends))

for i in drinking_buddies:
    print(i)
    
    