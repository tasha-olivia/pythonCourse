# exercise 2: calculate body mass index
weight = input("enter your weight in kg: ")
height = input("enter your height in m: ")

fbmi = float(weight) / (float(height) ** 2)
ibmi = round(fbmi, 2)

print(f"Your BMI is {ibmi} ")

if ibmi <= 18.5:
    print("Your are UNDERWEIGHT.")
elif ibmi <= 25:
    print("You are NORMAL WEIGHT.")
elif ibmi <= 30:
    print("You are OVERWEIGHT.")
elif ibmi <= 35:
    print("You are OBESED.")
else:
    print("You are CLINICALLY OBESED.")