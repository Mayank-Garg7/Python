# How to find a factorial of a entered number by user
num = int(input("Enter a number : "))
# formula of factorial of n is 
# n! = 1*2*3*........*n.


# Approach 1
# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial*i
# print("The factorial of "+str(num)+" is : "+str(factorial))


# Approach 2
# factorial = 1
# for i in range(num, 1, -1):
#     factorial = factorial*i
# print("The factorial of "+str(num)+" is : "+str(factorial))


# Approach 3
# find the factorial by using recursive function
# def rec_fact(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * rec_fact(n-1)
# a = int(input("Enter the number : "))
# print(rec_fact(a))
