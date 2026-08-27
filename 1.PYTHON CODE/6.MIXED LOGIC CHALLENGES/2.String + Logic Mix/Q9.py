'''
Find the word with maximum vowels in a sentence. 
'''

sen = input("Enter a sentence : ")
words = sen.split()
max_word = words[0]
count_box = []
for i in range(len(words)):
    count = 0
    for v in words[i]:
        if v in ['a','e','i','o','u','A','E','I','O','U']:
            count+=1
    count_box.append(count)
max_word = words[count_box.index(max(count_box))]
print("Maximum number of vowels present in",max_word)