'''
Swap first and last words in a sentence.
'''

str = input("Enter string : ")
words = str.split()
first = words[0]
last = words[-1]
words[0] = last
words[-1] = first
print(" ".join(words))