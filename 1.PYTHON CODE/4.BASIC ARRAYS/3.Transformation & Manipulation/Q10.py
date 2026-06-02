'''
Copy one array to another manually.
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print(arr)
copy_arr = []
for c in arr:
    copy_arr.append(c)
print("Copy array of 1st array",copy_arr)
