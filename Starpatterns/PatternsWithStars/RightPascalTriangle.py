# *****Right pascal's Triangle by star
n = int(input("Enter the number of rows : "))



for i in range(n-1):
    for j in range(i,n):
        print("  ",end = "")
    for k in range(i+1):
        print("*",end=" ")
    print("")
for i in range(n):
    for k in range(i+1):
        print("  ",end="")
    for j in range(i,n):
        print("*",end =" ")
    print("")