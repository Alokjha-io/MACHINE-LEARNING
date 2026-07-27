'''
Count how many words have even length.
'''

str = input("Enter string : ")
count = 0
words = str.split()
for w in words:
    if len(w)%2==0:
        count+=1
print(count)