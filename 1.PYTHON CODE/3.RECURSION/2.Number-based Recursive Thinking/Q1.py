'''
Count the number of digits in a number recursively. 
'''

n = int(input("Enter Number : "))

def number(n):
    count = 1
    if n==0:
        return 1
    return count + number(n//10) 
print(number(n)-1)
        