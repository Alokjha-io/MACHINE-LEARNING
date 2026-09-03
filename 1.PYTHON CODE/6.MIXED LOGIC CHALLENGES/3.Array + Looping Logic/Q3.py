'''
Print all unique elements from an array.
'''

arr = []
n = int(input("Enter size of array : "))
for i in range(n):
    arr.append(int(input("Enter Element : ")))
print("Unique Elements : ")
for x in arr:
    if arr.count(x) == 1:
        print(x)