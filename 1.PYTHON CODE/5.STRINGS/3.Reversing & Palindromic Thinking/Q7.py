'''
Print the second half of the string in reverse.
'''

str = input("Enter string : ")
mid_index = len(str) // 2
print(str[mid_index:][::-1])

