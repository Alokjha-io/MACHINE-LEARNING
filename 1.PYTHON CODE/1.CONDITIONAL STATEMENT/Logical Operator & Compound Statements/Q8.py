'''
Take a password string and check basic rules (length ≥ 8 and contains at least one 
digit). 
'''

passs = input("Enter Password : ")
if len(passs)>=8 and any(ch.isdigit() for ch in passs) :
    print("Password Available")
else:
    print("Choose a strong Password")
