'''
Find the index of the minimum element. 
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print(arr)
min_val = arr[0]
min_index = 0
for j in range(1,n):
    if arr[j] < min_val:
        min_val = arr[j]
        min_index = j
print("Minimum value of array is", min_val )
print("Minimum value index of array is", min_index)
