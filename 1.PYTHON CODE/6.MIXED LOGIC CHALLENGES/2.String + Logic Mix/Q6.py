'''
Count words that start and end with the same letter
'''

s = input("Enter a string : ")
count = 0
words = s.split()
for i in range(len(words)):
    if words[i][0].lower() == words[i][-1].lower():
        count+=1
print(count)