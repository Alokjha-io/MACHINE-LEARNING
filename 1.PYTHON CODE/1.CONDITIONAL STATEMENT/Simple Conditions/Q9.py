'''
Take a character and check if it’s a vowel or consonant. 
'''

c = input("Enter a character : ").lower()
vowel = ["a","e","i","o","u"]
if (c in vowel):
    print("Enterd character is vowel")
elif c.isalpha():
    print("Enterd character is consonant")
else :
    print("Invalid")