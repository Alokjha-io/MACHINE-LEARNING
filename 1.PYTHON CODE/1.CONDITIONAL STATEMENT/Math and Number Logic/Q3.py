'''
Check whether a given integer is single-digit, double-digit, or multi-digit.
'''

x = int(input("Enter a Integer : "))
if x<10:
    print("Single Digit")
if 10 <= x <= 99:
    print("Double Digit")
elif x>99:
    print("Multidigit Digit")