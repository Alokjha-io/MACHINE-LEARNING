'''
 Check whether a number is a perfect square (without using the square root function). 
'''

n = int(input("Enter a number : "))
flag = False
i = 1
while i * i <= n:
    if i * i == n:
        flag = True
        break
    i += 1
if flag:
    print("Perfect Square")
else:
    print("Not a Perfect Square")


