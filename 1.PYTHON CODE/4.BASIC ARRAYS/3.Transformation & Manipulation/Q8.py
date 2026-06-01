'''
Rotate an array by one position to the right. 
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print("Original array =",arr)
new_arr = [arr[n-1]] + arr[0:n-1]
print("Array by rotating one position to the Right =",new_arr)

