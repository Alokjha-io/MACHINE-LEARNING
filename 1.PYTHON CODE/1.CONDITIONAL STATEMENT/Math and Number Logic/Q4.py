'''
Check if a number is a multiple of 7 or ends with 7. 
'''

x = int(input("Enter a Number : "))

if x%7==0 and x%10==7:
    print("Enterd Number is Multiple of 7 or Ends with 7")
elif x%7==0 and x%10!=7:
    print("Enterd Number is Multiple of 7 or but not Ends with 7")
elif x%7!=0 and x%10==7:
    print("Enterd Number is not Multiple of 7 but Ends with 7")
else:
    print("Enterd Number is not Multiple of 7 or Ends with 7")
