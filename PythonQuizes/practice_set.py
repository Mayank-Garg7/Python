# PROBLEM NUMBER 1ST make the list by the entered values and print it
# f1 = input("Enter fruit name ")
# f2 = input("Enter fruit name ")
# f3 = input("Enter fruit name ")
# f4 = input("Enter fruit name ")
# f5 = input("Enter fruit name ")
# f6 = input("Enter fruit name ")
# f7 = input("Enter fruit name ")

# li = [f1,f2,f3,f4,f5,f6,f7]
# print(li)


# PROBLEM NUMBER 2ND Make the list from the entered value and sort it
# m1 = int(input("Enter the number of a student : "))
# m2 = int(input("Enter the number of a student : "))
# m3 = int(input("Enter the number of a student : "))
# m4 = int(input("Enter the number of a student : "))
# m5 = int(input("Enter the number of a student : "))
# m6 = int(input("Enter the number of a student : "))
# lis = [m1,m2,m3,m4,m5,m6]
# lis.sort()
# print(lis)



# PROBLEM NUMBER 3RD  print the value of list by using index number
# tp = (5,564,3,235,6)
# tp[2] = 54
# print(tp)



# PROBLEM NUMBER 4TH print the sum of all the values of list
# a = [3,5,6,2]
# print(a[0]+a[1]+a[2]+a[3])
# print(sum(a))


# PROBLEM NUMBER 5TH count the number of value of a tuple
# tup = (7,0,8,0,0,9)
# print(tup.count(0))



# PROBLEM NUMBER 6TH print the value from the dictionary by key
# dic = {
#     "post" : "pindrai",
#     "distric" : "Katni",
#     "state" : "katni",
#     "country" : "India"
# }
# print(dic.keys())
# a = input("Enter Your Choice : ")
# print(dic.get(a))



# PROBLEM NUMBER 7TH Store the unique value from the enterd values
# a = int(input("Enter the value in integer : "))
# b = int(input("Enter the value in integer : "))
# c = int(input("Enter the value in integer : "))
# d = int(input("Enter the value in integer : "))
# e = int(input("Enter the value in integer : "))
# f = int(input("Enter the value in integer : "))
# g = int(input("Enter the value in integer : "))
# h = int(input("Enter the value in integer : "))
# i = int(input("Enter the value in integer : "))
# st = {a,b,c,d,e,f,g,h,i}
# print(st)



# PROBLEM NUMBER 8TH  find greatest number from the four entered number
# list  = input("Enter any four number : ")
# if list[0]>list[1]:
#     f1 = list[0]
# else:
#     f1 = list[1]
# if list[2]>list[3]:
#     f2 = list[2]
# else: 
#     f2 = list[3]
# if f1>f2:
#     print("f1 is greatest number : ",f1)
# else:
#     print("f2 is greatest number : ",f2)



# PROBLEM NUMBER 9TH check percentage and decide you are fail or pass
# mark1 = int(input("Enter the marks of your 1st subject : "))
# mark2 = int(input("Enter the marks of your 2nd subject : "))
# mark3 = int(input("Enter the marks of your 3rd subject : "))
# if mark1<33 or mark2<33 or mark3<33 :
#     print("You are fail because your marks of a subject is less than 33%")
# elif (mark1+mark2+mark3)/3 > 40:
#     print("You are pass ")
# else:
#     print("You are fail because your total marks is less than 40%")



# PROBLEM NUMBER 10TH check the entered text is spam or not
# text = input("Enter the text for Scanning : ")
# if "danger" in text or "harm" in text or "crucail" in text:
#     print("Your file is spam.")
# else:
#     print("This text is not a spam.")



# PROBLEM NUMBER 11TH check the string is containing less than 10 char or not
# tx = input("Enter a text : ")
# if len(tx) >= 10 :
#     print("text is containing more than 10 character")
# else:
#     print("text is not containig 10 characters")



# PROBLEM NUMBER 12TH check your name is in list or not
# lis = ["harsh","shubhi","harshita"]
# number = input("Enter Your Name : ")
# if number in lis :
#     print("True")
# else:
#     print("False")



# PROBLEM NUMBER 13TH check which grade you are belongs to
# mark = int(input("Enter your marks : "))
# if mark>90:
#     print("Your Grade is EX")
# elif mark>80:
#     print("Your Grade is A")
# elif mark>70:
#     print("Your Grade is B")
# elif mark > 60:
#     print("Your Grade is C")
# elif mark > 50:
#     print("Your Grade is D")
# else:
#     print("Your Grade is F")



# PROBLEM NUMBER 14TH check the entered text is harsh or not in any way
# text = input("enter the value : ")
# if "HARSH" in text :
#     print("true")
# elif "Harsh" in text:
#     print("True")
# elif "haRsh" in text :
#     print("True")
# elif "harsH" in text:
#     print("True")
# else:
#     print("False")



# PROBLEM NUMBER 15TH print the value of list by using for and while loop both
# lis = [5,4,6,7,8,9,3,0,2,1]
# for i in range(0,10):
#     print(lis[i])


# i = 0
# while(i<=9):
#     print(lis[i])
#     i += 1



# PROBLEM NUMBER 16TH Two way to print table for given number
# num = int(input("Enter the number for finding table : "))
# for i in range(0,11): 
#     print(str(num) + " X " + str(i) + " = " + str(i*num))
#     print(f"{num} X {i} = {i*num}")



# PROBLEM NUMBER 17TH find the names who's are start with s character
# li = {"harshit","shubhi", "sohan","mayank"}
# for name in li:
#     if name.startswith("s"):
#         print("hello "+name)


# PROBLEM NUMBER 18TH Check the entered number is prime or not
# num = int(input("Enter a number : "))
# prime = True
# for i in range(2, num):
#     if(num%i == 0):
#         prime = False
# if prime:
#     print("number is prime")
# else:
#     print("number is not prime")


# PROBLEM NUMBER 19TH 1-10 count by while loop
# a = 0
# i = 0
# while i<=10:
#     a += i
#     i+=1
# print(a)


# PROBLEM NUMBER 20TH Factorial of a given number
# a = int(input("Enter the number : "))
# fact = 1
# for i in range(a,1,-1):
#     fact *= i
# print("factorial of given number is : ",fact)
# fact = 1
# for i in range(1, a+1):
#     fact = fact*i
# print(fact)



# PROBLEM NUMBER 21TH Right angle triangle by stars
# a = int(input("enter the numbers : "))
# for i in range(1,a+1):
#     print(i*" * ")



# PROBLEM NUMBER 22TH perfect Triangular star shape 
# a = int(input("enter the value : "))
# for i in range(a):
    # print(" " * (a-i-1), end="")
    # print("*" * (2*i+1), end="")
    # print(" " * (a-i-1))
    


# PROBLEM NUMBER 23TH Star box with black center
# a = int(input("enter the value : "))
# for i in range(a):
#     print(" * ", end = "")
#     if (i == 0 or i == a-1):
#         print(" * " * (a-2), end = "")
#     else:
#         print("   " * (a-2), end = "")
#     print(" * ")



# PROBLEM NUMBER 24TH Multiplication table of the given number
# a = int(input("enter the value : "))
# for i in range(10,0,-1):
#     print(f"{a} X {i} = {a*i}")


