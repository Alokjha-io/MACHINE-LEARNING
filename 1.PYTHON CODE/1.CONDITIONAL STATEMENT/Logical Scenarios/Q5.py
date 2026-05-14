'''
Take three numbers and check if they are in arithmetic progression. 
'''

x = float(input("Enter first Number : "))
y = float(input("Enter Second Number : "))
z = float(input("Enter Third Number : "))
if (x+z)/2 == y:
    print("They are in arithmetics progression")
else:
    print("They are not in arithmetics progression")
  