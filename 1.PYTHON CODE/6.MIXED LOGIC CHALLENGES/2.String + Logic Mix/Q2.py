'''
Count vowels in each word of a sentence.
'''

sen = input("Enter a sentence : ")
words = sen.split()
for i in range(len(words)):
    count = 0
    for v in words[i]:
        if v in ['a','e','i','o','u','A','E','I','O','U']:
            count+=1
    print("Count of vowels in",words[i],count)