'''
Check if a number is perfect (sum of factors equals number).
'''

n = int(input("Enter a number : "))
sum = 0
temp = n
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum == temp:
    print("Number is a perfect number")
else:
    print("Number is not a perfect number")
    


