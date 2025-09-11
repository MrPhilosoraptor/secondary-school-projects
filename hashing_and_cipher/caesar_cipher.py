import random

user_string = str(input("Enter a string to be encrypted:\n"))
cipher_shift = random.randint(1, 10)
cipher_string = ""

for letter in user_string:
    if letter.isalpha():
        stayAlpha = ord(letter) + cipher_shift
        if chr(stayAlpha).isalpha() == False:
            stayAlpha = ord(letter) - cipher_shift
        finalLetter = chr(stayAlpha)
        cipher_string += finalLetter
    elif letter.isspace():
        cipher_string += letter

print(cipher_string)
print(cipher_shift)