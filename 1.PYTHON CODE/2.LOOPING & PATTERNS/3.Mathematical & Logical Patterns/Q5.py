'''
Find LCM of two numbers using loops. 
'''

a = int(input("Enter a : "))
b = int(input("Enter b : "))
i = 1 

while i <= a*b:
    if i % a==0 and i%b==0:
        lcm=i
        break
    i+=1
print("LCM of the number is",lcm)