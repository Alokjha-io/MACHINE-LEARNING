'''
Take three numbers and print the median value (neither maximum nor minimum). 
'''

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if (a>=b and a<=c) or (a>=c and a<=b):
    print("Median is " , a)
elif (b>=c and b<=a) or (b>=a and b<=c):
    print("Median is " , b)
else:
    print("Median is " , c)