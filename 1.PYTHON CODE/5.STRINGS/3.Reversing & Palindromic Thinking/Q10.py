'''
Reverse string but skip spaces. 
'''

str = input("Enter string : ")
char = [c for c in str if c.isalpha()]
char.reverse()
result = []
i = 0
for c in str:
    if c.isspace():
        result.append(c)
    else:
        result.append(char[i])
        i+=1
print("".join(result))