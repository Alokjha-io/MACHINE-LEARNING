'''
Count how many characters (excluding spaces) are in the string.
'''

x = input("Enter string : ")
count = 0
for i in range(len(x)):
    if x[i]!= " ":
        count+=1
print("Number of character : ",count)