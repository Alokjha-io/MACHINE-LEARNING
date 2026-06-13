'''
Count how many elements are greater than the average of the array. 
'''

n = int(input("Enter n : "))
arr = []
sum = 0
for i in range (n):
    arr.append(int(input("Enter Element : ")))
    sum+=arr[i]
print(arr)
avg = sum/len(arr)
for x in arr:
    if x<avg:
        print(x)