#TRIANGLES USING NESTER WHILE LOOPS
#takes an input, converts it to int using the int() function
n = int(input("Enter height of the triangle: "))
i = 0
while i < n:
    j = 0
    while j <= i:
        #second argument 'end = ' specifies what the end character is. by default, it is '\n'
        print("*", end =' ')
        j = j+1
    #prints a new line
    print()
    i = i+1