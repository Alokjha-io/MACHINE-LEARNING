'''
Convert a number to binary recursively. 
'''

n = int(input("Enter Number : "))
def tobinary(n):
    if n == 0:
        return ""
    return tobinary(n//2) + str(n%2)
print("Binary of a number is",tobinary(n))