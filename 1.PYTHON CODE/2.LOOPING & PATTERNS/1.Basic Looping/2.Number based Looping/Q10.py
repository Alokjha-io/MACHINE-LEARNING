'''
Print sum of first n terms of Fibonacci series. 
'''

n = int(input("Enter number : "))
a,b = 0,1
sum=0
for i in range(0,n):
    sum+=a
    a,b=b,a+b
print("Sum of fibonaaci series upto",n,"is",sum)