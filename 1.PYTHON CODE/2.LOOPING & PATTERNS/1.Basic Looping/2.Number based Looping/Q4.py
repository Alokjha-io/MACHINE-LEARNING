'''
Check if a number is a palindrome. 
'''

n = int(input("Enter n : "))
rev = 0
while n>0:
    digit = n%10
    rev = rev*10 + digit
    n//=10
if rev==n:
    print("This number is palindrome")
else:
    print("This number is palindrome")