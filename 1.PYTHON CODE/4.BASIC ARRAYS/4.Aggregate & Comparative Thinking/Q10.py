'''
Print all elements that appear more than once
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print(arr)
freq = {}
r_arr = []
for x in arr:
    if x in freq:
        freq[x]+=1
    else:
        freq[x]=1
    if freq[x]>1:
         r_arr.append(x)
print(r_arr)