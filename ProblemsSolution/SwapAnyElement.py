# How to Swap any Two Element in the List
# arr = [8,4,0,9,2,1,6,3,5]
arr = [1,2,3,4,5,6,7,8,9,0]
print(f"{arr}\nCounting of the elements in a list is always start with '0'")
i = int(input("Enter the first index number for swapping : "))
j = int(input("Enter the second index number for swapping : "))

# Approach 1    Using temp variable
# temp = arr[i]
# arr[i] = arr[j]
# arr[j] = temp
# print(f"List after Swapping is here : {arr}\n")


# Approach 2    Using indexing 
# arr[i],arr[j] = arr[j],arr[i]
# print(f"List after Swapping is here : {arr}\n")


# Approach 3    Using tuple 
# get = (arr[i],arr[j])
# arr[j],arr[i] = get
# print(f"List after Swapping is here : {arr}\n")


# Approach 4    Using pop() & insert()
# temp1 = arr.pop(i)
# temp2 = arr.pop(j-1)
# arr.insert(i,temp2)
# arr.insert(j,temp1)
# print(f"List after Swapping is here : {arr}\n")


