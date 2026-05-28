'''
Count how many numbers are divisible by 3 and 5 both.
'''

n = int(input("Enter n : "))
arr = []
count = 0
for i in range (n):
    arr.append(int(input("Enter Element : ")))
    if arr[i]% 3 == 0 and arr[i]% 5==0:
        count+=1
print(arr)
print(count)
