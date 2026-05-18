'''
Find nCr (Combination formula) recursively using Pascal’s relation. 
'''

def ncr(n,r):
    if r==0 or r==n :
        return 1
    return ncr(n-1,r-1) + ncr(n-1,r)
n,r = map(int,input("Enter n and r : ").split())

print("ncr is",ncr(n,r))
