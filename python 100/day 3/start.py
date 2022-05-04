print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("How old are you "))

if height >= 120:
    print("You can ride the rollercoaster")

    if age < 12:
        bill = 5
        print("You will pay $5. ")
    elif age <= 18:
        bill = 7
        print("You will pay $7.")
    elif age > 44 and age < 56:
        print("Everything will be alright. Have a free ride.")
    else:
        bill = 12
        print("You will pay $12. ")

    photo = input("Do you want a photo? Y or N.  ")
    if photo == "Y":
        bill += 3

    print(f"Your final bill is {bill} ")
else:
    print("Sorry! you have to grow taller") 