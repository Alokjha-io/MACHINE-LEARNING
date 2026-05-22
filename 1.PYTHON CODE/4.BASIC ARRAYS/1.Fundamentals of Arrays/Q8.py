'''
Find the index of the maximum element. 
'''
n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print(arr)
max_val = arr[0]
max_index = 0
for j in range(1,n):
    if arr[j] > max_val:
        max_val=arr[j]
        max_index = j
print("Maximum value of array is", max_val )
print("Maximum value index of array is", max_index)
