import random

letters = ['a','b', 'c','d', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s', 't','u','v','w','x','y','z','A','B','C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator!")
nr_letters = int(input("How many letters would you like in your password\n"))
nr_numbers = int(input("How many numbers would you like in your password\n"))
nr_symbols = int(input("How many symbols would you like in your password\n"))

total = nr_letters + nr_numbers + nr_symbols
print(type(total))
for n in range(1, total):
    random_integer = random.randint(0, 71)
    if random_integer <= 52:
        print(letters[random_integer])
    elif random_integer > 52 and random_integer <= 62:
        number = random_integer - 52
        print(random_integer)
        print(number)
        print(numbers[number])
    else :
        position = random_integer - 62
        print(random_integer)
        print(position)
        print(symbols[position])
    

for n in range(1, total):
    random_integer = random.randint(1, 3)
    if random_integer == 1:
        for l in range(1, nr_letters):
            print(type(l))