'''
Take two numbers and determine whether both are even, both are odd, or one is 
even and one is odd. 
'''

x = int(input("Enter a first number : "))
y = int(input("Enter a second number : "))
if x%2==0 and y%2==0:
    print("both are even")
if x%2!=0 and y%2!=0:
    print("Both are odd")
if (x%2==0 and y%2!=0) or (x%2!=0 and y%2==0):
    print("One number is even or one is odd")