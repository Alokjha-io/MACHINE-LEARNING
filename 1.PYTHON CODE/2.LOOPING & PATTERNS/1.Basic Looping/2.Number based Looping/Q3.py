'''
Check if a number is a armstrong. 
'''

n = int(input("Enter n : "))
temp=n
sop=0
x = len(str(n))
while temp>0:
    digit = temp%10
    sop += digit**x
    temp//=10
if sop==n:
    print("This number is armstrong")
else:
    print("This number is not armstrong")
