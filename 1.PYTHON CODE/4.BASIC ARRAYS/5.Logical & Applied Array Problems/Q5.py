'''
Find the difference between the largest and smallest element. 
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print(arr)
arr.sort()
print("Difference between the largest and smallest element is",arr[n-1]-arr[0])