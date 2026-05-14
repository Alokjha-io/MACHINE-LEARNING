'''
Take electricity units consumed and calculate the bill as per slabs (using if-else). 
'''

u = int(input("Enter Electricity unit : "))
if u <= 100:
    print("Your Bill is ",u*5)
elif u <= 200:
    print("Your Bill is ",(u*5) + (u-100)*7)
elif u <= 300:
    print("Your Bill is ",(u*5) + (u-100)*7 + (u-200)*10)
else:
    print("Your Bill is ",(u*5) + (u-100)*7 + (u-200)*10 +(u-300)*15)

