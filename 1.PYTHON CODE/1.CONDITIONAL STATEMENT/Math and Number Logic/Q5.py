'''
Take coordinates (x, y) and determine which quadrant the point lies in.
'''

x = int(input("Enter x coordinates : "))
y = int(input("Enter y coordinates : "))
if x>0 and y>0:
    print(x,y,"lies on first quadrant")
elif x<0 and y>0:
    print(x,y,"lies on second quadrant")
elif x<0 and y<0:
    print(x,y,"lies on third quadrant")
else:
    print((x,y),"lies on second quadrant")
