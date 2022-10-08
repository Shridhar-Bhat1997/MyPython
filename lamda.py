# lambda function --> function written in one line using lamda keyword
# it accepts any number of arguments but only has one expression.

# lambda parameter:expression

def double(x):
    return x*2

print(double(5))

# in lambda 
double2=lambda y:y*5
print(double2(4))

multiply=lambda x,y: x * y
print(multiply(6,7))

add=lambda x,y,z:x+y+z
print(add(5,6,7))

full_name=lambda first_name,last_name:first_name+" "+last_name
print(full_name("bro","code"))

age_check=lambda age:True if age>18 else False
print(age_check(20))