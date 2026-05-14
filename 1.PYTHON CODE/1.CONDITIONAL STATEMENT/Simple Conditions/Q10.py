'''
 Take a character and check whether it’s uppercase, lowercase, a digit, or a special 
 character. 
'''

x = input("Enter a character : ")
if x.isupper() :
    print("Enterd character is Uppercase")
elif x.islower():
    print("Enterd character is Lowercase")
elif x.isdigit():
    print("Enterd character is digit")
else:
    print("Enterd character is a special character")