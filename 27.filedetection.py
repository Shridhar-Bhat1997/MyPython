import os

path=r"C:\Users\Hp\OneDrive\Desktop\sample.txt" # file
path2=r"C:\Users\Hp\OneDrive\Desktop\Sample1"  # folder

if os.path.exists(path):
    print("The location exists!")
    if os.path.isfile(path): # file
        print("that is a file")
    elif os.path.isdir(path2): # directory
        print("that is a directory")
else:
    print("That location doesn't exist")
    
    
# The Python "SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes
#in position" occurs when we have an unescaped backslash character in a path.
#To solve the error, prefix the path with r to mark it as a raw string.