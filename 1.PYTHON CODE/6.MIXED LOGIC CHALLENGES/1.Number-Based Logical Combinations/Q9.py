'''
Check if a number is palindrome (121 → true). 
'''

n = int(input("Enter N : "))
temp = n
rev = 0
while n>0:
    digit = n%10
    rev = rev*10 + digit
    n//=10
print(rev==temp)

