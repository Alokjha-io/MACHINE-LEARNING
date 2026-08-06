'''
Print all numbers between 1 and N that are divisible by both 3 and 5. 
'''
n = int(input("Enter N : "))
for i in range(0,n):
    if i%3 == 0 and i%5 == 0 :
        print(i)
        
