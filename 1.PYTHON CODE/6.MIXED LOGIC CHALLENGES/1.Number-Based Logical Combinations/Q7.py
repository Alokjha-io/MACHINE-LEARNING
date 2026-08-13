'''
Print all prime numbers between 1 and N.
'''

n = int(input("Enter Number : "))
for i in range(1,n):
    if (i > 1) and all(i % d != 0 for d in range(2, int(i**0.5) + 1)):
        print(i)
