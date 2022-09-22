# return statement --> functions send python values/objects back to the caller.
                   # these values/objects are known as the function's return value.
                   
def multiply(number1,number2):
    result=number1 * number2
    return result

x=multiply(7,9)
print(x)

def add(number1,number2):
    return number1+number2

y=add(3,4)
print(y)