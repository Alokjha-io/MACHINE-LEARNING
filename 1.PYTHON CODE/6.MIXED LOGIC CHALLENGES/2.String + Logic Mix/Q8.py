'''
Check if two strings are rotations of each other. 
'''

str1 = input("Enter String : ")
str2 = input("Enter another String : ")
str3 = str1 + str1
if str2 in str3:
    print("They are rotation of each other")
else:
    print("They are not the rotation of ecah other")

