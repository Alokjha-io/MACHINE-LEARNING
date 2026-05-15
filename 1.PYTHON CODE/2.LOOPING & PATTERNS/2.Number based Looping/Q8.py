'''
Check if a number is prime or not.  
'''

n=int(input("Enter number : "))
temp=n
is_prime = True
for i in range(2,int(temp**0.5)+1):
    if temp%i==0:
        is_prime = False
        break
if is_prime:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
