'''
Take a year and print the corresponding century (e.g., “19th century”, “20th century”)
'''

year = int(input("Enter year : "))
ce = (year//100)+1
print(year,"falls on",ce,"century")