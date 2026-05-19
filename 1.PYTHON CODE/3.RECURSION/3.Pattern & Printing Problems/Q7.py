'''
Print multiplication table of n recursively. 
'''

n = int(input("Enter n : "))
def table(i,n):
    if i>10:
        return ""
    return str(n*i) + "\n"  + str(table(i+1,n))
print(table(1,n))