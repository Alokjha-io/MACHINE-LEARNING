'''
Reverse only characters, keeping digits in place. 
'''

str = input("Enter string : ")
char = [c for c in str if c.isalpha()]
char.reverse()
result = []
i = 0
for c in str:
    if c.isdigit():
        result.append(c)
    else:
        result.append(char[i])
        i+=1
print("".join(result))