'''
Find the sum of digits of a number.
'''

n = int(input("Enter n : "))
sum=0
while n>0:
    digit = n%10
    sum += digit
    n//=10
print("Sum of digit is" ,sum)