'''
If the sides form a valid triangle, determine whether it is equilateral, isosceles, or 
scalene. 
'''

x = int(input("Enter first side of triangle : "))
y = int(input("Enter second side of triangle : "))
z = int(input("Enter third side of triangle : "))
if x+y>z and x+z>y and y+z>x :
    print("Triangle is valid")
    if x==y==z==x:
        print("This triangle is equilateral")
    elif x==y or x==z or y==z :
        print("This triangle is isosceles")
    else:
        print("This triangle is scalene")
else:
    print("Triangle isn't vaild")