'''
Print all factors of a given number. 
'''

n = int(input("Enter n : "))
print("Factor of",n,"is")
for i in range(1,n+1):
    if n%i==0:
        print(i)