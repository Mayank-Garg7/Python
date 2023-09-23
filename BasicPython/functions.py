# marks = [94,95,93,90]
# percentage = (sum(marks)/4)
# print("Your percentage is : ",percentage)

# def percent(marks):
#     return (sum(marks)/4)

# marks = [94,95,93,90]
# percentage = percent(marks)
# print("Your percentage is : ",percentage)

# def greet(name):
#     print("Good day",name)
# greet("mayank")

# Use open function to read the content the file !
# f = open("sample.txt","r") by default the mode of open function is read it means 'r'. 
# f = open("sample.txt") # for example. 
# data = f.read()
# data = f.read(20) for first 10 character from the file is read by the function.
# print(data)
# f.close()

# WE HAVE FOUR MODES FOR "OPEN FUNCTION"
#  UPDATE '+'
#  APPEND 'a'
#  READ   'r'
#  'rb' for open the file in binary mode for reading the content of file
#  'rt' for open the file in text mode for reading the content of file
#  WRITE  'w'


# a = open('sample.txt')
# data = a.readline()
# print(data)
# data = a.readline()
# print(data)
# a.close()  


# a = open('new_file.txt','w') # We can create a new file by using this line.
# a.write("  yeah, bro i am very good here.")  # You can write it multiple times.
# print(a)

# a = open('new_file.txt','a') #Appending new text into existing text file.
# a.write("  yeah, bro i am very good here.")
# print(a)

# with open('new_file.txt','r') as f:
#     a = f.read()
# with open('new_file.txt','w') as f:
#     a = f.write("hello dude")
# print(a)


with open('Ooops/Ooops.py','w') as f:
    a = f.write("a = 7\nb=5\nprint(a+b)")


