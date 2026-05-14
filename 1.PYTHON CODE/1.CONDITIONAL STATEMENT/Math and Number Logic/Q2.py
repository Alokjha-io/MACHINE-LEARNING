'''
Take a 3-digit number and determine if the middle digit is the largest, smallest, or 
neither.
'''

x = input("Enter three digit Number : ")
if x[1]>x[0] and x[1]>x[2]:
    print("Middle digit is largest")
elif x[1]<x[0] and x[1]<x[2]:
    print("Middle digit is Smallest")
else:
    print("Middle digit is niether larger nor Smaller")
