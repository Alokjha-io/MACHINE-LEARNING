'''
Find the sum of digits of a number. 
'''

n = int(input("Enter an Number : "))
def sum(n):
    if n==0:
        return 0
    return n%10 + sum(n//10)
print("Sum of digit is",sum(n))