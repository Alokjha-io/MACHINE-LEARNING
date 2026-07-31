'''
Print all words that start and end with the same letter. 
'''

str = input("Enter string : ")
words = str.split()
for w in words:
    if w[0] == w[-1]:
        print(w)