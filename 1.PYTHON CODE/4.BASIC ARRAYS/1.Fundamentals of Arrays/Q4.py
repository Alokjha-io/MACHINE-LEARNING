'''
Find the maximum element in an array.
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
    
print(arr)
maximum = arr[0]
for m in arr:
    if m>maximum:
        maximum = m
print("Maximum  is",maximum)
