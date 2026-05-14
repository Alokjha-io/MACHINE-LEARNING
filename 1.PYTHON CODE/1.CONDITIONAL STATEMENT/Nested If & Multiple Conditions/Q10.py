'''
 Take a month number (1–12) and print the number of days in that month (ignore leap 
years).
'''

ND = ["31","28","31","30","31","30","31","31","30","31","30","31"]
M = int(input("Enter a month number : "))
if 1 <= M <=12:
    print("Number of days",ND[M-1])
else:
    print("Invalid Input")