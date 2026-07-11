'''
Print the middle character(s) of a string. 
'''
str = input("Enter string : ")
mid_index = (len(str)-1)//2
if len(str)%2 != 0:
    print(str[mid_index])
else:
    print(str[mid_index : mid_index+2])