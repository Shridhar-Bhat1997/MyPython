# read a file in python

try:
    with open("test.txt") as file:# this will close file automatically
        
        print(file.read())

except FileNotFoundError:
    print("That file was not found")