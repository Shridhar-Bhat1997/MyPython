# conditional statements in Python

age=int(input("How old are you?: "))

if age==100:
    print("You are a century years old")
elif age>=18:
    print("You are an adult")
elif age<0:
    print("You haven't born yet")
else:
    print("you are a child")