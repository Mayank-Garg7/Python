a = int(input("Enter the number : "))

# ********Reverse triangle
# for i in range(a):
#     count = 1
#     for j in range(i+1, a+1):
#         print(count, end=" ")
#         count = count +1
#     print()


# ********left sided triangle
# for i in range(a):
#     count = 1
#     for j in range(i+1):
#         print(count, end=" ")
#         count = count +1
#     print()



# ********left sided based on numbers (1-1,2-2-2,3-3-3-3 and more) increasing triangle
# # Approach 1
# for i in range(a):
#     for j in range(i+1):
#         print(i+1, end=" ")
#     print()

# # Approach 2
# p = 1
# for i in range(a):
#     for j in range(i+1):
#         print(p, end=" ")
#     p += 1
#     print()



# ********Increasing triangle with starting number same
# for i in range(a):
#     count = 5
#     for j in range(i+1):
#         print(count, end=" ")
#         count = count -1
#     print()



# ********Increasing triangle with starting number same
# count = 1
# for i in range(a):
#     for j in range(i+1):
#         print(count, end=" ")
#         count = count +1
#     print()


# ********Reverse Right Decreasing triangle with ending number same
# Approach 1
# for i in range(a):
#     p = a-i
#     for k in range(i+1):
#         print("  ",end="")
#     for j in range(i,a):
#         print(p ,end =" ")
#         p -= 1
#     print()


# Approach 2
# for i in range(a):
#     p = a-i
#     for k in range(i+1):
#         print("  ",end="")
#     for j in range(i,a):
#         print(p ,end =" ")
#         p -= 1
#     print()




# ********left sided based on numbers 1(-1,2-2-2,3-3-3-3 and more) decreasing triangle
# # Approach 1
# for i in range(a):
#     for j in range(i+1):
#         print(a-i, end=" ")
#     print()

# # Approach 2
# p = a
# for i in range(a):
#     for j in range(i+1):
#         print(p, end=" ")
#     p -= 1
#     print()


# ********increasing triangle with even numbers
# # Approach 1
# p = 0
# for i in range(a):
#     for j in range(i+1):
#         if p%2 == 0:
#             print("1", end=" ")
#         else:
#             print("2", end=" ")
#     p += 1
#     print()


# ********decreasing triangle with special numbers
# p = 0
# for i in range(a):
#     for k in range(i+1):
#         print("  ",end="")
#     if p%2 == 0:
#         for j in range(i,a):
#             print("#",end =" ")
#     else:
#         for j in range(i,a):
#             print("$",end =" ")
#     p += 1
#     print()


# ********hill pattern  with a & b 
# p = 0
# for i in range(a):
#     for j in range(i+1,a):
#         print("  ",end = "")
#     if p%2 == 0:
#         for k in range(i):
#             print("a",end=" ")
#         for j in range(i+1):
#             print("a",end = " ")
#     else:
#         for k in range(i):
#             print("b",end=" ")
#         for j in range(i+1):
#             print("b",end = " ")
#     p = p+1
#     print("")



# ********hill pattern  increasing and decreasing numbers ()
# for i in range(a):
#     p = 1
#     for j in range(i+1,a):
#         print("  ",end = "")
#     for k in range(i):
#         print(p ,end=" ")
#         p = p+1
#     for j in range(i+1):
#         print(p ,end = " ")
#         p = p-1
#     print("")




# *****Diamond pattern by star continue/increasing numbers
# p = 1
# for i in range(a-1):
#     for j in range(i,a):
#         print("  ",end = "")
#     for k in range(i):
#         print(p,end=" ")
#     for k in range(i+1):
#         print(p,end=" ")
#     p = p+1
#     print("")
# for i in range(a):
#     for k in range(i+1):
#         print("  ",end="")
#     for j in range(i+1,a):
#         print(p,end =" ")
#     for j in range(i,a):
#         print(p,end =" ")
#     p = p+1
#     print("")



# *****Diamond pattern by star decreasing numbers
# p = 1
# for i in range(a-1):
#     for j in range(i,a):
#         print("  ",end = "")
#     for k in range(i):
#         print(p,end=" ")
#     for k in range(i+1):
#         print(p,end=" ")
#     p = p+1
#     print("")
# for i in range(a):
#     for k in range(i+1):
#         print("  ",end="")
#     for j in range(i+1,a):
#         print(p,end =" ")
#     for j in range(i,a):
#         print(p,end =" ")
#     p = p-1
#     print("")

    
# ********hill pattern  increasing number according to row
# p = 0
# for i in range(a):
#     for j in range(i+1,a):
#         print("  ",end = "")
#     for k in range(i):
#         print(p ,end=" ")
#     for j in range(i+1):
#         print(p ,end = " ")
#     p = p+1
#     print("")




# ********hill pattern  increasing number according to column
# for i in range(a):
#     p = 1
#     for j in range(i+1,a):
#         print("  ",end = "")
#     for k in range(i):
#         print(p ,end=" ")
#         p = p+1
#     for j in range(i+1):
#         print(p,end = " ") 
#         p = p+1
#     print("")













