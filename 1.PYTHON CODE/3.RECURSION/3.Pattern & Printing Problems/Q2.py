'''
Print a square of stars recursively (n×n). 
'''

n = int(input("Enter n : "))
def star(n,i):
    if i>n:
        return ""
    return ("*"*n) + "\n" +star(n,i+1)
print(star(n,1))
