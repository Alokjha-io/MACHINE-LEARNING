'''
Check if a number is a perfect number.
'''

n = int(input("Enter n : "))
sum=0
i=1
while i<=n/2:
    if n%i==0:
        sum+=i
    i+=1
if sum == n and n !=0:
    print(n,"is perfect Number")
else:
    print(n,"is not perfect Number")