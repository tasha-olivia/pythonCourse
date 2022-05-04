print("Welcomr to Pizza Deliveries!")
size = input("What size of pizza do you want? S, M or L ")
pepperoni = input("Do you want a pepperoni? Y or N ")
p_size = input("Do you want a small size or medium size pepperoni? S or M  ")
extra_cheese = input("Do you want extra chees? y or N ")


if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if pepperoni == "Y":
    if p_size == "S":
        bill += 2
    elif p_size == "M":
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is ${bill} ")
