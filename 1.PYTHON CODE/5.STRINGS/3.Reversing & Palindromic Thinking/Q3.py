'''
Reverse the order of words in a sentence.
'''

x = input("Enter string : ")
words = x.split()
rev_x = " ".join(reversed(words))
print(rev_x)