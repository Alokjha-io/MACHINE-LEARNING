'''
Count how many spaces are there in a sentence.
'''

x = input("Enter string : ")
sp_count=0
for s in x:
    if s == " ":
        sp_count+=1
print("Spaces count are there in sentences :",sp_count)