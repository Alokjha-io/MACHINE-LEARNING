'''
Reverse words in a string if their length is even.
'''

sen = input("Enter a sentence : ")
words = sen.split()
for i in range(len(words)):
    if len(words[i])%2 == 0:
        words[i] = "".join(reversed(words[i]))
sen = " ".join(words)
print(sen)
