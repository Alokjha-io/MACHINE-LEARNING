'''
Print pattern of numbers recursively (1 to n each row). 
'''
n = int(input("Enter n : "))
def pattern(i,n):
    if i>n:
        return ""
    row = " ".join(str(x) for x in range(1,i+1))
    return row + "\n" + pattern(i+1,n)
print(pattern(1,n))