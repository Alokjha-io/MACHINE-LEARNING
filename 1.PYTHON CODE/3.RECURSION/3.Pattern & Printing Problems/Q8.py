'''
Print numbers in increasing and decreasing order in same function. 
'''

n = int(input("Enter n : "))
def order(i,n):
    if i>n:
        return ""
    return str(i) + "" + order(i+1,n) + str(i) + ""
print(order(1,n))