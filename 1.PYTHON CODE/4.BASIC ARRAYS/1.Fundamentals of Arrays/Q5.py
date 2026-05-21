'''
Find the minimum element in an array.
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
    
print(arr)
minimum = arr[0]
for m in arr:
    if minimum<m:
        minimum
    else:
        minimum = m
print("Minimum  is",minimum)