'''
Check if two strings are anagrams (without using collections).
'''

str1 = input("Enter string one : ")
str2 = input("Enter string two : ")
if len(str1) != len(str2):
    print("Not an anagrams")
else:
    is_anagrams = True
    for ch in str1:
        if str1.count(ch) != str1.count(ch):
            is_anagrams = False
            break
if is_anagrams:
    print("Both are anagrams")
else:
    print("Not an anagrams")
        