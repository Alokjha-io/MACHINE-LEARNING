'''
Reverse an array (without using built-in reverse). 
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print("Original array =",arr)
new_arr=[]
for j in range(n-1,-1,-1):
    new_arr.append(arr[j])
print("Reversed of an array",new_arr)