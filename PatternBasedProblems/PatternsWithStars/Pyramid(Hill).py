# *****Hill(pyramid) pattern by star
n = int(input("Enter the number of rows : "))


# Approach 1
# for i in range(n):
#     for j in range(i,n):
#         print("  ",end = "")
#     for k in range(i):
#         print("*",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print("")