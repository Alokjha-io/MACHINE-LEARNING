'''
Find the sum of all elements except the largest and smallest.
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print(arr)
arr.sort()
arr = list(set(arr))
sum = 0
for i in range(1,n-1):
    sum+=arr[i]
print(sum)