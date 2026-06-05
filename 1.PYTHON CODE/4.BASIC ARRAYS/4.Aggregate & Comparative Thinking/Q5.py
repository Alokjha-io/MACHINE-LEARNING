'''
Find elements that are in one array but not in the other.
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
d_arr = []
for x in arr1:
    if x not in arr2 and x not in d_arr:
        d_arr.append(x)
for y in arr2:
    if y not in arr1 and y not in d_arr:
        d_arr.append(y)
print(d_arr)