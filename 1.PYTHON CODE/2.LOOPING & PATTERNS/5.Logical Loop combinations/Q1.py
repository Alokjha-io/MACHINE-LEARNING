'''
Print all numbers whose sum of digits is even (1–100). 
'''

for i in range(1,101):
    sod = 0
    n=i
    while n>0:
        digit = n%10
        sod+=digit
        n//=10
    if sod%2==0:
        print(i)
