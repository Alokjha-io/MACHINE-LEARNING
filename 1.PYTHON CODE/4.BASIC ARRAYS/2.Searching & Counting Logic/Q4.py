'''
Find the last occurrence of a given number.
'''

n = int(input("Enter n : "))
arr = []
for i in range(n):
    arr.append(int(input("Enter Element : ")))
print(arr)
x = int(input("Enter x : "))
lo_x = 0
for j in range(n):
    if x == arr[j]:
        lo_x=j
print("Last occurence of",x,"is in index",lo_x)