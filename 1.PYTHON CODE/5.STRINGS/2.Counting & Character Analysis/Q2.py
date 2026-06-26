'''
Count the number of digits, letters, and special characters in a string.
'''

x = input("Enter string : ").lower()
d_count = 0
l_count = 0
s_count = 0
for i in range(len(x)):
    if x[i].isalpha():
        l_count+=1
    elif x[i].isnumeric():
        d_count+=1
    else:
        s_count+=1
print("Count of digits :",d_count)
print("Count of letters :",l_count)
print("Count of special charcter :",s_count)

