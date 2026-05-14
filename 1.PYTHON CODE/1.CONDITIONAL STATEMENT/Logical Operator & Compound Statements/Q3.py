'''
Take 24-hour time (hours and minutes) and print whether it is AM or PM.
'''

x = int(input("Enter Time in Hour (0-23) : "))
y = int(input("Enter Time in Minutes (0-59) : "))
if x<12 and y<=59:
    print("AM")
else:
    print("PM")

