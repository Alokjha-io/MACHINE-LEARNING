'''
Print first n terms of an arithmetic progression (a, d). 
'''

n = int(input("Enter n : "))
a,d = map(int,input("Enter a and d : ").split())
print("First n terms of an arithmetic progression (a, d).")
for i in range(0,n):
    print(a+(i*d))