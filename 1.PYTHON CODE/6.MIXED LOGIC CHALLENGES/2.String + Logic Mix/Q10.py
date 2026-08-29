'''
Remove duplicate words from a sentence. 
'''

s = input("Enter a string : ")
words = s.split()
dup = []
for word in words:
    if word not in dup:
        dup.append(word)
sen = " ".join(dup)
print(sen)