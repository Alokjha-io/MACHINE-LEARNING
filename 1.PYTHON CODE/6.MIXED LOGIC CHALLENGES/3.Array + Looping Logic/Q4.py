'''
Reverse an array in-place. 
'''

arr = []
n = int(input("Enter size of array : "))
for i in range(n):
    arr.append(int(input("Enter Element : ")))
rev_arr = []
for i in range(n//2):
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
print(arr)