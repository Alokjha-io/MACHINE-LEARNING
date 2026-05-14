'''
Take two dates (day and month) and determine which one comes first in the 
calendar. 
'''

d , m = map(int,input("Enter fisrt date : ").split())
d1 ,m1= map(int,input("Enter second date : ").split())
if m<m1 or (m==m1 and d<d1):
    print(d,m,"comes first")
elif m>m1 or (m==m1 and d>d1):
    print(d1,m1,"comes first")
else:
    print("Both date is same")

