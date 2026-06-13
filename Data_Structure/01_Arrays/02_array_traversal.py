arr = [10, 20, 30, 40, 50]

# Method 1

for item in arr:
    print(item)

# Method 2

for i in range(len(arr)):
    print(arr[i])

# Method 3

for index, value in enumerate(arr):
    print(index, value)