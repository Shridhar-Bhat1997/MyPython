# Python loop control statements

# break= used to terminate the loop entirely.
# continue= skips to the next iteration of the loop.
# pass= does nothing, acts as a placeholder.

while True:
    name=input("enter your address: ")
    if name!="":
        break
    
phone_number="234-678-23"
for i in phone_number:
    if i=="-":
        continue
    print(i,end="")
    
for i in range(1,20):
    if i==13:
        pass
    else:
        print(i)
