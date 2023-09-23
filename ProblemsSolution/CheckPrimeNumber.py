# Check the number is prime or not
# Prime number is which has only 2 factors 1 and itself
# For example = 11 has only two factors 1 & 11(itself) it is prime no.
# and 16 has many factors such as 1,2,4,8 & 16 so it is not a prime number
num = int(input("Enter a number : "))

# Approach 1
# count = 0
# for i in range(2, num):
#     if num % i == 0:
#         count = count+1
# if count == 0:
#     print(str(num) + " is a Prime Number.")
# else:
#     print(str(num) + " is Not a Prime Number.")

# Approach 2
# prime = True
# for i in range(2, num):
#     if(num%i == 0):
#         prime = False
# if prime:
#     print(str(num) + " is a Prime Number.")
# else:
#     print(str(num) + " is Not a Prime Number.")
