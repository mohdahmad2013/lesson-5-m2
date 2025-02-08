print("There is gonna be a pattern")
rows=int(input("Enter the number of rows "))
for i in range (rows):
    for i in range (i+1):
        print("$*",end="")
    print("")