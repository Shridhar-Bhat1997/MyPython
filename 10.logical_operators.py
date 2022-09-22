# logical operators --> and,or,not

temp=int(input("what is the temperature outside?: "))

if temp>=0 and temp<=30:
    print("temperature is good")
    print("go outside!")
    
elif temp<0 or temp>30:
    print("temperature is bad")
    print("stay inside!")
    
val = 5  # Truthiness value is `True`
print(not val)    
