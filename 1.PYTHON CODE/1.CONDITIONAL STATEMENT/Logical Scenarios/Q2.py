'''
Take three numbers and check if they can form a Pythagorean triplet.
'''

x = int(input("Enter first Number : "))
y = int(input("Enter Second Number : "))
z = int(input("Enter Third Number : "))
if x^2 + y^2 == z^2:
    print(x,y,z,"are python triplet")
else:
    print(x,y,z,"are not python triplet")