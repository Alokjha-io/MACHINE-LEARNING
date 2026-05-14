'''
Take day and month and check if it forms a valid calendar date (ignoring leap years). 
'''

d = int(input("Enter date (0-31) : "))
m = int(input("Enter month(0-12) : "))
ND = [31,28,31,30,31,30,31,31,30,31,30,31]
if 1 <= m >=12 and 1 <= d == ND[m-1]:
    print("valid calender date")
else:
    print("Invalid date")