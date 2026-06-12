'''
Count how many pairs of elements have a sum equal to a given number k.
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print(arr)
k = int(input("Enter number : "))
count = 0
for i in range(n):
    for j in range(i+1,n):
        if arr[i] + arr[j] == k:
            count+=1
print("Number of pairs with sum", k, "is", count)
