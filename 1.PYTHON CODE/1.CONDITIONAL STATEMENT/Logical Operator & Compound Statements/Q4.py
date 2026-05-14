'''
Take income and age, and check if eligible for tax (age > 18 and income > 5 L). 
'''

i = int(input("Enter Income in Lakhs : "))
age = int(input("Enter age: "))
if i > 5 and age>18:
    print("Eligible for tax")
else:
    print("Not Eligible")