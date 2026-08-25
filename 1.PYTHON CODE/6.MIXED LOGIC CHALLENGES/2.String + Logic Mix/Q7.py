'''
Toggle case for every alternate word in a sentence
'''

s = input("Enter a string : ")
words = s.split()
for i in range(len(words)):
    if i%2 != 0:
        words[i] = words[i].upper()
str = " ".join(words)
print(str)

