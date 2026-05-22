'''
Count how many elements are even and odd.
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))  
print(arr)
even = 0
odd = 0
for eo in arr:
    if eo%2==0:
        even+=1
    else:
        odd+=1
print("Even count : ",even)
print("Odd count : ",odd)