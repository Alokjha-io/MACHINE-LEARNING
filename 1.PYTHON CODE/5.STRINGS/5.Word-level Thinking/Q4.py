'''
Find the shortest word in a sentence.
'''

str = input("Enter string : ")
words = str.split()
short_word = words[0]
for w in words:
    if len(w)<len(short_word):
        short_word = w
print("shortest word in a sentence is",short_word)