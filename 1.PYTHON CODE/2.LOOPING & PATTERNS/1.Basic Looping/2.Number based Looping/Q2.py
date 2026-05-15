'''
Print the reverse of a given number.
'''

n = int(input("Enter n : "))
rev = 0
while n>0:
    digit = n%10
    rev = rev*10 + digit
    n//=10
    
print("Reverse of a given digit is",rev)