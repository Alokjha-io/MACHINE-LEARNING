'''
Print characters that appear more than once (without map).
'''

s = input("Enter a string : ")
rep = []
dup = []
for ch in s:
    if ch in rep and ch not in dup:
        dup.append(ch)
        print(ch)
    else:
        rep.append(ch)