'''
Check if two strings are the reverse of each other.
'''

str1 = input("Enter string one : ")
str2 = input("Enter string two : ")
if "".join(reversed(str1)) == str2:
    print("Two strings are the reversed of each other")
else:
    print("Two strings are the not reversed of each other")