'''
Convert a string to uppercase recursively. 
'''

s = input("Enter string : ")
def upper(s,i=0):
    if i == len(s):
        return ""
    return s[i].upper() + upper(s,i+1)
print(upper(s))
