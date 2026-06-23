'''
Compare two strings lexicographically (like dictionary order). 
'''

x = input("Enter string one : ")
y = input("Enter string two : ")
if x < y:
    print(x,"comes first")
elif y < x:
    print(y,"comes first")
else:
    print("Both are same")