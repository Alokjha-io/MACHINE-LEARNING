'''
Find the average of array elements.
'''

n = int(input("Enter n : "))
arr = []
sum=0
for i in range (n):
    arr.append(int(input("Enter Element : ")))
    sum +=arr[i]
print(arr)
print("Avgerage of array is",sum/n)
