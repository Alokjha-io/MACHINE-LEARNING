'''
Take time (hours and minutes) and print the smaller angle between the hour and 
minute hands.
'''

x = int(input("Enter Time in Hour (0-23) : "))
y = int(input("Enter Time in Minutes (0-59) : "))

hour_angle = (x % 12) * 30 + (y * 0.5)
minute_angle = y * 6
angle = abs(hour_angle - minute_angle)
if angle>180:
    print("Angle is : " ,360-angle)
else:
    print("Angle is : " ,angle)