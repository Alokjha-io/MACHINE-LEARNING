'''
Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the 
origin. 
'''

x,y = map(int,input("Enter x and y coordinates : ").split())
if x==0 and y>0 :
    print("Point lies on Y axis")
elif y==0 and x>0:
    print("Point lies on X axis")
elif x==0 and y==0:
    print("Point lies at the origin")

