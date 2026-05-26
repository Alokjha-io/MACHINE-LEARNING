'''
Find the first occurrence of a given number. 
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print(arr)
x = int(input("Enter x : "))
fo_x = 0
for j in range(n):
    if x == arr[j]:
        fo_x = j
        break
print("Fisrt occurence of",x,"is in index ",fo_x)
