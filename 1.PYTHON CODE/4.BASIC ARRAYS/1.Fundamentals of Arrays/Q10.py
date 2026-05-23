'''
Take n elements and print only those greater than a given value k. 
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
k = int(input("Enter k : "))
print(arr)
new_arr = []
for g in arr:
    if g > k:
        new_arr.append(g)
print("Array after modifiaction",new_arr)
