'''
Count how many even digits a number contains
'''

n = int(input("Enter N : "))
count = 0
while n>0:
    digit = n%10
    if digit%2==0:
        count+=1
    n = n//10
print("Count of even digit in number is",count)
        