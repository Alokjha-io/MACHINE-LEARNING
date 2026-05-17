'''
Print only odd numbers from 1 to n recursively.
'''

n = int(input("Enter n : "))
def evennum(i,n):
    if i>n:
        return
    if i%2!=0:
        print(i)
    evennum(i+1,n)
evennum(1,n)