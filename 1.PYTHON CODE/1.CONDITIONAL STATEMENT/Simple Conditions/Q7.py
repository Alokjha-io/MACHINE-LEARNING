'''
Take three numbers and print the largest. 
'''

x = int(input("Enter a  number : "))
y = int(input("Enter a  number : "))
z = int(input("Enter a  number : "))
if (x>y and x>z):
    print(x)
elif(y>z and y>x):
    print(y)
else:
    print(z)