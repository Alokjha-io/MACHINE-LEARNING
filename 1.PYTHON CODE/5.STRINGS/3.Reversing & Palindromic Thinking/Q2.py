'''
Reverse each word in a sentence.
'''

x = input("Enter string : ")
words = x.split()
for w in words:
    print("".join(reversed(w)))
