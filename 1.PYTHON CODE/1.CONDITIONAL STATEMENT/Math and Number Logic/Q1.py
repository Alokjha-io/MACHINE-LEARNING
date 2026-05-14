'''
 Take a 3-digit number and check if all digits are distinct.
'''

x = input("Enter three digit Number : ")
if x[0]==x[1] or x[1]==x[2] or x[2]==x[0]:
    print("All digits are not distinct")
else:
    print("All digits are distinct")