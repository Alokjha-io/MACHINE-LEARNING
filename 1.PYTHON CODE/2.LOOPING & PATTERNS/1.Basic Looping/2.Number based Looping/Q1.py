'''
Count the number of digits in a given number.
'''

n = int(input("Enter n : "))
count=0
while n>0:
    count+=1
    n//=10
print(count)