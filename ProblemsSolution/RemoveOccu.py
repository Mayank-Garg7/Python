# How to remove the word which is occur more than one time from a list
# input arr = ["hello","Harsh","Is","Harsh"]
# Output = ["Hello","Harsh","Is"]
arr = ["hello","I","am","here","hello","hello","hello"]
print(arr)
# word = input("Enter the word which is repeated more than one time : ")
# n = int(input("Enter the number of occurance of word : "))
word = "hello"
n = 2
count = 0
for i in range(0, len(arr)-1):
    if(arr[i] == word):
        count = count+1
        if(count == n):
            del arr[i]
print(f"List after deleting the multiple word instead of one : {arr}")
