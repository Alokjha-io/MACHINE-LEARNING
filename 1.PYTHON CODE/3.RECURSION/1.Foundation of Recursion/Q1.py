'''
Print numbers from 1 to n using recursion. 
'''
n = int(input("Enter n : "))
def number(i,n):
    if i>n:
        return
    print(i)
    number(i+1,n)
number(1,n)