'''
Print all unique elements (those that occur exactly once). 
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print(arr)
freq = {}
for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
for key in freq:
    if freq[key] == 1:
        print(key)