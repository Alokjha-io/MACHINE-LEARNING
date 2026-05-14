'''
Take three numbers and check if they are in geometric progression. 
'''

x = float(input("Enter first Number : "))
y = float(input("Enter Second Number : "))
z = float(input("Enter Third Number : "))
if x*z == y^2:
    print("They are in geometrics progression")
else:
    print("They are not in geometrics progression")
  