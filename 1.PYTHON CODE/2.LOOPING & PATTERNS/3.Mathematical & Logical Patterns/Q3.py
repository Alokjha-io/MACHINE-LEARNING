'''
Print all numbers between a and b divisible by 7.
'''

a = int(input("Enter a : "))
b = int(input("Enter b : "))
for i in range(a,b):
    if i%7==0:
        print(i,"is divisible by 7")

