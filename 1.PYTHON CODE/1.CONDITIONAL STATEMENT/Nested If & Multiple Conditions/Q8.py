'''
Take an alphabet character and check if it lies between ‘a’ and ‘m’ or ‘n’ and ‘z’. 
'''

ch = input("Enter a character : ").lower()

if 'a' <= ch <= 'm':
    print("Between a and m")
elif 'n' <= ch <= 'z':
    print("Between n and z")
else:
    print("Invalid input")
