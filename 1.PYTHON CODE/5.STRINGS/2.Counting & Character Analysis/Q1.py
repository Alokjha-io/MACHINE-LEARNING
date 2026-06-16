'''
Count how many vowels and consonants are in a string. 
'''

x = input("Enter string : ").lower()
v_count = 0
c_count = 0
for i in range(len(x)):
    if x[i].isalpha():
        if x[i] in ['a','e','i','o','u']:
            v_count+=1
        else:
            c_count+=1
print("Vowels count :",v_count)
print("Consonants count :",c_count)