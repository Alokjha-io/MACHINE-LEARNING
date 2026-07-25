'''
Shift each character by 1 (e.g., “abc” → “bcd”). 
'''

str = input("Enter strings : ")

result = ""
for s in str:
    result += chr(ord(s)+1)
print(result)