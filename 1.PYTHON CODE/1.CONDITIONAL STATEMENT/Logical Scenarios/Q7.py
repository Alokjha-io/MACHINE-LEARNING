'''
 Take an integer (1–9999) and check if the sum of its digits is greater than the product 
of its digits. 
'''

x = int(input("Enter an integer (1-9999) : "))
s=0
p=1
temp = x
while temp>0:
    d = temp%10
    s += d
    p *= d
    temp//=10

if s>p:
    print("Sum is greater than product")
elif p>s:
    print("Product is greater than sum")
else:
    print("Sum and product are equal")

        

