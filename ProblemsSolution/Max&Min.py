# Find the Maximum and the Minimum elements in the array
# input arr = [2,5,7,3,4,37,8,9,34,62]
# Output = 62 & 2
arr = [2,5,7,3,4,37,8,9,34]
print(arr)

# Approach 1 Using for loop
# Finding the maximum value
# max = arr[0]
# for i in range(1,len(arr)):
#     if arr[i] > max:
#         max = arr[i]
# print(f"Maximum value is : {max}")

# # Finding the minimum value
# min = arr[0]
# for i in range(1,len(arr)):
#     if arr[i] < min:
#         max = arr[i]
# print(f"Minimum value is : {min}")



# Approach 2 Using sort method
# temp = sorted(arr)
# print(f"Maximum value is : {temp[-1]}\nMinimum value is : {temp[0]}")


# Approach 3 Using max and min method
# print(f"Maximum value is : {max(arr)}")
# print(f"Minimum value is : {min(arr)}")
