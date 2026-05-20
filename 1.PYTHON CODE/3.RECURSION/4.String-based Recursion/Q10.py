'''
Count consonants and vowels separately using recursion. 
'''

s = input("Enter string : ")
def count_vc(s,i=0):
    if i == len(s):
        return (0,0)
    v,c = count_vc(s,i+1)
    if s[i].isalpha:
        if s[i] in "aeiou":
            return (v+1,c)
        else:
            return (v,c+1)
    return (v,c)
vowels , constants = count_vc(s)
print("Vowels : " , vowels)
print("Consonants : ",constants)