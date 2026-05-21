'''
Find the sum of all elements in an array. 
'''

n = int(input("Enter n : "))
arr = []
sum=0
for i in range (n):
    arr.append(int(input("Enter Element : ")))
    sum +=arr[i]
print(arr)
print("Sum of array is",sum)
