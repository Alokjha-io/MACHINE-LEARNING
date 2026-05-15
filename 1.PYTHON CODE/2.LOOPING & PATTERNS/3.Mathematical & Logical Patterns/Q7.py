'''
Find the sum of all factors of a number.
'''

n = int(input("Enter n : "))
sum=0
for i in range(1,n+1):
    if n%i==0:
        sum+=i
print("Sum of all factor of",n,"is",sum)