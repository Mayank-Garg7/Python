# String contain any special character or not
text = input("Enter the text : ")

# Approach 1
# import re # regular expression module
# regex = re.compile('[`~!@#$%^&*(_+={|\":;<>?/.,})]')
# if regex.search(text) == None:
#     print("No special character present in a string")
# else:
#     print("Special character is present in the string")


# Approach 2 
# temp = '[`~!@#$%^&*(_+={|\":;<>?/.,})]'
# flag = False
# for i in temp :
#     if i in text:
#         flag = True
# if flag == True:
#     print("Special character is present in the string")
# else:
#     print("Special character is not present in a string")



