'''
Take a character and check if it is a letter, a digit, or neither.
'''

ch = input("Enter a charcter : ")
if ch.isalpha():
    print("This is a letter")
elif ch.isdigit():
    print("This is a digit")
else:
    print("Neither a number nor a digit")