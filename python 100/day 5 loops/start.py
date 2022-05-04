fruits = ["Apple", "Pear", "Gauva", "Mango" ]
for fruit in fruits:
    print(fruit)
print("END")


# the range function starts with the first number but the last digit is not included
# the 3rd number in the range function determines the steps
for number in range(1, 100, 20):
    print(number)

# sum of numbers from 1 to 100
total = 0
for number in range(1, 101):
    total += number
print(f" The sum of numbers from 0 to 100 is {total}")