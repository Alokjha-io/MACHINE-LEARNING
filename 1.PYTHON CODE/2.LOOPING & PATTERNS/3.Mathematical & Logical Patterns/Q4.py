'''
Find HCF (GCD) of two numbers using loops.
'''

a = int(input("Enter a : "))
b = int(input("Enter b : "))
gcd=1
i=1
while i<=a and i<= b:
    if a%i==0 and b%i==0:
        gcd = i
    i+=1
print("Gcd is",gcd)
