'''
Find product of digits of a number recursively. 
'''

n = int(input("Enter number : "))
def pod(n):
    if n==0:
        return 1
    return n%10 * pod(n//10)
print("Product of digits is",pod(n))


