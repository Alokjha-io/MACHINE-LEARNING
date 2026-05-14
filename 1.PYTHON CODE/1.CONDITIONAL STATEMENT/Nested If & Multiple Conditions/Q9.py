'''
Take a day number (1–7) and print the corresponding day name. 
'''

Days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
n = int(input("Enter day Number (1-7) : "))
if 1<=n<=7:
    print(Days[n-1])
else:
    print("Invalid")