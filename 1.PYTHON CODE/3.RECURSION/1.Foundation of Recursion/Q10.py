'''
Find sum of digits of a number recursively. 
'''

n = int(input("Enter Number : "))
def number(n):
    if n == 0:
        return 0
    else:
        return n%10 + number(n//10)
print("Sum of digit is",number(n))