'''
Count how many words end with ‘s’. 
'''

x = input("Enter String : ").lower()
count= 0
words = x.split()
for w in words:
    if w[-1] == 's':
        count+=1
print("Count of words end with s ",count)
