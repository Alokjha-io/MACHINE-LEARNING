'''
scalene. 
3. Take marks (0–100) and print the corresponding grade (A/B/C/D/F). 
'''

m = float(input("Enter marks (0-100) : "))
if (0<m<33):
    print("Grade F")
elif (33<m<40):
    print("Grade D")
elif (40<m<60):
    print("Grade C")
elif (60<m<80):
    print("Grade D")
else:
    print("Grade A")