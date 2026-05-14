'''
Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions.
'''

t = float(input("Enter Temprature : "))
if (t<20):
    print("Cold")
elif (20 < t < 30):
    print("Warm")
else:
    print("Hot")