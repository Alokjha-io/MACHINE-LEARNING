'''
Compare two arrays — check if they are equal (same elements & order).
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
if m==n:
    if arr1==arr2:
        print("These two arrays are equal")
    else:
        print("These two arrays are not Equal")
else:
    print("These two arrays are not Equal")