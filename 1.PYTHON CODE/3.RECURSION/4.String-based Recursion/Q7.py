'''
Print all characters of a string one by one recursively. 
'''

s = input("Enter string : ")
def obo(s,i=0):
    if i==len(s):
        return ""
    return s[i] + "\n" + obo(s,i+1)
print(obo(s))