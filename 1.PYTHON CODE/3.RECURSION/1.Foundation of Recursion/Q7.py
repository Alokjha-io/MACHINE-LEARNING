'''
Calculate power of a number (xⁿ) using recursion.
'''

x = int(input("Enter number : "))
n = int(input("Enter power : "))
def number(n):
    if n == 0:
        return 1
    return x*number(n-1)
print(number(n))