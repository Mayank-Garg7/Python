# s = int(input("Enter the number : "))
# print("{0:.2f}".format(s/3))
# a = input().split()

list = [2,4,5,2,5,24,23,3]
print(list)
n = int(input("Enter the number : "))
count = 0
# for i in list:
#     if i == n:
#         count += 1

if n in list:
    count += 1
print(count)
