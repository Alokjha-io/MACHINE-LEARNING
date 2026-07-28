'''
Find the longest word in a sentence.
'''

str = input("Enter string : ")
words = str.split()
long_word = words[0]
for w in words:
    if len(w)>len(long_word):
        long_word = w
print("Longest word in a sentence is",long_word)