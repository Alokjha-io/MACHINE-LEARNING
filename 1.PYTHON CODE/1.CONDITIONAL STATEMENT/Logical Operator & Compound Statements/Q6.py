'''
Take a single digit (0–9) and print its word form (“Zero” to “Nine”).
'''

x = int(input("Enter a single digit (0-9) : "))
wd = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
if x<9:
    print(wd[x])
else:
    print("Inavlid Input")