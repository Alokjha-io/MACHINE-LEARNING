'''
Take the hour of the day (0–23) and print “Good Morning”, “Good Afternoon”, “Good 
Evening”, or “Good Night”. 
'''

hr = int(input("Enter hour of a day (0-23) : "))
if hr<12:
    print("Good Morning")
elif 12<hr<=16:
    print("Good Afternoon")
elif 16<hr<=20:
    print("Good Evening")
elif 20<hr<=23:
    print("Good Night")
else:
    print("Invaild input")