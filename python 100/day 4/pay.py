import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# gets input elements from user and seperates them into a list.
name_of_group = input("List everyones name seperated by a comma immediately followed by a space in the group: \n")
names = name_of_group.split(", ")
# get total number of items in a list
n = len(names)

# generate random numbers between 0 and the last index
number = random.randint(0, n-1)

# it uses the random number generated to select the person to pay
pay_person = names[number]

# you pass the list of names into the choice function and it selects a random name
# pay_person = random.choice(names)

print(pay_person + " will pay the bill. ")
