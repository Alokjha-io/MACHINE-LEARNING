'''
Print factorial of a number recursively.
'''

n = int(input("Enter n : "))
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print("Factorial of given number is",fact(n))