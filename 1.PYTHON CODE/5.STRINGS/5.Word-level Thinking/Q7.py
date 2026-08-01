'''
Count how many words contain the letter ‘a’. 
'''

str = input("Enter string : ")
words = str.split()
count = 0
for w in words:
    if 'a' in w:
        count+=1
print(count)