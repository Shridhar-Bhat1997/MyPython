# scope--> The region that a variable is recognized...
# A local & global scoped versions of a variable can be created...

name="John" # global scope(available inside & outside functions)

def display_name():
    name="Cena" # local scope(available only inside the functions)
    print(name)
    
    
display_name()

print(name)