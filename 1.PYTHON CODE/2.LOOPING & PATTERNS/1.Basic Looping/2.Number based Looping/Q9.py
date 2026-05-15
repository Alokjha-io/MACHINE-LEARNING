'''
Print Fibonacci series up to n terms
'''

n = int(input("Enter number : "))
a,b = 0,1
print("finonacci series up to",n,"term")
for i in range(0,n):
    print(a)
    a,b=b,a+b

    