'''
Replace all spaces with ‘_’.
'''

str = input("Enter string : ")

for i in range(len(str)):
    if str[i] in " ":
        str = str.replace(str[i],'_')
print(str)