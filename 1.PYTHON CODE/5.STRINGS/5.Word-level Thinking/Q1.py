'''
Print each word of a sentence on a new line.
'''

str = input("Enter string : ")
words = str.split()
for w in words:
    print(w)