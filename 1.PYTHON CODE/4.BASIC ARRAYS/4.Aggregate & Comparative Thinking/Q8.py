'''
Find element-wise product of two arrays. 
'''

m = int(input("Enter m : "))
arr1 = []
for i in range (m):
    arr1.append(int(input("Enter Element : ")))
print(arr1)
n = int(input("Enter n : "))
arr2 = []
for i in range (n):
    arr2.append(int(input("Enter Element : ")))
print(arr2)
prd_arr = []
limit = min(m,n)
for i in range(limit):
    prd_arr.append(arr1[i]*arr2[i])
print("Element wise sum of two array is", prd_arr)