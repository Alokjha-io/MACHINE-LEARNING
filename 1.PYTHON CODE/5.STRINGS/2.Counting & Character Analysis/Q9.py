'''
Print how many words start with a vowel in a sentence.
'''

x = input("Enter String : ").lower()
count= 0
words = x.split()
for w in words:
    if w[0] in 'aeiou':
        count+=1
print("Count of words start with a vowel in a sentence : ",count)
