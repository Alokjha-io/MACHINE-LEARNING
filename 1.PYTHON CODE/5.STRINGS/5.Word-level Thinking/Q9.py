'''
Capitalize the first letter of each word.
'''

str = input("Enter string : ")
words = str.split()
for w in words:
    w = w.capitalize()
    print(w)
