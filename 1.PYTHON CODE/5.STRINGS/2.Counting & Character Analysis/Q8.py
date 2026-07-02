'''
Count how many substrings start and end with the same character (simple logic). 
'''

x = input("Enter String : ")
count = 0
for i in range(len(x)):
    for j in range(i+1,len(x)+1):
        sub = x[i:j]
        if sub[0] == sub[-1]:
            count+=1
print("Count of substrings start and end with the same character ",count)