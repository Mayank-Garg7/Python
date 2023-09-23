# Swap first and last element in a list
# input arr = [1,2,3,4]
# Output arr = [4,2,3,1]
arr = [7,5,8,3,9,2,0,6]
print(f"List without swapping {arr}\n")

# Approach 1    Using temp variable
# temp = arr[0]
# arr[0] = arr[len(arr) - 1]
# arr[len(arr) - 1] = temp
# print(f"List after Swapping is here : {arr}\n")


# Approach 2    Using indexing 
# arr[0],arr[-1] = arr[-1],arr[0]
# print(f"List after Swapping is here : {arr}\n")


# Approach 3    Using tuple 
# get = (arr[0],arr[-1])
# arr[-1],arr[0] = get
# print(f"List after Swapping is here : {arr}\n")


# Approach 4    * opetand
# start,*middle,end = arr
# arr = [end,*middle,start]
# print(f"List after Swapping is here : {arr}\n")


# Approach 5    Using pop() & insert()
# temp1 = arr.pop(0)
# temp2 = arr.pop(-1)
# arr.insert(0,temp2)
# arr.append(temp1)
# print(f"List after Swapping is here : {arr}\n")



