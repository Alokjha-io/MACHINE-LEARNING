'''
Print the reverse of a number (123 → 321). 
'''

n = int(input("Enter N : "))
rev = 0
while n>0:
    digit = n%10
    rev = rev*10 + digit
    n//=10
print(rev)
    
