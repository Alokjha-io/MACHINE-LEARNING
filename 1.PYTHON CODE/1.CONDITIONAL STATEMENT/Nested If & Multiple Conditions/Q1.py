'''
Take three sides and check if they form a valid triangle.
'''

x = int(input("Enter first side of triangle : "))
y = int(input("Enter second side of triangle : "))
z = int(input("Enter third side of triangle : "))
if x+y>z and x+z>y and y+z>x :
    print("Triangle is valid")
else:
    print("Triangle isn't vaild")