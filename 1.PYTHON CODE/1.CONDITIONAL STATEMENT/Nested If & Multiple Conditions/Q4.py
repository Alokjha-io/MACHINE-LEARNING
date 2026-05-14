'''
Check if one of two given numbers is a multiple of the other.
'''

x = int(input("Enter a first number : "))
y = int(input("Enter a second number : "))
if x%y==0:
    print(x,"is a multiple of",y)
elif y%x==0:
    print(y,"is a multiple of",x)  
else:
    print(x,y,"is not multiple of each other")  