'''
Print a triangle of stars recursively (top-down).
'''

n = int(input("Enter n : "))
def star(i,n):
    if i>n:
        return ""
    return ("*"*i) + "\n" +star(i+1,n)
print(star(1,n))
