'''
Print all Armstrong numbers between 1 and 1000
'''

for i in range(1,1000):
    Original = i
    sum = 0
    while i>0:
        digit = i%10
        sum+=(digit**3)
        i = i//10
    if Original == sum:
        print(Original)