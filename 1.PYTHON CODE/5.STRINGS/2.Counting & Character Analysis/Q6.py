'''
Count how many times a given character appears in a string. 
'''

x = input("Enter string : ")
g = input("Enter character :")
count = 0
for a in x:
    if a == g:
        count+=1
print("Count of given character in a string is",count)
