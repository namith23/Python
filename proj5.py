#password generator 
import random
letters = ['a', 'b','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm' '0' 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '0', 'P', 'Q', 'R', 'S', 'T', 'U', 'V' 'W', 'X', 'Y', 'Z'] 
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '%', '&', '(', ')', '+','#','$','^']

print('Welcome to the password generator:')
a_letter = int(input('How many letters do you like:'))
a_number = int(input('How many numbers do you like:'))
a_symbol = int(input('How many symbols do you like:'))

password = []
for char in range(1, a_letter + 1):
    password += random.choice(letters)
for char in range(1, a_number + 1):
    password += random.choice(numbers)
for char in range(1, a_symbol + 1):
    password += random.choice(symbols)
random.shuffle(password)
print(password)

passw = ""
for char in password:
    passw += char
print(f'Your password is:{passw}')
