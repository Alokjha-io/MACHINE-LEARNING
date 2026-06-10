'''
Find the second smallest element in an array. 
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print(arr)
arr.sort()
arr = list(set(arr))
if len(arr) < 2:
    print("There is less than 2 element")
else:
    print("Second Smallest element is",arr[1])
