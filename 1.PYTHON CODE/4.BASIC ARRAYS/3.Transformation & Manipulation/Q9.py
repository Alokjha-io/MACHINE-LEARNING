'''
Swap alternate elements (1st ↔ 2nd, 3rd ↔ 4th, etc.). 
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print("Original array =",arr)
for i in range(0, n-1, 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]

print("Array after swapping alternate elements =", arr)