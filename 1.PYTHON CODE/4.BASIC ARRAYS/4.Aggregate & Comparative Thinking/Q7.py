'''
Find element-wise sum of two arrays (A[i] + B[i]). 
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
sum_arr = []
limit = min(m,n)
for i in range(limit):
    sum_arr.append(arr1[i]+arr2[i])
print("Element wise sum of two array is", sum_arr)