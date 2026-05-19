'''
Count vowels in a string recursively. 
'''

s = input("Enter string : ")
def vowels(s,i):
    if i==len(s) :
        return 0
    if s[i].lower() in "aeiou":
        return 1 + vowels(s,i+1)
    else:
        return vowels(s,i+1)
print(vowels(s,0))