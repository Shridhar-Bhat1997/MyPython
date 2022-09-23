import os

path="samplefile.txt"

try:
    os.remove(path)

except FileNotFoundError:
    print("That file was not found")
    
else:
    print(path + " was deleted")

