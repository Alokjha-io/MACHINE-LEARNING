'''
Print first n terms of a geometric progression (a, r). 
'''

n = int(input("Enter n : "))
a,r = map(int,input("Enter a and r : ").split())
print("First n terms of an Geometric progression (a, r).")
for i in range(0,n):
    print(a*(r**i))