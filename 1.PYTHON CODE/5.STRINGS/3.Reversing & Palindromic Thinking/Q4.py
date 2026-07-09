'''
Check whether a string is a palindrome. 
'''

x = input("Enter string : ")
rev_x = "".join(reversed(x))
if x == rev_x:
    print("String is a palindrome")
else:
    print("String is not palindrome")