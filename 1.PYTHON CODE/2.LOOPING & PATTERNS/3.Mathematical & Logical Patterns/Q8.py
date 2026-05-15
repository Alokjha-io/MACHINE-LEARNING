'''
Check if a number is a strong number (sum of factorials of digits = number).
'''

n = int(input("Enter n : "))
original=n
sfd=0
while n>0:
    temp = n%10
    fact=1
    for j in range(1,temp+1):
        fact*=j
    sfd+=fact
    n//=10
if sfd==original:
    print("This Number is strong number")
else:
    print("This Number is not strong number")