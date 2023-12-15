import random

#this program will generagte a random password for given length of every part 

num_letters = int(input("Enter the number of letters do you want in your password! "))
num_char = int (input("Enter the number of special Characters do you want in your password! "))
num_number = int(input("Enter the number of numbers do you want in your password! "))

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.',
 '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


password = []

for letter in range(1, num_letters + 1):
    password.append(random.choice(letters))

for number in range(1, num_number + 1):
    password.append(random.choice(numbers))

for char in range(1, num_char + 1):
    password.append(random.choice(special_characters))

random.shuffle(password)

passwords = ""

for item in password:
    passwords += item

print(passwords)
