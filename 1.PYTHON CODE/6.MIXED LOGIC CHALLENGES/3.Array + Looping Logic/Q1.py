'''
Find the maximum and minimum element in an array.
'''

arr = []
n = int(input("Enter size of array : "))
for i in range(n):
    arr.append(int(input("Enter Element : ")))

max = arr[0]
min = arr[0]

for a in arr:
    if a>max:
        max = a
    if a<min:
        min = a
print("Maximum element : ",max)
print("Minimum element : ",min)
