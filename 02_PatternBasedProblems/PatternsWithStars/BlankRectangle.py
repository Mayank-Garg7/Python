# *****Blank Rectangle by star
a = int(input("Enter the number of rows : "))


# Approach 1
# for i in range(a):
#     for j in range(a):
#         if i == 0 or i == a-1 or j == 0 or j == a-1:
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print("")


# Approach 2
# for i in range(a):
#     print(" * ", end = "")
#     if (i == 0 or i == a-1):
#         print(" * " * (a-2), end = "")
#     else:
#         print("   " * (a-2), end = "")
#     print(" * ")

