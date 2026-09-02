'''
Count how many positive, negative, and zero elements are in an array. 
'''

arr = []
n = int(input("Enter size of array : "))
for i in range(n):
    arr.append(int(input("Enter Element : ")))

p_count = 0
n_count = 0
z_count = 0

for a in arr:
    if a>0:
        p_count+=1
    elif a<0:
        n_count+=1
    else:
        z_count+=1
print("Positive Element count : ",p_count)
print("Negative Element count : ",n_count)
print("Zero Element count : ",z_count)

