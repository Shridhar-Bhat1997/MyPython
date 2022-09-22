# nested loops --> the "inner loop" will finish all of it's iteration before finishing
                 # one iteration of "outer loop".
                 
rows=int(input("How many rows?: "))
columns=int(input("How many columns?: "))
symbol=input("Enter a symbol to use: ")

for i in range(rows): # outer loop
    for j in range(columns): # inner loop
        print(symbol,end="")
    print()
    
# since print() automatically inserts a newline after each execution.
# we can use end to skip insertion of an automatic newline.
