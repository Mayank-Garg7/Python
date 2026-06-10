# *****Decreasing Triangle by star
n = int(input("Enter the number of rows : "))


# Approach 1
# for i in range(n,0,-1):
#     print(i*"* ")


# Approach 2
# for i in range(n):
#     for j in range(0,n-i):
#         print("*",end = " ")
#     print("")



# Approach 3
# for i in range(n):
#     for j in range(i,n):
#         print("*",end = " ")
#     print("")