# exception --> events detected during execution that interrupt the flow of a program.

try:
    
    numerator=int(input("Enter a number to divide: "))
    denominator=int(input("Enter a number to divide by: "))
    result=numerator/denominator
    
except ZeroDivisionError:
    print("You can't divide by zero")
    
except ValueError as e: # this is standard practice
    print(e)
    print("Enter only numbers")
    
else:
    print(result)
    
finally:
    print("finally block always execute")
    