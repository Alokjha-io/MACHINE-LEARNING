'''
Check if a number is divisible by both 3 and 5. 
'''

x = int(input("Enter a number : "))
if (x%3==0 and x%5==0):
    print("Entered number is divisible by 3 and 5")
else:
    print("Entered number is not divisible by 3 and 5")